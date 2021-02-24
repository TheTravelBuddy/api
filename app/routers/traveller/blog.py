from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from neomodel import db
from pydantic import AnyUrl, BaseModel

from ...dependencies.auth import get_registered_user
from ...helpers.conversion import get_query_response
from ...models.database import Blog

router = APIRouter()


async def get_blog(blog_id: str):
    try:
        return Blog.nodes.get(uid=blog_id)
    except Blog.DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found."
        )


class BlogDetailResponse(BaseModel):
    id: str
    title: str
    content: str
    published_on: datetime
    photos: List[AnyUrl]
    location: str
    topic: str
    authorName: str
    authorUri: str
    likes: int


class BlogCommentsResponse(BaseModel):
    commenterName: str
    comment: str
    datetime: datetime


class BlogApiResponse(BaseModel):
    blog: BlogDetailResponse
    comments: List[BlogCommentsResponse]


GET_BLOG_DETAIL_QUERY = """
MATCH 
    ()-[like:LIKES_BLOG]-(blog:Blog {uid:$blog})-[:AUTHOR_OF]-(traveller:Traveller),
    (blog)-[:TAGGED_TOPIC]-(topic),
    (blog)-[:TAGGED_LOCATION]-(location)
RETURN 
    blog.uid as id, 
    blog.title as title,
    blog.content as content,
    blog.published_on as published_on, 
    blog.photos as photos,
    topic.name as topic, 
    location.name as location, 
    traveller.name as authorName, 
    traveller.profile_picture as authorUri,
    COUNT(like) as likes
"""

GET_BLOG_COMMENTS_QUERY = """
MATCH 
    (blog:Blog {uid:$blog})-[comment:COMMENTED_ON]-(traveller:Traveller) 
RETURN 
    traveller.name as commenterName,
    comment.content as comment, 
    comment.datetime as datetime
ORDER BY datetime DESC
"""

# user=Depends(get_registered_user)
@router.get("", response_model=BlogApiResponse)
async def get_blog_data(blog=Depends(get_blog), user=Depends(get_registered_user)):
    return BlogApiResponse(
        blog=get_query_response(GET_BLOG_DETAIL_QUERY, {"blog": blog.uid})[0],
        comments=get_query_response(GET_BLOG_COMMENTS_QUERY, {"blog": blog.uid}),
    )


@router.post("/like")
async def blog_like(blog=Depends(get_blog), user=Depends(get_registered_user)):
    with db.transaction:
        if not user.likes_blog.is_connected(blog):
            user.likes_blog.connect(blog)


@router.delete("/unlike")
async def blog_unlike(blog=Depends(get_blog), user=Depends(get_registered_user)):
    with db.transaction:
        if user.likes_blog.is_connected(blog):
            user.likes_blog.disconnect(blog)
