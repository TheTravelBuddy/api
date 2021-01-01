from typing import List

from fastapi import APIRouter

from ..models import database, validation

router = APIRouter()


@router.get("/")
async def read_shops() -> List[validation.Shop]:
    return [validation.Shop(**shop.__dict__) for shop in database.Shop.nodes.all()]


@router.post("/")
def add_shop(shop: validation.Shop) -> str:
    shop = database.Shop(**shop.__dict__).save()
    return shop.uid


@router.get("/{shop_id}")
async def read_shop(shop_id: str) -> validation.Shop:
    return validation.Shop(**database.Shop.nodes.first(uid=shop_id).__dict__)


@router.put("/{shop_id}")
async def update_shop(shop_id: str, shop: validation.Shop) -> validation.Shop:
    selected_shop = database.Shop.nodes.first(uid=shop_id)
    for key, value in shop.__dict__.items():
        if key != "uid":
            setattr(selected_shop, key, value)
    selected_shop.save()
    return validation.Shop(**selected_shop.__dict__)


@router.delete("/{shop_id}")
async def delete_shop(shop_id: str):
    database.Shop.nodes.first(uid=shop_id).delete()
