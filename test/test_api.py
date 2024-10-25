import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models.review import GitHubRepoRequest, GitHubRepoResponse, AnalyzeRequest, AnalyzeResponse

client = TestClient(app)

@pytest.mark.asyncio
async def test_fetch_repo_content_success(monkeypatch):
    # Мокируем функцию `get_repo_content` для симуляции успешного вызова API
    async def mock_get_repo_content(repo_url: str):
        return {
            "files": [{"name": "file1.py", "path": "src/file1.py"}],
            "directories": [{"name": "src", "path": "src/"}],
        }

    monkeypatch.setattr("app.services.github_service.get_repo_content", mock_get_repo_content)

    response = client.post("/api/github/repo-content", json={"repo_url": "user/repo"})
    assert response.status_code == 200
    assert "files" in response.json()
    assert response.json()["files"][0]["name"] == "file1.py"

@pytest.mark.asyncio
async def test_fetch_repo_content_failure(monkeypatch):
    # Мокируем функцию `get_repo_content`, чтобы она вызывала исключение
    async def mock_get_repo_content(repo_url: str):
        raise Exception("Error fetching repository content")

    monkeypatch.setattr("app.services.github_service.get_repo_content", mock_get_repo_content)

    response = client.post("/api/github/repo-content", json={"repo_url": "user/repo"})
    assert response.status_code == 500
    assert "Error fetching repository content" in response.json()["detail"]

@pytest.mark.asyncio
async def test_analyze_repo_success(monkeypatch):
    async def mock_analyze_code(request):
        return AnalyzeResponse(
            files=["file1.py"],
            issues=["Issue found"],
            rating="good",
            conclusion="All looks good."
        )

    monkeypatch.setattr("app.services.openai_service.analyze_code", mock_analyze_code)

    response = client.post("/api/analyze", json={
        "task_description": "Check the code for efficiency.",
        "repo_content": "print('Hello World')",
        "candidate_level": "junior"
    })
    
    assert response.status_code == 200
    assert response.json()["rating"] == "good"
