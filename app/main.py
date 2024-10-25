from fastapi import FastAPI
from aioredis import create_redis_pool

app = FastAPI()

# Event to initialize Redis
@app.on_event("startup")
async def startup_event():
    global redis
    redis = await create_redis_pool("redis://localhost")

# Event to close Redis connection
@app.on_event("shutdown")
async def shutdown_event():
    redis.close()
    await redis.wait_closed()

# Include routes from review
from app.routes.review import router as review_router
app.include_router(review_router)
