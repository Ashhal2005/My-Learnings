from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import declarative_base, Mapped, mapped_column

engine = create_engine("mariadb+mariadbconnector://ashhal:ashhal123@localhost:3306/ORM")
Base = declarative_base()

class student(Base):
    __tablename__ = "student"

    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    name:Mapped[str] = mapped_column(String(50))
    age:Mapped[int] = mapped_column(Integer)
    course:Mapped[str]= mapped_column( String(50))

Base.metadata.create_all(engine)
