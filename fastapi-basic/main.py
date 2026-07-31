from fastapi import FastAPI

app = FastAPI() #   FastAPI 서버 생성

@app.get("/")
async def welcome() -> dict :     # (key : value ..)
    return {
        "message" : "GET :: welcome to FastAPI world !!"
    }

@app.post("/")
async def welcome() -> dict :     # (key : value ..)
    return {
        "message" : "POST :: welcome to FastAPI world !!"
    }

@app.get("/hello")
async def say_hello() -> dict :     # (key : value ..)
    return {
        "message" : "hello nuri"
    }

@app.post("/hello")
async def say_hello() -> dict :     # (key : value ..)
    return {
        "message" : "hello nuri"
    }