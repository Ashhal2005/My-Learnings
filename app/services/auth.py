from model.user import User
from schema.user_schema import UserCreate
from utils.security import hash_pswd
from database import SessionLocal


def create_user (user : UserCreate):
    session = SessionLocal()
    hash_password = hash_pswd(user.pswd)
    new_user = User(
        username = user.username,
        email = user.email,
        h_pswd = hash_password
    )
    
    
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    session.close()
    return new_user