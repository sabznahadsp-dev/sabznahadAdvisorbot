from sqlalchemy.ext.asyncio import AsyncSession

from app.models.activity_log import ActivityLog


async def create_activity_log(
    session: AsyncSession,
    user_id: int,
    action: str,
    description: str
):

    activity = ActivityLog(
        user_id=user_id,
        action=action,
        description=description
    )

    session.add(activity)

    await session.commit()

    await session.refresh(activity)

    return activity