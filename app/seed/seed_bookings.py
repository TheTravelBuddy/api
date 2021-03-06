from ..models.database import Hotel, Package, PackageDay


def seed_hotel():
    return dict(
        hotel1=Hotel(
            name="Taj Mahal Palace",
            price=3500,
            description="Built in 1903, The Taj Mahal Palace, Mumbai is India's first luxury hotel. Offering panoramic views of the Arabian Sea and the Gateway of India, the hotel is a city landmark.",
            photos=[
                "https://media-cdn.tripadvisor.com/media/photo-m/1280/1b/a5/d8/c1/exterior.jpg",
                "https://media-cdn.tripadvisor.com/media/photo-m/1280/1b/a5/d8/c1/exterior.jpg",
                "https://media-cdn.tripadvisor.com/media/photo-m/1280/19/3f/1e/5b/other.jpg",
            ],
            locality="Colaba",
            postal_code=400001,
            address="Apollo Bandar",
            longitude=72.8333,
            latitude=18.922,
            phone="+911234567890",
            amenities=[
                "WIFI",
                "SWIMMING_POOL",
                "AIR_CONDITIONING",
                "GYM",
                "PARKING",
                "SPA",
            ],
        ).save(),
        hotel2=Hotel(
            name="JW Marriott",
            price=4000,
            description="JW Marriott Mumbai Juhu is situated on the sands of Mumbai, India's popular Juhu Beach with a breathtaking view of the Arabian Sea.",
            photos=[
                "https://imgcy.trivago.com/c_lfill,d_dummy.jpeg,e_sharpen:60,f_auto,h_450,q_auto,w_450/itemimages/27/36/2736904_v5.jpeg",
                "https://media-cdn.tripadvisor.com/media/photo-m/1280/1c/32/d3/ca/recreational-facilities.jpg",
            ],
            locality="Juhu",
            postal_code=400049,
            address="Juhu Rd, Juhu Tara",
            longitude=72.83,
            latitude=19.1,
            phone="+911234567890",
            amenities=[
                "WIFI",
                "SWIMMING_POOL",
                "AIR_CONDITIONING",
                "GYM",
                "PARKING",
                "SPA",
            ],
        ).save(),
        hotel3=Hotel(
            name="Adarsh Baug Hotel",
            price=1050,
            description="Situated in Mumbai, Hotel Adarsh Baug is an ideal place for both a quick weekend getaway and a rejuvenating extended period of stay for people from all walks of life. The property is located at a distance of 2km from Mumbai CST Station.",
            photos=[
                "https://imgcy.trivago.com/c_lfill,d_dummy.jpeg,e_sharpen:60,f_auto,h_450,q_auto,w_450/itemimages/99/50/99501_v5.jpeg"
            ],
            locality="Kalbadevi",
            postal_code=400002,
            address="No.103, Dr. Atmaram Merchant Road",
            longitude=72.835,
            latitude=18.955,
            phone="+911234567890",
            amenities=["WIFI", "AIR_CONDITIONING", "PARKING"],
        ).save(),
        hotel5=Hotel(
            name="The Oberoi",
            price=4000,
            description="The Oberoi, New Delhi is an iconic luxury hotel in New Delhi. It is located in the centre of India's cosmopolitan capital city. ",
            photos=[
                "https://media-cdn.tripadvisor.com/media/photo-o/11/ad/f2/bd/premier-plus-rooms-555.jpg",
                "https://media-cdn.tripadvisor.com/media/photo-o/11/ad/f9/6e/swimming-pool.jpg",
                "https://media-cdn.tripadvisor.com/media/photo-o/11/ad/f2/bd/premier-plus-rooms-555.jpg",
            ],
            locality="Zakir Hussain Marg",
            postal_code=110003,
            address="Dr. Zakir Hussain Marg",
            longitude=77.237778,
            latitude=28.601633,
            phone="+911234567890",
            amenities=[
                "WIFI",
                "SWIMMING_POOL",
                "AIR_CONDITIONING",
                "PARKING",
                "SPA",
            ],
        ).save(),
        hotel6=Hotel(
            name="Taj Palace",
            price=6384,
            description="Nestled amidst the heart of the historic Indian capital city, the iconic Taj Palace, New Delhi has held a distinguished position amongst the finest hotels of the world for close to four decades. ",
            photos=[
                "https://media-cdn.tripadvisor.com/media/photo-s/1b/86/6e/77/exterior.jpg",
                "https://media-cdn.tripadvisor.com/media/photo-m/1280/14/12/23/62/taj-palace-new-delhi.jpg",
            ],
            locality="Diplomatic Enclave",
            postal_code=110021,
            address="Sardar Patel Marg",
            longitude=77.183970,
            latitude=28.603750,
            phone="+911234567890",
            amenities=[
                "WIFI",
                "AIR_CONDITIONING",
                "GYM",
                "PARKING",
                "SPA",
            ],
        ).save(),
        hotel7=Hotel(
            name="Hotel Novotel Aerocity",
            price=3651,
            description="Novotel New Delhi Aerocity is an excellent choice for travellers visiting New Delhi, offering a family-friendly environment alongside many helpful amenities designed to enhance your stay.",
            photos=[
                "https://media-cdn.tripadvisor.com/media/photo-o/09/bb/11/96/novotel-new-delhi-aerocity.jpg",
                "https://media-cdn.tripadvisor.com/media/photo-o/11/54/45/31/pool.jpg",
            ],
            locality="IGI Airport",
            postal_code=110037,
            address="Asset No 02 GMR Hospitality District",
            longitude=77.122304,
            latitude=28.5925928,
            phone="+911234567890",
            amenities=[
                "WIFI",
                "SWIMMING_POOL",
                "AIR_CONDITIONING",
                "GYM",
                "PARKING",
            ],
        ).save(),
        hotel8=Hotel(
            name="The Corinthians Resort & Club",
            price=5854,
            description="The Corinthians is a five-star hotel located in the verdant hilltop of South Pune. Well-appointed Rooms, Executive and Presidential Suites designed in Moroccan architecture, The Corinthians Boutique Hotel reflects the glory of a bygone era, re-created with all minute details, providing all the modern amenities that the business traveler would wish to have. ",
            photos=[
                "https://media-cdn.tripadvisor.com/media/photo-o/03/c5/3e/5d/the-corinthians-boutique.jpg"
            ],
            locality="South Pune",
            postal_code=411001,
            address="Nyati County, NIBM Annex",
            longitude=73.8554,
            latitude=18.5196,
            phone="+911234567890",
            amenities=[
                "WIFI",
                "SWIMMING_POOL",
                "AIR_CONDITIONING",
                "PARKING",
                "SPA",
            ],
        ).save(),
        hotel9=Hotel(
            name="Royal Orchid Central",
            price=2970,
            description="Royal Orchid Central – the upscale Business hotel centrally located in the heart of Pune City, which is carefully designed keeping in mind the diverse needs of today’s discerning global business traveler.",
            photos=[
                "https://media-cdn.tripadvisor.com/media/photo-o/14/81/b1/5e/exterior.jpg"
            ],
            locality="Kalyani Nagar",
            postal_code=411014,
            address="Kalyani Nagar, Marisoft Annexe",
            longitude=73.9248107,
            latitude=18.5514138,
            phone="+911234567890",
            amenities=[
                "WIFI",
                "AIR_CONDITIONING",
                "GYM",
                "PARKING",
                "SPA",
            ],
        ).save(),
        hotel10=Hotel(
            name="Amanora The Fern",
            price=4390,
            description="Amanora The Fern is the most premium club & hotel committed to offering top notch facilities ,perfect for corporate as well as leisure travellers.",
            photos=[
                "https://media-cdn.tripadvisor.com/media/photo-m/1280/0f/3f/83/92/getlstd-property-photo.jpg",
                "https://media-cdn.tripadvisor.com/media/photo-s/02/5d/b1/b4/outdoor.jpg",
            ],
            locality="Amanora Park Town",
            postal_code=411028,
            address="Amanora Magarpatta Road",
            longitude=73.9167,
            latitude=18.5167,
            phone="+911234567890",
            amenities=[
                "WIFI",
                "SWIMMING_POOL",
                "AIR_CONDITIONING",
                "GYM",
                "PARKING",
            ],
        ).save(),
        hotel11=Hotel(
            name="Trident",
            price=5929,
            description="Surrender to the charms of this beautiful city when you stay in Trident, Jaipur; ranked amongst the best resorts in Jaipur.",
            photos=[
                "https://media-cdn.tripadvisor.com/media/photo-s/01/f7/e0/77/exterior.jpg",
                "https://media-cdn.tripadvisor.com/media/photo-s/01/f7/e0/7b/swimming-pool.jpg",
                "https://media-cdn.tripadvisor.com/media/photo-o/1c/62/b3/1d/trident-jaipur.jpg",
            ],
            locality="Jal Mahal",
            postal_code=302002,
            address="Amber Fort Rd",
            longitude=75.7878,
            latitude=26.9196,
            phone="+911234567890",
            amenities=[
                "WIFI",
                "SWIMMING_POOL",
                "AIR_CONDITIONING",
                "PARKING",
            ],
        ).save(),
        hotel12=Hotel(
            name="The Fern Residency",
            price=1794,
            description="The Fern Residency Jaipur is a midscale hotel located in the city center of Jaipur, best suited for both business and leisure travelers.",
            photos=[
                "https://media-cdn.tripadvisor.com/media/photo-s/15/4c/1f/e0/bird-eye-view.jpg",
                "https://media-cdn.tripadvisor.com/media/photo-m/1280/15/4c/1c/09/the-fern-residency.jpg",
                "https://media-cdn.tripadvisor.com/media/photo-m/1280/15/4c/1b/f8/the-fern-residency.jpg",
                "https://media-cdn.tripadvisor.com/media/photo-m/1280/15/4c/1b/d6/the-fern-residency.jpg",
            ],
            locality="Raja Park",
            postal_code=302004,
            address="A-13, Govind Marg near Pink Square Mall",
            longitude=75.8189817,
            latitude=26.9154576,
            phone="+911234567890",
            amenities=[
                "WIFI",
                "SWIMMING_POOL",
                "AIR_CONDITIONING",
                "GYM",
                "PARKING",
                "SPA",
            ],
        ).save(),
        hotel13=Hotel(
            name="Hotel Anuraag Villa",
            price=1112,
            description="ANURAAG VILLA is situated in a serene posh residential colony with pleasant interiors and aesthetic rooms, in the vicinity of central bus stand and main railway station. ",
            photos=[
                "https://media-cdn.tripadvisor.com/media/photo-o/03/07/4b/04/hotel-anuraag-villa.jpg",
                "https://media-cdn.tripadvisor.com/media/photo-o/04/96/a2/d0/hotel-anuraag-villa.jpg",
            ],
            locality="Bani Park",
            postal_code=302016,
            address="D-249, Devi Marg",
            longitude=75.7898622,
            latitude=26.9265113,
            phone="+911234567890",
            amenities=[
                "WIFI",
                "SWIMMING_POOL",
                "AIR_CONDITIONING",
                "SPA",
            ],
        ).save(),
        hotel14=Hotel(
            name="Novotel",
            price=3719,
            description="Featuring floor to ceiling windows, an open air swimming pool and spacious modern rooms, Novotel Ahmedabad is located on S G Highway. Free Wi-Fi is available throughout.",
            photos=[
                "https://media-cdn.tripadvisor.com/media/photo-m/1280/1b/45/a4/3c/exterior-view.jpg",
                "https://media-cdn.tripadvisor.com/media/photo-o/05/99/9a/32/novotel-ahmedabad.jpg",
                "https://media-cdn.tripadvisor.com/media/photo-o/05/99/99/9d/novotel-ahmedabad.jpg",
            ],
            locality="Ahmedabad",
            postal_code=380015,
            address="S G Highway",
            longitude=78.1196,
            latitude=9.9173,
            phone="+911234567890",
            amenities=["WIFI", "AIR_CONDITIONING", "PARKING", "SPA"],
        ).save(),
        hotel15=Hotel(
            name="Fortune Park",
            price=3024,
            description="Fortune Park, Ahmedabad is a contemporary business hotel located centrally in one of the greenest areas of the city with excellent connectivity to the airport/ railway station, commercial zone and shopping hub.",
            photos=[
                "https://media-cdn.tripadvisor.com/media/photo-o/0a/cd/e8/6e/caption.jpg",
                "https://media-cdn.tripadvisor.com/media/photo-o/09/cd/9e/6b/lobby.jpg",
            ],
            locality="Ellis Bridge",
            postal_code=380006,
            address="Opposite Gujarat College",
            longitude=72.3005439,
            latitude=22.7280538,
            phone="+911234567890",
            amenities=[
                "WIFI",
                "AIR_CONDITIONING",
                "GYM",
                "PARKING",
                "SPA",
            ],
        ).save(),
        hotel16=Hotel(
            name="Hyatt",
            price=6153,
            description="Hyatt Ahmedabad their hotel of choice when visiting Ahmedabad. Providing an ideal mix of value, comfort and convenience, it offers a luxury setting with an array of amenities designed for travellers like you.",
            photos=[
                "https://media-cdn.tripadvisor.com/media/photo-o/11/6f/7d/c8/swimming-pool.jpg",
                "https://media-cdn.tripadvisor.com/media/photo-m/1280/15/22/33/65/outer-deck-tg-s-the-oriental.jpg",
                "https://media-cdn.tripadvisor.com/media/photo-o/11/73/ca/5c/hotel-exterior.jpg",
            ],
            locality="Vastrapur Lake",
            postal_code=380015,
            address="Plot 216, Town Plan Scheme 1",
            longitude=23.0233421,
            latitude=72.5303767,
            phone="+911234567890",
            amenities=[
                "WIFI",
                "AIR_CONDITIONING",
                "PARKING",
                "SPA",
            ],
        ).save(),
    )


