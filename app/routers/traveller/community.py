from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends
from pydantic import AnyUrl, BaseModel

from ...dependencies.auth import get_registered_user
from ...helpers.db_query import get_query_response
from ...helpers.queries import (
    GET_TOP_BANNER_BLOGS_QUERY,
    GET_TOP_BLOG_TOPICS_QUERY,
    GET_TOP_LOCATION_BLOGS_QUERY,
)

router = APIRouter()


class TopBannerBlogResponse(BaseModel):
    id: str
    authorProfile: AnyUrl
    title: str
    content: str
    likes: int
    coverUri: AnyUrl
    publishedOn: datetime


class TopBlogTopicResponse(BaseModel):
    id: str
    name: str
    blogs: int


class TopLocationBlogResponse(BaseModel):
    id: str
    coverUri: AnyUrl
    title: str
    content: str
    likes: int
    authorProfile: AnyUrl
    publishedOn: datetime
    locationId: str
    locationName: str


class CommunityApiResponse(BaseModel):
    topBannerBlogs: List[TopBannerBlogResponse]
    topBlogTopics: List[TopBlogTopicResponse]
    topLocationBlogs: List[TopLocationBlogResponse]


@router.get("", response_model=CommunityApiResponse)
async def get_community_data(user=Depends(get_registered_user)):
    return CommunityApiResponse(
        topBannerBlogs=get_query_response(GET_TOP_BANNER_BLOGS_QUERY, {"n": 3}),
        topBlogTopics=get_query_response(GET_TOP_BLOG_TOPICS_QUERY, {"n": 5}),
        topLocationBlogs=get_query_response(GET_TOP_LOCATION_BLOGS_QUERY, {"n": 3}),
    )
