from typing import List

from fastapi import APIRouter, Depends
from pydantic import BaseModel, confloat

from ...dependencies.auth import get_registered_user
from ...helpers.db_query import get_query_response
from ...helpers.queries import GET_ALL_CITIES_QUERY, GET_FAV_CITIES_QUERY

router = APIRouter()


class CityApiResponse(BaseModel):
    id: str
    name: str
    latitude: confloat(ge=-90, le=90)
    longitude: confloat(ge=-180, le=180)


@router.get("", response_model=List[CityApiResponse])
async def get_cities(_=Depends(get_registered_user)):
    return get_query_response(GET_ALL_CITIES_QUERY)


@router.get("/favs")
async def get_fav_cities(user: str):
    return get_query_response(GET_FAV_CITIES_QUERY, {"userId": user})
