from datetime import date

from fastapi import APIRouter, Depends
from pydantic import AnyUrl, BaseModel

from ...dependencies.auth import get_registered_user
from ...helpers.conversion import deflate_request
from ...helpers.db_query import get_query_response, update_node
from ...helpers.queries import (
    GET_FAVORITE_CITIES,
    GET_USER_BLOGS_QUERY,
    GET_USER_BOOKINGS_QUERY,
)
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


@router.get("/booking")
async def get_bookings(user=Depends(get_registered_user)):
    return get_query_response(GET_USER_BOOKINGS_QUERY, {"user": user.uid})


@router.get("/blog")
async def get_blogs(user=Depends(get_registered_user)):
    return get_query_response(GET_USER_BLOGS_QUERY, {"user": user.uid})


@router.get("/favorite")
async def get_favorites(user=Depends(get_registered_user)):
    return {"cities": get_query_response(GET_FAVORITE_CITIES, {"user": user.uid})}
