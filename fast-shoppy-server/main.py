from fastapi import FastAPI
from schemas.member import member_router

app = FastAPI()

app.include_router(member_router)