def seed_hotel_city_relations(hotels, cities):
    hotels["hotel1"].located_in.connect(cities["city1"])
    hotels["hotel2"].located_in.connect(cities["city1"])
    hotels["hotel3"].located_in.connect(cities["city1"])

    hotels["hotel5"].located_in.connect(cities["city3"])
    hotels["hotel6"].located_in.connect(cities["city3"])
    hotels["hotel7"].located_in.connect(cities["city3"])

    hotels["hotel8"].located_in.connect(cities["city2"])
    hotels["hotel9"].located_in.connect(cities["city2"])
    hotels["hotel10"].located_in.connect(cities["city2"])

    hotels["hotel11"].located_in.connect(cities["city4"])
    hotels["hotel12"].located_in.connect(cities["city4"])
    hotels["hotel13"].located_in.connect(cities["city4"])

    hotels["hotel14"].located_in.connect(cities["city5"])
    hotels["hotel15"].located_in.connect(cities["city5"])
    hotels["hotel16"].located_in.connect(cities["city5"])


def seed_package_review_relation(travellers, packages):
    travellers["traveller1"].reviewed_package.connect(
        packages["package1"],
        {
            "rating": 3,
            "review": "complete package",
            "photos": ["https://picsum.photos/1090"],
        },
    )
    travellers["traveller2"].reviewed_package.connect(
        packages["package1"],
        {
            "rating": 4,
            "review": "complete package",
            "photos": ["https://picsum.photos/1090"],
        },
    )
    travellers["traveller2"].reviewed_package.connect(
        packages["package2"],
        {
            "rating": 5,
            "review": "complete package",
            "photos": ["https://picsum.photos/1090"],
        },
    )
    travellers["traveller3"].reviewed_package.connect(
        packages["package2"],
        {
            "rating": 4,
            "review": "complete package",
            "photos": ["https://picsum.photos/1090"],
        },
    )
    travellers["traveller1"].reviewed_package.connect(
        packages["package2"],
        {
            "rating": 4,
            "review": "complete package",
            "photos": ["https://picsum.photos/1090"],
        },
    )
    travellers["traveller4"].reviewed_package.connect(
        packages["package3"],
        {
            "rating": 5,
            "review": "complete package",
            "photos": ["https://picsum.photos/1090"],
        },
    )
    travellers["traveller5"].reviewed_package.connect(
        packages["package3"],
        {
            "rating": 3,
            "review": "complete package",
            "photos": ["https://picsum.photos/1090"],
        },
    )
    travellers["traveller5"].reviewed_package.connect(
        packages["package3"],
        {
            "rating": 3,
            "review": "complete package",
            "photos": ["https://picsum.photos/1090"],
        },
    )
    travellers["traveller2"].reviewed_package.connect(
        packages["package4"],
        {
            "rating": 3,
            "review": "complete package",
            "photos": ["https://picsum.photos/1090"],
        },
    )
    travellers["traveller4"].reviewed_package.connect(
        packages["package4"],
        {
            "rating": 5,
            "review": "complete package",
            "photos": ["https://picsum.photos/1090"],
        },
    )
    travellers["traveller4"].reviewed_package.connect(
        packages["package5"],
        {
            "rating": 4,
            "review": "complete package",
            "photos": ["https://picsum.photos/1090"],
        },
    )
    travellers["traveller2"].reviewed_package.connect(
        packages["package5"],
        {
            "rating": 5,
            "review": "complete package",
            "photos": ["https://picsum.photos/1090"],
        },
    )
    travellers["traveller2"].reviewed_package.connect(
        packages["package6"],
        {
            "rating": 4,
            "review": "complete package",
            "photos": ["https://picsum.photos/1090"],
        },
    )
    travellers["traveller5"].reviewed_package.connect(
        packages["package6"],
        {
            "rating": 5,
            "review": "complete package",
            "photos": ["https://picsum.photos/1090"],
        },
    )


