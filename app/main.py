from fastapi import FastAPI
from app.routers import logs

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "ok"}

app.include_router(logs.router)