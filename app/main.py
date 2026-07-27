from fastapi import FastAPI

from app.api.auth import router as auth_router


app = FastAPI(
    title="SabzNahad Advisor Bot API",
    description="API for SabzNahad authentication and services",
    version="1.0.0"
)


# Authentication routes
app.include_router(auth_router)


@app.get("/")
async def root():
    return {
        "message": "SabzNahad API is running"
    }