def seed_city_review_relation(travellers, cities):
    travellers["traveller4"].reviewed_city.connect(
        cities["city1"],
        {"rating": 3, "review": "sweet city", "photos": ["https://picsum.photos/1666"]},
    )
    travellers["traveller2"].reviewed_city.connect(
        cities["city1"],
        {"rating": 3, "review": "sweet city", "photos": ["https://picsum.photos/1666"]},
    )
    travellers["traveller3"].reviewed_city.connect(
        cities["city1"],
        {"rating": 5, "review": "sweet city", "photos": ["https://picsum.photos/1666"]},
    )
    travellers["traveller2"].reviewed_city.connect(
        cities["city2"],
        {"rating": 5, "review": "sweet city", "photos": ["https://picsum.photos/1666"]},
    )
    travellers["traveller3"].reviewed_city.connect(
        cities["city2"],
        {"rating": 5, "review": "sweet city", "photos": ["https://picsum.photos/1666"]},
    )
    travellers["traveller4"].reviewed_city.connect(
        cities["city2"],
        {"rating": 5, "review": "sweet city", "photos": ["https://picsum.photos/1666"]},
    )
    travellers["traveller3"].reviewed_city.connect(
        cities["city3"],
        {"rating": 4, "review": "sweet city", "photos": ["https://picsum.photos/1666"]},
    )
    travellers["traveller2"].reviewed_city.connect(
        cities["city3"],
        {"rating": 4, "review": "sweet city", "photos": ["https://picsum.photos/1666"]},
    )
    travellers["traveller4"].reviewed_city.connect(
        cities["city3"],
        {"rating": 3, "review": "sweet city", "photos": ["https://picsum.photos/1666"]},
    )
    travellers["traveller4"].reviewed_city.connect(
        cities["city4"],
        {"rating": 5, "review": "sweet city", "photos": ["https://picsum.photos/1666"]},
    )
    travellers["traveller5"].reviewed_city.connect(
        cities["city4"],
        {"rating": 4, "review": "sweet city", "photos": ["https://picsum.photos/1666"]},
    )
    travellers["traveller3"].reviewed_city.connect(
        cities["city4"],
        {"rating": 4, "review": "sweet city", "photos": ["https://picsum.photos/1666"]},
    )
    travellers["traveller4"].reviewed_city.connect(
        cities["city5"],
        {"rating": 5, "review": "sweet city", "photos": ["https://picsum.photos/1666"]},
    )
    travellers["traveller3"].reviewed_city.connect(
        cities["city5"],
        {"rating": 5, "review": "sweet city", "photos": ["https://picsum.photos/1666"]},
    )
    travellers["traveller5"].reviewed_city.connect(
        cities["city5"],
        {"rating": 3, "review": "sweet city", "photos": ["https://picsum.photos/1666"]},
    )


