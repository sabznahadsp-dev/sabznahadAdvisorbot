import asyncio
import httpx


LOGIN_URL = "http://127.0.0.1:8000/auth/login"


async def test_login():

    async with httpx.AsyncClient() as client:

        response = await client.post(
            LOGIN_URL,
            data={
                "username": "admin",
                "password": "Admin@12345"
            }
        )

        print("Status Code:")
        print(response.status_code)

        print("\nResponse:")
        print(response.json())


if __name__ == "__main__":
    asyncio.run(test_login())