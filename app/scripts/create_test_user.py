import asyncio

from app.database.connection import AsyncSessionLocal
from app.models.user import User


async def create_user():

    async with AsyncSessionLocal() as session:

        user = User(
            first_name="Test",
            last_name="User",
            phone="09121111111",
            username="testuser",
            password_hash="test_password_hash",
            role_id=2,
            is_active=True,
            phone_verified=False
        )

        session.add(user)

        await session.commit()

        await session.refresh(user)

        print(
            "Created user:",
            user.id,
            user.username,
            user.role_id
        )


if __name__ == "__main__":
    asyncio.run(create_user())