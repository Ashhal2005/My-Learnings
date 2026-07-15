from fastapi import FastAPI
from pydantic import BaseModel

app =  FastAPI()

tasks = []

class Task(BaseModel):
    id:int
    title:str
    description:str
    completed:bool = False

@app.get("/ToDo_list")
def To_Do_list():
    return tasks

@app.post("/add_task")
def add_task(task:Task):
    tasks.append(task.model_dump())
    return task

@app.get("/task_by_id")
def TaskByID(id:int):
    for t in tasks:
        if t["id"] == id:
            return t
    return {"message":"Task not found"}

@app.put("/update_task")
def update(id:int):
    for t in tasks:
        if t["id"] == id:
            t["completed"] = True
            return t
    return {"message":"Task not found"}

@app.delete("/delete_task")
def delete(id:int):
    for t in tasks:
        if t["id"] == id:
            tasks.remove(t)
            return {"message":"Task deleted"}
    return {"message":"Task not found"}

