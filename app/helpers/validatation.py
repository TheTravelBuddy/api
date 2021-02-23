from enum import Enum


class GenderEnum(str, Enum):
    Male = "M"
    Female = "F"
    Other = "O"


class MoodEnum(str, Enum):
    Relax = "RELAX"
    Adventure = "ADVENTURE"
    Mixed = "MIXED"


class HotelAmenitiesEnum(str, Enum):
    WiFi = "WIFI"
    SwimmingPool = "SWIMMINGPOOL"
    Ac = "AC"
    Toiletries = "TOILETRIES"
    Gym = "GYM"
    Parking = "PARKING"
    Medical = "MEDICAL"
    Spa = "SPA"


PHONE_NUMBER_REGEX = r"^\+(\d){12}$"
