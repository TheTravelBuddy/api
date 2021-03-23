from enum import Enum


class BusinessTypeEnum(str, Enum):
    TravelAgency = "TRAVEL_AGENCY"
    HotelOwner = "HOTEL_OWNER"
    ShopOwner = "SHOP_OWNER"


class GenderEnum(str, Enum):
    Male = "M"
    Female = "F"
    Other = "O"


class MoodEnum(str, Enum):
    Relax = "RELAX"
    Adventure = "ADVENTURE"
    Mixed = "MIXED"


class TopicsEnum(str, Enum):
    Cuisine = "CUISINE"
    Adventure = "ADVENTURE"
    Historical = "HISTORICAL"
    Culture = "CULTURE"
    Art = "ART"
    Beaches = "BEACHES"
    Mountains = "MOUNTAINS"
    Religious = "RELIGIOUS"
    Trekking = "TREKKING"
    Romantic = "ROMANTIC"
    Shopping = "SHOPPING"
    JungleSafari = "JUNGLE_SAFARI"
    HillStations = "HILL_STATIONS"
    RoadTrips = "ROAD_TRIPS"
    TouristAttractions = "TOURIST_ATTRACTIONS"
    Festivals = "FESTIVALS"


class ServicesEnum(str, Enum):
    PetrolPump = "PETROL _PUMP"
    PoliceStation = "POLICE_STATION"
    Hospital = "HOSPITAL"
    Atm = "ATM"
    Gym = "GYM"
    Library = "LIBRARY"
    BeautySalon = "BEAUTY_SALON"
    Parking = "PARKING"
    Chemist = "CHEMIST"


class PackageAmenitiesEnum(str, Enum):
    Hotels = "HOTELS"
    Sightseeing = "SIGHTSEEING"
    Transfers = "TRANSFERS"
    Activities = "ACTIVITIES"
    Flights = "FLIGHTS"
    Meals = "MEALS"
    CityTours = "CITY TOURS"


class HotelAmenitiesEnum(str, Enum):
    Wifi = "WIFI"
    Swimming_pool = "SWIMMING_POOL"
    AirConditioning = "AIR_CONDITIONING"
    Parking = "PARKING"
    Spa = "SPA"
    Bar = "BAR"
    Laundry = "LAUNDRY"
    Lawn = "LAWN"
    IroningServices = "IRONING_SERVICES"
    Housekeeping = "HOUSEKEEPING"
    Newspaper = "NEWSPAPER"
    OutdoorSports = "OUTDOOR_SPORTS"
    ChildcareServices = "CHILDCARE_SERVICES"
    Gym = "GYM"
    Salon = "SALON"


PHONE_NUMBER_REGEX = r"^\+(\d){12}$"
