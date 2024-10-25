from pydantic import BaseModel

class ReviewResult(BaseModel):
    files: list
    issues: list
    rating: str
    conclusion: str
