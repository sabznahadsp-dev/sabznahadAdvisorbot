from sqlalchemy.ext.asyncio import AsyncSession

from app.models.role import Role


async def create_default_roles(
    session: AsyncSession
):

    roles = [
        "admin",
        "customer",
        "advisor",
    ]

    for role_name in roles:

        existing_role = await session.execute(
            Role.__table__.select()
            .where(Role.name == role_name)
        )

        role = existing_role.first()

        if not role:
            session.add(
                Role(
                    name=role_name
                )
            )

    await session.commit()