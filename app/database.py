from sqlalchemy import create_engine 
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("mariadb+mariadbconnector://ashhal:112233@localhost:3306/authapp")
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)



