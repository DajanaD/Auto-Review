from pydantic import BaseModel
from typing import List, Dict

class GitHubRepoRequest(BaseModel):
    repo_url: str

class GitHubRepoResponse(BaseModel):
    files: List[Dict[str, str]]
    directories: List[Dict[str, str]]
   

class RepoContent(BaseModel):
    type: str  
    name: str 
    path: str  
    content: str = None 
    url: str 


class AnalyzeRequest(BaseModel):
    task_description: str
    repo_content: str
    candidate_level: str

class AnalyzeResponse(BaseModel):
    files: List[str]
    issues: List[str]
    rating: str
    conclusion: str

