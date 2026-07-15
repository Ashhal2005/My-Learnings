from sqlalchemy import column, Integer, String, DateTime
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class User(Base):
    __tablename__ = "users"
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    username:Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email:Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    h_pswd:Mapped[str] = mapped_column(String(255), nullable=False)
    timestamp:Mapped[datetime] = mapped_column(DateTime,default=datetime.utcnow)

