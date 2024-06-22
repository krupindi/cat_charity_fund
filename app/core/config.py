from typing import Optional

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    app_title: str = 'Благотворительный фонд поддержки котиков'
    app_description: str = 'Котики'
    database_url: str = 'sqlite+aiosqlite:///./qrkot_charity_fund.db'
    secret: str = 'secret'
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None
    PASSWORD_MIN_LENGTH: int = 3
    MIN_INVESTED_AMOUNT: int = 0

    class Config:
        env_file = '.env'


settings = Settings()
