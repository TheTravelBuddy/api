from fastapi import APIRouter

from . import auth, blog, community, home, hotel

router = APIRouter()

router.include_router(auth.router, prefix="/auth")
router.include_router(community.router, prefix="/community")
router.include_router(home.router, prefix="/home")
router.include_router(blog.router, prefix="/blog")
router.include_router(hotel.router, prefix="/hotel")
