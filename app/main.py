import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# NextJS server origin
# what domains can send requests to this API
origins = [
    "http://localhost:3000"
]

# CORS middleware
# Security, only allows the fronend to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class FilmInput(BaseModel):
    films: list[str]

@app.post("/submit-films")
def submit_films(input: FilmInput):
    recommended = generate_recommendations(input.films)
    return {"recommended": recommended}

# input.films = ["Inception, Shawshank, Star Wars"]

def generate_recommendations():
    return