from fastapi import APIRouter
from pydantic import BaseModel

from bot import new_bot
from mail import new_mail, send_message, close
from repo import get_all_chat_ids, get_all_emails

base_router = APIRouter()
bot = new_bot()


class Req(BaseModel):
    message: str
    token: str


class MailReq(BaseModel):
    message: str
    producer_mail: str


@base_router.post("/tg/send")
def send_tg(item: Req):

    ids = get_all_chat_ids(int(item.token.split('.')[1]))

    for i in ids:
        bot.send_message(i, item.message)

    return {"message": "ok"}


@base_router.post("/mail/send")
def send_mail(req: MailReq):
    smtp = new_mail()

    emails = get_all_emails(req.producer_mail)
    for mail in emails:
        send_message(smtp, mail, req.message)

    close(smtp)

    return {"message": "ok"}
