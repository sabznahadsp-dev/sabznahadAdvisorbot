from fastapi import APIRouter, Depends

from app.models.user import User
from app.core.dependencies import get_current_user


router = APIRouter(
    prefix="/protected",
    tags=["Protected"]
)


@router.get("/profile")
async def profile(
    user: User = Depends(get_current_user)
):

    return {
        "id": user.id,
        "username": user.username,
        "role_id": user.role_id
    }