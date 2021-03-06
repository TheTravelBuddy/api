from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from neomodel import db
from pydantic import AnyUrl, BaseModel, confloat, constr

from ...dependencies.auth import get_registered_user
from ...dependencies.entities import get_hotel
from ...helpers.conversion import get_query_response
from ...helpers.queries import GET_HOTEL_DETAILS_QUERY, GET_HOTEL_REVIEWS_QUERY
from ...helpers.validatation import PHONE_NUMBER_REGEX, HotelAmenitiesEnum
from ...models.database import Hotel

router = APIRouter()


class HotelReviewResponse(BaseModel):
    id: str
    rating: int
    review: str
    datetime: datetime
    name: str


class HotelApiResponse(BaseModel):
    id: str
    photos: List[AnyUrl]
    name: str
    locality: str
    address: str
    postalCode: str
    city: str
    rating: Optional[float] = None
    price: int
    phoneNumber: constr(min_length=13, max_length=13, regex=PHONE_NUMBER_REGEX)
    latitude: confloat(ge=-90, le=90)
    longitude: confloat(ge=-180, le=180)
    about: str
    amenities: List[HotelAmenitiesEnum]
    liked: bool
    reviews: List[HotelReviewResponse]


@router.get("", response_model=HotelApiResponse)
async def get_hotel_detail(hotel=Depends(get_hotel), user=Depends(get_registered_user)):
    try:
        return HotelApiResponse(
            **get_query_response(
                GET_HOTEL_DETAILS_QUERY,
                {"hotel": hotel.uid, "user": user.uid},
            )[0],
            reviews=get_query_response(
                GET_HOTEL_REVIEWS_QUERY, {"hotel": hotel.uid, "n": 3}
            ),
        )
    except IndexError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Hotel not found.",
        )


@router.post("/like")
async def hotel_like(hotel=Depends(get_hotel), user=Depends(get_registered_user)):
    with db.transaction:
        if not user.likes_hotel.is_connected(hotel):
            user.likes_hotel.connect(hotel)


@router.delete("/unlike")
async def hotel_unlike(hotel=Depends(get_hotel), user=Depends(get_registered_user)):
    with db.transaction:
        if user.likes_hotel.is_connected(hotel):
            user.likes_hotel.disconnect(hotel)
