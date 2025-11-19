import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
import httpx
from pydantic import BaseModel
from typing import List

TMDB_API_KEY = os.getenv("TMDB_API_KEY")
TMDB_IMAGE_BASE = os.getenv("TMDB_IMAGE_BASE", "https://image.tmdb.org/t/p/w500")

app = FastAPI()

# CORS middleware
# Security, only allows the fronend to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"]
)

class TMDBResult(BaseModel):
    id: int
    title: str
    year: str | None
    overview: str | None
    poster_url: str | None

class SearchResponse(BaseModel):
    query: str
    results: List[TMDBResult]