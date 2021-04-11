from ..models.database import Topic


def seed_topic():
    return dict(
        topic1=Topic(name="Adventure").save(),
        topic2=Topic(name="Cuisine").save(),
        topic3=Topic(name="Beaches").save(),
        topic4=Topic(name="Historical").save(),
    )
