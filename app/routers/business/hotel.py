from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from neomodel import db
from pydantic import AnyUrl, BaseModel, confloat, constr

from ...helpers.conversion import deflate_request
from ...helpers.db_query import get_query_response
from ...helpers.queries import GET_OWNED_HOTELS_QUERY
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
    amenities: List[str]


# user=Depends(get_business)
@router.get("/owned")
async def get_owned_hotels(hotelier=Depends(get_business)):
    return get_query_response(GET_OWNED_HOTELS, {"hotelierId": hotelier.uid})


@router.post("/add")
async def add_hotel(hotelier: str, hotelData: NewHotelRequest):
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
