from typing import List

from fastapi import APIRouter

from ..models import database, validation

router = APIRouter()


@router.get("/")
async def read_attractions() -> List[validation.Attraction]:
    return [
        validation.Attraction(**attraction.__dict__)
        for attraction in database.Attraction.nodes.all()
    ]


@router.post("/")
def add_attraction(attraction: validation.Attraction) -> str:
    attraction = database.Attraction(**attraction.__dict__).save()
    return attraction.uid


@router.get("/{attraction_id}")
async def read_attraction(attraction_id: str) -> validation.Attraction:
    return validation.Attraction(
        **database.Attraction.nodes.first(uid=attraction_id).__dict__
    )


@router.put("/{attraction_id}")
async def update_attraction(
    attraction_id: str, attraction: validation.Attraction
) -> validation.Attraction:
    selected_attraction = database.Attraction.nodes.first(uid=attraction_id)
    for key, value in attraction.__dict__.items():
        if key != "uid":
            setattr(selected_attraction, key, value)
    selected_attraction.save()
    return validation.Attraction(**selected_attraction.__dict__)


@router.delete("/{attraction_id}")
async def delete_attraction(attraction_id: str):
    database.Attraction.nodes.first(uid=attraction_id).delete()
