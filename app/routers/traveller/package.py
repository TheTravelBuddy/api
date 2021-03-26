from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, status
from neomodel import db
from pydantic import BaseModel

from ...dependencies.auth import get_registered_user
from ...dependencies.entities import get_package, get_package_booking
from ...helpers.conversion import deflate_request
from ...helpers.db_query import get_query_response
from ...helpers.queries import (
    GET_PACKAGE_BOOKING_DETAILS_QUERY,
    GET_PACKAGE_DETAILS_QUERY,
    GET_PACKAGE_REVIEWS_ALL_QUERY,
    GET_PACKAGE_REVIEWS_QUERY,
    PACKAGE_SEARCH_QUERY,
)
from ...models.database import PackageBooking

# from typing import List, Optional


# from pydantic import AnyUrl, BaseModel, confloat, constr


# from ...helpers.validation import PHONE_NUMBER_REGEX, PackageAmenitiesEnum


router = APIRouter()


# class PackageReviewResponse(BaseModel):
#     id: str
#     rating: int
#     review: str
#     publishedOn: datetime
#     name: str


# class PackageApiResponse(BaseModel):
#     id: str
#     photos: List[AnyUrl]
#     name: str
#     locality: str
#     address: str
#     postalCode: str
#     city: str
#     rating: Optional[float] = None
#     price: int
#     phoneNumber: constr(min_length=13, max_length=13, regex=PHONE_NUMBER_REGEX)
#     latitude: confloat(ge=-90, le=90)
#     longitude: confloat(ge=-180, le=180)
#     about: str
#     amenities: List[HotelAmenitiesEnum]
#     liked: bool
#     visited: bool
#     reviews: List[HotelReviewResponse]


@router.get("")
async def get_package_detail(
    package=Depends(get_package), user=Depends(get_registered_user)
):
    try:
        return dict(
            **get_query_response(
                GET_PACKAGE_DETAILS_QUERY,
                {"package": package.uid, "user": user.uid},
            )[0],
            reviews=get_query_response(
                GET_PACKAGE_REVIEWS_QUERY, {"package": package.uid, "n": 3}
            ),
        )
    except IndexError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Package not found.",
        )


@router.get("/search")
async def package_search(
    cityId: str,
    budgetMin: int = 0,
    budgetMax: int = 100_000_000,
    query: str = "",
    user=Depends(get_registered_user),
):
    return get_query_response(
        PACKAGE_SEARCH_QUERY,
        {
            "cityId": cityId,
            "budgetMin": budgetMin,
            "budgetMax": budgetMax,
            "query": query.lower(),
        },
    )


@router.post("/like")
async def package_like(package=Depends(get_package), user=Depends(get_registered_user)):
    with db.transaction:
        if not user.likes_package.is_connected(package):
            user.likes_package.connect(package)


@router.delete("/like")
async def package_unlike(
    package=Depends(get_package), user=Depends(get_registered_user)
):
    with db.transaction:
        if user.likes_package.is_connected(package):
            user.likes_package.disconnect(package)


@router.post("/visited")
async def package_visited(
    package=Depends(get_package), user=Depends(get_registered_user)
):
    with db.transaction:
        if not user.taken_package.is_connected(package):
            user.taken_package.connect(package)


@router.delete("/visited")
async def package_not_visited(
    package=Depends(get_package), user=Depends(get_registered_user)
):
    with db.transaction:
        if user.taken_package.is_connected(package):
            user.taken_package.disconnect(package)


class PackageReviewRequest(BaseModel):
    rating: int
    review: str


@router.post("/review")
async def write_package_review(
    review: PackageReviewRequest,
    package=Depends(get_package),
    user=Depends(get_registered_user),
):
    with db.transaction:
        if user.reviewed_package.is_connected(package):
            user.reviewed_package.disconnect(package)

        user.reviewed_package.connect(
            package, deflate_request(review, {"rating", "review"})
        )


@router.get("/reviews")
async def get_package_reviews(
    package=Depends(get_package), _=Depends(get_registered_user)
):
    return get_query_response(GET_PACKAGE_REVIEWS_ALL_QUERY, {"package": package.uid})


class BookingRequest(BaseModel):
    date: datetime
    people: int


@router.post("/booking")
async def add_package_booking(
    booking_details: BookingRequest,
    package=Depends(get_package),
    user=Depends(get_registered_user),
):
    with db.transaction:
        booking = PackageBooking(
            **deflate_request(booking_details, {"people"}),
            booking_date=booking_details.date.date(),
        ).save()
        user.has_package_booking.connect(booking)
        booking.for_package.connect(package)

        return booking.uid


@router.get("/booking")
async def get_package_booking_details(
    package_booking=Depends(get_package_booking),
    user=Depends(get_registered_user),
):
    return get_query_response(
        GET_PACKAGE_BOOKING_DETAILS_QUERY,
        {"packageBooking": package_booking.uid},
    )[0]
