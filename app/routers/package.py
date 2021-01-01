from typing import List

from fastapi import APIRouter

from ..models import database, validation

router = APIRouter()


@router.get("/")
async def read_packages() -> List[validation.Package]:
    return [
        validation.Package(**package.__dict__)
        for package in database.Package.nodes.all()
    ]


@router.post("/")
def add_package(package: validation.Package) -> str:
    package = database.Package(**package.__dict__).save()
    return package.uid


@router.get("/{package_id}")
async def read_package(package_id: str) -> validation.Package:
    return validation.Package(**database.Package.nodes.first(uid=package_id).__dict__)


@router.put("/{package_id}")
async def update_package(
    package_id: str, package: validation.Package
) -> validation.Package:
    selected_package = database.Package.nodes.first(uid=package_id)
    for key, value in package.__dict__.items():
        if key != "uid":
            setattr(selected_package, key, value)
    selected_package.save()
    return validation.Package(**selected_package.__dict__)


@router.delete("/{package_id}")
async def delete_package(package_id: str):
    database.Package.nodes.first(uid=package_id).delete()
