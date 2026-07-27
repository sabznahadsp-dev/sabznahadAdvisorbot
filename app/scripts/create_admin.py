import asyncio

from sqlalchemy import select

from app.database.connection import AsyncSessionLocal
from app.models.user import User
from app.models.role import Role
from app.core.security import hash_password


ADMIN_FIRST_NAME = "Sabz"
ADMIN_LAST_NAME = "Manager"
ADMIN_PHONE = "09120000000"
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "Admin@12345"


async def create_admin():

    async with AsyncSessionLocal() as session:

        # پیدا کردن Role admin
        result = await session.execute(
            select(Role).where(Role.name == "admin")
        )

        admin_role = result.scalar_one_or_none()

        if not admin_role:
            print("Admin role not found")
            return


        # بررسی وجود کاربر
        result = await session.execute(
            select(User).where(
                User.username == ADMIN_USERNAME
            )
        )

        existing_user = result.scalar_one_or_none()


        if existing_user:
            print("Admin user already exists")
            return


        # ساخت کاربر مدیر
        admin_user = User(
            first_name=ADMIN_FIRST_NAME,
            last_name=ADMIN_LAST_NAME,
            phone=ADMIN_PHONE,
            username=ADMIN_USERNAME,
            password_hash=hash_password(ADMIN_PASSWORD),
            role_id=admin_role.id,
            is_active=True,
            phone_verified=True
        )


        session.add(admin_user)

        await session.commit()

        print("Admin user created successfully")
        print("----------------------------")
        print("Username:", ADMIN_USERNAME)
        print("Password:", ADMIN_PASSWORD)



if __name__ == "__main__":
    asyncio.run(create_admin())