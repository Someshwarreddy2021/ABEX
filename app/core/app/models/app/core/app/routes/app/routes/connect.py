from fastapi import APIRouter
from app.models.schemas import ConnectRequest
from app.core.linkedin import LinkedInBot

router = APIRouter()

@router.post("/connect")
def connect(data: ConnectRequest):
    bot = LinkedInBot()
    bot.connect(data.profile_url)
    return {"status": "Connection request sent"}
