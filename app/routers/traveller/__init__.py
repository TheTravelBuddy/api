from fastapi import APIRouter

from . import auth, blog, booking, city, community, home, hotel, package, profile

router = APIRouter()

router.include_router(auth.router, prefix="/auth")
router.include_router(booking.router, prefix="/booking")
router.include_router(community.router, prefix="/community")
router.include_router(home.router, prefix="/home")
router.include_router(blog.router, prefix="/blog")
router.include_router(hotel.router, prefix="/hotel")
router.include_router(package.router, prefix="/package")
router.include_router(profile.router, prefix="/profile")
router.include_router(city.router, prefix="/city")
