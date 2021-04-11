from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends
from neomodel import db
from pydantic import AnyUrl, BaseModel

from ...dependencies.auth import get_registered_user
from ...dependencies.entities import get_blog
from ...helpers.db_query import get_query_response
from ...helpers.queries import (
    GET_BLOG_COMMENTS_QUERY,
    GET_BLOG_DETAILS_QUERY,
    GET_FAV_BLOG_QUERY,
)

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


@router.get("/favs")
async def get_fav_blogs(user=Depends(get_registered_user)):
    return get_query_response(GET_FAV_BLOG_QUERY, {"userId": user.uid})
