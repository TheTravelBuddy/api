from typing import List

from fastapi import APIRouter, Depends
from pydantic import BaseModel, confloat

from ...dependencies.auth import get_registered_user
from ...helpers.db_query import get_query_response

router = APIRouter()


class CityApiResponse(BaseModel):
    id: str
    name: str
    latitude: confloat(ge=-90, le=90)
    longitude: confloat(ge=-180, le=180)


GET_ALL_CITY_QUERY = """
MATCH (city:City)
RETURN
    city.uid AS id,
    city.name AS name,
    city.latitude AS latitude,
    city.longitude AS longitude
"""


@router.get("", response_model=List[CityApiResponse])
async def get_cities(_=Depends(get_registered_user)):
    return get_query_response(GET_ALL_CITY_QUERY)
