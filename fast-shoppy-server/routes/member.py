from fastapi import APIRouter, Depends, HTTPException, status
from schemas.member import memberItem
from models.member import MemberModel
from sqlalchemy.orm import Session
from database.connection import get_db

member_router = APIRouter()

@member_router.post("/signup")
async def signup(memberItem) -> dict :
    memberModel = MemberModel (
        id = memberItem.id,
        pwd = memberItem.pwd,
        name = memberItem.name,
        phone = memberItem.phone,
        email = memberItem.email
    )   

    db.add(memberModel)
    db.commit()
    db.refresh(memberModel)

    return {
        "message" : "signup"
    }