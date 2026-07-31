# /todo - get(R), post(C), put(U), delete(D)

from fastapi import APIRouter
from pydantic import BaseModel

todo_router = APIRouter()

# Item model
class Item(BaseModel) :
    item : str
    status : str

# Todo model
class Todo(BaseModel) :
    item : int
    status : Item

# Todo list
todo_list = []


# C : Create
@todo_router.post("/todo")
async def create_todo(todo : Todo) -> dict : 
    todo_list.append(todo)   
    return {
        "message" : "create !!",
        "todo" : todo
    }

# R : Read
@todo_router.get("/todo")
async def read_todo() -> dict :    
    return {
        "message" : "read !!"
    }

# U : Update
@todo_router.put("/todo")
async def update_todo() -> dict :    
    return {
        "message" : "update !!"
    }

# D : delete
@todo_router.delete("/todo")
async def delete_todo() -> dict :    
    return {
        "message" : "delete !!"
    }