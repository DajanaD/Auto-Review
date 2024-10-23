from fastapi import FastAPI
from app.routes import review

app = FastAPI(title="CodeReviewAI")

app.include_router(review.router)
