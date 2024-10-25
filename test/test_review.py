import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_review():
    response = client.post("/review", json={
        "task_description": "Test task",
        "github_repo_url": "example/repo",
        "candidate_level": "junior"
    })
    assert response.status_code == 200
    data = response.json()
    assert "files_found" in data
    assert "issues_comments" in data
    assert "rating" in data
    assert "conclusion" in data