def seed_hotel_review_relation(travellers, hotels):
    travellers["traveller4"].reviewed_hotel.connect(
        hotels["hotel1"],
        {
            "rating": 5,
            "review": "Amazing place, Ambience, staff, location, views, service everything is worth.Good Hotel with good resturants-renovated rooms and good facility at an ideal location in Mumbai-convenient for both business as well as leisure travellers. The food and choice of resturants are good. Hotel staff is friendly and courteous.",
            "photos": [
                "https://media-cdn.tripadvisor.com/media/photo-m/1280/1b/a5/d8/c1/exterior.jpg"
            ],
        },
    )
    travellers["traveller2"].reviewed_hotel.connect(
        hotels["hotel1"],
        {
            "rating": 3,
            "review": "We were given dinner coupons. They are taking outside walkin customers too. We got no place to sit in at Masala Craft or Shamiana. Our family had to dine at the ball room which was a bad experience. Its like a marriage hall. We could not sit together as men wanted to drink but ambience was not that great. We complained to the food and beverage manager,he was not very helping, trying to convince us that only ballroom dinner was in the package. While booking your executive Beverly clearly mentioned that lunch or dinner could be had at Masala craft or shamiana. We wasted an hour to request a place to sit for 8 people. After a bad experience next morning post bfast we asked for for a lunch booking at one of the designated restaurants. Reception directed to go see the restaurant. MASALA craft was closed. When we went to shamiana we were told appointments are only given to walkins! Some confusion in their own staff. F&B manager had to book for us at shamiana.This could have been handled better. Some positives too- suites were excellent, sea lounge for its view,and amazing lunch at shamiana cellar.",
            "photos": [
                "https://media-cdn.tripadvisor.com/media/photo-m/1280/19/3f/1e/5b/other.jpg"
            ],
        },
    )
    travellers["traveller3"].reviewed_hotel.connect(
        hotels["hotel2"],
        {
            "rating": 5,
            "review": " had a good experience at the JW Marriott Juhu. After many months of being cooped up at home due to Covid, I visited this hotel in October. I was a trifle nervous as this was my first trip out of home post-Covid. However, it was a very reassuring experience to see contactless check-in, room service delivery outside the room and all staff wearing shields. Our room had a reasonable view of the sea and it was a delight to walk on Juhu Beach. I would like to particularly thank Mr. Rohit Tiwari- Director Rooms and Chef Alok Verma for taking great care of us. I hope to visit again",
            "photos": [
                "https://media-cdn.tripadvisor.com/media/photo-m/1280/1c/32/d3/ca/recreational-facilities.jpg"
            ],
        },
    )
    travellers["traveller4"].reviewed_hotel.connect(
        hotels["hotel3"],
        {
            "rating": 5,
            "review": "Great staff, nice rooms, good breakfast and cool activities organized by the hostel. Great place to meet other people. Definitely recommend staying here when visiting Mumbai staff is very good and friendly",
            "photos": [
                "https://media-cdn.tripadvisor.com/media/photo-o/11/ad/f2/bd/premier-plus-rooms-555.jpg"
            ],
        },
    )
    travellers["traveller2"].reviewed_hotel.connect(
        hotels["hotel3"],
        {
            "rating": 4,
            "review": "I stay in Adarsh Baug every year in August or September as a part of my business visit to Mumbai every year. I can really recommend it. Great hotel to stay if you like a homely environment with excellent staff and neighborhood. The manager and Reception Staff are wonderful and helpful !",
            "photos": [
                "https://media-cdn.tripadvisor.com/media/photo-o/11/ad/f2/bd/premier-plus-rooms-555.jpg"
            ],
        },
    )
    travellers["traveller4"].reviewed_hotel.connect(
        hotels["hotel7"],
        {
            "rating": 5,
            "review": "Stayed in room number 418, there seems to be an issue in the washroom, WC to be specific, it backs the water thereby it gets dirty water back to the WC in few minutes. Also I had booked double (king size bed) room and was given a twin room without any intimation by the front desk. I keep traveling to Delhi and generally stay in Holiday Inn or Roseate House, but I thought this time I will try a new hotel but not impressed. Just because I am traveling solo I shouldn't be given a twin room when I specifically booked a double room and incase you don't have rooms available then you should inform me at the reception before assigning the room to me. Also HK needs to look into the bathroom issue. Though I want to give a shout out to your service staff Mr. Saurabh, he attended me at breakfast and was extremely courteous and helpful.",
            "photos": [
                "https://media-cdn.tripadvisor.com/media/photo-o/11/ad/f2/bd/premier-plus-rooms-555.jpg"
            ],
        },
    )
    travellers["traveller3"].reviewed_hotel.connect(
        hotels["hotel7"],
        {
            "rating": 5,
            "review": "I had a safe, comfortable and convenient stay during my transit through New Delhi on a business travel.Hotel was clean and adequate cleanliness and COVID19 related protocols were comforting. It felt safe and staff was very co-operative and responsive.",
            "photos": [
                "https://media-cdn.tripadvisor.com/media/photo-o/11/ad/f2/bd/premier-plus-rooms-555.jpg"
            ],
        },
    )
    travellers["traveller3"].reviewed_hotel.connect(
        hotels["hotel5"],
        {
            "rating": 4,
            "review": "This was my first stay at any hotel since Covid 19 and was a little scared of how it would be but the moment I went into the lobby till my check out I was very well attended to and maintaining all the protection that's required to prevent Covid. Thanks a lot Vinayak and his team for taking good care and making me feel at home. Looking forward to staying with you guys again shortly",
            "photos": [
                "https://media-cdn.tripadvisor.com/media/photo-o/11/ad/f2/bd/premier-plus-rooms-555.jpg"
            ],
        },
    )
    travellers["traveller4"].reviewed_hotel.connect(
        hotels["hotel5"],
        {
            "rating": 4,
            "review": "There are not enough good words to say about the Oberoi New Delhi! It is EXCELLENT! We spent two weeks at the hotel and we were blown away by the accommodations, food and service. We traveled with our toddler and the hotel did an excellent job of meeting his and our needs. We did not want to leave!!! We had the most amazing meals and we were blown away by the Christmas day Santa and breath-taking buffet! The staff went above and beyond and got to know our family but also maintained professionalism.",
            "photos": [
                "https://media-cdn.tripadvisor.com/media/photo-o/11/ad/f2/bd/premier-plus-rooms-555.jpg"
            ],
        },
    )
    travellers["traveller2"].reviewed_hotel.connect(
        hotels["hotel5"],
        {
            "rating": 4,
            "review": "his was my first visit to Delhi post Covid and living in uttarakhand I had been very paranoid about travelling. I must say I was highly impressed with the protocols the hotel is following while as always maintaining the highest quality of services and hospitality. One can feel that they are really taking care to ensure your safety in these times. The staff is very professional and courteous and takes care of all your needs. We had a very pleasant stay",
            "photos": [
                "https://media-cdn.tripadvisor.com/media/photo-o/11/ad/f2/bd/premier-plus-rooms-555.jpg"
            ],
        },
    )


