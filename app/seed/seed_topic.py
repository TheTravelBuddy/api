from ..models.database import Topic


def seed_topic():
    return dict(
        adventure=Topic(name="Adventure").save(),
        cuisine=Topic(name="Cuisine").save(),
        beaches=Topic(name="Beaches").save(),
        history=Topic(name="Historical").save(),
    )
