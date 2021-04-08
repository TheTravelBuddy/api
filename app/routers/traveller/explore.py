from os import environ

import requests
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import AnyUrl, BaseModel, confloat, constr

from ...dependencies.auth import get_registered_user
from ...dependencies.entities import get_city
from ...helpers.db_query import get_query_response
from ...helpers.queries import GET_EXPLORE_DATA_QUERY

router = APIRouter()


class AttractionPreviewResponse(BaseModel):
    id: str
    name: constr(min_length=5, max_length=120)
    coverUri: AnyUrl
    rating: float


EXPLORE_SERVICES = [
    {"id": "PARKING", "name": "Parking"},
    {"id": "POLICE_STATION", "name": "Police Station"},
    {"id": "PETROL_PUMP", "name": "Petrol Pump"},
    {"id": "ATM", "name": "ATM"},
    {"id": "HOSPITAL", "name": "Hospital"},
]


@router.get("")
async def get_explore_data(
    latitude: confloat(ge=-90, le=90),
    longitude: confloat(ge=-180, le=180),
    city=Depends(get_city),
    user=Depends(get_registered_user),
):
    return {
        **get_query_response(
            GET_EXPLORE_DATA_QUERY,
            {"city": city.uid, "latitude": latitude, "longitude": longitude},
        )[0],
        "services": EXPLORE_SERVICES,
    }


async def get_service(serviceId: str):
    try:
        return next(
            service for service in EXPLORE_SERVICES if service["id"] == serviceId
        )
    except StopIteration:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Service not found."
        )


services_cache = dict()


def parse_service_result(service_result):
    address = service_result.get("address", {})
    position = service_result.get("position", {})

    service = {
        "name": service_result.get("title", ""),
        "address": address.get("label", ""),
        "latitude": position.get("lat"),
        "longitude": position.get("lng"),
        "distance": service_result.get("distance", 1) / 1000,
    }

    open_hours = service_result.get("openingHours", [None])[0]
    if open_hours:
        service["timings"] = open_hours.get("text", [None])[0]

    contacts = service_result.get("contacts", [None])[0]
    if contacts:
        www = contacts.get("www")
        if www:
            service["website"] = www[0].get("value")

        phone = contacts.get("phone")
        if phone:
            service["phone"] = phone[0].get("value")

    return service


@router.get("/service")
async def get_explore_services(
    latitude: confloat(ge=-90, le=90),
    longitude: confloat(ge=-180, le=180),
    service=Depends(get_service),
):
    key = (service["id"], latitude, longitude)

    if key in services_cache:
        return services_cache[key]

    response = requests.get(
        "https://discover.search.hereapi.com/v1/discover",
        {
            "q": service["name"].lower(),
            "at": f"{latitude},{longitude}",
            "apiKey": environ["HERE_MAPS_API_KEY"],
        },
    ).json()

    services = [
        parse_service_result(item)
        for item in response["items"]
        if item["resultType"] == "place"
    ]

    services_cache[key] = services

    return services
