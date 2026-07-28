from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.ext.asyncio import AsyncSession

from app.database.connection import get_db

from app.core.permissions import require_admin

from app.models.user import User

from app.schemas.admin import (
    UserAdminResponse,
    UserRoleUpdate,
    UserStatusUpdate
)

from app.services.user_service import (
    get_all_users,
    get_user_by_id,
    update_user_role,
    update_user_status
)


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


@router.get(
    "/users",
    response_model=list[UserAdminResponse]
)
async def list_users(
    current_user: User = Depends(require_admin),
    session: AsyncSession = Depends(get_db)
):

    users = await get_all_users(
        session
    )

    return [
        {
            "id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "phone": user.phone,
            "role": user.role.name,
            "is_active": user.is_active
        }
        for user in users
    ]


@router.get(
    "/users/{user_id}",
    response_model=UserAdminResponse
)
async def get_user(
    user_id: int,
    current_user: User = Depends(require_admin),
    session: AsyncSession = Depends(get_db)
):

    user = await get_user_by_id(
        session,
        user_id
    )

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "id": user.id,
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "phone": user.phone,
        "role": user.role.name,
        "is_active": user.is_active
    }


@router.patch(
    "/users/{user_id}/role",
    response_model=UserAdminResponse
)
async def change_user_role(
    user_id: int,
    data: UserRoleUpdate,
    current_user: User = Depends(require_admin),
    session: AsyncSession = Depends(get_db)
):

    user = await get_user_by_id(
        session,
        user_id
    )

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )


    user = await update_user_role(
        session,
        user,
        data.role_id
    )


    return {
        "id": user.id,
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "phone": user.phone,
        "role": user.role.name,
        "is_active": user.is_active
    }


@router.patch(
    "/users/{user_id}/status",
    response_model=UserAdminResponse
)
async def change_user_status(
    user_id: int,
    data: UserStatusUpdate,
    current_user: User = Depends(require_admin),
    session: AsyncSession = Depends(get_db)
):

    user = await get_user_by_id(
        session,
        user_id
    )

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )


    user = await update_user_status(
        session,
        user,
        data.is_active
    )


    return {
        "id": user.id,
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "phone": user.phone,
        "role": user.role.name,
        "is_active": user.is_active
    }