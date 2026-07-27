import asyncio

from sqlalchemy import select

from app.database.connection import AsyncSessionLocal
from app.models.role import Role


async def check_roles():
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Role))
        roles = result.scalars().all()

        for role in roles:
            print(role.id, role.name)


if __name__ == "__main__":
    asyncio.run(check_roles())