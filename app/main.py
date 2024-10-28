from fastapi import FastAPI
from app.routes import review
from app.utils.redis_client import redis  # Імпортуємо Redis із redis_client

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    try:
        await redis.ping()
        print("Successfully connected to Redis.")
    except Exception as e:
        print(f"Error connecting to Redis: {e}")

@app.on_event("shutdown")
async def shutdown_event():
    await redis.close()

app.include_router(review.router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
