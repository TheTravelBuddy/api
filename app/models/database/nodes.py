from neomodel import (
    ArrayProperty,
    BooleanProperty,
    DateProperty,
    DateTimeProperty,
    FloatProperty,
    IntegerProperty,
    JSONProperty,
    RegexProperty,
    RelationshipFrom,
    RelationshipTo,
    StringProperty,
    StructuredNode,
    UniqueIdProperty,
    cardinality,
)

from .relations import (
    BookedRel,
    CommentedOnRel,
    LikesRel,
    OwnsRel,
    ReviewedRel,
    StayedAtRel,
    VisitedRel,
)

GENDERS = {"F": "Female", "M": "Male", "O": "Other"}
MOODS = {"RELAX": "Relax", "ADVENTURE": "Adventure", "MIXED": "Mixed"}


class User(StructuredNode):
    uid = UniqueIdProperty()
    firebase_id = StringProperty()
    name = StringProperty(max_length=120, required=True)
    phone = RegexProperty(expression=r"^\+(\d){12}$", required=True)
    profile_picture = StringProperty(default="https:/picsum.photos/201")


class Traveller(User):
    gender = StringProperty(choices=GENDERS, required=True)
    dob = DateProperty(required=True)
    mood = StringProperty(choices=MOODS, default="M")

    likes_hotel = RelationshipTo("Hotel", "LIKES_HOTEL", model=LikesRel)
    likes_package = RelationshipTo("Package", "LIKES_PACKAGE", model=LikesRel)
    likes_city = RelationshipTo("City", "LIKES_CITY", model=LikesRel)
    likes_shop = RelationshipTo("Shop", "LIKES_SHOP", model=LikesRel)
    likes_attraction = RelationshipTo("Attraction", "LIKES_ATTRACTION", model=LikesRel)
    likes_blog = RelationshipTo("Blog", "LIKES_BLOG", model=LikesRel)

    booked_hotel = RelationshipTo("Hotel", "BOOKED_HOTEL", model=BookedRel)
    booked_package = RelationshipTo("Package", "BOOKED_PACKAGE", model=BookedRel)

    reviewed_hotel = RelationshipTo("Hotel", "REVIEWED_HOTEL", model=ReviewedRel)
    reviewed_package = RelationshipTo("Package", "REVIEWED_PACKAGE", model=ReviewedRel)
    reviewed_city = RelationshipTo("City", "REVIEWED_CITY", model=ReviewedRel)
    reviewed_shop = RelationshipTo("Shop", "REVIEWED_SHOP", model=ReviewedRel)
    reviewed_attraction = RelationshipTo(
        "Attraction", "REVIEWED_ATTRACTION", model=ReviewedRel
    )

    visited_shop = RelationshipTo("Shop", "VISITED_SHOP", model=VisitedRel)
    visited_attraction = RelationshipTo(
        "Attraction", "VISITED_ATTRACTIONS", model=VisitedRel
    )

    read_blog = RelationshipTo("Blog", "READ_BLOG", model=VisitedRel)

    stayed_at_city = RelationshipTo("City", "STAYED_AT_CITY", model=StayedAtRel)
    stayed_at_hotel = RelationshipTo("Hotel", "STAYED_AT_HOTEL", model=StayedAtRel)

    author_of = RelationshipTo("Blog", "AUTHOR_OF", model=OwnsRel)

    commented_on = RelationshipTo("Blog", "COMMENTED_ON", model=CommentedOnRel)


class Business(User):
    is_verified = BooleanProperty(default=False)
    address = StringProperty(max_length=512, required=True)
    latitude = FloatProperty(required=True)
    longitude = FloatProperty(required=True)


class Agency(Business):
    offers_package = RelationshipTo("Package", "OFFERS_PACKAGE", model=OwnsRel)


class ShopOwner(Business):
    owns_shop = RelationshipTo("Shop", "OWNS_SHOP", model=OwnsRel)


class HotelOwner(Business):
    owns_hotel = RelationshipTo("Hotel", "OWNS_HOTEL", model=OwnsRel)


