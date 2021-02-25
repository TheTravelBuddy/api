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
    SwimmingPool = "SWIMMING_POOL"
    Ac = "AIR_CONDITIONING"
    Toiletries = "TOILETRIES"
    Gym = "GYM"
    Parking = "PARKING"
    Medical = "MEDICAL"
    Spa = "SPA"


PHONE_NUMBER_REGEX = r"^\+(\d){12}$"
