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


def seed_package_review_relation(travellers, packages):
    travellers["Selena"].reviewed_package.connect(
        packages["package1"],
        {
            "rating": 3,
            "review": "complete package",
            "photos": ["https://picsum.photos/1090"],
        },
    )
    travellers["Justin"].reviewed_package.connect(
        packages["package1"],
        {
            "rating": 4,
            "review": "complete package",
            "photos": ["https://picsum.photos/1090"],
        },
    )
    travellers["Justin"].reviewed_package.connect(
        packages["package2"],
        {
            "rating": 5,
            "review": "complete package",
            "photos": ["https://picsum.photos/1090"],
        },
    )
    travellers["Selena"].reviewed_package.connect(
        packages["package2"],
        {
            "rating": 4,
            "review": "complete package",
            "photos": ["https://picsum.photos/1090"],
        },
    )
    travellers["Selena"].reviewed_package.connect(
        packages["package3"],
        {
            "rating": 5,
            "review": "complete package",
            "photos": ["https://picsum.photos/1090"],
        },
    )
    travellers["Ester"].reviewed_package.connect(
        packages["package3"],
        {
            "rating": 3,
            "review": "complete package",
            "photos": ["https://picsum.photos/1090"],
        },
    )
    travellers["Justin"].reviewed_package.connect(
        packages["package4"],
        {
            "rating": 3,
            "review": "complete package",
            "photos": ["https://picsum.photos/1090"],
        },
    )
    travellers["Selena"].reviewed_package.connect(
        packages["package4"],
        {
            "rating": 5,
            "review": "complete package",
            "photos": ["https://picsum.photos/1090"],
        },
    )
    travellers["Selena"].reviewed_package.connect(
        packages["package5"],
        {
            "rating": 4,
            "review": "complete package",
            "photos": ["https://picsum.photos/1090"],
        },
    )
    travellers["Justin"].reviewed_package.connect(
        packages["package5"],
        {
            "rating": 5,
            "review": "complete package",
            "photos": ["https://picsum.photos/1090"],
        },
    )
    travellers["Justin"].reviewed_package.connect(
        packages["package6"],
        {
            "rating": 4,
            "review": "complete package",
            "photos": ["https://picsum.photos/1090"],
        },
    )
    travellers["Ester"].reviewed_package.connect(
        packages["package6"],
        {
            "rating": 5,
            "review": "complete package",
            "photos": ["https://picsum.photos/1090"],
        },
    )
