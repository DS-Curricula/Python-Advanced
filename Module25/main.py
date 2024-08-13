from fastapi import FastAPI, HTTPException
from typing import List
import database
import models
from models import Movie, MovieCreate

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Movies CRUD API"}

@app.post("/movies/", response_model=Movie)
def create_movie(movie: MovieCreate):
    """Creates a new movie in the database."""
    movie_id = database.create_movie(movie)
    return models.Movie(id=movie_id, **movie.dict())

@app.get("/movies/", response_model=List[Movie])
def read_movies():
    """Retrieves all movies from the database."""
    return database.read_movies()

@app.get("/movies/{movie_id}", response_model=Movie)
def read_movie(movie_id: int):
    """Retrieves a single movie by its ID."""
    movie = database.read_movie(movie_id)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@app.put("/movies/{movie_id}", response_model=Movie)
def update_movie(movie_id: int, movie: MovieCreate):
    """Updates an existing movie in the database."""
    updated = database.update_movie(movie_id, movie)
    if not updated:
        raise HTTPException(status_code=404, detail="Movie not found")
    return models.Movie(id=movie_id, **movie.dict())

@app.delete("/movies/{movie_id}", response_model=dict)
def delete_movie(movie_id: int):
    """Deletes a movie from the database by its ID."""
    deleted = database.delete_movie(movie_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Movie not found")
    return {"message": "Movie deleted successfully"}
