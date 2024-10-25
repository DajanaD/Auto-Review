from app.main import redis

async def cache_repo_content(key: str, value: dict, expiration: int = 3600):
    """
    Caches the repository content in Redis.

    Parameters:
    - key (str): The Redis key to store the content under, typically including the repository URL for uniqueness.
    - value (dict): The content to cache, structured as a dictionary (often a serialized JSON format).
    - expiration (int): The expiration time for the cached data in seconds (default is 3600 seconds or 1 hour).

    Description:
    Stores the repository content in Redis using the specified key and sets an expiration time. 
    Once cached, this content can be quickly retrieved to avoid redundant GitHub API calls.

    Returns:
    - None: This function only sets a key in Redis without returning any value.
    """
    await redis.set(key, value, ex=expiration)  # Store content in Redis with the specified expiration time

async def get_cached_content(key: str):
    """
    Retrieves cached repository content from Redis.

    Parameters:
    - key (str): The Redis key to look up the cached content.

    Returns:
    - The cached content associated with the key if it exists, or None if there is no data cached for the key.
    """
    return await redis.get(key)  # Fetch cached content by key, or return None if not present
