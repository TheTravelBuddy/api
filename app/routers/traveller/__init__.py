from fastapi import APIRouter

from . import auth, community, home, hotelDetail

router = APIRouter()

router.include_router(auth.router, prefix="/auth")
router.include_router(community.router, prefix="/community")
router.include_router(home.router, prefix="/home")
router.include_router(hotelDetail.router, prefix="/hotel")
