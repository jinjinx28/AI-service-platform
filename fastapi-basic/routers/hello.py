from fastapi import APIRouter

router = APIRouter()

@router.get("/hello")
async def say_hello() -> dict :     # (key : value ..)
    return {
        "message" : "hello nuri"
    }

@router.post("/hello")
async def say_hello() -> dict :     # (key : value ..)
    return {
        "message" : "hello nuri"
    }