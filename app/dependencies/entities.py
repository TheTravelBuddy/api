from fastapi import HTTPException, status

from ..models.database import Blog, Hotel, HotelBooking


async def get_blog(blogId: str):
    try:
        return Blog.nodes.get(uid=blogId)
    except Blog.DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found."
        )


async def get_hotel(hotelId: str):
    try:
        return Hotel.nodes.get(uid=hotelId)
    except Hotel.DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Hotel not found."
        )


async def get_hotel_booking(hotelBookingId: str):
    try:
        return HotelBooking.nodes.get(uid=hotelBookingId)
    except HotelBooking.DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Booking not found."
        )
