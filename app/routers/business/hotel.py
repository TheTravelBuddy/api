from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from neomodel import db
from pydantic import AnyUrl, BaseModel, confloat, constr

from ...helpers.conversion import deflate_request
from ...helpers.db_query import get_query_response
from ...helpers.queries import (
    GET_HOTEL_DETAILS_QUERY,
    GET_HOTEL_REVIEWS_QUERY,
    GET_OWNED_HOTELS_QUERY,
)
from ...helpers.validation import PHONE_NUMBER_REGEX, HotelAmenitiesEnum
from ...models.database import Hotel
from .auth import get_business

router = APIRouter()


class NewHotelRequest(BaseModel):
    name: str
    price: int
    description: str
    photos: List[AnyUrl]
    address: constr(min_length=10, max_length=120)
    locality: str
    postal_code: int
    latitude: float
    longitude: float
    phone: str
    amenities: List[HotelAmenitiesEnum]


GET_HOTEL_DETAIL_QUERY = """
MATCH
    (city:City)-[:LOCATED_IN]-(hotel:Hotel {uid:$hotel})
OPTIONAL MATCH
    (hotel)-[review:REVIEWED_HOTEL]-()
OPTIONAL MATCH
	(hotel)-[likes:LIKES_HOTEL]-()
RETURN
    hotel.uid AS id,
    hotel.photos AS photos,
    hotel.name AS name,
    city.name AS city,
    hotel.locality AS locality,
    hotel.address AS address,
    hotel.postal_code AS postalCode,
    AVG(review.rating) AS rating,
    hotel.phone AS phoneNumber,
    hotel.latitude AS latitude,
    hotel.longitude AS longitude,
    hotel.price AS price,
    hotel.description AS about,
    hotel.amenities AS amenities,
    COUNT(likes) AS likes
"""


class HotelReviewResponse(BaseModel):
    id: str
    rating: int
    review: str
    publishedOn: datetime
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
    likes: int
    amenities: List[HotelAmenitiesEnum]
    reviews: List[HotelReviewResponse]


# user=Depends(get_business)
@router.get("/owned")
async def get_owned_hotels(hotelier=Depends(get_business)):
    return get_query_response(GET_OWNED_HOTELS, {"hotelierId": hotelier.uid})


@router.post("/add")
async def add_hotel(hotelData: NewHotelRequest, hotelier=Depends(get_business)):
    with db.transaction:
        hotel = Hotel(
            **deflate_request(
                hotelData,
                {
                    "name",
                    "price",
                    "photos",
                    "address",
                    "description",
                    "locality",
                    "postal_code",
                    "latitude",
                    "longitude",
                    "phone",
                    "amenities",
                },
            )
        ).save()
        hotel.owned_by.connect(hotelier)


# ,hotelier=Depends(get_business)
@router.get("/hoteldetail")
async def hotel_detail(hotel: str):
    try:
        return HotelApiResponse(
            **get_query_response(
                GET_HOTEL_DETAIL_QUERY,
                {"hotel": hotel},
            )[0],
            reviews=get_query_response(
                GET_HOTEL_REVIEWS_QUERY, {"hotel": hotel, "n": 3}
            ),
        )
    except IndexError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Hotel not found.",
        )
