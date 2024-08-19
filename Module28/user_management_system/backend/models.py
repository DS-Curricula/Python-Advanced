from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str
    role: str

class UserUpdate(BaseModel):
    username: str
    role: str

class UserLogin(BaseModel):
    username: str
    password: str

class AuthenticatedUser(BaseModel):
    username: str
    role: str

class UserView(BaseModel):
    id: int
    username: str
    role: str

    class Config:
        from_attributes = True  # For Pydantic V2 compatibility
