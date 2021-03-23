from os import environ

import firebase_admin
from fastapi import FastAPI
from firebase_admin import credentials
from neomodel import config

from .routers import business, traveller
from .seed import seed_db

cred = credentials.Certificate("/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

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


app.include_router(traveller.router, prefix="/traveller")
app.include_router(business.router, prefix="/business")
