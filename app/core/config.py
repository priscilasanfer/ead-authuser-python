from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "ead-auth-user-python"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True

    DATABASE_URL: str
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    DB_HOST: str
    DB_PORT: str

    API_V1_STR: str = "/api/v1"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings() # type: ignore
