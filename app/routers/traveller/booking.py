from typing import List

from fastapi import APIRouter, Depends
from pydantic import AnyUrl, BaseModel, confloat, constr

from ...dependencies.auth import get_registered_user
from ...helpers.db_query import get_query_response
from ...helpers.queries import (
    GET_BUDGET_HOTELS_QUERY,
    GET_NEARBY_HOTELS_QUERY,
    GET_RECOMMENDED_PACKAGES_QUERY,
    GET_TOP_HOTELS_QUERY,
    GET_TOP_PACKAGES_QUERY,
)

router = APIRouter()


class PackagePreviewResponse(BaseModel):
    id: str
    name: constr(min_length=5, max_length=120)
    coverUri: AnyUrl
    rating: float


class HotelPreviewResponse(BaseModel):
    id: str
    name: constr(max_length=120)
    coverUri: AnyUrl
    rating: float
    locality: str
    city: str
    price: int


class BookingApiResponse(BaseModel):
    recommendedPackages: List[PackagePreviewResponse]
    topPackages: List[PackagePreviewResponse]
    nearbyHotels: List[HotelPreviewResponse]
    budgetHotels: List[HotelPreviewResponse]


@router.get("", response_model=BookingApiResponse)
async def get_home_data(
    latitude: confloat(ge=-90, le=90) = None,
    longitude: confloat(ge=-180, le=180) = None,
    user=Depends(get_registered_user),
):
    return BookingApiResponse(
        recommendedPackages=get_query_response(
            GET_RECOMMENDED_PACKAGES_QUERY, {"n": 3}
        ),
        topPackages=get_query_response(GET_TOP_PACKAGES_QUERY, {"n": 5}),
        nearbyHotels=get_query_response(
            GET_NEARBY_HOTELS_QUERY,
            {"n": 5, "latitude": latitude, "longitude": longitude},
        )
        if latitude and longitude
        else get_query_response(GET_TOP_HOTELS_QUERY, {"n": 5}),
        budgetHotels=get_query_response(GET_BUDGET_HOTELS_QUERY, {"n": 5}),
    )
