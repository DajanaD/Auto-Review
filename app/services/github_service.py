import httpx
from app.utils.cache import cache_repo_content, get_cached_content
from app.models.review import GitHubRepoResponse, RepoContent
from typing import List

async def fetch_repo_content(repo_url: str) -> List[RepoContent]:
    """
    Fetches the content of a GitHub repository using the GitHub API.

    Parameters:
    - repo_url (str): The GitHub repository URL, used to locate repository contents.

    Returns:
    - List[RepoContent]: List of repository content items, including files and directories.

    Raises:
    - httpx.HTTPStatusError: Raised if the HTTP request fails or returns a non-2xx status.
    """
    async with httpx.AsyncClient() as client:
        # Sends a GET request to GitHub API to retrieve repository content
        response = await client.get(f"https://api.github.com/repos/{repo_url}/contents")
        response.raise_for_status()  # Raises an error for any unsuccessful status code
        data = response.json()  # Parses response JSON data
        return [RepoContent(**item) for item in data]  # Maps response data to RepoContent objects

async def get_repo_content(repo_url: str) -> GitHubRepoResponse:
    """
    Retrieves GitHub repository content, either from cache or by fetching from GitHub API.

    Parameters:
    - repo_url (str): The GitHub repository URL used to locate repository contents.

    Returns:
    - GitHubRepoResponse: Structured response object containing files and directories from the repository.
    """
    cache_key = f"repo_content:{repo_url}"  # Defines a unique cache key based on the repository URL

    # Checks if the repository content is cached to avoid redundant API calls
    cached_content = await get_cached_content(cache_key)
    if cached_content:
        # If content is cached, returns it as a GitHubRepoResponse object
        return GitHubRepoResponse(**cached_content)

    # If no cached content, fetches from GitHub API
    repo_content = await fetch_repo_content(repo_url)

    # Constructs the response, separating files and directories from the fetched data
    response_data = GitHubRepoResponse(
        files=[{"name": file["name"], "path": file["path"]} for file in repo_content if file["type"] == "file"],
        directories=[{"name": dir["name"], "path": dir["path"]} for dir in repo_content if dir["type"] == "dir"]
    )

    # Caches the newly fetched content to optimize future requests
    await cache_repo_content(cache_key, response_data.dict())
    return response_data
