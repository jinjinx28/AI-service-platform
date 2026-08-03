from fastapi import APIRouter, Path
from schemas.todo_schema import Todo, TodoItem, TodoItems

todo_router = APIRouter()

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
@todo_router.put("/todo/{id}")
async def update_todo(todo_data : TodoItem, id : int = Path(...)) -> dict :
    for todo in todo_list :
        if todo.id == id :
            todo.item = todo_data.item
            return {
                "message" : "todo 업데이트 성공"
            }
        
    return {
        "message" : "id가 존재하지 않습니다."
    }

# D

# all
@todo_router.delete("/todo", response_model = TodoItems)
async def deleteAll() -> dict :
    if len(todo_list) > 0 :
        todo_list.clear()
        return {
            "message" : "todo 삭제 성공"
        }
    return {
        "message" : "todo_list가 존재하지 않습니다"
    }

# id
@todo_router.delete("/todo/{id}")
async def deleteId(id : int) -> dict :
    for index in range(len(todo_list)) :
        todo = todo_list[index]
        if todo.id == id :
            todo_list.pop(index)
            return {
                "message" : "todo 삭제 완료"
            }
        
    return {
        "message" : "id가 존재하지 않습니다"
    }