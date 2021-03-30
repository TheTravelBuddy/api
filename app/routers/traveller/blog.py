from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, Depends
from neomodel import db
from pydantic import AnyUrl, BaseModel

from ...dependencies.auth import get_registered_user
from ...dependencies.entities import get_blog
from ...helpers.conversion import deflate_request
from ...helpers.db_query import get_query_response
from ...helpers.queries import (
    GET_ALL_TOPICS_QUERY,
    GET_BLOG_COMMENTS_QUERY,
    GET_BLOG_DETAILS_QUERY,
)
from ...models.database import Blog, Location, Topic

router = APIRouter()


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


class NewBlogRequest(BaseModel):
    title: str
    content: str
    photos: List[AnyUrl]
    topic: Optional[str]
    location: Optional[str]


@router.post("")
async def add_new_blog(blogData: NewBlogRequest, user=Depends(get_registered_user)):
    with db.transaction:
        blog = Blog(**deflate_request(blogData, {"title", "content", "photos"})).save()
        blog.authored_by.connect(user)

        if blogData.topic:
            blog.tagged_topic.connect(Topic.nodes.get(uid=blogData.topic))

        if blogData.location:
            blog.tagged_location.connect(Location.nodes.get(uid=blogData.location))

        return blog.uid


class TopicResponse(BaseModel):
    id: str
    name: str


@router.get("/topic", response_model=List[TopicResponse])
async def get_topics(_=Depends(get_registered_user)):
    return get_query_response(GET_ALL_TOPICS_QUERY)


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
