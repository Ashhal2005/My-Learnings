from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student (BaseModel):
    name:str
    age:int
    grade:str

@app.get ("/name")
def name ():
    return {"massage":"Assalamua'alikum! from Ashhal"}

@app.get("/{id}")
def root(id:int):
    return {"massage":f"Assalamua'alikum! from id {id}"}

@app.post("/search")
def Search(name:str):
    return {"name":name}

@app.post("/student")
def student(s:Student):
    return s

