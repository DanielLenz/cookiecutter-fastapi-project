from fastapi import APIRouter

from app.common.interfaces import Chat, ChatRequest
from app.logic.llm import call_model

router = APIRouter()


@router.post("/generate", response_model=Chat, tags=["Chat"])
async def generate_chat(request: ChatRequest):
    answer = call_model()
    return Chat(message=answer)
