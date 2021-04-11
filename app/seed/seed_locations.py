from ..models.database import Attraction, City, Shop


def seed_city():
    return dict(
        city1=City(
            name="Mumbai",
            description="A city of dreams that never sleeps",
            latitude=19.076090,
            longitude=72.877426,
            photos=["https://picsum.photos/1099"],
        ).save(),
        city2=City(
            name="Delhi",
            description="Dillbar Dilli",
            latitude=28.644800,
            longitude=77.216721,
            photos=["https://picsum.photos/1100"],
        ).save(),
        city3=City(
            name="Ahmedabad",
            description="Aapnu amdavad",
            latitude=23.033863,
            longitude=72.585022,
            photos=[
                "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQB-L9mqh5Eo2Zpdh7IfnLlPXj6BQSTnR20Gw&usqp=CAU"
            ],
        ).save(),
        city4=City(
            name="Jaipur",
            description="Padharo mhare desh",
            latitude=26.922070,
            longitude=75.778885,
            photos=["https://picsum.photos/1102"],
        ).save(),
        city5=City(
            name="Pune",
            description="Punari parimano",
            latitude=18.516726,
            longitude=73.856255,
            photos=[
                "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSzzEDLMcDiA2bp3wTAYdYlWfX_9eG70r2wkQ&usqp=CAU"
            ],
        ).save(),
    )


def seed_attraction():
    return dict(
        attraction1=Attraction(
            name="Gateway of India",
            description=(
                "Gateway of India, the best place to visit in Mumbai, "
                "was built in 1924 by George Willet to honor the visit of King George "
                "V and Queen Mary to Mumbai"
            ),
            latitude=18.9204,
            longitude=72.8301,
            photos=[],
        ).save(),
        attraction2=Attraction(
            name="Sanjay Gandhi National Park",
            description=(
                "Sprawling over an area of 104 sq. km. of land, this is one of "
                "the most-visited national parks in Asia and because of this, I give "
                "it the 2nd spot among all the best places to visit in Mumbai",
            ),
            latitude=19.2288,
            longitude=72.9182,
            photos=[],
        ).save(),
        attraction3=Attraction(
            name="Red Carpet Wax Museum",
            description=(
                "The array of wax statues displayed at The Red Carpet wax "
                "Museum is a one of its kind and stature here in India or be it Mumbai."
            ),
            latitude=19.099356,
            longitude=72.916344,
            photos=[],
        ).save(),
        attraction4=Attraction(
            name="The Red Fort",
            description=(
                "The beautiful Red Fort was built by Shah Jahan in 1648 and "
                "served as the seat of Mughal power until 1857."
            ),
            latitude=28.656473,
            longitude=77.242943,
            photos=[],
        ).save(),
        attraction5=Attraction(
            name=" Qutub Minar",
            description=(
                'Qutab Minar, is a minaret and "victory tower" that forms part of '
                "the Qutb complex, a UNESCO World Heritage Site in the Mehrauli area1 "
                "of New Delhi, India."
            ),
            latitude=28.6266,
            longitude=77.2091,
            photos=[],
        ).save(),
        attraction6=Attraction(
            name="Dada Hari Ni Vav",
            description=(
                "Built around 500 years ago under the reign of Mehmud Begda, "
                "Dada Hari Ni Vav is a stepwell."
            ),
            latitude=23.0512,
            longitude=72.6055,
            photos=[],
        ).save(),
        attraction7=Attraction(
            name="Sarkhej Roza",
            description=(
                "Located 7 kilometres southwest of Ahmedabad in the village "
                "of Makraba, Sarkhej Roza is an elegant architectural structure "
                "comprising various buildings grouped around a stepped tank. "
            ),
            latitude=22.9960,
            longitude=72.4997,
            photos=[],
        ).save(),
        attraction8=Attraction(
            name="Balvatika",
            description=(
                "Located on top of a hill in Ahmedabad, Balvatika is a "
                "children’s park overlooking the Kankaria Lake."
            ),
            latitude=23.0022,
            longitude=72.3604,
            photos=[],
        ).save(),
        attraction9=Attraction(
            name="Shaniwar Wada Palace",
            description=(
                "A prominent historical landmark in Pune is Shaniwarwada which "
                "is considered as one of the best pune tourist places. "
            ),
            latitude=18.5181,
            longitude=73.8533,
            photos=[],
        ).save(),
        attraction10=Attraction(
            name="Aga Khan Palace",
            description=(
                "Aga Khan Palace which was built by Sultan Muhammed Shah Aga "
                "Khan III in 1892."
            ),
            latitude=18.5523,
            longitude=73.9015,
            photos=[],
        ).save(),
        attraction11=Attraction(
            name="Dagdusheth Halwai Temple",
            description=(
                "A famous Ganesha temple in Pune is Shreemath Dagdusheth "
                "Halwai Temple which is a major attraction in Maharashtra. "
            ),
            latitude=18.5098,
            longitude=73.8535,
            photos=[],
        ).save(),
        attraction12=Attraction(
            name="Gurudwara Bangle Sahib",
            description=(
                "Gurudwara Bangla Sahib is one of the most prominent Sikh "
                "gurdwara, or Sikh house of worship, in Delhi, India"
            ),
            latitude=28.6267,
            longitude=77.2089,
            photos=[],
        ).save(),
        attraction13=Attraction(
            name="City Palace",
            description=(
                "City Palace has stood at the heart of the Old City of Jaipur "
                "for nearly three centuries, shortly after Maharaja Sawai Jai Singh ",
                "II decided to relocate his court from the city of Amber. Protected ",
                "by huge guard walls, the fairy-tale-like structure is still the ",
                "home of Jaipur's modern-day royal family, and is more extravagant ",
                "and enchanting than you might imagine.",
            ),
            latitude=26.9258,
            longitude=75.8237,
            photos=[],
        ).save(),
        attraction14=Attraction(
            name="Jantar Mantar",
            description=(
                "Jantar Mantar may look to be nothing more than a bunch ",
                "of larger-than-life abstract sculptures. But this is not an art ",
                "gallery—it's a special collection of astronomical tools started ",
                "by Rajput ruler Jai Singh II to measure the heavens nearly 300 ",
                "years ago.",
            ),
            latitude=26.9248,
            longitude=75.8246,
            photos=[],
        ).save(),
        attraction15=Attraction(
            name="Sinhagad Fort",
            description=(
                "Sinhagad is a hill fortress located at around 35 km southwest of "
                "the city of Pune, India."
            ),
            latitude=18.21563,
            longitude=73.451897,
            photos=[],
        ).save(),
    )


