from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.core.security import verify_password
from app.core.jwt import create_access_token


class AuthenticationError(Exception):
    """
    Raised when authentication fails.
    """
    pass


async def authenticate_user(
    session: AsyncSession,
    username: str,
    password: str
):
    """
    Authenticate user with username and password.
    """

    result = await session.execute(
        select(User).where(
            User.username == username
        )
    )

    user = result.scalar_one_or_none()

    if user is None:
        raise AuthenticationError("Invalid username or password")

    if not verify_password(
        password,
        user.password_hash
    ):
        raise AuthenticationError("Invalid username or password")

    if not user.is_active:
        raise AuthenticationError("User account is inactive")

    token = create_access_token(
        {
            "user_id": user.id,
            "username": user.username,
            "role_id": user.role_id
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer",
        "user": user
    }