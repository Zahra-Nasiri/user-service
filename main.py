from fastapi import FastAPI
from user_app.router import router as user_router

app = FastAPI()
app.include_router(user_router)
