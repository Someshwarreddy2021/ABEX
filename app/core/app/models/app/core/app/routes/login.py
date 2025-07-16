from fastapi import APIRouter
from app.models.schemas import LoginRequest
from app.core.linkedin import LinkedInBot

router = APIRouter()

@router.post("/login")
def login(data: LoginRequest):
    bot = LinkedInBot()
    bot.login(data.username, data.password)
    return {"status": "Logged in successfully"}
