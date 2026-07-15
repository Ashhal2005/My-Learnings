from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship

engine = create_engine ("mariadb+mariadbconnector://ashhal:ashhal123@localhost:3306/ORM")

Base = declarative_base()

class Company(Base):
    __tablename__ = "company"

    id:Mapped[int]=mapped_column(Integer, primary_key=True)
    name:Mapped[str]=mapped_column(String(50))
    cars:Mapped[list["Car"]]=relationship(back_populates="company")


class Car(Base):
    __tablename__ = "car"

    id:Mapped[int]=mapped_column(Integer, primary_key=True)
    model:Mapped[str]=mapped_column(String(50))
    company_id:Mapped[int] = mapped_column(Integer, ForeignKey("company.id"))
    company:Mapped["Company"]=relationship(back_populates="cars")

Base.metadata.create_all(engine)