def seed_hotel_like_relation(travellers, hotels):
    travellers["traveller2"].likes_hotel.connect(hotels["hotel1"])
    travellers["traveller2"].likes_hotel.connect(hotels["hotel3"])
    travellers["traveller3"].likes_hotel.connect(hotels["hotel5"])
    travellers["traveller3"].likes_hotel.connect(hotels["hotel6"])
    travellers["traveller4"].likes_hotel.connect(hotels["hotel2"])
    travellers["traveller4"].likes_hotel.connect(hotels["hotel1"])
    travellers["traveller4"].likes_hotel.connect(hotels["hotel5"])


def seed_hotelier_relations(hoteliers, hotels):
    hoteliers["hotelowner1"].owns_hotel.connect(hotels["hotel1"])
    hoteliers["hotelowner1"].owns_hotel.connect(hotels["hotel2"])
    hoteliers["hotelowner1"].owns_hotel.connect(hotels["hotel3"])
    hoteliers["hotelowner1"].owns_hotel.connect(hotels["hotel5"])
    hoteliers["hotelowner1"].owns_hotel.connect(hotels["hotel6"])
    hoteliers["hotelowner1"].owns_hotel.connect(hotels["hotel7"])
    hoteliers["hotelowner1"].owns_hotel.connect(hotels["hotel8"])
    hoteliers["hotelowner1"].owns_hotel.connect(hotels["hotel9"])
    hoteliers["hotelowner3"].owns_hotel.connect(hotels["hotel10"])
    hoteliers["hotelowner3"].owns_hotel.connect(hotels["hotel11"])
    hoteliers["hotelowner3"].owns_hotel.connect(hotels["hotel12"])
    hoteliers["hotelowner3"].owns_hotel.connect(hotels["hotel13"])
    hoteliers["hotelowner3"].owns_hotel.connect(hotels["hotel14"])
    hoteliers["hotelowner3"].owns_hotel.connect(hotels["hotel15"])
    hoteliers["hotelowner3"].owns_hotel.connect(hotels["hotel16"])


