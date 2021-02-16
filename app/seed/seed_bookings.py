from ..models.database import Hotel, Package


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
            address="Apollo Bandar, Colaba, Mumbai, Maharashtra 400001",
            latitude=72.8333,
            longitude=18.922,
        ).save(),
        hotel2=Hotel(
            name="JW Marriott",
            price=4000,
            description="JW Marriott Mumbai Juhu is situated on the sands of Mumbai, India's popular Juhu Beach with a breathtaking view of the Arabian Sea.",
            photos=[
                "https://imgcy.trivago.com/c_lfill,d_dummy.jpeg,e_sharpen:60,f_auto,h_450,q_auto,w_450/itemimages/27/36/2736904_v5.jpeg",
                "https://media-cdn.tripadvisor.com/media/photo-m/1280/1c/32/d3/ca/recreational-facilities.jpg",
            ],
            address="Juhu Rd, Juhu Tara, Juhu, Mumbai, Maharashtra 400049",
            latitude=72.83,
            longitude=19.1,
        ).save(),
        hotel3=Hotel(
            name="Adarsh Baug Hotel",
            price=1050,
            description="Situated in Mumbai, Hotel Adarsh Baug is an ideal place for both a quick weekend getaway and a rejuvenating extended period of stay for people from all walks of life. The property is located at a distance of 2km from Mumbai CST Station.",
            photos=[
                "https://imgcy.trivago.com/c_lfill,d_dummy.jpeg,e_sharpen:60,f_auto,h_450,q_auto,w_450/itemimages/99/50/99501_v5.jpeg"
            ],
            address="No.103, Dr. Atmaram Merchant Road, Kalbadevi Road 400002 Mumbai India",
            latitude=72.835,
            longitude=18.955,
        ).save(),
        hotel5=Hotel(
            name="The Oberoi, New Delhi",
            price=4000,
            description="The Oberoi, New Delhi is an iconic luxury hotel in New Delhi. It is located in the centre of India's cosmopolitan capital city. ",
            photos=[
                "https://media-cdn.tripadvisor.com/media/photo-o/11/ad/f2/bd/premier-plus-rooms-555.jpg",
                "https://media-cdn.tripadvisor.com/media/photo-o/11/ad/f9/6e/swimming-pool.jpg",
                "https://media-cdn.tripadvisor.com/media/photo-o/11/ad/f2/bd/premier-plus-rooms-555.jpg",
            ],
            address="Dr. Zakir Hussain Marg, New Delhi 110003 India",
            latitude=77.237778,
            longitude=28.601633,
        ).save(),
        hotel6=Hotel(
            name="Taj Palace, New Delhi",
            price=6384,
            description="Nestled amidst the heart of the historic Indian capital city, the iconic Taj Palace, New Delhi has held a distinguished position amongst the finest hotels of the world for close to four decades. ",
            photos=[
                "https://media-cdn.tripadvisor.com/media/photo-s/1b/86/6e/77/exterior.jpg",
                "https://media-cdn.tripadvisor.com/media/photo-m/1280/14/12/23/62/taj-palace-new-delhi.jpg",
            ],
            address="2 Taj Palace, New Delhi Sardar Patel Marg Diplomatic Enclave, New Delhi 110021 India",
            latitude=77.183970,
            longitude=28.603750,
        ).save(),
        hotel7=Hotel(
            name="Hotel Novotel New Delhi Aerocity",
            price=3651,
            description="Novotel New Delhi Aerocity is an excellent choice for travellers visiting New Delhi, offering a family-friendly environment alongside many helpful amenities designed to enhance your stay.",
            photos=[
                "https://media-cdn.tripadvisor.com/media/photo-o/09/bb/11/96/novotel-new-delhi-aerocity.jpg",
                "https://media-cdn.tripadvisor.com/media/photo-o/11/54/45/31/pool.jpg",
            ],
            address="Asset No 02 GMR Hospitality District, IGI Airport, New Delhi 110037 India",
            latitude=77.122304,
            longitude=28.5925928,
        ).save(),
        hotel8=Hotel(
            name="The Corinthians Resort & Club",
            price=5854,
            description="The Corinthians is a five-star hotel located in the verdant hilltop of South Pune. Well-appointed Rooms, Executive and Presidential Suites designed in Moroccan architecture, The Corinthians Boutique Hotel reflects the glory of a bygone era, re-created with all minute details, providing all the modern amenities that the business traveler would wish to have. ",
            photos=[
                "https://media-cdn.tripadvisor.com/media/photo-o/03/c5/3e/5d/the-corinthians-boutique.jpg"
            ],
            address="Nyati County, NIBM Annex South Pune, Pune 411001 India",
            latitude=73.8554,
            longitude=18.5196,
        ).save(),
        hotel9=Hotel(
            name="Royal Orchid Central Pune",
            price=2970,
            description="Royal Orchid Central – the upscale Business hotel centrally located in the heart of Pune City, which is carefully designed keeping in mind the diverse needs of today’s discerning global business traveler.",
            photos=[
                "https://media-cdn.tripadvisor.com/media/photo-o/14/81/b1/5e/exterior.jpg"
            ],
            address="Kalyani Nagar Marisoft Annexe, Pune 411014 India",
            latitude=73.9248107,
            longitude=18.5514138,
        ).save(),
        hotel10=Hotel(
            name="Amanora The Fern",
            price=4390,
            description="Amanora The Fern is the most premium club & hotel committed to offering top notch facilities ,perfect for corporate as well as leisure travellers.",
            photos=[
                "https://media-cdn.tripadvisor.com/media/photo-m/1280/0f/3f/83/92/getlstd-property-photo.jpg",
                "https://media-cdn.tripadvisor.com/media/photo-s/02/5d/b1/b4/outdoor.jpg",
            ],
            address="Amanora Magarpatta Road Amanora Park Town, Pune 411028 India",
            latitude=73.9167,
            longitude=18.5167,
        ).save(),
        hotel11=Hotel(
            name="Trident, Jaipur",
            price=5929,
            description="Surrender to the charms of this beautiful city when you stay in Trident, Jaipur; ranked amongst the best resorts in Jaipur.",
            photos=[
                "https://media-cdn.tripadvisor.com/media/photo-s/01/f7/e0/77/exterior.jpg",
                "https://media-cdn.tripadvisor.com/media/photo-s/01/f7/e0/7b/swimming-pool.jpg",
                "https://media-cdn.tripadvisor.com/media/photo-o/1c/62/b3/1d/trident-jaipur.jpg",
            ],
            address="Amber Fort Rd opposite Jal Mahal, Jaipur 302002 India",
            latitude=75.7878,
            longitude=26.9196,
        ).save(),
        hotel12=Hotel(
            name="The Fern Residency",
            price=1794,
            description="he Fern Residency Jaipur is a midscale hotel located in the city center of Jaipur, best suited for both business and leisure travelers.",
            photos=[
                "https://media-cdn.tripadvisor.com/media/photo-s/15/4c/1f/e0/bird-eye-view.jpg",
                "https://media-cdn.tripadvisor.com/media/photo-m/1280/15/4c/1c/09/the-fern-residency.jpg",
                "https://media-cdn.tripadvisor.com/media/photo-m/1280/15/4c/1b/f8/the-fern-residency.jpg",
                "https://media-cdn.tripadvisor.com/media/photo-m/1280/15/4c/1b/d6/the-fern-residency.jpg",
            ],
            address="A-13, Govind Marg near Pink Square Mall Raja Park, Jaipur 302004 India",
            latitude=75.8189817,
            longitude=26.9154576,
        ).save(),
        hotel13=Hotel(
            name="Hotel Anuraag Villa",
            price=1112,
            description="ANURAAG VILLA is situated in a serene posh residential colony with pleasant interiors and aesthetic rooms, in the vicinity of central bus stand and main railway station. ",
            photos=[
                "https://media-cdn.tripadvisor.com/media/photo-o/03/07/4b/04/hotel-anuraag-villa.jpg",
                "https://media-cdn.tripadvisor.com/media/photo-o/04/96/a2/d0/hotel-anuraag-villa.jpg",
            ],
            address="D-249, Devi Marg Bani Park, Jaipur 302016 India",
            latitude=75.7898622,
            longitude=26.9265113,
        ).save(),
        hotel14=Hotel(
            name="Novotel Ahmedabad",
            price=3719,
            description="Featuring floor to ceiling windows, an open air swimming pool and spacious modern rooms, Novotel Ahmedabad is located on S G Highway. Free Wi-Fi is available throughout.",
            photos=[
                "https://media-cdn.tripadvisor.com/media/photo-m/1280/1b/45/a4/3c/exterior-view.jpg",
                "https://media-cdn.tripadvisor.com/media/photo-o/05/99/9a/32/novotel-ahmedabad.jpg",
                "https://media-cdn.tripadvisor.com/media/photo-o/05/99/99/9d/novotel-ahmedabad.jpg",
            ],
            address="S G Highway ISKCON Cross road, Ahmedabad 380015 India",
            latitude=78.1196,
            longitude=9.9173,
        ).save(),
        hotel15=Hotel(
            name="Fortune Park, Ahmedabad",
            price=3024,
            description="Fortune Park, Ahmedabad is a contemporary business hotel located centrally in one of the greenest areas of the city with excellent connectivity to the airport/ railway station, commercial zone and shopping hub.",
            photos=[
                "https://media-cdn.tripadvisor.com/media/photo-o/0a/cd/e8/6e/caption.jpg",
                "https://media-cdn.tripadvisor.com/media/photo-o/09/cd/9e/6b/lobby.jpg",
            ],
            address="Opposite Gujarat College, Ellis Bridge, Ahmedabad 380 006 India",
            latitude=72.3005439,
            longitude=22.7280538,
        ).save(),
        hotel16=Hotel(
            name="Hyatt Ahmedabad",
            price=6153,
            description="Hyatt Ahmedabad their hotel of choice when visiting Ahmedabad. Providing an ideal mix of value, comfort and convenience, it offers a luxury setting with an array of amenities designed for travellers like you.",
            photos=[
                "https://media-cdn.tripadvisor.com/media/photo-o/11/6f/7d/c8/swimming-pool.jpg",
                "https://media-cdn.tripadvisor.com/media/photo-m/1280/15/22/33/65/outer-deck-tg-s-the-oriental.jpg",
                "https://media-cdn.tripadvisor.com/media/photo-o/11/73/ca/5c/hotel-exterior.jpg",
            ],
            address="Plot 216, Town Plan Scheme 1 Near Vastrapur Lake, Ahmedabad 380015 India",
            latitude=23.0233421,
            longitude=72.5303767,
        ).save(),
    )


