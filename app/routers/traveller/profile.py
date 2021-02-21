from typing import List

from fastapi import APIRouter, Depends
from pydantic import AnyUrl, BaseModel, constr

from ...dependencies.auth import get_registered_user
from ...helpers.conversion import get_query_response

router = APIRouter()


class ProfileBookingResponse(BaseModel):
    pass


class ProfileReviewResponse(BaseModel):
    pass


class ProfileBlogResponse(BaseModel):
    pass


class ProfileFavResponse(BaseModel):
    pass


class ProfileApiResponse(BaseModel):
    id: str
    name: str
    coverUri: AnyUrl
    phoneNumber: str
    name: str
    bookings: List[ProfileBookingResponse]
    reviews: List[ProfileReviewResponse]
    blogs: List[ProfileBlogResponse]
    favs: List[ProfileFavResponse]
