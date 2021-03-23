from datetime import date
from typing import Union

from fastapi import APIRouter, Depends
from pydantic import AnyUrl, BaseModel, constr

from ...dependencies.auth import get_firebase_user
from ...helpers.conversion import deflate_request
from ...helpers.validation import PHONE_NUMBER_REGEX, GenderEnum, MoodEnum
from ...models.database import Traveller

router = APIRouter()


class AuthUserRespose(BaseModel):
    pass


class RegisteredUserResponse(AuthUserRespose):
    registered: bool = True
    name: constr(min_length=3, max_length=120)
    phoneNumber: constr(min_length=13, max_length=13, regex=PHONE_NUMBER_REGEX)
    gender: GenderEnum
    dob: date
    mood: MoodEnum = MoodEnum.Mixed
    profilePicture: AnyUrl


class UnregisteredUserResponse(AuthUserRespose):
    registered: bool = False


@router.get(
    "/userData", response_model=Union[RegisteredUserResponse, UnregisteredUserResponse]
)
async def get_traveller(user=Depends(get_firebase_user)):
    try:
        traveller = Traveller.nodes.get(firebase_id=user["uid"])
        return RegisteredUserResponse(
            **deflate_request(
                traveller,
                {
                    "name",
                    ("phone", "phoneNumber"),
                    "gender",
                    "mood",
                    "dob",
                    ("profile_picture", "profilePicture"),
                },
            )
        )
    except Traveller.DoesNotExist:
        return UnregisteredUserResponse(uid=user["uid"])


class RegisterUserRequest(BaseModel):
    name: constr(min_length=3, max_length=120)
    gender: GenderEnum
    dob: date
    mood: MoodEnum = MoodEnum.Mixed


@router.post("/registerUser")
async def register_user(
    userDetails: RegisterUserRequest,
    user=Depends(get_firebase_user),
):
    Traveller(
        **deflate_request(user, {("uid", "firebase_id"), ("phone_number", "phone")}),
        **deflate_request(userDetails, {"name", "gender", "dob", "mood"}),
    ).save()
