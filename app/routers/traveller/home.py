from typing import List

from fastapi import APIRouter, Depends
from pydantic import AnyUrl, BaseModel, constr

from ...dependencies.auth import get_registered_user
from ...helpers.conversion import get_query_response

router = APIRouter()


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
MATCH (city:City)-[:LOCATED_IN]-(hotel:Hotel)-[review:REVIEWED_HOTEL]-(user)
RETURN
    hotel.uid AS id,
    hotel.photos[0] AS coverUri,
    hotel.name AS name,
    hotel.price AS price,
    AVG(review.rating) AS rating,
    hotel.locality AS locality,
    city.name AS city
ORDER BY rating DESC
LIMIT $n
"""

GET_TOP_BLOGS_QUERY = """
MATCH (blog:Blog)-[like:LIKES_BLOG]-(),
    (blog:Blog)-[:AUTHOR_OF]-(author)
RETURN
    blog.uid AS id,
    blog.title AS title,
    left(blog.content, 100) AS content,
    COUNT(like) AS likes,
    author.profile_picture as authorProfile
ORDER BY likes DESC LIMIT $n;
"""


class PackagePreviewResponse(BaseModel):
    id: str
    name: constr(min_length=5, max_length=120)
    coverUri: AnyUrl
    rating: float


class DestinationPreviewResponse(BaseModel):
    id: str
    name: constr(min_length=3, max_length=120)
    coverUri: AnyUrl
    rating: float


class HotelPreviewResponse(BaseModel):
    id: str
    name: constr(max_length=120)
    coverUri: AnyUrl
    rating: float
    locality: str
    city: str
    price: int


class BlogPreviewResponse(BaseModel):
    id: str
    authorProfile: AnyUrl
    title: str
    content: str
    likes: int


class HomeApiResponse(BaseModel):
    topPackages: List[PackagePreviewResponse]
    topDestinations: List[DestinationPreviewResponse]
    topHotels: List[HotelPreviewResponse]
    topBlogs: List[BlogPreviewResponse]


@router.get("", response_model=HomeApiResponse)
async def get_home_data(user=Depends(get_registered_user)):
    return HomeApiResponse(
        topPackages=get_query_response(GET_TOP_PACKAGES_QUERY, {"n": 3}),
        topDestinations=get_query_response(GET_TOP_DESTINATIONS_QUERY, {"n": 5}),
        topHotels=get_query_response(GET_TOP_HOTELS_QUERY, {"n": 5}),
        topBlogs=get_query_response(GET_TOP_BLOGS_QUERY, {"n": 5}),
    )
