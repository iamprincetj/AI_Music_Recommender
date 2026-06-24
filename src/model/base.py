from pydantic import BaseModel
from typing import List


class RequestModel(BaseModel):
    """This class is the model/shape of the 
    accepted request format a user should send"""

    song: str
    artist: str


class AIResponseModel(BaseModel):
  """This class is the model/shape of the accepted AI response format"""
  query_intent: str
  recommendations: List[RecommendationModel]
  grouping: str
  confidence_note: str


class RecommendationModel(BaseModel):
  """This class is the model/shape of the accepted AI recommendations format"""
  artist: str
  track: str
  year: int
  reason: str


