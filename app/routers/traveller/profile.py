from datetime import date

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from ...dependencies.auth import get_registered_user
from ...helpers.conversion import deflate_request, get_query_response
from ...helpers.db_query import update_node
from ...helpers.queries import GET_ALL_FAV_QUERY
from ...helpers.validation import GenderEnum, MoodEnum

router = APIRouter()


class ProfileEditRequest(BaseModel):
    name: str
    dob: date
    gender: GenderEnum
    mood: MoodEnum


@router.put("/edit")
async def edit_profile(
    userDetail: ProfileEditRequest, user=Depends(get_registered_user)
):
    update_node(user, deflate_request(userDetail, {"name", "gender", "dob", "mood"}))


@router.get("/favs")
async def profile_favs(user: str):
    return get_query_response(GET_ALL_FAV_QUERY, {"userId": user})
