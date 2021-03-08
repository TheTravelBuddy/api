from datetime import date

from fastapi import APIRouter, Depends, HTTPException, status
from neomodel import db
from pydantic import AnyUrl, BaseModel, confloat, constr

from ...dependencies.auth import get_registered_user
from ...helpers.conversion import deflate_request
from ...helpers.db_query import update_node
from ...helpers.validatation import GenderEnum, MoodEnum
from ...models.database.nodes import User
from ...models.validation import Traveller

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
