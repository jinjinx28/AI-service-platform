from fastapi import FastAPI
from schemas.member import member_router
from database.connection import engine, Base
from models.member import MemberModel

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(member_router)