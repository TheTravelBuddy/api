from fastapi import APIRouter

from . import auth, blog, home

router = APIRouter()

router.include_router(auth.router, prefix="/auth")
router.include_router(blog.router, prefix="/blog")
router.include_router(home.router, prefix="/home")
