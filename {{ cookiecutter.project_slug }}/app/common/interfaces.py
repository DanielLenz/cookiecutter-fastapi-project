from pydantic import BaseModel


# Response models
#################
class ChatResponse(BaseModel):
    message: str


# Request models
################
class ChatRequest(BaseModel):
    message: str
