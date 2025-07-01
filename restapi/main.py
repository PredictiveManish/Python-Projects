from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

class Student(BaseModel):
    name: str
    age: int
    course: str
students_db: Dict[int, Student] ={}
id_counter = 1

@app.get("/")
def home():
    return {"message": "Welcome to the Student Management API!"}

# Student creation
@app.post("/students/")
def create_student(student: Student):
    global id_counter
    students_db[id_counter] = student 
    return {"id":id_counter, "data":student}
    id_counter += 1

# Get all students
@app.get("/students/")
def get_all_students():
    return students_db

@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found!")
    return students_db[student_id]

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found!")
    del students_db[student_id]
    return {"message": "Student deleted successfully"}

@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    if student_id not in students_db:
        return HTTPException(status_code=404, detail="Student not found")
    students_db[student_id] = student
    return {"message": "Student updated","data":student}