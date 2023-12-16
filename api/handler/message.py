from fastapi import APIRouter
from pydantic import BaseModel

from bot import new_bot
from repo import get_all_chat_ids

base_router = APIRouter()
bot = new_bot()


class Req(BaseModel):
    Message: str


@base_router.post("/tg/send")
def send_tg(item: Req):
    ids = get_all_chat_ids()

    for i in ids:
        bot.send_message(i, item.Message)

    return {"message": "ok"}
