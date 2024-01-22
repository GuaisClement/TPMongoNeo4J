import uuid
from typing import Optional, List, Union
from pydantic import BaseModel, Field, HttpUrl

from datetime import datetime


class Imdb(BaseModel):
    rating: Optional[Union[float, str]] = None
    votes: Optional[Union[int, str]] = None
    id: Optional[int] = None

class Tomato(BaseModel):
    fresh: Optional[int] = None
    rotten: Optional[int] = None
    lastUpdated: Optional[datetime] = None

class Award(BaseModel):
    wins: Optional[int] = None
    nominations: Optional[int] = None
    text: Optional[str] = None

class Movie(BaseModel):
    _id: dict
    plot: Optional[str] = None
    genres: Optional[List[str]] = None
    runtime: Optional[int] = None
    cast: Optional[List[str]] = None
    title: Optional[str] = None
    poster: Optional[str] = None
    fullplot: Optional[str] = None
    languages: Optional[List[str]] = None
    released: Optional[datetime] = None
    directors: Optional[List[str]] = None
    rated: Optional[str] = None
    awards: Optional[Award] = None
    lastupdated: Optional[datetime] = None
    year: Optional[Union[int, str]] = None
    imdb: Optional[Imdb] = None
    countries: Optional[List[str]] = None
    type: Optional[str] = None
    tomatoes: Optional[Tomato] = None
    num_mflix_comments: Optional[int] = None

    class Config:
        schema_extra = {
            "example": {
                "_id": {"$oid": "573a1390f29313caabcd42e8"},
                "plot": "A group of bandits stage a brazen train hold-up, only to find a determined posse hot on their heels.",
                "genres": ["Short", "Western"],
                "runtime": 11,
                "cast": ["A.C. Abadie", "Gilbert M. 'Broncho Billy' Anderson", "George Barnes", "Justus D. Barnes"],
                "poster": "https://m.media-amazon.com/images/M/MV5BMTU3NjE5NzYtYTYyNS00MDVmLWIwYjgtMmYwYWIxZDYyNzU2XkEyXkFqcGdeQXVyNzQzNzQxNzI@._V1_SY1000_SX677_AL_.jpg",
                "title": "The Great Train Robbery",
                "fullplot": "Among the earliest existing films in American cinema...",
                "languages": ["English"],
                "released": {"$date": {"$numberLong": "-2085523200000"}},
                "directors": ["Edwin S. Porter"],
                "rated": "TV-G",
                "awards": {"wins": 1, "nominations": 0, "text": "1 win."},
                "lastupdated": "2015-08-13 00:27:59.177000000",
                "year": 1903,
                "imdb": {"rating": 7.4, "votes": 9847, "id": 439},
                "countries": ["USA"],
                "type": "movie",
                "tomatoes": {"viewer": {"rating": 3.7, "numReviews": 2559, "meter": 75},
                             "fresh": 6,
                             "critic": {"rating": 7.6, "numReviews": 6, "meter": 100},
                             "rotten": 0,
                             "lastUpdated": {"$date": "2015-08-08T19:16:10Z"}},
                "num_mflix_comments": 0
            }
        }


class MovieUpdate(BaseModel):
    plot: Optional[str] = None
    genres: Optional[List[str]] = None
    runtime: Optional[int] = None
    cast: Optional[List[str]] = None
    title: Optional[str] = None
    poster: Optional[str] = None
    fullplot: Optional[str] = None
    languages: Optional[List[str]] = None
    released: Optional[datetime] = None
    directors: Optional[List[str]] = None
    rated: Optional[str] = None
    awards: Optional[Award] = None
    lastupdated: Optional[datetime] = None
    year: Optional[str] = None
    imdb: Optional[Imdb] = None
    countries: Optional[List[str]] = None
    type: Optional[str] = None
    tomatoes: Optional[Tomato] = None
    num_mflix_comments: Optional[int] = None

    class Config:
        schema_extra = {
            "example": {
                "plot": "A group of bandits stage a brazen train hold-up, only to find a determined posse hot on their heels.",
                "genres": ["Short", "Western"],
                "runtime": 11,
                "cast": ["A.C. Abadie", "Gilbert M. 'Broncho Billy' Anderson", "George Barnes", "Justus D. Barnes"],
                "poster": "https://m.media-amazon.com/images/M/MV5BMTU3NjE5NzYtYTYyNS00MDVmLWIwYjgtMmYwYWIxZDYyNzU2XkEyXkFqcGdeQXVyNzQzNzQxNzI@._V1_SY1000_SX677_AL_.jpg",
                "title": "The Great Train Robbery",
                "fullplot": "Among the earliest existing films in American cinema...",
                "languages": ["English"],
                "released": {"$date": {"$numberLong": "-2085523200000"}},
                "directors": ["Edwin S. Porter"],
                "rated": "TV-G",
                "awards": {"wins": 1, "nominations": 0, "text": "1 win."},
                "lastupdated": "2015-08-13 00:27:59.177000000",
                "year": 1903,
                "imdb": {"rating": 7.4, "votes": 9847, "id": 439},
                "countries": ["USA"],
                "type": "movie",
                "tomatoes": {"viewer": {"rating": 3.7, "numReviews": 2559, "meter": 75},
                             "fresh": 6,
                             "critic": {"rating": 7.6, "numReviews": 6, "meter": 100},
                             "rotten": 0,
                             "lastUpdated": {"$date": "2015-08-08T19:16:10Z"}},
                "num_mflix_comments": 0
            }
        }

class ReviewerInfo(BaseModel):
    userName: str
    numberOfMoviesRated: Optional[int] = None
    ratedMovies: Optional[List[str]] = None
