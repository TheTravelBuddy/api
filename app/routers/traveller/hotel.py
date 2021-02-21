from datetime import datetime
from enum import Enum
from typing import List, Optional

from fastapi import APIRouter, Depends
from pydantic import AnyUrl, BaseModel, confloat, constr

from ...dependencies.auth import get_registered_user
from ...helpers.conversion import get_query_response
from ...helpers.validatation import PHONE_NUMBER_REGEX, HotelAmenitiesEnum
from ...models.database import Hotel, Traveller

router = APIRouter()


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


GET_HOTELDETAIL_QUERY = """
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
GET_HOTELDETAILREVIEW_QUERY = """
MATCH
    (hotel:Hotel {uid:$hotel})-[review:REVIEWED_HOTEL]-(traveller:Traveller)
RETURN
    traveller.uid as id,
    review.rating as rating,
    left(review.review,150) as review,
    review.datetime as datetime,
    traveller.name as name
ORDER BY datetime DESC LIMIT 3
"""

# =Depends(get_registered_user)
# e2813cf7e74a441bbe416589b976475c Selena id
# 874951cbee4443d38867423834efe5c9 TMP id


@router.get("", response_model=HotelApiResponse)
async def get_hotel_detail(id: str, user=Depends(get_registered_user)):
    return HotelApiResponse(
        hotelDetails=get_query_response(
            GET_HOTELDETAIL_QUERY,
            {"hotel": id, "user": user.uid},
        )[0],
        hotelReviews=get_query_response(GET_HOTELDETAILREVIEW_QUERY, {"hotel": id}),
    )


@router.post("/like")
async def hotel_like(id: str, user: str):
    traveller = Traveller.nodes.get(uid=user)
    hotel = Hotel.nodes.get(uid=id)
    traveller.likes_hotel.connect(hotel)
    # if traveller.likes_hotel.is_connected(hotel):
    #     print("Relation Exists")
    # else:


@router.delete("/unlike")
async def hotel_unlike(id: str, user: str):
    traveller = Traveller.nodes.get(uid=user)
    hotel = Hotel.nodes.get(uid=id)
    traveller.likes_hotel.disconnect(hotel)
