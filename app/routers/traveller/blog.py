from typing import List

from fastapi import APIRouter, Depends
from pydantic import AnyUrl, BaseModel, constr

from ...dependencies.auth import get_registered_user
from ...helpers.conversion import get_query_response

router = APIRouter()
