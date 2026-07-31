from fastapi import APIRouter

hello_router = APIRouter()

@hello_router.get("/hello")
async def say_hello() -> dict :     # (key : value ..)
    return {
        "message" : "hello nuri"
    }

@hello_router.post("/hello")
async def say_hello() -> dict :     # (key : value ..)
    return {
        "message" : "hello nuri"
    }