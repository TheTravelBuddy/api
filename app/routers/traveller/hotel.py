from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from neomodel import db
from pydantic import AnyUrl, BaseModel, confloat, constr

from ...dependencies.auth import get_registered_user
from ...dependencies.entities import get_hotel, get_hotel_booking
from ...helpers.conversion import deflate_request
from ...helpers.db_query import get_query_response
from ...helpers.queries import (
    GET_FAV_HOTELS_QUERY,
    GET_HOTEL_BOOKING_DETAILS_QUERY,
    GET_HOTEL_DETAILS_QUERY,
    GET_HOTEL_REVIEWS_ALL_QUERY,
    GET_HOTEL_REVIEWS_QUERY,
    HOTEL_SEARCH_QUERY,
)
from ...helpers.validation import PHONE_NUMBER_REGEX, HotelAmenitiesEnum
from ...models.database.nodes import HotelBooking

router = APIRouter()


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
    amenities: List[HotelAmenitiesEnum]
    liked: bool
    visited: bool
    reviews: List[HotelReviewResponse]


@router.get("", response_model=HotelApiResponse)
async def get_hotel_detail(hotel=Depends(get_hotel), user=Depends(get_registered_user)):
    try:
        return HotelApiResponse(
            **get_query_response(
                GET_HOTEL_DETAILS_QUERY,
                {"hotel": hotel.uid, "user": user.uid},
            )[0],
            reviews=get_query_response(
                GET_HOTEL_REVIEWS_QUERY, {"hotel": hotel.uid, "n": 3}
            ),
        )
    except IndexError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Hotel not found.",
        )


@router.get("/search")
async def hotel_search(
    cityId: str,
    budgetMin: int = 0,
    budgetMax: int = 100_000_000,
    query: str = "",
    user=Depends(get_registered_user),
):
    return get_query_response(
        HOTEL_SEARCH_QUERY,
        {
            "cityId": cityId,
            "budgetMin": budgetMin,
            "budgetMax": budgetMax,
            "query": query.lower(),
        },
    )


@router.post("/like")
async def hotel_like(hotel=Depends(get_hotel), user=Depends(get_registered_user)):
    with db.transaction:
        if not user.likes_hotel.is_connected(hotel):
            user.likes_hotel.connect(hotel)


@router.delete("/like")
async def hotel_unlike(hotel=Depends(get_hotel), user=Depends(get_registered_user)):
    with db.transaction:
        if user.likes_hotel.is_connected(hotel):
            user.likes_hotel.disconnect(hotel)


@router.post("/visited")
async def hotel_visited(hotel=Depends(get_hotel), user=Depends(get_registered_user)):
    with db.transaction:
        if not user.visited_hotel.is_connected(hotel):
            user.visited_hotel.connect(hotel)


@router.delete("/visited")
async def hotel_not_visited(
    hotel=Depends(get_hotel), user=Depends(get_registered_user)
):
    with db.transaction:
        if user.visited_hotel.is_connected(hotel):
            user.visited_hotel.disconnect(hotel)


class HotelReviewRequest(BaseModel):
    rating: int
    review: str


@router.post("/review")
async def write_hotel_review(
    review: HotelReviewRequest,
    hotel=Depends(get_hotel),
    user=Depends(get_registered_user),
):
    with db.transaction:
        if user.reviewed_hotel.is_connected(hotel):
            user.reviewed_hotel.disconnect(hotel)

        user.reviewed_hotel.connect(
            hotel, deflate_request(review, {"rating", "review"})
        )


@router.get("/reviews")
async def get_hotel_reviews(hotel=Depends(get_hotel), _=Depends(get_registered_user)):
    return get_query_response(GET_HOTEL_REVIEWS_ALL_QUERY, {"hotelId": hotel.uid})


class BookingRequest(BaseModel):
    date: datetime
    days: int
    adults: int
    children: int = 0
    rooms: int


@router.post("/booking")
async def add_hotel_booking(
    booking_details: BookingRequest,
    hotel=Depends(get_hotel),
    user=Depends(get_registered_user),
):
    with db.transaction:
        booking = HotelBooking(
            **deflate_request(
                booking_details,
                {"days", "adults", "children", "rooms"},
            ),
            booking_date=booking_details.date.date(),
        ).save()
        user.has_hotel_booking.connect(booking)
        booking.for_hotel.connect(hotel)

        return booking.uid


@router.get("/booking")
async def get_hotel_booking(
    hotel_booking=Depends(get_hotel_booking),
    user=Depends(get_registered_user),
):
    return get_query_response(
        GET_HOTEL_BOOKING_DETAILS_QUERY,
        {"hotelBooking": hotel_booking.uid},
    )[0]


@router.get("/favs")
async def get_fav_hotels(user=Depends(get_registered_user)):
    return get_query_response(GET_FAV_HOTELS_QUERY, {"userId": user.uid})
