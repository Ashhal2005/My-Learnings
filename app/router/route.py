from fastapi import APIRouter
from schema.user_schema import UserCreate, UserResponse
from services.auth import create_user

router = APIRouter()

@router.post('/register', response_model=UserResponse)
def register(user: UserCreate):
    new_user = create_user(user)
    return new_user
