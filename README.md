📘 FastAPI + PostgreSQL + Docker

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-teal?logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15%2B-blue?logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-Compose-lightblue?logo=docker)

A fully containerized FastAPI application running with PostgreSQL using Docker Compose.
This project demonstrates a clean, production‑ready setup for building, running, and deploying a backend API with a relational database.

⚙️ Prerequisites
#### Docker Desktop installed
#### Python 3.10+ (optional for local development)
#### Git
⚙️ Prerequisites
Before running this project, ensure you have:
Docker Desktop installed
Python 3.10+ (optional for local development)
Git

1️⃣ Clone the repository

git clone https://github.com/Prane23/FastApi_With_Postgress_on_Docker.git
cd FastApi_With_Postgress_on_Docker

2️⃣ Create a .env file
Create a .env file in the project root:
DATABASE_URL=postgresql://postgres:postgres@db:5432/mydatabase
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=mydatabase

3️⃣ Build & Run with Docker
docker compose up --build

4️⃣ Access the API
Once running:

URL	Description
http://localhost:8000/docs	Swagger UI
http://localhost:8000/redoc	ReDoc documentation
http://localhost:8000/students	Student API endpoints

🧪 Running Locally (Without Docker)
#### Install dependencies
python -m pip install -r requirements.txt
#### Load environment variables
Add this to main.py:
from dotenv import load_dotenv
load_dotenv()
#### Start FastAPI
uvicorn app.main:app --reload

🧰 Useful Docker Commands
#Stop containers:
docker compose down
#Stop & remove volumes:
docker compose down --volumes
#Rebuild without cache:
docker compose build --no-cache
#View logs:
docker logs fastapi_app


🚀 Features
- FastAPI backend with automatic interactive API docs (`/docs` and `/redoc`)
- PostgreSQL database running in a Docker container
- SQLAlchemy ORM models and Pydantic schemas
- Modular project layout (`core/`, `models/`, `schemas/`, `crud.py`, `main.py`)
- Docker Compose for easy orchestration

## 📂 Project Structure
```
FastApi_With_Postgress_on_Docker/
│
├── core/            # Database configuration
│   └── database.py
│   └── crud.py
│ 
├── models/          # SQLAlchemy models
│   └── models.py
│
├── schemas/         # Pydantic schemas
│   └── schemas.py
│
             # CRUD operations
├── main.py             # FastAPI entrypoint
├── Dockerfile          # FastAPI container
├── dbContainer.yml  # Postgress container
└── requirements.txt    # Packages needed for fastapi
```
## [Swagger docs]
![FastAPI with Postgres](assets/fastapi_postgress_docker.png)

🧩 Example API Endpoints
✅ Create Student POST /students/
✅ Get All Students GET /students/
✅ Get Student by ID GET /students/{id}
✅ Update Student PUT /students/{id}
✅ Delete Student DELETE /students/{id}

🛠 Tech Stack
FastAPI — async Python web framework
PostgreSQL — relational database
Docker Compose — service orchestration
SQLAlchemy ORM — database modeling
Pydantic — data validation

✅ Future Enhancements
Alembic migrations
JWT authentication
Pagination & filtering
CI/CD pipeline

📖 Notes
Default database connection is configured in core/database.py.
Update docker-compose.yml with your own Postgres credentials if needed.
---

