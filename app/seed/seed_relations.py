def seed_hotel_city_relations(hotels, cities):
    hotels["hotel1"].located_in.connect(cities["Mumbai"])
    hotels["hotel2"].located_in.connect(cities["Mumbai"])
    hotels["hotel3"].located_in.connect(cities["Mumbai"])

    hotels["hotel5"].located_in.connect(cities["Delhi"])
    hotels["hotel6"].located_in.connect(cities["Delhi"])
    hotels["hotel7"].located_in.connect(cities["Delhi"])

    hotels["hotel8"].located_in.connect(cities["Pune"])
    hotels["hotel9"].located_in.connect(cities["Pune"])
    hotels["hotel10"].located_in.connect(cities["Pune"])

    hotels["hotel11"].located_in.connect(cities["Jaipur"])
    hotels["hotel12"].located_in.connect(cities["Jaipur"])
    hotels["hotel13"].located_in.connect(cities["Jaipur"])

    hotels["hotel14"].located_in.connect(cities["Ahmedabad"])
    hotels["hotel15"].located_in.connect(cities["Ahmedabad"])
    hotels["hotel16"].located_in.connect(cities["Ahmedabad"])


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
    travellers["Lucifer"].reviewed_package.connect(
        packages["package2"],
        {
            "rating": 4,
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


def seed_city_review_relation(travellers, cities):
    travellers["Selena"].reviewed_city.connect(
        cities["Mumbai"],
        {"rating": 3, "review": "sweet city", "photos": ["https://picsum.photos/1666"]},
    )
    travellers["Justin"].reviewed_city.connect(
        cities["Mumbai"],
        {"rating": 3, "review": "sweet city", "photos": ["https://picsum.photos/1666"]},
    )
    travellers["Lucifer"].reviewed_city.connect(
        cities["Mumbai"],
        {"rating": 5, "review": "sweet city", "photos": ["https://picsum.photos/1666"]},
    )
    travellers["Justin"].reviewed_city.connect(
        cities["Pune"],
        {"rating": 5, "review": "sweet city", "photos": ["https://picsum.photos/1666"]},
    )
    travellers["Lucifer"].reviewed_city.connect(
        cities["Pune"],
        {"rating": 5, "review": "sweet city", "photos": ["https://picsum.photos/1666"]},
    )
    travellers["Selena"].reviewed_city.connect(
        cities["Pune"],
        {"rating": 5, "review": "sweet city", "photos": ["https://picsum.photos/1666"]},
    )
    travellers["Lucifer"].reviewed_city.connect(
        cities["Delhi"],
        {"rating": 4, "review": "sweet city", "photos": ["https://picsum.photos/1666"]},
    )
    travellers["Justin"].reviewed_city.connect(
        cities["Delhi"],
        {"rating": 4, "review": "sweet city", "photos": ["https://picsum.photos/1666"]},
    )
    travellers["Selena"].reviewed_city.connect(
        cities["Delhi"],
        {"rating": 3, "review": "sweet city", "photos": ["https://picsum.photos/1666"]},
    )
    travellers["Jelena"].reviewed_city.connect(
        cities["Jaipur"],
        {"rating": 5, "review": "sweet city", "photos": ["https://picsum.photos/1666"]},
    )
    travellers["Ester"].reviewed_city.connect(
        cities["Jaipur"],
        {"rating": 4, "review": "sweet city", "photos": ["https://picsum.photos/1666"]},
    )
    travellers["Lucifer"].reviewed_city.connect(
        cities["Jaipur"],
        {"rating": 4, "review": "sweet city", "photos": ["https://picsum.photos/1666"]},
    )
    travellers["Selena"].reviewed_city.connect(
        cities["Ahmedabad"],
        {"rating": 5, "review": "sweet city", "photos": ["https://picsum.photos/1666"]},
    )
    travellers["Lucifer"].reviewed_city.connect(
        cities["Ahmedabad"],
        {"rating": 5, "review": "sweet city", "photos": ["https://picsum.photos/1666"]},
    )
    travellers["Ester"].reviewed_city.connect(
        cities["Ahmedabad"],
        {"rating": 3, "review": "sweet city", "photos": ["https://picsum.photos/1666"]},
    )


def seed_hotel_review_relation(travellers, hotels):
    travellers["Selena"].reviewed_hotel.connect(
        hotels["hotel1"],
        {
            "rating": 5,
            "review": "nice hotel",
            "photos": [
                "https://media-cdn.tripadvisor.com/media/photo-m/1280/1b/a5/d8/c1/exterior.jpg"
            ],
        },
    )
    travellers["Justin"].reviewed_hotel.connect(
        hotels["hotel1"],
        {
            "rating": 3,
            "review": "nice hotel",
            "photos": [
                "https://media-cdn.tripadvisor.com/media/photo-m/1280/19/3f/1e/5b/other.jpg"
            ],
        },
    )
    travellers["Lucifer"].reviewed_hotel.connect(
        hotels["hotel2"],
        {
            "rating": 5,
            "review": "nice hotel",
            "photos": [
                "https://media-cdn.tripadvisor.com/media/photo-m/1280/1c/32/d3/ca/recreational-facilities.jpg"
            ],
        },
    )
    travellers["Jelena"].reviewed_hotel.connect(
        hotels["hotel3"],
        {
            "rating": 5,
            "review": "nice hotel",
            "photos": [
                "https://media-cdn.tripadvisor.com/media/photo-o/11/ad/f2/bd/premier-plus-rooms-555.jpg"
            ],
        },
    )
    travellers["Justin"].reviewed_hotel.connect(
        hotels["hotel3"],
        {
            "rating": 4,
            "review": "nice hotel",
            "photos": [
                "https://media-cdn.tripadvisor.com/media/photo-o/11/ad/f2/bd/premier-plus-rooms-555.jpg"
            ],
        },
    )
    travellers["Selena"].reviewed_hotel.connect(
        hotels["hotel7"],
        {
            "rating": 5,
            "review": "nice hotel",
            "photos": [
                "https://media-cdn.tripadvisor.com/media/photo-o/11/ad/f2/bd/premier-plus-rooms-555.jpg"
            ],
        },
    )
    travellers["Lucifer"].reviewed_hotel.connect(
        hotels["hotel7"],
        {
            "rating": 5,
            "review": "nice hotel",
            "photos": [
                "https://media-cdn.tripadvisor.com/media/photo-o/11/ad/f2/bd/premier-plus-rooms-555.jpg"
            ],
        },
    )
    travellers["Lucifer"].reviewed_hotel.connect(
        hotels["hotel5"],
        {
            "rating": 4,
            "review": "nice hotel",
            "photos": [
                "https://media-cdn.tripadvisor.com/media/photo-o/11/ad/f2/bd/premier-plus-rooms-555.jpg"
            ],
        },
    )
    travellers["Selena"].reviewed_hotel.connect(
        hotels["hotel5"],
        {
            "rating": 4,
            "review": "nice hotel",
            "photos": [
                "https://media-cdn.tripadvisor.com/media/photo-o/11/ad/f2/bd/premier-plus-rooms-555.jpg"
            ],
        },
    )
    travellers["Justin"].reviewed_hotel.connect(
        hotels["hotel5"],
        {
            "rating": 4,
            "review": "nice hotel",
            "photos": [
                "https://media-cdn.tripadvisor.com/media/photo-o/11/ad/f2/bd/premier-plus-rooms-555.jpg"
            ],
        },
    )
