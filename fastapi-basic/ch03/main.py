from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def welcome() -> dict :
    return {
        "message" : "welcome ch03 !!"
    }