def seed_package():
    return dict(
        package1=Package(
            name="Monsoon Mumbai",
            price=110,
            description="Enjoy monsoon of mumbai at your pleasure",
            photos=[
                "https://picsum.photos/1000",
                "https://picsum.photos/1002",
                "https://picsum.photos/1003",
                "https://picsum.photos/1004",
            ],
            amenities=[
                "HOTELS",
                "SIGHTSEEING",
                "TRANSFERS",
                "MEALS",
                "CITY_TOURS",
            ],
        ).save(),
        package2=Package(
            name="Majistic Mumbai",
            price=15,
            description="The glory and majisticism of mumbai",
            photos=[
                "https://picsum.photos/1005",
                "https://picsum.photos/1006",
                "https://picsum.photos/1007",
                "https://picsum.photos/1008",
            ],
            amenities=[
                "HOTELS",
                "SIGHTSEEING",
                "TRANSFERS",
                "MEALS",
            ],
        ).save(),
        package3=Package(
            name="Aamchi Mumbai",
            price=110,
            description="Enjoy your mumbai",
            photos=[
                "https://picsum.photos/1009",
                "https://picsum.photos/1010",
                "https://picsum.photos/1011",
                "https://picsum.photos/1012",
            ],
            amenities=[
                "HOTELS",
                "FLIGHTS",
                "MEALS",
            ],
        ).save(),
        package4=Package(
            name="Royalty of Jaipur",
            price=200,
            description="Experience the royalty and plushiness of jaipur",
            photos=[
                "https://picsum.photos/1013",
                "https://picsum.photos/1014",
                "https://picsum.photos/1015",
                "https://picsum.photos/1016",
            ],
            amenities=[
                "HOTELS",
                "SIGHTSEEING",
                "TRANSFERS",
                "ACTIVITIES",
                "FLIGHTS",
                "MEALS",
                "CITY_TOURS",
            ],
        ).save(),
        package5=Package(
            name="Dil se Dilli Dekho",
            price=500,
            description="See the delhi for what it is, its heart",
            photos=[
                "https://picsum.photos/1017",
                "https://picsum.photos/1018",
                "https://picsum.photos/1019",
                "https://picsum.photos/1020",
            ],
            amenities=[
                "HOTELS",
                "TRANSFERS",
                "FLIGHTS",
                "MEALS",
            ],
        ).save(),
        package6=Package(
            name="Have Pleasure in Pune",
            price=100,
            description="Have pleasure of reliving the marathas of pune",
            photos=[
                "https://www.smartcitiesworld.net/AcuCustom/Sitename/DAM/022/Life-Republic-township-Pune_Planet.jpg",
                "https://picsum.photos/1022",
                "https://picsum.photos/1023",
                "https://picsum.photos/1024",
            ],
            amenities=[
                "HOTELS",
                "ACTIVITIES",
                "MEALS",
                "CITY_TOURS",
            ],
        ).save(),
    )


