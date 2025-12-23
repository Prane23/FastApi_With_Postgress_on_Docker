from sqlalchemy.orm import Session
from models.models import Student
from schemas.schemas import StudentCreate, StudentUpdate

def get_students(db: Session):
    return db.query(Student).all()

def get_student(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()

def create_student(db: Session, student: StudentCreate):
    db_student = Student(name=student.name, age=student.age, grade=student.grade)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def update_student(db: Session, id: int, student_data: StudentUpdate):
    student = db.query(Student).filter(Student.id == id).first()

    if not student:
        return None

    update_data = student_data.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(student, key, value)

    db.commit()
    db.refresh(student)
    return student


def delete_student(db: Session, id: int):
    student = db.query(Student).filter(Student.id == id).first()

    if not student:
        return None

    db.delete(student)
    db.commit()
    return True