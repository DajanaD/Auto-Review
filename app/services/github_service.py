import httpx
from app.utils.cache import cache_repo_content, get_cached_content
from app.models.review import GitHubRepoResponse, RepoContent

async def fetch_repo_content(repo_url: str) -> List[RepoContent]:
    """
    Запрашивает содержимое репозитория с GitHub API.
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://api.github.com/repos/{repo_url}/contents")
        response.raise_for_status()
        data = response.json()
        return [RepoContent(**item) for item in data]

async def get_repo_content(repo_url: str) -> GitHubRepoResponse:
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
