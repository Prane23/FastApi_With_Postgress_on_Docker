from fastapi import FastAPI, HTTPException, Depends   
from pydantic import BaseModel

from sqlalchemy import text
from sqlalchemy.orm import Session
from core import crud
from core.database import Base, SessionLocal,engine
from schemas import schemas
from models.models import Student

Base.metadata.create_all(bind=engine)

app = FastAPI(title="CRUD API", description="FastAPI CRUD with Swagger", version="1.0")

@app.get("/")
def status():
    return {"status": "ok"}


def get_db():
    db = SessionLocal()   # create a new session
    try:
        yield db          # give it to the endpoint
    finally:
        db.close()        # cleanup after request


@app.get("/version")
def get_postgres_version(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT version();"))  
    version = result.scalar()                      
    return {"postgres_version": version}


@app.get("/databases")
def list_databases(db: Session = Depends(get_db)):
    # Query Postgres system catalog for database names
    result = db.execute(text("SELECT datname FROM pg_database WHERE datistemplate = false;"))
    databases = [row[0] for row in result.fetchall()]
    return {"databases": databases}

@app.post("/students/", response_model=schemas.Student)
def add_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_student(db, student)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating student: {str(e)}")


@app.get("/students/", response_model=list[schemas.Student])
def list_students(db: Session = Depends(get_db)):
    try:
        students = crud.get_students(db)
        return students
    except Exception as e:
        # Log the error if you have logging configured
        # logger.error(f"Error fetching students: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while fetching students: {str(e)}" )