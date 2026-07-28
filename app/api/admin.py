from fastapi import APIRouter, Depends

from app.core.permissions import require_admin
from app.models.user import User


router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


@router.get("/dashboard")
async def admin_dashboard(
    current_user: User = Depends(require_admin)
):

    return {
        "message": "Welcome Admin",
        "username": current_user.username,
        "role": current_user.role.name
    }