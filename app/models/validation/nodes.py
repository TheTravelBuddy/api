from datetime import date, datetime
from enum import Enum
from typing import Any, List

from pydantic import AnyUrl, BaseModel, PositiveInt, confloat, constr


class GenderEnum(str, Enum):
    Male = "M"
    Female = "F"
    Other = "O"


class MoodEnum(str, Enum):
    Relax = "RELAX"
    Adventure = "ADVENTURE"
    Mixed = "MIXED"


PHONE_NUMBER_REGEX = r"^\+(\d){12}$"


class User(BaseModel):
    uid: str = None
    name: constr(min_length=3, max_length=120)
    phone: constr(min_length=13, max_length=13, regex=PHONE_NUMBER_REGEX)


class Traveller(User):
    gender: GenderEnum
    dob: date
    mood: MoodEnum = MoodEnum.Mixed


class Business(User):
    is_verified: bool = False
    address: constr(max_length=512, min_length=10)
    latitude: confloat(ge=-90, le=90)
    longitude: confloat(ge=-180, le=180)


class Agency(Business):
    pass


class ShopOwner(Business):
    pass


class HotelOwner(Business):
    pass


class Location(BaseModel):
    uid: str = None
    name: constr(min_length=3, max_length=120)
    description: constr(min_length=10, max_length=4096)
    latitude: confloat(ge=-90, le=90)
    longitude: confloat(ge=-180, le=180)
    photos: List[AnyUrl]


class City(Location):
    pass


class Attraction(Location):
    pass


class Shop(Location):
    pass


class Blog(BaseModel):
    uid: str = None
    title: constr(min_length=10, max_length=120)
    content: constr(min_length=120, max_length=4096)
    published_on: datetime = datetime.today()
    photos: List[AnyUrl]


class Hotel(BaseModel):
    uid: str = None
    name: constr(max_length=120)
    price: PositiveInt
    description: constr(max_length=4096)
    photos: List[AnyUrl]
    address: constr(max_length=1024)
    latitude: confloat(ge=-90, le=90)
    longitude: confloat(ge=-180, le=180)


class Package(BaseModel):
    uid: str = None
    name: constr(max_length=120)
    price: PositiveInt
    description: constr(max_length=4096)
    photos: List[AnyUrl]
    itinerary: Any = {}
