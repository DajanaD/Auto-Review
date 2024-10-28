import httpx
from app.utils.cache import cache_repo_content, get_cached_content
from app.models.review import GitHubRepoResponse, RepoContent
from typing import List

async def fetch_repo_content(repo_url: str) -> List[RepoContent]:
    """
    Fetches the content of a GitHub repository using the GitHub API.
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"https://api.github.com/repos/{repo_url}/contents")
            response.raise_for_status()  # Підняти виняток для статусу не 2xx
            data = response.json()
            return [RepoContent(**item) for item in data]
    except httpx.HTTPStatusError as e:
        print(f"HTTP error occurred: {e}")
        raise
    except Exception as e:
        print(f"Error fetching repo content: {e}")
        raise

async def get_repo_content(repo_url: str) -> GitHubRepoResponse:
    """
    Retrieves GitHub repository content, either from cache or by fetching from GitHub API.
    """
    cache_key = f"repo_content:{repo_url}"
    cached_content = await get_cached_content(cache_key)
    if cached_content:
        return GitHubRepoResponse(**cached_content)

    repo_content = await fetch_repo_content(repo_url)

    response_data = GitHubRepoResponse(
        files=[{"name": file["name"], "path": file["path"]} for file in repo_content if file["type"] == "file"],
        directories=[{"name": dir["name"], "path": dir["path"]} for dir in repo_content if dir["type"] == "dir"]
    )

    await cache_repo_content(cache_key, response_data.dict())
    return response_data
