import asyncio

from sqlalchemy import select, func

from app.database.connection import AsyncSessionLocal
from app.models.activity_log import ActivityLog


async def test_activity_logs():

    print("\n=== Activity Logs Test ===\n")

    async with AsyncSessionLocal() as session:

        # تعداد رکوردها
        result = await session.execute(
            select(
                func.count(ActivityLog.id)
            )
        )

        count = result.scalar()

        print(
            "Total activity logs:",
            count
        )


        # نمایش رکوردها
        result = await session.execute(
            select(ActivityLog)
            .order_by(
                ActivityLog.id
            )
        )

        logs = result.scalars().all()


        if not logs:
            print(
                "No activity logs found"
            )

        else:

            for log in logs:

                print(
                    "ID:",
                    log.id
                )

                print(
                    "User ID:",
                    log.user_id
                )

                print(
                    "Action:",
                    log.action
                )

                print(
                    "Description:",
                    log.description
                )

                print(
                    "Created:",
                    log.created_at
                )

                print(
                    "----------------"
                )


if __name__ == "__main__":

    asyncio.run(
        test_activity_logs()
    )