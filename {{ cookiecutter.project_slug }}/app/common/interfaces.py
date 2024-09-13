from pydantic import BaseModel


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


class UserUpdate(BaseModel):
    name: str
