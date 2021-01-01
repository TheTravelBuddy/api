from typing import List

from fastapi import APIRouter

from ..models import database, validation

router = APIRouter()


@router.get("/")
async def read_shop_owners() -> List[validation.ShopOwner]:
    return [
        validation.ShopOwner(**shop_owner.__dict__)
        for shop_owner in database.ShopOwner.nodes.all()
    ]


@router.post("/")
def add_shop_owner(shop_owner: validation.ShopOwner) -> str:
    shop_owner = database.ShopOwner(**shop_owner.__dict__).save()
    return shop_owner.uid


@router.get("/{shop_owner_id}")
async def read_shop_owner(shop_owner_id: str) -> validation.ShopOwner:
    return validation.ShopOwner(
        **database.ShopOwner.nodes.first(uid=shop_owner_id).__dict__
    )


@router.put("/{shop_owner_id}")
async def update_shop_owner(
    shop_owner_id: str, shop_owner: validation.ShopOwner
) -> validation.ShopOwner:
    selected_shop_owner = database.ShopOwner.nodes.first(uid=shop_owner_id)
    for key, value in shop_owner.__dict__.items():
        if key != "uid":
            setattr(selected_shop_owner, key, value)
    selected_shop_owner.save()
    return validation.ShopOwner(**selected_shop_owner.__dict__)


@router.delete("/{shop_owner_id}")
async def delete_shop_owner(shop_owner_id: str):
    database.ShopOwner.nodes.first(uid=shop_owner_id).delete()
