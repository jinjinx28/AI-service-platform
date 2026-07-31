from fastapi import APIRouter
from pydantic import BaseModel

hello_router = APIRouter()

person_list = []

 # Person 클래스 정의
class Person(BaseModel) :
    name : str
    age : int

@hello_router.get("/hello")
async def say_hello() -> dict :     # (key : value ..)
    return {
        "message" : "hello nuri"
    }

@hello_router.post("/hello")
async def say_hello(person: Person) -> dict :     
    person_list.append(person)
    return {
        "message" : person
    }