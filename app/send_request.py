import requests

url = "http://127.0.0.1:8000/api/analyze"
data = {
    "task_description": "Auto review service of assignment projects on GitHub: create a backend prototype for a Coding Assignment Auto-Review Tool using Python. This tool will help automate the process of reviewing coding assignments by leveraging OpenAI GPT API for code analysis and the GitHub API for repository access.",
    "candidate_level": "Junior",
    "repo_url": "https://github.com/DajanaD"
}

try:
    response = requests.post(url, json=data)
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())
except requests.exceptions.RequestException as e:
    print("Error:", e)
