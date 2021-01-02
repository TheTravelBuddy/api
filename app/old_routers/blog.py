from typing import List

from fastapi import APIRouter

from ..models import database, validation

router = APIRouter()


@router.get("/")
async def read_blogs() -> List[validation.Blog]:
    return [validation.Blog(**blog.__dict__) for blog in database.Blog.nodes.all()]


@router.post("/")
def add_blog(blog: validation.Blog) -> str:
    blog = database.Blog(**blog.__dict__).save()
    return blog.uid


@router.get("/{blog_id}")
async def read_blog(blog_id: str) -> validation.Blog:
    return validation.Blog(**database.Blog.nodes.first(uid=blog_id).__dict__)


@router.put("/{blog_id}")
async def update_blog(blog_id: str, blog: validation.Blog) -> validation.Blog:
    selected_blog = database.Blog.nodes.first(uid=blog_id)
    for key, value in blog.__dict__.items():
        if key != "uid":
            setattr(selected_blog, key, value)
    selected_blog.save()
    return validation.Blog(**selected_blog.__dict__)


@router.delete("/{blog_id}")
async def delete_blog(blog_id: str):
    database.Blog.nodes.first(uid=blog_id).delete()
