from fastapi import APIRouter
from pydantic import BaseModel

todo_router = APIRouter()

# Todo Model
class Todo(BaseModel) :
    id : int
    item : str

# todo_list
todo_list = []

# C
@todo_router("/todo")
async def add_todo(todo : Todo) -> dict : 
    todo_list.append(Todo)
    return {
        "message" : "Todo 객체 추가 완료"
    }

# R 
@todo_router.get("/todo")
async def getAll() -> dict :
    return {
        "message" : todo_list
    }

# id
@todo_router.get("/todo/{id}")
async def getId() -> dict :
    for todo in todo_list :
        if todo.id == id :
            return {
                "message" : todo
            }
        
    return {
        "message" : "id가 존재하지 않습니다."
    }

# U 
# D