from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends
from pydantic import AnyUrl, BaseModel, confloat, constr

from ...dependencies.auth import get_registered_user
from ...helpers.conversion import Enum, get_query_response
from ...helpers.validatation import PHONE_NUMBER_REGEX

router = APIRouter()


class HotelDetailResponse(BaseModel):
    id: str
    photos: List[AnyUrl]
    name: str
    location: str
    city: str
    rating: float
    phoneNumber: constr(min_length=13, max_length=13, regex=PHONE_NUMBER_REGEX)
    latitude: confloat(ge=-90, le=90)
    longitude: confloat(ge=-180, le=180)
    about: str
    amenities: List[Enum]
    likes: bool


GET_HOTELDETAIL_QUERY = """
MATCH
    (city:City)-[:LOCATED_IN]-(hotel:Hotel {uid:$hotel})-[review:REVIEWED_HOTEL]-(),
    (user:Traveller {uid:$user})
RETURN
    hotel.uid as id,
    hotel.photos as photos,
    hotel.name as name,
    city.name as city,
    hotel.address+" "+hotel.locality+" "+hotel.postal_code as location,
    AVG(review.rating) as rating,
    hotel.phone as phoneNumber,
    hotel.latitude as latitude,
    hotel.longitude as longitude,
    hotel.description as about,
    hotel.amenities as amenities,
    EXISTS ((hotel)-[:LIKES_HOTEL]-(user)) as likes
"""


@router.get("", response_model=HotelDetailResponse)
async def get_hotel_detail(id: int, user: int):
    return HotelDetailResponse(
        get_query_response(GET_HOTELDETAIL_QUERY, {"hotel": id, "user": userid})
    )