def seed_shopier_relation(shopiers, shops):
    shopiers["shopowner1"].owns_shop.connect(shops["shop1"])
    shopiers["shopowner1"].owns_shop.connect(shops["shop2"])
    shopiers["shopowner1"].owns_shop.connect(shops["shop3"])
    shopiers["shopowner1"].owns_shop.connect(shops["shop4"])
    shopiers["shopowner1"].owns_shop.connect(shops["shop5"])
    shopiers["shopowner2"].owns_shop.connect(shops["shop6"])
    shopiers["shopowner2"].owns_shop.connect(shops["shop7"])
    shopiers["shopowner2"].owns_shop.connect(shops["shop8"])
    shopiers["shopowner2"].owns_shop.connect(shops["shop9"])
    shopiers["shopowner2"].owns_shop.connect(shops["shop10"])
    shopiers["shopowner3"].owns_shop.connect(shops["shop11"])
    shopiers["shopowner3"].owns_shop.connect(shops["shop12"])
    shopiers["shopowner3"].owns_shop.connect(shops["shop13"])
    shopiers["shopowner3"].owns_shop.connect(shops["shop14"])
    shopiers["shopowner3"].owns_shop.connect(shops["shop15"])


def seed_package_agency(packages, agencies):
    packages["package1"].offered_by.connect(agencies["agency1"])
    packages["package2"].offered_by.connect(agencies["agency2"])
    packages["package3"].offered_by.connect(agencies["agency3"])
    packages["package4"].offered_by.connect(agencies["agency1"])
    packages["package5"].offered_by.connect(agencies["agency2"])
    packages["package6"].offered_by.connect(agencies["agency3"])


def seed_shop_review_relation(travellers, shops):
    travellers["traveller1"].reviewed_shop.connect(
        shops["shop1"],
        {
            "rating": 3,
            "review": "nice shop, really polite customer service, cute stuff",
            "photos": ["https://picsum.photos/1090"],
        },
    )
    travellers["traveller2"].reviewed_shop.connect(
        shops["shop15"],
        {
            "rating": 4,
            "review": "nice shop, really polite customer service, cute stuff",
            "photos": ["https://picsum.photos/1090"],
        },
    )
    travellers["traveller2"].reviewed_shop.connect(
        shops["shop2"],
        {
            "rating": 5,
            "review": "nice shop, really polite customer service, cute stuff",
            "photos": ["https://picsum.photos/1090"],
        },
    )
    travellers["traveller3"].reviewed_shop.connect(
        shops["shop14"],
        {
            "rating": 4,
            "review": "nice shop, really polite customer service, cute stuff",
            "photos": ["https://picsum.photos/1090"],
        },
    )
    travellers["traveller1"].reviewed_shop.connect(
        shops["shop13"],
        {
            "rating": 4,
            "review": "nice shop, really polite customer service, cute stuff",
            "photos": ["https://picsum.photos/1090"],
        },
    )
    travellers["traveller1"].reviewed_shop.connect(
        shops["shop12"],
        {
            "rating": 5,
            "review": "nice shop, really polite customer service, cute stuff",
            "photos": ["https://picsum.photos/1090"],
        },
    )
    travellers["traveller5"].reviewed_shop.connect(
        shops["shop11"],
        {
            "rating": 3,
            "review": "nice shop, really polite customer service, cute stuff",
            "photos": ["https://picsum.photos/1090"],
        },
    )
    travellers["traveller5"].reviewed_shop.connect(
        shops["shop10"],
        {
            "rating": 3,
            "review": "nice shop, really polite customer service, cute stuff",
            "photos": ["https://picsum.photos/1090"],
        },
    )
    travellers["traveller2"].reviewed_shop.connect(
        shops["shop4"],
        {
            "rating": 3,
            "review": "nice shop, really polite customer service, cute stuff",
            "photos": ["https://picsum.photos/1090"],
        },
    )
    travellers["traveller1"].reviewed_shop.connect(
        shops["shop9"],
        {
            "rating": 5,
            "review": "nice shop, really polite customer service, cute stuff",
            "photos": ["https://picsum.photos/1090"],
        },
    )
    travellers["traveller1"].reviewed_shop.connect(
        shops["shop5"],
        {
            "rating": 4,
            "review": "nice shop, really polite customer service, cute stuff",
            "photos": ["https://picsum.photos/1090"],
        },
    )
    travellers["traveller2"].reviewed_shop.connect(
        shops["shop8"],
        {
            "rating": 5,
            "review": "nice shop, really polite customer service, cute stuff",
            "photos": ["https://picsum.photos/1090"],
        },
    )
    travellers["traveller2"].reviewed_shop.connect(
        shops["shop6"],
        {
            "rating": 4,
            "review": "nice shop, really polite customer service, cute stuff",
            "photos": ["https://picsum.photos/1090"],
        },
    )
    travellers["traveller5"].reviewed_shop.connect(
        shops["shop6"],
        {
            "rating": 5,
            "review": "nice shop, really polite customer service, cute stuff",
            "photos": ["https://picsum.photos/1090"],
        },
    )


