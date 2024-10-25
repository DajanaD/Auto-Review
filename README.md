# Code Review AI

### Instructions for Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/code-review-ai.git
   cd code-review-ai
   ```
2. Create and activate a virtual environment:

   ```bash

   python3 -m venv .venv
   source .venv/bin/activate  # For Unix or macOS
   .venv\Scripts\activate     # For Windows
   ```
3.   Install dependencies:
   
   ```bash

   poetry install
   ```

4.  Start the server:

   ```bash
   Копировать код
   poetry run uvicorn app.main:app --reload
   ```
 ## Instructions for Running with Docker
 
1. Build and start the services using Docker Compose:

   ```bash
   Копировать код
   docker-compose up --build
   ```
2. Access the API via your browser at http://localhost:8000/docs