from fastapi import Depends, HTTPException, status

from app.core.dependencies import get_current_user
from app.models.user import User


def require_role(required_role: str):

    async def role_checker(
        current_user: User = Depends(get_current_user)
    ):

        if current_user.role.name != required_role:

            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"{required_role} access required"
            )

        return current_user

    return role_checker


async def require_admin(
    current_user: User = Depends(get_current_user)
):

    if current_user.role.name != "admin":

        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )

    return current_user


async def require_advisor(
    current_user: User = Depends(get_current_user)
):

    if current_user.role.name != "advisor":

        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Advisor access required"
        )

    return current_user


async def require_customer(
    current_user: User = Depends(get_current_user)
):

    if current_user.role.name != "customer":

        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Customer access required"
        )

    return current_user