def seed_shops():
    return dict(
        shop1=Shop(
            name="Fast and Furios Food",
            description="Best Food ever",
            latitude=18.2204,
            longitude=72.5301,
            photos=["https://picsum.photos/1099"],
            phone="+919757266106",
            address="Shop No #, Bulguia Complex, City",
            locality="No Head Drangon Marg",
            postal_code=400360,
        ).save(),
        shop2=Shop(
            name="Fast and Furios Fashion",
            description="Best Fashion Ever",
            latitude=19.1288,
            longitude=72.9182,
            photos=["https://picsum.photos/1099"],
            phone="+919757266107",
            address="Shop No #, Bulguia Complex, City",
            locality="No Head Drangon Marg",
            postal_code=400361,
        ).save(),
        shop3=Shop(
            name="Beauty and Beat",
            description="Best glamourous fashion store",
            latitude=19.99356,
            longitude=72.16344,
            photos=["https://picsum.photos/1099"],
            phone="+919757266108",
            address="Shop No #, Bulguia Complex, City",
            locality="No Head Drangon Marg",
            postal_code=400362,
        ).save(),
        shop4=Shop(
            name="Memories Artical Shop",
            description="Artical Shop for Art",
            latitude=28.56473,
            longitude=77.42943,
            photos=["https://picsum.photos/1099"],
            phone="+919757266109",
            address="Shop No #, Bulguia Complex, City",
            locality="No Head Drangon Marg",
            postal_code=400363,
        ).save(),
        shop5=Shop(
            name="Gabrail Choor Gift Shop",
            description="Gift Shop from famous choor lane",
            latitude=28.266,
            longitude=77.091,
            photos=["https://picsum.photos/1099"],
            phone="+919757266101",
            address="Shop No #, Bulguia Complex, City",
            locality="No Head Drangon Marg",
            postal_code=400364,
        ).save(),
        shop6=Shop(
            name="Fire Food",
            description="Most Spicy Food Ever",
            latitude=23.512,
            longitude=72.055,
            photos=["https://picsum.photos/1099"],
            phone="+919757266102",
            address="Shop No #, Bulguia Complex, City",
            locality="No Head Drangon Marg",
            postal_code=400365,
        ).save(),
        shop7=Shop(
            name="Fcuk Fashion",
            description="Exclusive Fcuk store",
            latitude=22.960,
            longitude=72.997,
            photos=["https://picsum.photos/1099"],
            phone="+919757266103",
            address="Shop No #, Bulguia Complex, City",
            locality="No Head Drangon Marg",
            postal_code=400366,
        ).save(),
        shop8=Shop(
            name="Free Gift Shop",
            description="Free Gift Shops",
            latitude=23.90022,
            longitude=72.604,
            photos=["https://picsum.photos/1099"],
            phone="+919757266104",
            address="Shop No #, Bulguia Complex, City",
            locality="No Head Drangon Marg",
            postal_code=400367,
        ).save(),
        shop9=Shop(
            name="Esctasy Food",
            description="A Spine Tingling Food",
            latitude=18.5181,
            longitude=73.8533,
            photos=["https://picsum.photos/1099"],
            phone="+919757266105",
            address="Shop No #, Bulguia Complex, City",
            locality="No Head Drangon Marg",
            postal_code=400368,
        ).save(),
        shop10=Shop(
            name="depresso",
            description="A differnet Coffee Shop",
            latitude=18.5523,
            longitude=73.9015,
            photos=["https://picsum.photos/1099"],
            phone="+919757266111",
            address="Shop No #, Bulguia Complex, City",
            locality="No Head Drangon Marg",
            postal_code=400369,
        ).save(),
        shop11=Shop(
            name="Bang Bang Gift Shop",
            description="Gift Shop for those who bang",
            latitude=18.098,
            longitude=73.535,
            photos=["https://picsum.photos/1099"],
            phone="+919757266112",
            address="Shop No #, Bulguia Complex, City",
            locality="No Head Drangon Marg",
            postal_code=400370,
        ).save(),
        shop12=Shop(
            name="Smash Street",
            description="Smashing Street Food",
            latitude=26.6267,
            longitude=76.2089,
            photos=["https://picsum.photos/1099"],
            phone="+919757266113",
            address="Shop No #, Bulguia Complex, City",
            locality="No Head Drangon Marg",
            postal_code=400371,
        ).save(),
        shop13=Shop(
            name="Mark 42 Gift Shop",
            description="A Future Tech Gift Shop",
            latitude=26.258,
            longitude=75.237,
            photos=["https://picsum.photos/1099"],
            phone="+919757266114",
            address="Shop No #, Bulguia Complex, City",
            locality="No Head Drangon Marg",
            postal_code=400372,
        ).save(),
        shop14=Shop(
            name="Jantar Mantar Gift Shop",
            description=(
                "Jantar Mantar miniature Gifts larger-than-life abstract ",
                "sculptures.",
            ),
            latitude=26.9248,
            longitude=75.8246,
            photos=["https://picsum.photos/1099"],
            phone="+919757266115",
            address="Shop No #, Bulguia Complex, City",
            locality="No Head Drangon Marg",
            postal_code=400373,
        ).save(),
        shop15=Shop(
            name="Sinhagad Fort Gift Shop",
            description="Sinhagad is a hill fortress Gift Shop",
            latitude=18.21563,
            longitude=73.451897,
            photos=["https://picsum.photos/1099"],
            phone="+919757266117",
            address="Shop No #, Bulguia Complex, City",
            locality="No Head Drangon Marg",
            postal_code=400374,
        ).save(),
    )
