from os import environ

from fastapi import FastAPI
from neomodel import config

from .routers import (
    agency,
    attraction,
    blog,
    city,
    hotel,
    hotel_owner,
    package,
    shop,
    shop_owner,
    traveller,
)
from .seed import seed_db

app = FastAPI()
config.DATABASE_URL = (
    f"bolt://{environ['NEO4J_AUTH_USER']}"
    f":{environ['NEO4J_AUTH_PASS']}"
    f"@{environ['NEO4J_HOST']}:7687"
)


@app.get("/")
def read_root():
    return "Travel Buddy API"


@app.get("/seed/")
def seed_endpoint():
    seed_db()


app.include_router(agency.router, prefix="/agency")
app.include_router(attraction.router, prefix="/attraction")
app.include_router(blog.router, prefix="/blog")
app.include_router(city.router, prefix="/city")
app.include_router(hotel.router, prefix="/hotel")
app.include_router(hotel_owner.router, prefix="/hotel_owner")
app.include_router(package.router, prefix="/package")
app.include_router(shop.router, prefix="/shop")
app.include_router(shop_owner.router, prefix="/shop_owner")
app.include_router(traveller.router, prefix="/traveller")