def seed_package():
    return dict(
        package1=Package(
            name="monsoon mumbai",
            price=110,
            description="Enjoy monsoon of mumbai at your pleasure",
            photos=[
                "https://picsum.photos/1000",
                "https://picsum.photos/1002",
                "https://picsum.photos/1003",
                "https://picsum.photos/1004",
            ],
            itinerary={},
        ).save(),
        package2=Package(
            name="majistic mumbai",
            price=15,
            description="The glory and majisticism of mumbai",
            photos=[
                "https://picsum.photos/1005",
                "https://picsum.photos/1006",
                "https://picsum.photos/1007",
                "https://picsum.photos/1008",
            ],
            itinerary={},
        ).save(),
        package3=Package(
            name="aamchi mumbai",
            price=110,
            description="Enjoy your mumbai",
            photos=[
                "https://picsum.photos/1009",
                "https://picsum.photos/1010",
                "https://picsum.photos/1011",
                "https://picsum.photos/1012",
            ],
            itinerary={},
        ).save(),
        package4=Package(
            name="Royalty of Jaipur",
            price=200,
            description="Experincy the royalty and plushiness of jaipur",
            photos=[
                "https://picsum.photos/1013",
                "https://picsum.photos/1014",
                "https://picsum.photos/1015",
                "https://picsum.photos/1016",
            ],
            itinerary={},
        ).save(),
        package5=Package(
            name="Dil se Dilli dekho",
            price=500,
            description="See the dehli for what it is, its heart",
            photos=[
                "https://picsum.photos/1017",
                "https://picsum.photos/1018",
                "https://picsum.photos/1019",
                "https://picsum.photos/1020",
            ],
            itinerary={},
        ).save(),
        package6=Package(
            name="Have Pleasure in Pune",
            price=100,
            description="Have pleasure of reliving the marathas of pune",
            photos=[
                "https://picsum.photos/1021",
                "https://picsum.photos/1022",
                "https://picsum.photos/1023",
                "https://picsum.photos/1024",
            ],
            itinerary={},
        ).save(),
    )
