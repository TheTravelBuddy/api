from fastapi import APIRouter, Depends

from ...dependencies.auth import get_registered_user
from ...helpers.db_query import get_query_response
from ...helpers.queries import GET_FAV_SHOPS_QUERY

router = APIRouter()


@router.get("/favs")
async def get_fav_shops(user=Depends(get_registered_user)):
    return get_query_response(GET_FAV_SHOPS_QUERY, {"userId": user.uid})
