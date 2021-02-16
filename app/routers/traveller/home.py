from typing import List

# from fastapi import APIRouter, Depends
from fastapi import APIRouter
from neomodel import db
from pydantic import AnyUrl, BaseModel, constr

# from ...dependencies.auth import get_registered_user
from ...helpers.conversion import inflate_query_result

# from ...helpers.conversion import deflate_request

router = APIRouter()


class TopPackagesResponse(BaseModel):
    id: str
    name: constr(min_length=5, max_length=100)
    coverUri: AnyUrl
    rating: float


class TopDestinationResponse(BaseModel):
    id: str
    name: constr(min_length=3, max_length=100)
    coverUri: AnyUrl
    rating: float


class TopHotelResponse(BaseModel):
    id: str
    name: constr(max_length=120)
    coverUri: AnyUrl
    rating: float
    # TODO:Add these back
    # locality: str
    # city: str
    price: int


GET_TOP_PACKAGES_QUERY = """
MATCH (package:Package)-[review:REVIEWED_PACKAGE]-(user)
RETURN
    package.uid AS id,
    package.photos[0] AS coverUri,
    package.name AS name,
    AVG(review.rating) AS rating
ORDER BY rating DESC
LIMIT $n
"""

GET_TOP_DESTINATIONS_QUERY = """
MATCH (city:City)-[review:REVIEWED_CITY]-(user)
RETURN
    city.uid AS id,
    city.photos[0] AS coverUri,
    city.name AS name,
    AVG(review.rating) AS rating
ORDER BY rating DESC
LIMIT $n
"""


GET_TOP_HOTELS_QUERY = """
MATCH (hotel:Hotel)-[review:REVIEWED_HOTEL]-(user)
RETURN
    hotel.uid AS id,
    hotel.photos[0] AS coverUri,
    hotel.name AS name,
    hotel.price AS price,
    AVG(review.rating) AS rating
ORDER BY rating DESC
LIMIT $n
"""

# TODO: add back `user=Depends(get_registered_user)`,


@router.get("/topPackages", response_model=List[TopPackagesResponse])
async def get_top_packages(n: int = 3):
    return inflate_query_result(
        db.cypher_query(GET_TOP_PACKAGES_QUERY, {"n": n}), TopPackagesResponse
    )


@router.get("/topDestinations", response_model=List[TopDestinationResponse])
async def get_top_destinations(n: int = 5):
    return inflate_query_result(
        db.cypher_query(GET_TOP_DESTINATIONS_QUERY, {"n": n}), TopDestinationResponse
    )


@router.get("/topHotel", response_model=List[TopHotelResponse])
async def get_top_hotel(n: int = 5):
    return inflate_query_result(
        db.cypher_query(GET_TOP_HOTELS_QUERY, {"n": n}), TopHotelResponse
    )
