from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.api.protected import router as protected_router


app = FastAPI(
    title="SabzNahad Advisor Bot API",
    description="API for SabzNahad authentication and services",
    version="1.0.0"
)


# Authentication API
app.include_router(auth_router)


# Protected API
app.include_router(protected_router)


@app.get("/")
async def root():
    return {
        "message": "SabzNahad API is running"
    }