from fastapi import FastAPI
from redis.asyncio import Redis
from app.routes import review

app = FastAPI()
redis = Redis(host="localhost", port=6379, decode_responses=True)

@app.on_event("startup")
async def startup_event():
    # Проверка соединения с Redis
    try:
        await redis.ping()
        print("Successfully connected to Redis.")
    except Exception as e:
        print(f"Error connecting to Redis: {e}")

@app.on_event("shutdown")
async def shutdown_event():
    await redis.close()

# Включение маршрутов
app.include_router(review.router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
