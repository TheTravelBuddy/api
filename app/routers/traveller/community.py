from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends
from pydantic import AnyUrl, BaseModel

from ...dependencies.auth import get_registered_user
from ...helpers.conversion import get_query_response

router = APIRouter()


class TopBannerBlogResponse(BaseModel):
    id: str
    authorProfile: AnyUrl
    title: str
    content: str
    likes: int
    coverUri: AnyUrl
    publishedOn: datetime


GET_TOP_BANNER_BLOGS_QUERY = """
MATCH
    (blog:Blog)-[like:LIKES_BLOG]-(),
    (blog:Blog)-[:AUTHOR_OF]-(author)
RETURN
    blog.uid AS id,
    blog.title AS title,
    left(blog.content, 150) AS content,
    COUNT(like) AS likes,
    author.profile_picture AS authorProfile,
    blog.photos[0] as coverUri,
    blog.published_on AS publishedOn
ORDER BY likes DESC
LIMIT $n;
"""


class TopBlogTopicResponse(BaseModel):
    id: str
    name: str
    blogs: int


GET_TOP_BLOG_TOPICS_QUERY = """
MATCH
    (blog:Blog)-[:TAGGED_TOPIC]->(topic:Topic)
RETURN
    topic.uid as id,
    topic.name as name,
    COUNT(blog) as blogs
ORDER BY blogs DESC
LIMIT $n
"""


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


GET_TOP_LOCATION_BLOGS_QUERY = """
MATCH
    (blog:Blog)-[like:LIKES_BLOG]-(),
    (blog:Blog)-[:AUTHOR_OF]-(author),
    (blog:Blog)-[:TAGGED_LOCATION]-(location)
WITH blog, author, location, COUNT(like) AS likes
ORDER BY likes DESC
WITH
    COLLECT(blog)[0] AS blog,
    COLLECT(author)[0] AS author,
    COLLECT(likes)[0] AS likes,
    location
RETURN
    blog.uid AS id,
    blog.photos[0] as coverUri,
    blog.title AS title,
    blog.published_on AS publishedOn,
    LEFT(blog.content, 100) AS content,
    likes,
    author.profile_picture AS authorProfile,
    location.uid AS locationId,
    location.name AS locationName
LIMIT $n
"""


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
