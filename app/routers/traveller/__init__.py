from fastapi import APIRouter

from . import auth, blog

router = APIRouter()

router.include_router(auth.router, prefix="/auth")
router.include_router(blog.router, prefix="/blog")
