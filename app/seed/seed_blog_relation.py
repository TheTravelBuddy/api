def seed_blog_relations(travellers, blogs):
    travellers["Jenovah"].author_of.connect(blogs["blog1"])
    travellers["Ester"].author_of.connect(blogs["blog2"])
    travellers["Ester"].author_of.connect(blogs["blog3"])
    travellers["Jenovah"].author_of.connect(blogs["blog4"])
    travellers["Ester"].author_of.connect(blogs["blog5"])
    travellers["Lucifer"].author_of.connect(blogs["blog6"])

    travellers["Justin"].likes_blog.connect(blogs["blog1"])
    travellers["Justin"].likes_blog.connect(blogs["blog3"])
    travellers["Justin"].likes_blog.connect(blogs["blog5"])
    travellers["Justin"].likes_blog.connect(blogs["blog6"])

    travellers["Selena"].likes_blog.connect(blogs["blog2"])
    travellers["Selena"].likes_blog.connect(blogs["blog3"])
    travellers["Selena"].likes_blog.connect(blogs["blog4"])


def seed_blog_topic_relation(topics, blogs):
    blogs["blog1"].tagged_topic.connect(topics["adventure"])
    blogs["blog2"].tagged_topic.connect(topics["cuisine"])
    blogs["blog3"].tagged_topic.connect(topics["adventure"])
    blogs["blog4"].tagged_topic.connect(topics["adventure"])
    blogs["blog5"].tagged_topic.connect(topics["cuisine"])
    blogs["blog6"].tagged_topic.connect(topics["history"])


def seed_blog_location_relation(cities, blogs):
    blogs["blog1"].tagged_location.connect(cities["Mumbai"])
    blogs["blog2"].tagged_location.connect(cities["Pune"])
    blogs["blog3"].tagged_location.connect(cities["Pune"])
    blogs["blog4"].tagged_location.connect(cities["Mumbai"])
    blogs["blog5"].tagged_location.connect(cities["Delhi"])
    blogs["blog6"].tagged_location.connect(cities["Delhi"])


def seed_blog_comment_relation(travellers, blogs):
    blogs["blog1"].commented_by.connect(
        travellers["Selena"],
        {
            "content": "Nice Blog was really helpful and informative got know alot of in and out"
        },
    )
    blogs["blog6"].commented_by.connect(
        travellers["Justin"],
        {
            "content": "Nice Blog was really helpful and informative got know alot of in and out"
        },
    )
    blogs["blog5"].commented_by.connect(
        travellers["Lucifer"],
        {
            "content": "Nice Blog was really helpful and informative got know alot of in and out"
        },
    )
    blogs["blog4"].commented_by.connect(
        travellers["Ester"],
        {
            "content": "Nice Blog was really helpful and informative got know alot of in and out"
        },
    )
    blogs["blog3"].commented_by.connect(
        travellers["Justin"],
        {
            "content": "Nice Blog was really helpful and informative got know alot of in and out"
        },
    )
    blogs["blog2"].commented_by.connect(
        travellers["Lucifer"],
        {
            "content": "Nice Blog was really helpful and informative got know alot of in and out"
        },
    )
