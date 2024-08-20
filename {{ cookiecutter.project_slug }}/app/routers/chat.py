from fastapi import APIRouter

from app.common.interfaces import ChatRequest, ChatResponse
from app.logic.llm import call_model

router = APIRouter()


@router.post("/generate", response_model=ChatResponse, tags=["Chat"])
async def generate_chat(request: ChatRequest):
    answer = call_model()
    return ChatResponse(message=answer)
