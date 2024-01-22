from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from movieController import router as artist_router

from neo4j import GraphDatabase

config = dotenv_values(".env")

app = FastAPI()

@app.on_event("startup")
def startup_db_client():
    driverneo = GraphDatabase.driver(config["NEO4J_URL"],
                                     auth=(config["NEO4J_USERNAME"], config["NEO4J_PWD"]))
    driverneo.verify_connectivity()

    app.neo4j_driver = driverneo
    app.mongodb_client = MongoClient(config["MONGODB_URL"])
    app.database = app.mongodb_client[config["DB_NAME"]]

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()
    app.neo4j_driver.close()


app.include_router(artist_router, tags=["movies"], prefix="/movies")