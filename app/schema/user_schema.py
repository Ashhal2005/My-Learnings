from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    pswd: str

class UserLogin(BaseModel):
    email: EmailStr
    pswd: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    timestamp: datetime

    class Config:
        from_attributes = True