def seed_package_day(packages, cities):
    day1 = PackageDay(
        title="Leaving for Mumbai", description="Leave for mumbai from pune station"
    ).save()
    day2 = PackageDay(title="Travelling full day").save()
    day3 = PackageDay(
        title="Reach mumbai and do masti",
        description="Visit iconing bandra area of mumbai",
    ).save()
    day4 = PackageDay(
        title="South Bombay",
        description="Adore the victorian architecture of south bombay",
    ).save()
    day5 = PackageDay(
        title="Back with memories",
        description="Return to pune in flight",
    ).save()

    day1.visits_city.connect(cities["Pune"])
    day3.visits_city.connect(cities["Mumbai"])
    day4.visits_city.connect(cities["Mumbai"])
    day5.visits_city.connect(cities["Pune"])

    packages["package1"].has_day.connect(day1, {"day": 1})
    packages["package1"].has_day.connect(day2, {"day": 2})
    packages["package1"].has_day.connect(day3, {"day": 3})
    packages["package1"].has_day.connect(day4, {"day": 4})
    packages["package1"].has_day.connect(day5, {"day": 5})

    packages["package2"].has_day.connect(day2, {"day": 1})
    packages["package2"].has_day.connect(day3, {"day": 2})
    packages["package2"].has_day.connect(day4, {"day": 3})

    packages["package3"].has_day.connect(day1, {"day": 1})
    packages["package3"].has_day.connect(day2, {"day": 2})
    packages["package3"].has_day.connect(day3, {"day": 3})
    packages["package3"].has_day.connect(day4, {"day": 4})
    packages["package3"].has_day.connect(day5, {"day": 5})
