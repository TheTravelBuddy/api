from typing import List

from fastapi import APIRouter

from ..models import database, validation

router = APIRouter()


@router.get("/")
async def read_cities() -> List[validation.City]:
    return [validation.City(**city.__dict__) for city in database.City.nodes.all()]


@router.post("/")
def add_city(city: validation.City) -> str:
    city = database.City(**city.__dict__).save()
    return city.uid


@router.get("/{city_id}")
async def read_city(city_id: str) -> validation.City:
    return validation.City(**database.City.nodes.first(uid=city_id).__dict__)


@router.put("/{city_id}")
async def update_city(city_id: str, city: validation.City) -> validation.City:
    selected_city = database.City.nodes.first(uid=city_id)
    for key, value in city.__dict__.items():
        if key != "uid":
            setattr(selected_city, key, value)
    selected_city.save()
    return validation.City(**selected_city.__dict__)


@router.delete("/{city_id}")
async def delete_city(city_id: str):
    database.City.nodes.first(uid=city_id).delete()
