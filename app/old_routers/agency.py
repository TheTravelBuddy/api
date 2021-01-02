from typing import List

from fastapi import APIRouter

from ..models import database, validation

router = APIRouter()


@router.get("/")
async def read_agencys() -> List[validation.Agency]:
    return [
        validation.Agency(**agency.__dict__) for agency in database.Agency.nodes.all()
    ]


@router.post("/")
def add_agency(agency: validation.Agency) -> str:
    agency = database.Agency(**agency.__dict__).save()
    return agency.uid


@router.get("/{agency_id}")
async def read_agency(agency_id: str) -> validation.Agency:
    return validation.Agency(**database.Agency.nodes.first(uid=agency_id).__dict__)


@router.put("/{agency_id}")
async def update_agency(agency_id: str, agency: validation.Agency) -> validation.Agency:
    selected_agency = database.Agency.nodes.first(uid=agency_id)
    for key, value in agency.__dict__.items():
        if key != "uid":
            setattr(selected_agency, key, value)
    selected_agency.save()
    return validation.Agency(**selected_agency.__dict__)


@router.delete("/{agency_id}")
async def delete_agency(agency_id: str):
    database.Agency.nodes.first(uid=agency_id).delete()
