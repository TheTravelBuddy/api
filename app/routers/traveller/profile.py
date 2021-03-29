from datetime import date

from fastapi import APIRouter, Depends
from pydantic import AnyUrl, BaseModel

from ...dependencies.auth import get_registered_user
from ...helpers.conversion import deflate_request
from ...helpers.db_query import update_node
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


class ProfilePhotoEditRequest(BaseModel):
    profilePicture: AnyUrl


@router.put("/picture")
async def edit_profile_photo(
    userDetail: ProfilePhotoEditRequest, user=Depends(get_registered_user)
):
    user.profile_picture = str(userDetail.profilePicture)
    user.save()
