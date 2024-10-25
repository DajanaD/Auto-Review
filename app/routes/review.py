from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from app.services.github_service import get_repo_content
from app.services.openai_service import analyze_code
from app.utils.validators import validate_review_request

router = APIRouter()

class ReviewRequest(BaseModel):
    task_description: str
    github_repo_url: str
    candidate_level: str

@router.post("/review")
async def create_review(request: ReviewRequest):
    # Validate request data
    validate_review_request(request)
    
    # Get repository content (with Redis caching)
    repo_content = await get_repo_content(request.github_repo_url)
    
    # Analyze the code using OpenAI API
    review_result = await analyze_code(request.task_description, repo_content, request.candidate_level)
    
    return {
        "files_found": review_result.files,
        "issues_comments": review_result.issues,
        "rating": review_result.rating,
        "conclusion": review_result.conclusion
    }
