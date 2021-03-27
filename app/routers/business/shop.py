from fastapi import APIRouter, Depends, HTTPException, status
from neomodel import db
from pydantic import AnyUrl, BaseModel, confloat, constr

from ...helpers.db_query import get_query_response
from ...helpers.queries import GET_OWNED_SHOPS_QUERY
from .auth import get_business

router = APIRouter()


# user=Depends(get_business)
@router.get("/owned")
async def get_owned_shops(shopier=Depends(get_business)):
    return get_query_response(GET_OWNED_SHOPS_QUERY, {"shopierId": shopier.uid})
