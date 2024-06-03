from fastapi import APIRouter, Depends

from app.controllers.chat import ChatController
from app.schemas.requests.chat import ChatRequest
from app.schemas.responses import APIResponse
from app.schemas.responses.chat import ChatResponse
from core.factory import Factory
from core.utils.json_encoder import jsonable_encoder

chat_router = APIRouter()


@chat_router.post("/")
async def chat(
    chat_request: ChatRequest,
    chat_controller: ChatController = Depends(Factory().get_chat_controller),
) -> APIResponse[ChatResponse]:
    response = await chat_controller.chat(chat_request)
    return APIResponse(
        data=jsonable_encoder(response), message="Chat response returned successfully!"
    )