from pydantic import BaseModel
from typing import List, Dict

class GitHubRepoRequest(BaseModel):
    repo_url: str

class GitHubRepoResponse(BaseModel):
    files: List[Dict[str, str]]
    directories: List[Dict[str, str]]
    # app/models/models.py

class RepoContent(BaseModel):
    type: str  # Тип элемента, например, 'file' или 'dir'
    name: str  # Название файла или папки
    path: str  # Путь до элемента
    content: str = None  # Содержимое файла, если есть
    url: str  # URL для доступа к содержимому


class AnalyzeRequest(BaseModel):
    task_description: str
    repo_content: str
    candidate_level: str

class AnalyzeResponse(BaseModel):
    files: List[str]
    issues: List[str]
    rating: str
    conclusion: str
