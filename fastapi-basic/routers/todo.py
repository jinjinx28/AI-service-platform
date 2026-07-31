# /todo - get(R), post(C), put(U), delete(D)

from fastapi import APIRouter

todo_router = APIRouter()

# C : Create
@todo_router.post("/todo")
async def create_todo() -> dict :    
    return {
        "message" : "create !!"
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