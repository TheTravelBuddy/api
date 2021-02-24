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


class BlogCommentResponse(BaseModel):
    id: str
    commenterName: str
    comment: str


class BlogApiResponse(BaseModel):
    blog: BlogDetailResponse
    comments: List[BlogCommentResponse]


# user=Depends(get_registered_user)
@router.get("", response_model=BlogApiResponse)
async def get_blog_data(blog=Depends(get_blog)):
    blogdetail = dict()
    blogdetail["id"] = blog.uid
    blogdetail["title"] = blog.title
    blogdetail["content"] = blog.content
    blogdetail["published_on"] = blog.published_on
    blogdetail["photos"] = blog.photos
    blogdetail["topic"] = blog.tagged_topic.all()[0].__dict__["name"]
    blogdetail["authorName"] = blog.authored_by.all()[0].__dict__["name"]
    blogdetail["authorUri"] = blog.authored_by.all()[0].__dict__["profile_picture"]
    blogdetail["likes"] = len(blog.liked_by.all())
    print(blogdetail)
