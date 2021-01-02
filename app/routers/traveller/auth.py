from typing import Union

from fastapi import APIRouter, Depends
from pydantic import BaseModel, constr

from ...dependencies.auth import get_firebase_user
from ...models.database import Traveller

router = APIRouter()


class AuthUserRespose(BaseModel):
    uid: str


class RegisteredUserResponse(AuthUserRespose):
    registered: bool = True
    name: constr(min_length=3, max_length=120)


class UnregisteredUserResponse(AuthUserRespose):
    registered: bool = False


@router.get(
    "/userData", response_model=Union[RegisteredUserResponse, UnregisteredUserResponse]
)
async def get_traveller(user_id=Depends(get_firebase_user)):
    try:
        traveller = Traveller.nodes.get(uid=user_id)
        return RegisteredUserResponse(
            uid=user_id, name=traveller.name, phoneNumber=traveller.phone
        )
    except Traveller.DoesNotExist:
        return UnregisteredUserResponse(uid=user_id)
