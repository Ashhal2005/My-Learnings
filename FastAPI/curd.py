from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

students = []

class Student (BaseModel):
    name:str
    age:int
    course:str

@app.post("/student")
def student(s:Student):
    students.append(s)
    return s

print(students)

@app.get("/studentbyname")
def studentbyID(name:str):
    for s in students:
        if s.name == name:
            return s
    return {"message":"Student not found"}