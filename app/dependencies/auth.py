from fastapi import Header, HTTPException, status
from fastapi.param_functions import Depends
from firebase_admin import auth

from ..models.database import Traveller


async def get_firebase_user(Authorization: str = Header(...)) -> str:
    try:
        token = Authorization.split(" ")[1]
        user = auth.verify_id_token(token)
        return user["uid"]
    except (
        IndexError,
        auth.ExpiredIdTokenError,
        auth.InvalidIdTokenError,
        auth.RevokedIdTokenError,
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication token.",
        )


async def get_registered_user(user_id=Depends(get_firebase_user)):
    try:
        return Traveller.nodes.get(uid=user_id)
    except Traveller.DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not registered.",
        )
