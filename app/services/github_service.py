from app.utils.cache import cache_repo_content, get_cached_content
import httpx

async def fetch_repo_content(repo_url: str):
    # Replace with actual GitHub API fetching logic
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://api.github.com/repos/{repo_url}/contents")
        response.raise_for_status()
        return response.json()

async def get_repo_content(repo_url: str):
    cache_key = f"repo_content:{repo_url}"
    
    # Check Redis cache
    cached_content = await get_cached_content(cache_key)
    if cached_content:
        return cached_content
    
    # Fetch content from GitHub API
    repo_content = await fetch_repo_content(repo_url)
    
    # Cache the content
    await cache_repo_content(cache_key, repo_content)
    
    return repo_content
