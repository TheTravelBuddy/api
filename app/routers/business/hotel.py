from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from neomodel import db
from pydantic import AnyUrl, BaseModel, confloat, constr

from ...helpers.conversion import deflate_request
from ...helpers.db_query import get_query_response
from ...helpers.queries import GET_OWNED_HOTELS_QUERY
from ...helpers.validation import HotelAmenitiesEnum
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
