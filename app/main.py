from fastapi import FastAPI
from app.routers import logs

app = FastAPI()

app.include_router(logs.router)