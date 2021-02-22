from datetime import datetime
from enum import Enum
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.params import Depends
from neomodel import db
from pydantic import AnyUrl, BaseModel, confloat, constr

from ...dependencies.auth import get_registered_user
from ...helpers.conversion import get_query_response
from ...helpers.validatation import PHONE_NUMBER_REGEX, HotelAmenitiesEnum
from ...models.database import Hotel, Traveller

router = APIRouter()


async def get_hotel(hotelId: str):
    try:
        return Hotel.nodes.get(uid=hotelId)
    except Hotel.DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Hotel not found"
        )


class HotelReviewsResponse(BaseModel):
    id: str
    rating: int
    review: str
    datetime: datetime
    name: str


class HotelDetailsResponse(BaseModel):
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
    likes: bool


class HotelApiResponse(BaseModel):
    hotelDetails: HotelDetailsResponse
    hotelReviews: List[HotelReviewsResponse]


GET_HOTEL_DETAILS_QUERY = """
MATCH
    (city:City)-[:LOCATED_IN]-(hotel:Hotel {uid:$hotel})
OPTIONAL MATCH
    (hotel)-[review:REVIEWED_HOTEL]-()
RETURN
    hotel.uid as id,
    hotel.photos as photos,
    hotel.name as name,
    city.name as city,
    hotel.locality as locality,
    hotel.address as address,
    hotel.postal_code as postalCode,
    AVG(review.rating) as rating,
    hotel.phone as phoneNumber,
    hotel.latitude as latitude,
    hotel.longitude as longitude,
    hotel.price as price,
    hotel.description as about,
    hotel.amenities as amenities,
    EXISTS ((hotel)-[:LIKES_HOTEL]-(:User {uid:$user})) as likes
"""
GET_HOTEL_REVIEWS_QUERY = """
MATCH
    (hotel:Hotel {uid:$hotel})-[review:REVIEWED_HOTEL]-(traveller:Traveller)
RETURN
    traveller.uid as id,
    review.rating as rating,
    left(review.review,150) as review,
    review.datetime as datetime,
    traveller.name as name
ORDER BY datetime 
DESC LIMIT 3
"""

# =Depends(get_registered_user)
# e2813cf7e74a441bbe416589b976475c Selena id
# 874951cbee4443d38867423834efe5c9 TMP id


@router.get("", response_model=HotelApiResponse)
async def get_hotel_detail(hotel=Depends(get_hotel), user=Depends(get_registered_user)):
    try:
        return HotelApiResponse(
            hotelDetails=get_query_response(
                GET_HOTEL_DETAILS_QUERY,
                {"hotel": hotel.uid, "user": user.uid},
            )[0],
            hotelReviews=get_query_response(
                GET_HOTEL_REVIEWS_QUERY, {"hotel": hotel.id}
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
        if not user.likes_hotel.is_connect(hotel):
            user.likes_hotel.connect(hotel)


@router.delete("/unlike")
async def hotel_unlike(hotel=Depends(get_hotel), user=Depends(get_registered_user)):
    with db.transaction:
        if user.likes_hotel.is_connect(hotel):
            user.likes_hotel.disconnect(hotel)
