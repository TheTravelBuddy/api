from fastapi import APIRouter, Depends

from ...helpers.db_query import get_query_response
from ...helpers.queries import GET_OFFERED_PACKAGES_QUERY
from .auth import get_business

router = APIRouter()


# user=Depends(get_business)
@router.get("/owned")
async def get_offered_packages(agency=Depends(get_business)):
    return get_query_response(GET_OFFERED_PACKAGES_QUERY, {"agencyId": agency.uid})
