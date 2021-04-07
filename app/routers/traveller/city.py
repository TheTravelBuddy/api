from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from neomodel import db
from pydantic import BaseModel, confloat

from ...dependencies.auth import get_registered_user
from ...dependencies.entities import get_city
from ...helpers.db_query import get_query_response
from ...helpers.queries import GET_ALL_CITIES_QUERY, GET_CITY_DETAILS_QUERY

router = APIRouter()


class CitiesApiResponse(BaseModel):
    id: str
    name: str
    latitude: confloat(ge=-90, le=90)
    longitude: confloat(ge=-180, le=180)


@router.get("/all", response_model=List[CitiesApiResponse])
async def get_cities(_=Depends(get_registered_user)):
    return get_query_response(GET_ALL_CITIES_QUERY)


@router.get("")
async def get_city_detail(city=Depends(get_city), user=Depends(get_registered_user)):
    try:
        return get_query_response(
            GET_CITY_DETAILS_QUERY,
            {"city": city.uid, "user": user.uid},
        )[0]
    except IndexError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Hotel not found.",
        )


@router.post("/like")
async def city_like(city=Depends(get_city), user=Depends(get_registered_user)):
    with db.transaction:
        if not user.likes_city.is_connected(city):
            user.likes_city.connect(city)


@router.delete("/like")
async def city_unlike(city=Depends(get_city), user=Depends(get_registered_user)):
    with db.transaction:
        if user.likes_city.is_connected(city):
            user.likes_city.disconnect(city)
