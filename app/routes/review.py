from fastapi import APIRouter, HTTPException, status
from app.services.github_service import get_repo_content
from app.services.openai_service import analyze_code
from app.models.review import GitHubRepoRequest, GitHubRepoResponse, AnalyzeRequest, AnalyzeResponse

router = APIRouter()

@router.post("/github/repo-content", response_model=GitHubRepoResponse)
async def fetch_repo_content(request: GitHubRepoRequest):
    """
    Fetch content from a specified GitHub repository.
    """
    try:
        repo_content = await get_repo_content(request.repo_url)
        return repo_content
    except Exception as e:
        # Логування помилок
        print(f"Error fetching repository content: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error fetching repository content."
        )

@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze_repo(request: AnalyzeRequest):
    """
    Analyze code within the specified GitHub repository using OpenAI’s API.
    """
    try:
        analysis_result = await analyze_code(request)
        return analysis_result
    except Exception as e:
        # Логування помилок
        print(f"Error analyzing repository: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error analyzing repository."
        )
