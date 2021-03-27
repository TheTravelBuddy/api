from fastapi import APIRouter, Depends, HTTPException, status
from neomodel import db
from pydantic import AnyUrl, BaseModel, confloat, constr

from ...helpers.db_query import get_query_response
from ...helpers.queries import GET_OWNED_HOTELS_QUERY
from ...models.database import Hotel, HotelOwner
from .auth import get_business

router = APIRouter()


# user=Depends(get_business)
@router.get("/owned")
async def get_hotels(hotelier=Depends(get_business)):
    return get_query_response(GET_OWNED_HOTELS, {"hotelierId": hotelier.uid})
