from fastapi import APIRouter

from . import agency, auth, hotel, shop

router = APIRouter()

router.include_router(auth.router, prefix="/auth")
router.include_router(hotel.router, prefix="/hotel")
router.include_router(shop.router, prefix="/shop")
router.include_router(agency.router, prefix="/agency")
