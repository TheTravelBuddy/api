from typing import List

from fastapi import APIRouter

from ..models import database, validation

router = APIRouter()


@router.get("/")
async def read_hotel_owners() -> List[validation.HotelOwner]:
    return [
        validation.HotelOwner(**hotel_owner.__dict__)
        for hotel_owner in database.HotelOwner.nodes.all()
    ]


@router.post("/")
def add_hotel_owner(hotel_owner: validation.HotelOwner) -> str:
    hotel_owner = database.HotelOwner(**hotel_owner.__dict__).save()
    return hotel_owner.uid


@router.get("/{hotel_owner_id}")
async def read_hotel_owner(hotel_owner_id: str) -> validation.HotelOwner:
    return validation.HotelOwner(
        **database.HotelOwner.nodes.first(uid=hotel_owner_id).__dict__
    )


@router.put("/{hotel_owner_id}")
async def update_hotel_owner(
    hotel_owner_id: str, hotel_owner: validation.HotelOwner
) -> validation.HotelOwner:
    selected_hotel_owner = database.HotelOwner.nodes.first(uid=hotel_owner_id)
    for key, value in hotel_owner.__dict__.items():
        if key != "uid":
            setattr(selected_hotel_owner, key, value)
    selected_hotel_owner.save()
    return validation.HotelOwner(**selected_hotel_owner.__dict__)


@router.delete("/{hotel_owner_id}")
async def delete_hotel_owner(hotel_owner_id: str):
    database.HotelOwner.nodes.first(uid=hotel_owner_id).delete()
