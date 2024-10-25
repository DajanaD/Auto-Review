import httpx
from app.models.review import AnalyzeRequest, AnalyzeResponse

async def analyze_code(request: AnalyzeRequest) -> AnalyzeResponse:
    """
    Analyzes repository code using OpenAI's API, based on the provided task description and candidate level.

    Parameters:
    - request (AnalyzeRequest): Object containing the level of the candidate, task description, and repository content to analyze.

    Returns:
    - AnalyzeResponse: Structured response containing a list of files analyzed, identified issues, a rating, and a conclusion.

    Raises:
    - httpx.HTTPStatusError: Raised if the HTTP request to the OpenAI API fails or returns a non-2xx status.
    """
    headers = {
        "Authorization": "Bearer YOUR_OPENAI_API_KEY"  # Authorization header for OpenAI API
    }

    # Constructs the prompt for analysis by combining task details with repository content
    prompt = f"Analyze the following code for a {request.candidate_level} candidate based on the task: {request.task_description}.\n\n{request.repo_content}"

    # Initiates an async HTTP request to OpenAI's API to process the code analysis
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.openai.com/v1/completions",
            headers=headers,
            json={"model": "gpt-4-turbo", "prompt": prompt, "max_tokens": 1000}
        )
        response.raise_for_status()  # Raises an error for unsuccessful response status codes
        result = response.json()  # Parses response JSON data

    # Constructs and returns the AnalyzeResponse with structured data from the OpenAI response
    return AnalyzeResponse(
        files=result.get("files", []),
        issues=result.get("issues", []),
        rating=result.get("rating", "unknown"),
        conclusion=result.get("conclusion", "No conclusion")
    )
