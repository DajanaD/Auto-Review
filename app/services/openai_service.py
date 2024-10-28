import os
import httpx
from app.models.review import AnalyzeRequest, AnalyzeResponse

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # API ключ зберігається в змінних оточення

async def analyze_code(request: AnalyzeRequest) -> AnalyzeResponse:
    """
    Analyzes repository code using OpenAI's API.
    """
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }

    prompt = f"Analyze the following code for a {request.candidate_level} candidate based on the task: {request.task_description}.\n\n{request.repo_content}"

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://api.openai.com/v1/completions",
                headers=headers,
                json={"model": "gpt-4-turbo", "prompt": prompt, "max_tokens": 1000}
            )
            response.raise_for_status()
            result = response.json()

        return AnalyzeResponse(
            files=result.get("files", []),
            issues=result.get("issues", []),
            rating=result.get("rating", "unknown"),
            conclusion=result.get("conclusion", "No conclusion")
        )
    except httpx.HTTPStatusError as e:
        print(f"HTTP error while analyzing code: {e}")
        raise
    except Exception as e:
        print(f"General error in code analysis: {e}")
        raise
