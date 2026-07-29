from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy.orm import selectinload

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



async def get_all_activities(
    session: AsyncSession
):

    result = await session.execute(
        select(ActivityLog)
        .options(
            selectinload(
                ActivityLog.user
            )
        )
        .order_by(
            ActivityLog.created_at.desc()
        )
    )


    return result.scalars().all()



async def get_user_activities(
    session: AsyncSession,
    user_id: int
):

    result = await session.execute(
        select(ActivityLog)
        .options(
            selectinload(
                ActivityLog.user
            )
        )
        .where(
            ActivityLog.user_id == user_id
        )
        .order_by(
            ActivityLog.created_at.desc()
        )
    )


    return result.scalars().all()