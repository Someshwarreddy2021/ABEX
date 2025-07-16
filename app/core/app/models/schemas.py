from pydantic import BaseModel

class LoginRequest(BaseModel):
    username: str
    password: str

class ConnectRequest(BaseModel):
    profile_url: str

class CheckConnectionRequest(BaseModel):
    profile_url: str
    message: str
