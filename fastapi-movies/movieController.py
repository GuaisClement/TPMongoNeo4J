from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from models import MovieUpdate, Movie, ReviewerInfo

router = APIRouter()

@router.get("/mongodb/", response_description="List all Movies", response_model=List[Movie])
def list_movies(request: Request):
    movies = list(request.app.database["movies"].find(limit=100))
    return movies

@router.get("/mongodb/title/{title}", response_description="Get movie by title", response_model=Movie)
def find_movie(title: str, request: Request):
    if (movie := request.app.database["movies"].find_one({"title": title})) is not None:
        return movie
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Movie with title {title} not found")

@router.get("/mongodb/actor/{actor}", response_description="Get movies by actor name", response_model=List[Movie])
def find_movies(actor: str, request: Request):
    if (movies := request.app.database["movies"].find({ "cast": { "$in": [actor] } })) is not None:
        return movies
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Artist with name {actor} not found")

@router.put("/mongodb/{title}", response_description="Update a Movie", response_model=Movie)
def update_movie(title: str, request: Request, movie: MovieUpdate = Body(...)):
    movie_data = {k: v for k, v in movie.dict().items() if v is not None}
    if len(movie_data) >= 1:

        update_result = request.app.database["movies"].update_one(
            {"title": title}, {"$set": movie_data}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Movie with title {title} not found")

    if (
        existing_movie := request.app.database["movies"].find_one({"title": title})
    ) is not None:
        return existing_movie

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Movie with title {title} not found")

@router.get("/neo4j/{movieTitle}", response_description="List all reviewer of a movie", response_model=List[str])
def list_movies(movieTitle: str, request: Request):
    cypher_query = '''
    MATCH (p:Person)-[:REVIEWED]->(m:Movie {title: $movie})
        RETURN p.name
    '''

    with request.app.neo4j_driver.session(database="neo4j") as session:
        results = session.read_transaction(
            lambda tx: tx.run(cypher_query,
                              movie=movieTitle).data())

        if not results:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No reviews for {movieTitle}")

        # Extract names from results and return as a list
        names = [record['p.name'] for record in results]

        return names

@router.get("/neo4j/person/{person}", response_description="List all reviews of a person", response_model=List[ReviewerInfo])
def list_movies(person: str, request: Request):
    cypher_query = '''
    MATCH (p:Person {name: $person})-[:REVIEWED]->(m:Movie)
        RETURN p.name AS userName, COUNT(m) AS numberOfMoviesRated, COLLECT(m.title) AS ratedMovies
    '''

    with request.app.neo4j_driver.session(database="neo4j") as session:
        results = session.read_transaction(
            lambda tx: tx.run(cypher_query,
                              person=person).data())

        if not results:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No movies reviewed by {person}")

        reviewer_info_list = [ReviewerInfo(**record) for record in results]
        return reviewer_info_list

@router.get("/neo4j_mongodb/", response_description="List all commmon movie", response_model=int)
def list_movies(request: Request):
    movies_from_mongodb = list(request.app.database["movies"].find( projection={"title": 1, "_id": 0}))
    # Extract names from results and return as a list
    titles_from_mongodb = [record['title'] for record in movies_from_mongodb]

    cypher_query = '''
    MATCH(m:Movie)
        RETURN m.title
    '''
    with request.app.neo4j_driver.session(database="neo4j") as session:
        results = session.read_transaction(
            lambda tx: tx.run(cypher_query).data())

        if not results:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No movies retrieved")

        # Extract names from results and return as a list
        titles_from_neo4j = [record['m.title'] for record in results]

        # Comptez le nombre de titres présents à la fois dans MongoDB et Neo4j
        common_titles_count = sum(1 for title in titles_from_mongodb if title in titles_from_neo4j)

        return common_titles_count

