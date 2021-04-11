def seed_blog_relations(travellers, blogs):
    travellers["traveller1"].author_of.connect(blogs["blog1"])
    travellers["traveller1"].author_of.connect(blogs["blog2"])
    travellers["traveller1"].author_of.connect(blogs["blog3"])
    travellers["traveller1"].author_of.connect(blogs["blog4"])
    travellers["traveller1"].author_of.connect(blogs["blog5"])
    travellers["traveller3"].author_of.connect(blogs["blog6"])

    travellers["traveller4"].likes_blog.connect(blogs["blog1"])
    travellers["traveller4"].likes_blog.connect(blogs["blog3"])
    travellers["traveller4"].likes_blog.connect(blogs["blog5"])
    travellers["traveller4"].likes_blog.connect(blogs["blog6"])

    travellers["traveller4"].likes_blog.connect(blogs["blog2"])
    travellers["traveller4"].likes_blog.connect(blogs["blog3"])
    travellers["traveller4"].likes_blog.connect(blogs["blog4"])


def seed_blog_topic_relation(topics, blogs):
    blogs["blog1"].tagged_topic.connect(topics["topic1"])
    blogs["blog2"].tagged_topic.connect(topics["topic2"])
    blogs["blog3"].tagged_topic.connect(topics["topic1"])
    blogs["blog4"].tagged_topic.connect(topics["topic1"])
    blogs["blog5"].tagged_topic.connect(topics["topic2"])
    blogs["blog6"].tagged_topic.connect(topics["topic3"])


def seed_blog_location_relation(cities, blogs):
    blogs["blog1"].tagged_location.connect(cities["city1"])
    blogs["blog2"].tagged_location.connect(cities["city2"])
    blogs["blog3"].tagged_location.connect(cities["city2"])
    blogs["blog4"].tagged_location.connect(cities["city1"])
    blogs["blog5"].tagged_location.connect(cities["city3"])
    blogs["blog6"].tagged_location.connect(cities["city3"])


def seed_blog_comment_relation(travellers, blogs):
    blogs["blog1"].commented_by.connect(
        travellers["traveller4"],
        {
            "content": "Nice Blog was really helpful and informative got know alot of in and out"
        },
    )
    blogs["blog6"].commented_by.connect(
        travellers["traveller4"],
        {
            "content": "Nice Blog was really helpful and informative got know alot of in and out"
        },
    )
    blogs["blog5"].commented_by.connect(
        travellers["traveller3"],
        {
            "content": "Nice Blog was really helpful and informative got know alot of in and out"
        },
    )
    blogs["blog4"].commented_by.connect(
        travellers["traveller1"],
        {
            "content": "Nice Blog was really helpful and informative got know alot of in and out"
        },
    )
    blogs["blog3"].commented_by.connect(
        travellers["traveller4"],
        {
            "content": "Nice Blog was really helpful and informative got know alot of in and out"
        },
    )
    blogs["blog2"].commented_by.connect(
        travellers["traveller3"],
        {
            "content": "Nice Blog was really helpful and informative got know alot of in and out"
        },
    )
