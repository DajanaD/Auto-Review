from app.utils.redis_client import redis  # Імпортуємо Redis із redis_client

async def cache_repo_content(key: str, value: dict, expiration: int = 3600):
    """
    Caches the repository content in Redis.
    """
    try:
        await redis.set(key, value, ex=expiration)
    except Exception as e:
        print(f"Error caching data in Redis: {e}")

async def get_cached_content(key: str):
    """
    Retrieves cached repository content from Redis.
    """
    try:
        cached_value = await redis.get(key)
        if cached_value:
            return cached_value
    except Exception as e:
        print(f"Error retrieving data from Redis: {e}")
    return None
