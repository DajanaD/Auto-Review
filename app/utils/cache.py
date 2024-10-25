from aioredis import Redis

redis = Redis()

async def cache_repo_content(key: str, repo_content: str, expiration: int = 3600):
    """
    Cache the repository content with a specified expiration time.
    """
    await redis.set(key, repo_content, expire=expiration)

async def get_cached_content(key: str):
    """
    Retrieve cached content from Redis.
    """
    return await redis.get(key)
