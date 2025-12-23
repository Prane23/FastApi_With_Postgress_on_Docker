
📘 FastAPI + PostgreSQL + Docker

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-teal?logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15%2B-blue?logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-Compose-lightblue?logo=docker)

A fully containerized FastAPI application running with PostgreSQL using Docker Compose. 
This project demonstrates a clean, production‑ready setup for building, running, and deploying a backend API with a relational database.

---

📖 About

This project provides a ready‑to‑use backend environment using **FastAPI**, **PostgreSQL**, and **Docker Compose**.  
It is ideal for learning, prototyping, or building microservices with a clean and maintainable structure.

Key highlights:
- **FastAPI** for high‑performance APIs  
- **PostgreSQL** running in a dedicated Docker container  
- **SQLAlchemy ORM** for database modeling  
- **Pydantic** for request/response validation  
- **Docker Compose** for easy orchestration  
- **Automatic API docs** via Swagger UI and ReDoc  

---

# Swagger Docs

![FastAPI Screenshot](assets/fastapi_postgress_docker.png)

📂 Project Structure

```text
FastApi_With_Postgress_on_Docker/
FastApi_With_Postgress_on_Docker/
│── app/
│   ├── main.py
│   ├── core/
│   │   ├── database.py
│   │   └── crud.py
│   ├── models/
│   │   └── models.py
│   ├── schemas/
│       └── schemas.py
│  │
│── Dockerfile
│── docker-compose.yml
│── requirements.txt
│── .env
│── README.md

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
# Install dependencies
python -m pip install -r requirements.txt
# Load environment variables
Add this to main.py:
from dotenv import load_dotenv
load_dotenv()
# Start FastAPI
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

🧩 Example Endpoints

API Endpoints
✅ Create Student
POST /students/

✅ Get All Students
GET /students/

✅ Get Student by ID
GET /students/{id}

✅ Update Student
PUT /students/{id}

✅ Delete Student
DELETE /students/{id}


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
Unit tests with PyTest

## [Swagger docs](https://raw.githubusercontent.com/Prane23/FastApi_With_Postgress_on_Docker/refs/heads/main/assets/fastapi_postgress_docker.png)
![FastAPI with Postgres](/assets/fastapi_postgress_docker.png)


📖 Notes
Default database connection is configured in core/database.py.
Update docker-compose.yml with your own Postgres credentials if needed.
---