def seed_shop_like_relation(travellers, shops):
    travellers["traveller2"].likes_shop.connect(shops["shop1"])
    travellers["traveller2"].likes_shop.connect(shops["shop3"])
    travellers["traveller3"].likes_shop.connect(shops["shop5"])
    travellers["traveller3"].likes_shop.connect(shops["shop6"])
    travellers["traveller1"].likes_shop.connect(shops["shop2"])
    travellers["traveller1"].likes_shop.connect(shops["shop1"])
    travellers["traveller1"].likes_shop.connect(shops["shop5"])
    travellers["traveller1"].likes_shop.connect(shops["shop4"])


def seed_shop_city_relation(shops, cities):
    shops["shop1"].located_in.connect(cities["city1"])
    shops["shop2"].located_in.connect(cities["city1"])
    shops["shop3"].located_in.connect(cities["city1"])

    shops["shop4"].located_in.connect(cities["city3"])
    shops["shop5"].located_in.connect(cities["city3"])
    shops["shop6"].located_in.connect(cities["city3"])
    shops["shop7"].located_in.connect(cities["city3"])

    shops["shop8"].located_in.connect(cities["city2"])
    shops["shop9"].located_in.connect(cities["city2"])
    shops["shop10"].located_in.connect(cities["city2"])

    shops["shop11"].located_in.connect(cities["city4"])
    shops["shop12"].located_in.connect(cities["city4"])

    shops["shop13"].located_in.connect(cities["city5"])
    shops["shop15"].located_in.connect(cities["city5"])


def seed_attraction_city_relation(attractions, cities):
    attractions["attraction1"].located_in.connect(cities["city1"])
    attractions["attraction2"].located_in.connect(cities["city1"])
    attractions["attraction3"].located_in.connect(cities["city1"])
    attractions["attraction4"].located_in.connect(cities["city2"])
    attractions["attraction5"].located_in.connect(cities["city2"])
    attractions["attraction6"].located_in.connect(cities["city2"])
    attractions["attraction7"].located_in.connect(cities["city3"])
    attractions["attraction8"].located_in.connect(cities["city3"])
    attractions["attraction9"].located_in.connect(cities["city3"])
    attractions["attraction10"].located_in.connect(cities["city4"])
    attractions["attraction11"].located_in.connect(cities["city4"])
    attractions["attraction12"].located_in.connect(cities["city4"])
    attractions["attraction13"].located_in.connect(cities["city5"])
    attractions["attraction14"].located_in.connect(cities["city5"])
    attractions["attraction15"].located_in.connect(cities["city5"])


def seed_package_like_relation(packages, travellers):
    travellers["traveller1"].likes_package.connect(packages["package1"])
    travellers["traveller2"].likes_package.connect(packages["package2"])
    travellers["traveller3"].likes_package.connect(packages["package3"])
    travellers["traveller1"].likes_package.connect(packages["package4"])
    travellers["traveller2"].likes_package.connect(packages["package5"])
    travellers["traveller3"].likes_package.connect(packages["package6"])
