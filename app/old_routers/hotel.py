from typing import List

from fastapi import APIRouter

from ..models import database, validation

router = APIRouter()


@router.get("/")
async def read_hotels() -> List[validation.Hotel]:
    return [validation.Hotel(**hotel.__dict__) for hotel in database.Hotel.nodes.all()]


@router.post("/")
def add_hotel(hotel: validation.Hotel) -> str:
    hotel = database.Hotel(**hotel.__dict__).save()
    return hotel.uid


@router.get("/{hotel_id}")
async def read_hotel(hotel_id: str) -> validation.Hotel:
    return validation.Hotel(**database.Hotel.nodes.first(uid=hotel_id).__dict__)


@router.put("/{hotel_id}")
async def update_hotel(hotel_id: str, hotel: validation.Hotel) -> validation.Hotel:
    selected_hotel = database.Hotel.nodes.first(uid=hotel_id)
    for key, value in hotel.__dict__.items():
        if key != "uid":
            setattr(selected_hotel, key, value)
    selected_hotel.save()
    return validation.Hotel(**selected_hotel.__dict__)


@router.delete("/{hotel_id}")
async def delete_hotel(hotel_id: str):
    database.Hotel.nodes.first(uid=hotel_id).delete()
