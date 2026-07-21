
from pydantic import BaseModel


class ReviewResponse(

    BaseModel

):

    summary: str

    feedback: str

    ats_score: str

    suggestions: str
