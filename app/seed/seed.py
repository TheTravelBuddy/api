from neomodel import db, install_all_labels, remove_all_labels

from .seed_blogs import seed_blog
from .seed_bookings import seed_hotel, seed_package
from .seed_locations import seed_attraction, seed_city
from .seed_relations import (
    seed_blog_relations,
    seed_city_review_relation,
    seed_package_review_relation,
)
from .seed_users import seed_agency, seed_hotel_owner, seed_shop_owner, seed_traveller


def seed_db():
    print("Seeding DB...")
    db.cypher_query("MATCH (n) DETACH DELETE n")

    remove_all_labels()
    print("Installing Labels...")
    install_all_labels()

    with db.transaction:
        print("Seeding Nodes...")
        seed_hotel()
        packages = seed_package()
        seed_attraction()
        cities = seed_city()
        seed_agency()
        seed_hotel_owner()
        seed_shop_owner()
        travellers = seed_traveller()
        blogs = seed_blog()

        print("Seeding Relations...")
        seed_blog_relations(travellers, blogs)
        seed_package_review_relation(travellers, packages)
        seed_city_review_relation(travellers, cities)
        print("Done.")
