import asyncio

from sqlalchemy import text

from app.database.connection import engine


async def check_database():

    print("\n=== Database Inspection ===\n")

    async with engine.connect() as session:

        tables = await session.execute(
            text(
                """
                SELECT name
                FROM sqlite_master
                WHERE type='table'
                ORDER BY name;
                """
            )
        )

        print("Tables:")

        for table in tables.fetchall():
            print("-", table[0])


        print("\n=== Activity Logs Check ===")

        result = await session.execute(
            text(
                """
                SELECT name
                FROM sqlite_master
                WHERE type='table'
                AND name='activity_logs';
                """
            )
        )


        activity_table = result.fetchone()


        if activity_table:
            print(
                "activity_logs table EXISTS"
            )

            columns = await session.execute(
                text(
                    """
                    PRAGMA table_info(activity_logs);
                    """
                )
            )

            print("\nColumns:")

            for column in columns.fetchall():
                print(
                    column
                )

        else:
            print(
                "activity_logs table DOES NOT EXIST"
            )


if __name__ == "__main__":
    asyncio.run(check_database())