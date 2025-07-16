from fastapi import FastAPI
from app.routes import login, connect, check_connection, close

app = FastAPI()

app.include_router(login.router)
app.include_router(connect.router)
app.include_router(check_connection.router)
app.include_router(close.router)
