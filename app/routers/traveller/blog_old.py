from typing import List

from app.models.database.nodes import Traveller
from fastapi import APIRouter, HTTPException, status
from fastapi.params import Depends

from ...dependencies.auth import get_registered_user
from ...models import database, validation
from ...models.database import Blog

router = APIRouter(dependencies=[Depends(get_registered_user)])


@router.get("")
async def read_blogs() -> List[validation.Blog]:
    return [validation.Blog(**blog.__dict__) for blog in database.Blog.nodes.all()]


@router.post("")
def add_blog(blog: validation.Blog) -> str:
    blog = database.Blog(**blog.__dict__).save()
    return blog.uid


async def get_blog(blog_id: str):
    try:
        return validation.Blog(**Blog.nodes.get(uid=blog_id).__dict__)
    except Blog.DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Blog not found.",
        )


@router.get("/{blog_id}")
async def read_blog(blog=Depends(get_blog)) -> validation.Blog:
    return blog


async def get_blog_author(blog=Depends(get_blog), user_id=Depends(get_registered_user)):
    try:
        blog.authored_by.get(uid=user_id)
    except Traveller.DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not authorized.",
        )


@router.put("/{blog_id}", dependencies=[Depends(get_blog_author)])
async def update_blog(blog_id: str, blog: validation.Blog) -> validation.Blog:
    selected_blog = database.Blog.nodes.first(uid=blog_id)
    for key, value in blog.__dict__.items():
        if key != "uid":
            setattr(selected_blog, key, value)
    selected_blog.save()
    return validation.Blog(**selected_blog.__dict__)


@router.delete("/{blog_id}", dependencies=[Depends(get_blog_author)])
async def delete_blog(blog_id: str):
    database.Blog.nodes.first(uid=blog_id).delete()
