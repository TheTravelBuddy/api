from typing import List

from fastapi import APIRouter, Depends
from pydantic import AnyUrl, BaseModel, constr

from ...dependencies.auth import get_registered_user
from ...helpers.conversion import get_query_response
from ...models.database import Traveller

router = APIRouter()


class ProfileBookingsResponse(BaseModel):
    pass


class ProfileReviewsResponse(BaseModel):
    pass


class ProfileBlogsResponse(BaseModel):
    pass


class ProfileFavsResponse(BaseModel):
    pass


class ProfileApiResponse(BaseModel):
    id: str
    name: str
    coverUri: AnyUrl
    phoneNumber: str
    name: str
    bookings: List[ProfileBookingsResponse]
    reviews: List[ProfileReviewsResponse]
    blogs: List[ProfileBlogsResponse]
    favs: List[ProfileFavsResponse]


# =Depends(get_registered_user)
@router.get("", response_model=ProfileApiResponse)
async def get_profile_data(user: str):
    traveller = Traveller.nodes.get(uid=user)
    bookings = traveller.nodes.booked_hotel.all()
    bookings += traveller.nodes.booked_package.all()
    # print("bookings:", bookings)
    reviews = traveller.nodes.reviewed_attraction.all()
    reviews += traveller.nodes.reviewed_city.all()
    reviews += traveller.nodes.reviewed_package.all()
    reviews += traveller.nodes.reviewed_shop.all()
    reviews += traveller.nodes.reviewed_hotel.all()
    # print("reviews:", reviews)
    blogs = traveller.nodes.author_of.all()
    # print("blogs:", blogs)
    favs = traveller.nodes.likes_hotel.all()
    favs += traveller.nodes.likes_city.all()
    favs += traveller.nodes.likes_package.all()
    favs += traveller.nodes.likes_shop.all()
    favs += traveller.nodes.likes_blog.all()
    favs += traveller.nodes.likes_attraction.all()
    print("favs:", favs)
