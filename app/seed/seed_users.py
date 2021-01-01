from datetime import date

from ..models.database import Agency, HotelOwner, ShopOwner, Traveller


def seed_traveller():
    return dict(
        Lucifer=Traveller(
            name="Lucifer",
            phone="+917738886661",
            gender="M",
            dob=date(1999, 11, 1),
            mood="RELAX",
        ).save(),
        Michael=Traveller(
            name="Michael",
            phone="+917738883002",
            gender="M",
            dob=date(1998, 1, 4),
            mood="RELAX",
        ).save(),
        Jenovah=Traveller(
            name="Jenovah",
            phone="+917738883013",
            gender="M",
            dob=date(1999, 12, 25),
            mood="MIXED",
        ).save(),
        Ester=Traveller(
            name="Ester",
            phone="+917738883024",
            gender="F",
            dob=date(1999, 10, 18),
            mood="RELAX",
        ).save(),
        Lahari=Traveller(
            name="Lahari",
            phone="+917738883035",
            gender="M",
            dob=date(1999, 2, 20),
            mood="MIXED",
        ).save(),
        Gautam=Traveller(
            name="Gautam",
            phone="+917738883046",
            gender="M",
            dob=date(1999, 12, 12),
            mood="MIXED",
        ).save(),
        Justin=Traveller(
            name="Justin",
            phone="+917738883697",
            gender="M",
            dob=date(1999, 12, 13),
            mood="ADVENTURE",
        ).save(),
        Selena=Traveller(
            name="Selena",
            phone="+917738880377",
            gender="F",
            dob=date(1999, 7, 22),
            mood="ADVENTURE",
        ).save(),
        Jelena=Traveller(
            name="Jelena",
            phone="+917738881438",
            gender="F",
            dob=date(2010, 11, 7),
            mood="ADVENTURE",
        ).save(),
        Karki=Traveller(
            name="Karki",
            phone="+917738881429",
            gender="M",
            dob=date(1999, 12, 15),
            mood="ADVENTURE",
        ).save(),
    )


def seed_agency():
    return dict(
        Manish=Agency(
            name="Manish Travel Agency",
            phone="+912228074493",
            address=(
                "3,Puranmal Budna Shopping Centre,Central Bank, S V Road, ",
                "Jethava Nagar, Saket, Delhi, 110001",
            ),
            is_verified=False,
            latitude=28.644800,
            longitude=77.216721,
        ).save(),
        Lohana=Agency(
            name="Lohana Tour's and Travel",
            phone="+912228056448",
            address=(
                "Brahma Krupa,Kamla Nehru Cross Road Number 2, ",
                "Best Colony, Jethava Nagar, Kandivali West, Mumbai, ",
                "Maharashtra 400067",
            ),
            is_verified=True,
            latitude=19.076090,
            longitude=72.877426,
        ).save(),
        DNO=Agency(
            name="DiscountsAndOffers",
            phone="+919930989241",
            address="1,DiscountsAndOffers,Patel Road,Kandivali West,400067",
            is_verified=True,
            latitude=19.076090,
            longitude=72.877426,
        ).save(),
    )


def seed_shop_owner():
    return dict(
        Mittal=ShopOwner(
            name="Mittal",
            phone="+919930989200",
            address="5, Race Course Road,New Delhi,110001",
            is_verified=True,
            latitude=28.644800,
            longitude=77.216721,
        ).save(),
        Adani=ShopOwner(
            name="Adani",
            phone="+919930989201",
            address="7, Race Course Road,Mumbai,4000060",
            is_verified=True,
            latitude=19.076090,
            longitude=72.877426,
        ).save(),
        Ambani=ShopOwner(
            name="Ambani",
            phone="+919930989200",
            address="1, Race Course Road,Ahemdabad,320008",
            is_verified=True,
            latitude=19.076090,
            longitude=72.877426,
        ).save(),
    )


def seed_hotel_owner():
    return dict(
        Sanjiv=HotelOwner(
            name="Sanjiv Khana",
            phone="+919930989231",
            address=(
                "Asset No 02 Gmr Hospitality District, Igi Airport New Delhi, ",
                "New Delhi, Delhi 110037",
            ),
            is_verified=True,
            latitude=28.644800,
            longitude=77.216721,
        ),
        Ranveer=HotelOwner(
            name="Ranveer Bhar",
            phone="+919930989222",
            address="Balraj Sahani Marg, Juhu Beach, Juhu, Mumbai, Maharashtra 400049",
            is_verified=True,
            latitude=19.076090,
            longitude=72.877426,
        ),
        Vikas=HotelOwner(
            name="Vikas Khaana",
            phone="+919930989233",
            address=(
                "Iscon Cross Roads, Sarkhej - Gandhinagar Hwy, next to Wide ",
                "Angle Cinema, Ahmedabad, Gujarat 380015",
            ),
            is_verified=True,
            latitude=19.076090,
            longitude=72.877426,
        ),
    )
