from fastapi import FastAPI
from app.api.endpoints import  users,notification

app = FastAPI(title = "NMS FastAPI")


app.include_router(notification.router,prefix="/notification", tags=["notifications"])
app.include_router(users.router,prefix="/users", tags=["users"])