class Location(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(max_length=120, required=True)
    description = StringProperty(max_length=1024, required=True)
    latitude = FloatProperty(required=True)
    longitude = FloatProperty(required=True)
    photos = ArrayProperty(base_property=StringProperty(), default=[])


class City(Location):
    liked_by = RelationshipFrom("Traveller", "LIKES_CITY", model=LikesRel)
    reviewed_by = RelationshipFrom("Traveller", "REVIEWED_CITY", model=ReviewedRel)

    stayed_by = RelationshipFrom("Traveller", "STAYED_AT_CITY", model=StayedAtRel)

    has_hotels = RelationshipFrom("Hotel", "LOCATED_IN", model=OwnsRel)


class Attraction(Location):
    liked_by = RelationshipFrom("Traveller", "LIKES_ATTRACTION", model=LikesRel)
    reviewed_by = RelationshipFrom(
        "Traveller", "REVIEWED_ATTRACTION", model=ReviewedRel
    )

    visited_by = RelationshipFrom("Traveller", "VISITED_ATTRACTION", model=VisitedRel)


class Shop(Location):
    liked_by = RelationshipFrom("Traveller", "LIKES_SHOP", model=LikesRel)
    reviewed_by = RelationshipFrom("Traveller", "REVIEWED_SHOP", model=ReviewedRel)
    owned_by = RelationshipFrom("ShopOwner", "OWNS_SHOP", model=OwnsRel)

    visited_by = RelationshipFrom("Traveller", "VISITED_SHOP", model=VisitedRel)


class Blog(StructuredNode):
    uid = UniqueIdProperty()
    title = StringProperty(max_length=120, required=True)
    content = StringProperty(max_length=4096, required=True)
    published_on = DateTimeProperty(default_now=True)
    photos = ArrayProperty(base_property=StringProperty())

    authored_by = RelationshipFrom("Traveller", "AUTHOR_OF", model=OwnsRel)

    read_by = RelationshipFrom("Traveller", "READ_BLOG", model=VisitedRel)
    liked_by = RelationshipFrom("Traveller", "LIKES_BLOG", model=LikesRel)
    commented_by = RelationshipFrom("Traveller", "COMMENTED_ON", model=CommentedOnRel)


class Hotel(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(max_length=120, required=True)
    price = IntegerProperty(required=True)
    description = StringProperty(max_length=1024, required=True)
    photos = ArrayProperty(required=True, base_property=StringProperty())
    address = StringProperty(max_length=512, required=True)
    locality = StringProperty(required=True)
    postalCode = IntegerProperty(required=True)
    latitude = FloatProperty(required=True)
    longitude = FloatProperty(required=True)

    located_in = RelationshipTo(
        "City", "LOCATED_IN", model=OwnsRel, cardinality=cardinality.One
    )

    owned_by = RelationshipFrom("HotelOwner", "OWNS_HOTEL", model=OwnsRel)

    liked_by = RelationshipFrom("Traveller", "LIKES_HOTEL", model=LikesRel)
    booked_by = RelationshipFrom("Traveller", "BOOKED_HOTEL", model=BookedRel)
    reviewed_by = RelationshipFrom("Traveller", "REVIEWED_HOTEL", model=ReviewedRel)

    stayed_by = RelationshipFrom("Traveller", "STAYED_AT_HOTEL", model=StayedAtRel)


class Package(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(max_length=120, required=True)
    price = IntegerProperty(required=True)
    description = StringProperty(max_length=1024, required=True)
    photos = ArrayProperty(base_property=StringProperty())
    itinerary = JSONProperty(required=True)

    offered_by = RelationshipFrom("Agency", "OFFERS_PACKAGE", model=OwnsRel)

    liked_by = RelationshipFrom("Traveller", "LIKES_PACKAGE", model=LikesRel)
    booked_by = RelationshipFrom("Traveller", "BOOKED_PACKAGE", model=BookedRel)
    reviewed_by = RelationshipFrom("Traveller", "REVIEWED_PACKAGE", model=ReviewedRel)
