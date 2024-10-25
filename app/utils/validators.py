from fastapi import HTTPException, status

def validate_review_request(request):
    if request.candidate_level not in ["junior", "mid", "senior"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid candidate level. Must be 'junior', 'mid', or 'senior'."
        )
