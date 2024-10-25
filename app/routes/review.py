from fastapi import APIRouter, HTTPException, status
from app.services.github_service import get_repo_content
from app.services.openai_service import analyze_code
from app.utils.validators import validate_review_request
from app.models.review import GitHubRepoRequest, GitHubRepoResponse, AnalyzeRequest, AnalyzeResponse

router = APIRouter()

@router.post("/github/repo-content", response_model=GitHubRepoResponse)
async def fetch_repo_content(request: GitHubRepoRequest):
    """
    Fetch content from a specified GitHub repository.

    Parameters:
    - request (GitHubRepoRequest): Request object containing the GitHub repository URL.

    Returns:
    - GitHubRepoResponse: Contains content details and metadata of the repository.

    Raises:
    - HTTPException: Raises 500 Internal Server Error if fetching repository content fails.
    """
    try:
        repo_content = await get_repo_content(request.repo_url)
        return repo_content
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error fetching repository content: {str(e)}"
        )

@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze_repo(request: AnalyzeRequest):
    """
    Analyze code within the specified GitHub repository using OpenAI’s API.

    Parameters:
    - request (AnalyzeRequest): Request object containing the GitHub repository URL and analysis parameters.

    Returns:
    - AnalyzeResponse: Analysis results, including code insights and recommendations.

    Raises:
    - HTTPException: Raises 500 Internal Server Error if analyzing the repository fails.
    """
    validate_review_request(request)
    try:
        analysis_result = await analyze_code(request)
        return analysis_result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error analyzing repository: {str(e)}"
        )

