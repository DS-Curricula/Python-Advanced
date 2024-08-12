from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# User model used in API endpoints
class User(BaseModel):
    id: int
    name: str
    age: int
    email: str

# Person model for another endpoint
class Person(BaseModel):
    name: str
    age: int

class PersonResponse(BaseModel):
    message: str

@app.post("/users/")
async def create_user(user: User):
    return user

@app.post("/create_person/", response_model=PersonResponse)
async def create_person(person: Person):
    return {"message": f"Person {person.name} created with age {person.age}"}
