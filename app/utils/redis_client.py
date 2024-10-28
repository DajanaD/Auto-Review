import os
from redis.asyncio import Redis

# Ініціалізація Redis з конфігурації
redis = Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    decode_responses=True
)
