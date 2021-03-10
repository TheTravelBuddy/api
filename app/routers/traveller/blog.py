from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends
from neomodel import db
from pydantic import AnyUrl, BaseModel

from ...dependencies.auth import get_registered_user
from ...dependencies.entities import get_blog
from ...helpers.conversion import deflate_request
from ...helpers.db_query import get_query_response, update_node
from ...helpers.queries import GET_BLOG_COMMENTS_QUERY, GET_BLOG_DETAILS_QUERY
from ...models.database import Blog, Traveller

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


class BlogUpdateRequest(BaseModel):
    title: str
    content: str
    photos: List[AnyUrl]


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


#
@router.put("/update")
async def update_blog(
    blogDetail: BlogUpdateRequest,
    blog=Depends(get_blog),
    user=Depends(get_registered_user),
):
    # print(user.uid == blog.authored_by.single().uid)
    if user.uid == blog.authored_by.single().uid:
        update_node(blog, deflate_request(blogDetail, {"title", "content", "photos"}))
