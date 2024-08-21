from pydantic import BaseModel
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


# Response models
#################
class Chat(BaseModel):
    message: str


class User(BaseModel):
    id: int
    name: str


# Request models
################
class ChatRequest(BaseModel):
    message: str


class UserCreate(BaseModel):
    name: str


# DB models
###########
class Base(DeclarativeBase):
    pass


class DBUser(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(index=True, primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
