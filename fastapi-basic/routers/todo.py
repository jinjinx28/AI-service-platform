# /todo - get(R), post(C), put(U), delete(D)

from fastapi import APIRouter, Path
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


# C : Create - all
@todo_router.post("/todo/all")
async def create_todo(todo : Todo) -> dict :   
    return {
        "message :: All" : todo_list
    }

# R : Read - id별 조회
@todo_router.get("/todo/{id}")
async def read_todo(id : int) -> dict : 
    for todo in todo_list :   
        if todo.id == id :
            return {
                "todo" : todo
            }
    return {
        "message" : "read !!"
    }

# U : Update
@todo_router.put("/todo/{id}")
async def update_todo(new_item : Item, id : int = Path(..., title = "id")) -> dict :    
    for todo in todo_list :
        if todo.id ==id :
            todo.item = new_item
            return { "message" : "update 성공 !!" }
    return {
        "message" : "id 확인 !!"
    }

# D : delete
@todo_router.delete("/todo/{id}")
async def delete_todo() -> dict :    
    return {
        "message" : "delete !!"
    }