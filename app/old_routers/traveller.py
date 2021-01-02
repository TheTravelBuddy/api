from typing import List

from fastapi import APIRouter

from ..models import database, validation

router = APIRouter()


@router.get("/")
async def read_travellers() -> List[validation.Traveller]:
    return [
        validation.Traveller(**traveller.__dict__)
        for traveller in database.Traveller.nodes.all()
    ]


@router.post("/")
def add_traveller(traveller: validation.Traveller) -> str:
    traveller = database.Traveller(**traveller.__dict__).save()
    return traveller.uid


@router.get("/{travller_id}")
async def read_traveller(travller_id: str) -> validation.Traveller:
    return validation.Traveller(
        **database.Traveller.nodes.first(uid=travller_id).__dict__
    )


@router.put("/{travller_id}")
async def update_traveller(
    travller_id: str, traveller: validation.Traveller
) -> validation.Traveller:
    selected_traveller = database.Traveller.nodes.first(uid=travller_id)
    for key, value in traveller.__dict__.items():
        if key != "uid":
            setattr(selected_traveller, key, value)
    selected_traveller.save()
    return validation.Traveller(**selected_traveller.__dict__)


@router.delete("/{traveller_id}")
async def delete_traveller(traveller_id: str):
    database.Traveller.nodes.first(uid=traveller_id).delete()
