from fastapi import FastAPI
from redis.asyncio import Redis
import uvicorn
from app.routes.review import router as routes_review

app = FastAPI()
redis = Redis(host="localhost", port=6379, decode_responses=True)

@app.on_event("startup")
async def startup_event():
    await redis.ping()

@app.on_event("shutdown")
async def shutdown_event():
    await redis.close()

app.include_router(routes_review.router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
