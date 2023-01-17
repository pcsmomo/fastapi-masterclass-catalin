from pydantic import BaseSettings


class RedisSettings(BaseSettings):
    REDIS_HOST: str = "localhost"
    REDIS_PORT: str = "6379"
    REDIS_PASSWORD: str = ""


class WarehouseSettings(BaseSettings):
    WAREHOUSE_HOST: str = "localhost"
    WAREHOUSE_PORT: str = "8000"


class Settings(RedisSettings, WarehouseSettings):
    pass


def get_settings() -> Settings:
    """
        Cache the settings, this allows the settings to be used in dependencies
        and for overwriting in tests
    """
    return Settings()
