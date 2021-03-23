from typing import Union

from fastapi import APIRouter, Depends
from pydantic import AnyUrl, BaseModel, constr

from ...dependencies.auth import get_firebase_user
from ...helpers.conversion import deflate_request
from ...helpers.validation import PHONE_NUMBER_REGEX, BusinessTypeEnum
from ...models.database import Agency, Business, HotelOwner, ShopOwner

router = APIRouter()


business_user_selector = {
    "TRAVEL_AGENCY": Agency,
    "HOTEL_OWNER": HotelOwner,
    "SHOP_OWNER": ShopOwner,
}


class AuthBusinessRespose(BaseModel):
    pass


class RegisteredBusinessResponse(AuthBusinessRespose):
    registered: bool = True
    name: constr(min_length=3, max_length=120)
    phoneNumber: constr(min_length=13, max_length=13, regex=PHONE_NUMBER_REGEX)
    profilePicture: AnyUrl
    businessType: BusinessTypeEnum


class UnregisteredBusinessResponse(AuthBusinessRespose):
    registered: bool = False


@router.get(
    "/userData",
    response_model=Union[RegisteredBusinessResponse, UnregisteredBusinessResponse],
)
async def get_business(user=Depends(get_firebase_user)):
    try:
        business = Business.nodes.get(firebase_id=user["uid"])
        return RegisteredBusinessResponse(
            **deflate_request(
                business,
                {
                    "name",
                    ("phone", "phoneNumber"),
                    ("profile_picture", "profilePicture"),
                    ("business_type", "businessType"),
                },
            )
        )
    except Business.DoesNotExist:
        return UnregisteredBusinessResponse(uid=user["uid"])


class RegisterBusinessRequest(BaseModel):
    name: constr(min_length=3, max_length=120)
    businessType: BusinessTypeEnum


@router.post("/registerUser")
async def register_user(
    userDetails: RegisterBusinessRequest,
    user=Depends(get_firebase_user),
):
    BusinessUser = business_user_selector[userDetails.businessType]
    BusinessUser(
        **deflate_request(
            user,
            {
                ("uid", "firebase_id"),
                ("phone_number", "phone"),
            },
        ),
        **deflate_request(userDetails, {"name"}),
    ).save()
