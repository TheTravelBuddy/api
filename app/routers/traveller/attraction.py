from fastapi import APIrouter, Depends

from ...dependencies.auth import get_registered_user
from ...helpers.db_query import get_query_response
from ...helpers.queries import GET_FAV_ATT_QUERY

router = APIrouter()


@router.get("/fav")
async def get_fav_attraction(user=Depends(get_registered_user)):
    return get_query_response(GET_FAV_ATT_QUERY, {"userId": user.uid})
