from pathlib import Path

from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict
)


BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    """
    Application configuration
    """

    # Telegram
    BOT_TOKEN: str


    # Database
    DATABASE_URL: str


    # Admin
    ADMIN_ID: int


    # Website
    WEBSITE_URL: str


    # Support
    SUPPORT_PHONE: str | None = None


    # AI
    OPENAI_API_KEY: str | None = None


    # Payment gateways
    MELLAT_TERMINAL_ID: str | None = None
    MELLI_MERCHANT_ID: str | None = None
    SAMAN_MERCHANT_ID: str | None = None


    # JWT Security
    SECRET_KEY: str

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60


    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()