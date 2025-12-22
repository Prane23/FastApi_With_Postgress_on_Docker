# FastAPI with PostgreSQL on Docker

# FastAPI with PostgreSQL on Docker

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-teal?logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15%2B-blue?logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-Compose-lightblue?logo=docker)

A fully containerized **FastAPI + PostgreSQL** starter template designed for building scalable backend services.  
This project demonstrates clean architecture, modular design, and production‑ready patterns for API development.

---

## 📖 About

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

## 📂 Project Structure

```text
FastApi_With_Postgress_on_Docker/
│
├── core/            # Database configuration
│   └── database.py
│
├── models/          # SQLAlchemy models
│   └── models.py
│
├── schemas/         # Pydantic schemas
│   └── schemas.py
│
├── crud.py             # CRUD operations
├── main.py             # FastAPI entrypoint
├── Dockerfile          # FastAPI container
├── docker-compose.yml  # Postgress container
└── requirements.txt    # Packages needed for fastapi

⚙️ Setup & Run

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/Prane23/FastApi_With_Postgress_on_Docker.git
cd FastApi_With_Postgress_on_Docker

### 2. Start services with Docker Compose
  docker compose up --build
  This will spin up:
  fastapi_app → FastAPI backend
  db → PostgreSQL database

### 3. Access the app
API root: http://localhost:8000
Swagger docs: http://localhost:8000/docs
ReDoc docs: http://localhost:8000/redoc

🧩 Example Endpoints
Add student → POST /students/
List students → GET /students/

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
![Project Screenshot](assets/fastapi_postgress_docker.png)

📖 Notes
Default database connection is configured in core/database.py.
Update docker-compose.yml with your own Postgres credentials if needed.
---

