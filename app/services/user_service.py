from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.user import User


async def get_all_users(
    session: AsyncSession
):

    result = await session.execute(
        select(User)
        .options(
            selectinload(User.role)
        )
    )

    users = result.scalars().all()

    return users


async def get_user_by_id(
    session: AsyncSession,
    user_id: int
):

    result = await session.execute(
        select(User)
        .options(
            selectinload(User.role)
        )
        .where(
            User.id == user_id
        )
    )

    return result.scalar_one_or_none()


async def update_user_role(
    session: AsyncSession,
    user: User,
    role_id: int
):

    user.role_id = role_id

    await session.commit()

    result = await session.execute(
        select(User)
        .options(
            selectinload(User.role)
        )
        .where(
            User.id == user.id
        )
    )

    updated_user = result.scalar_one()

    return updated_user


async def update_user_status(
    session: AsyncSession,
    user: User,
    is_active: bool
):

    user.is_active = is_active

    await session.commit()

    result = await session.execute(
        select(User)
        .options(
            selectinload(User.role)
        )
        .where(
            User.id == user.id
        )
    )

    updated_user = result.scalar_one()

    return updated_user