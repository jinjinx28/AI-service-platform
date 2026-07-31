from fastapi import APIRouter
from pydantic import BaseModel

hello_router = APIRouter()

 # Person 클래스 정의
class Person(BaseModel) :
    name : str
    age : int

person_list = []

# Path Variable ( 경로 매개변수 )
@hello_router.get("/hello/{name}")          # http://127.0.0.1:8000/hello/hong
async def say_hello(name : str) -> dict :     # (key : value ..)
    return {
        "message" : "hello nuri" + name
    }

# QueryString ( 쿼리 매개변수 )
@hello_router.get("/hello2")
async def say_hello(name : str) -> dict :     
    return {
        "message" : "hello nuri" + name
    }

@hello_router.post("/hello")
async def say_hello(person: Person) -> dict :     
    person_list.append(person)
    return {
        "message" : person
    }