from typing import List

from fastapi import APIRouter, Depends
from pydantic import AnyUrl, BaseModel, constr

from ...dependencies.auth import get_registered_user
from ...helpers.db_query import get_query_response
from ...helpers.queries import (
    GET_TOP_BLOGS_QUERY,
    GET_TOP_DESTINATIONS_QUERY,
    GET_TOP_HOTELS_QUERY,
    GET_TOP_PACKAGES_QUERY,
)

router = APIRouter()


class PackagePreviewResponse(BaseModel):
    id: str
    name: constr(min_length=5, max_length=120)
    coverUri: AnyUrl
    rating: float


class DestinationPreviewResponse(BaseModel):
    id: str
    name: constr(min_length=3, max_length=120)
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


class BlogPreviewResponse(BaseModel):
    id: str
    authorProfile: AnyUrl
    title: str
    content: str
    likes: int


class HomeApiResponse(BaseModel):
    topPackages: List[PackagePreviewResponse]
    topDestinations: List[DestinationPreviewResponse]
    topHotels: List[HotelPreviewResponse]
    topBlogs: List[BlogPreviewResponse]


@router.get("", response_model=HomeApiResponse)
async def get_home_data(user=Depends(get_registered_user)):
    return HomeApiResponse(
        topPackages=get_query_response(GET_TOP_PACKAGES_QUERY, {"n": 3}),
        topDestinations=get_query_response(GET_TOP_DESTINATIONS_QUERY, {"n": 5}),
        topHotels=get_query_response(GET_TOP_HOTELS_QUERY, {"n": 5}),
        topBlogs=get_query_response(GET_TOP_BLOGS_QUERY, {"n": 5}),
    )
