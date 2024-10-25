from fastapi import APIRouter, HTTPException, status
from app.services.github_service import get_repo_content
from app.services.openai_service import analyze_code
from app.models.review import GitHubRepoRequest, GitHubRepoResponse, AnalyzeRequest, AnalyzeResponse

router = APIRouter()

@router.post("/github/repo-content", response_model=GitHubRepoResponse)
async def fetch_repo_content(request: GitHubRepoRequest):
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
    try:
        analysis_result = await analyze_code(request)
        return analysis_result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error analyzing repository: {str(e)}"
        )
