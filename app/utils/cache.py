from app.main import redis

async def cache_repo_content(key: str, value: dict, expiration: int = 3600):
    await redis.set(key, value, ex=expiration)

async def get_cached_content(key: str):
    return await redis.get(key)
