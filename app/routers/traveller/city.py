from typing import List

from fastapi import APIRouter, Depends
from neomodel import db
from pydantic import AnyUrl, BaseModel

from ...dependencies.auth import get_registered_user
from ...helpers.db_query import get_query_response
from ...models.database import City

router = APIRouter()


class CityApiResponse(BaseModel):
    id: str
    name: str


# user=Depends(get_registered_user)
GET_ALL_CITY_QUERY = """
MATCH (c:City) 
RETURN 
    c.uid as id, 
    c.name as name
"""


@router.get("", response_model=List[CityApiResponse])
async def get_cities():
    return get_query_response(GET_ALL_CITY_QUERY)
