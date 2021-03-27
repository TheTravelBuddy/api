from neomodel import (
    ArrayProperty,
    DateProperty,
    DateTimeProperty,
    IntegerProperty,
    StringProperty,
    StructuredRel,
)


class OwnsRel(StructuredRel):
    pass


class LikesRel(StructuredRel):
    datetime = DateTimeProperty(default_now=True)


class BookedRel(StructuredRel):
    booked_at = DateTimeProperty(required=True)
    booking_date = DateProperty(required=True)
    no_of_days = IntegerProperty(required=True)
    no_of_people = IntegerProperty(required=True)


class VisitedRel(StructuredRel):
    date = DateTimeProperty(default_now=True)


class StayedAtRel(StructuredRel):
    from_date = DateProperty(required=True)
    to_date = DateProperty(required=True)


class ReviewedRel(StructuredRel):
    rating = IntegerProperty(required=True)
    review = StringProperty(max_length=4096, required=True)
    photos = ArrayProperty(base_property=StringProperty())
    datetime = DateTimeProperty(default_now=True)


class CommentedOnRel(StructuredRel):
    content = StringProperty(max_length=4096, required=True)
    datetime = DateTimeProperty(default_now=True)


class TaggedRel(StructuredRel):
    pass


class PackageDayRel(StructuredRel):
    day = IntegerProperty(required=True)
