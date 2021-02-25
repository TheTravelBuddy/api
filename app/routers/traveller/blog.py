from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from neomodel import db
from pydantic import AnyUrl, BaseModel

from ...dependencies.auth import get_registered_user
from ...helpers.conversion import get_query_response
from ...models.database import Blog

router = APIRouter()


async def get_blog(blogId: str):
    try:
        return Blog.nodes.get(uid=blogId)
    except Blog.DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found."
        )


class BlogCommentResponse(BaseModel):
    name: str
    comment: str
    datetime: datetime


class BlogApiResponse(BaseModel):
    id: str
    title: str
    content: str
    publishedOn: datetime
    photos: List[AnyUrl]
    location: str
    topic: str
    authorName: str
    authorProfile: AnyUrl
    likes: int
    liked: bool
    comments: List[BlogCommentResponse]


GET_BLOG_DETAILS_QUERY = """
MATCH
    (blog:Blog {uid:$blog})-[:AUTHOR_OF]-(traveller:Traveller),
    (blog)-[:TAGGED_TOPIC]-(topic),
    (blog)-[:TAGGED_LOCATION]-(location)
OPTIONAL MATCH
    (blog)-[like:LIKES_BLOG]-()
RETURN
    blog.uid AS id,
    blog.title AS title,
    blog.content AS content,
    blog.published_on AS publishedOn,
    blog.photos AS photos,
    topic.name AS topic,
    location.name AS location,
    traveller.name AS authorName,
    traveller.profile_picture AS authorProfile,
    COUNT(like) AS likes,
    EXISTS ((blog)-[:LIKES_BLOG]-(:User {uid:$user})) as liked
"""

GET_BLOG_COMMENTS_QUERY = """
MATCH
    (:Blog {uid:$blog})-[comment:COMMENTED_ON]-(traveller:Traveller)
RETURN
    traveller.name AS name,
    comment.content AS comment,
    comment.datetime AS datetime
ORDER BY datetime DESC
LIMIT $n
"""


@router.get("", response_model=BlogApiResponse)
async def get_blog_data(blog=Depends(get_blog), user=Depends(get_registered_user)):
    return BlogApiResponse(
        **get_query_response(
            GET_BLOG_DETAILS_QUERY, {"blog": blog.uid, "user": user.uid}
        )[0],
        comments=get_query_response(
            GET_BLOG_COMMENTS_QUERY, {"blog": blog.uid, "n": 3}
        ),
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
