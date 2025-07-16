from fastapi import APIRouter
from app.models.schemas import CheckConnectionRequest
from app.core.linkedin import LinkedInBot

router = APIRouter()

@router.post("/check_connection")
def check_connection(data: CheckConnectionRequest):
    bot = LinkedInBot()
    connected = bot.check_connection_and_message(data.profile_url, data.message)
    return {"connected": connected}
