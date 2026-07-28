import asyncio

from app.database.connection import AsyncSessionLocal
from app.services.activity_service import create_activity_log


async def test():

    async with AsyncSessionLocal() as session:

        log = await create_activity_log(
            session=session,
            user_id=1,
            action="TEST",
            description="Testing activity log service"
        )

        print(
            "Created Activity Log:"
        )

        print(
            "ID:",
            log.id
        )

        print(
            "Action:",
            log.action
        )

        print(
            "Description:",
            log.description
        )


if __name__ == "__main__":
    asyncio.run(test())