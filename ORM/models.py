from sqlalchemy import Column, Integer, String , create_engine
from sqlalchemy.orm import declarative_base, Mapped, mapped_column

engine = create_engine("mysql+mariadbconnector://ashhal:ashhal123@localhost:3306/ORM")
base = declarative_base()
class User(base):
    __tablename__ = "users"
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    name:Mapped[str] = mapped_column(String(50))
    email:Mapped[str] = mapped_column(String(50))

class car(base):
    __tablename__ = "cars"
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    name:Mapped[str] = mapped_column(String(50))
    model:Mapped[str] = mapped_column(String(50))

base.metadata.create_all(engine)
