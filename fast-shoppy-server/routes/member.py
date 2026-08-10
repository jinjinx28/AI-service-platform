from fastapi import APIRouter

member_router = APIRouter()

@member_router.post("/signup")
async def signup() -> dict :
    return {
        "message" : "signup!"
    }
