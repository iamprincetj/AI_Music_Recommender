from pydantic import BaseModel
from typing import List


class RequestModel(BaseModel):
    """This class is the model/shape of the 
    accepted request format a user should send"""

    search: str
    category: str


class RecommendationModel(BaseModel):
  """This class is the model/shape of the accepted AI recommendations format"""
  artist: str
  track: str
  year: int
  reason: str





class MusicRecommendation(BaseModel):
    artist: str
    track: str
    genre: List[str]
    album: str | None = None
    year: int | None = None
    reason: str
    similarity_percent: int


class MovieRecommendation(BaseModel):
    title: str
    director: str
    year: int | None = None
    genre: str | None = None
    reason: str
    similarity_percent: int


class BookRecommendation(BaseModel):
    title: str
    author: str
    year: int | None = None
    genre: str | None = None
    reason: str
    similarity_percent: int


class GameRecommendation(BaseModel):
    title: str
    developer: str
    year: int | None = None
    genre: str | None = None
    platforms: list[str] = []
    reason: str
    similarity_percent: int


class NewsRecommendation(BaseModel):
  headline: str
  topic: str
  source: str
  published_date: str
  summary: str
  reason: str
  relevance_percent: int


class SportRecommendation(BaseModel):
  name: str
  type: str
  sport: str
  league: str
  year: int
  reason: str
  relevance_percent: int


class AnimeRecommendation(BaseModel):
  title: str
  studio: str
  year: int
  type: str
  genres: List[str] = []
  reason: str
  similarity_percent: int


class AIResponseModel(BaseModel):
  """This class is the model/shape of the accepted AI response format"""
  query_intent: str
  recommendations: List[MusicRecommendation | AnimeRecommendation | NewsRecommendation | GameRecommendation | BookRecommendation | SportRecommendation | MovieRecommendation]
  grouping: str
  confidence_note: str