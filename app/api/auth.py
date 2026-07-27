from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.connection import get_db
from app.services.auth_service import (
    authenticate_user,
    AuthenticationError
)
from app.schemas.auth import TokenResponse

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/login",
    response_model=TokenResponse
)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: AsyncSession = Depends(get_db)
):
    try:
        result = await authenticate_user(
            session=session,
            username=form_data.username,
            password=form_data.password
        )

        return {
            "access_token": result["access_token"],
            "token_type": result["token_type"]
        }

    except AuthenticationError:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )