from fastapi import APIRouter
from app.llm import get_chat_llm ,return_response
from api.schemas.chat import ChatRequest
router = APIRouter(prefix='/chat')

@router.post("/")
def chatApi(request: ChatRequest):
    print("request recieved")
    query = request.query
    history = request.history

    llm = get_chat_llm()
    response = llm.invoke(query)
    return {"ai_message":return_response(response)}
