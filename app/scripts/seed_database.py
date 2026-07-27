import asyncio

from app.database.connection import AsyncSessionLocal
from app.database.seed.roles import create_default_roles


async def main():

    async with AsyncSessionLocal() as session:

        await create_default_roles(session)

        print("Default roles created successfully")


if __name__ == "__main__":
    asyncio.run(main())