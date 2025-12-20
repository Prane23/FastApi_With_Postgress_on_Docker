
from typing import Optional
from pydantic import BaseModel

# Shared fields
class StudentBase(BaseModel):
    name: str
    age: int
    grade: str

# For creating a student 
class StudentCreate(StudentBase):
    pass

# For returning a student (includes ID)
class Student(StudentBase):
    id: int

    class Config:
        orm_mode = True

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    grade: Optional[str] = None
