from typing import List

from fastapi import APIRouter, Depends
from pydantic import AnyUrl, BaseModel, constr, datetime

from ...dependencies.auth import get_registered_user
from ...helpers.conversion import get_query_response

router = APIRouter()


class TopBlogResponse(BaseModel):
    id: str
    authorProfile: AnyUrl
    title: str
    content: str
    likes: int


GET_TOP_BLOGS_QUERY = """
MATCH 
    (blog:Blog)-[like:LIKES_BLOG]-(),
    (blog:Blog)-[:AUTHOR_OF]-(author)
RETURN
    blog.uid AS id,
    blog.title AS title,
    left(blog.content, 100) AS content,
    COUNT(like) AS likes,
    author.profile_picture as authorProfile
ORDER BY likes DESC LIMIT $n;
"""


class TopBlogTopicResponse(BaseModel):
    id: str
    name: str
    blogs: int


GET_TOP_BLOGTOPIC_QUERY = """
MATCH 
    (blog:Blog)-[:ABOUT_TOPIC]->(topic:Topic) 
RETURN 
    topic.uid as id, 
    topic.name as name, 
    COUNT(blog) as blogs 
ORDER BY blogs DESC LIMIT $n
"""


class TopLocationBlogResponse(BaseModel):
    id: str
    coverUri: AnyUrl
    title: str
    content: str
    likes: int
    authorProfile: AnyUrl
    datetime: datetime
    locationId: str
    locationName: str


GET_TOP_LOCATIONBLOG_QUERY = """

"""


class CommunityApiResponse(BaseModel):
    TopLocationBlogs: List[TopLocationBlogResponse]
    TopBlogTopics: List[TopBlogTopicResponse]
    TopBlogs: List[TopBlogResponse]


@router.get("/community", response_model=CommunityApiResponse)
# TODO: Add user=Depends(get_registered_user)
async def get_community_data():
    return CommunityApiResponse(
        TopLocationBlogs=get_query_response(GET_TOP_LOCATIONBLOG_QUERY, {"n": 3}),
        TopBlogs=get_query_response(GET_TOP_BLOGS_QUERY, {"n": 3}),
        TopBlogTopics=get_query_response(GET_TOP_BLOGTOPIC_QUERY, {"n": 3}),
    )
