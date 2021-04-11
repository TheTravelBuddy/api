from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from neomodel import db
from pydantic import AnyUrl, BaseModel, confloat, constr

from ...helpers.conversion import deflate_request
from ...helpers.db_query import get_query_response
from ...helpers.queries import GET_OWNED_SHOPS_QUERY
from ...models.database import City, Shop, ShopOwner
from .auth import get_business

router = APIRouter()


class NewShopRequest(BaseModel):
    name: str
    description: str
    latitude: confloat(ge=-90, le=90)
    longitude: confloat(ge=-180, le=180)
    photos: List[AnyUrl]
    address: constr(min_length=3, max_length=120)
    locality: str
    postal_code: int
    phone: str


# user=Depends(get_business)
@router.get("/owned")
async def get_owned_shops(shopier=Depends(get_business)):
    return get_query_response(GET_OWNED_SHOPS_QUERY, {"shopierId": shopier.uid})


@router.post("/add")
async def add_shop(shopData: NewShopRequest, city: str, shopier=Depends(get_business)):
    with db.transaction:
        city = City.nodes.get(uid=city)
        shop = Shop(
            **deflate_request(
                shopData,
                {
                    "name",
                    "description",
                    "latitude",
                    "longitude",
                    "photos",
                    "address",
                    "locality",
                    "postal_code",
                    "phone",
                },
            )
        ).save()
        shop.owned_by.connect(shopier)
        shop.located_in.connect(city)
