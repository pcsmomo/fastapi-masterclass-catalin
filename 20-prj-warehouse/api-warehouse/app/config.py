from pydantic import BaseSettings


class RedisSettings(BaseSettings):
    REDIS_HOST: str = "localhost"
    REDIS_PORT: str = "6379"
    REDIS_PASSWORD: str = ""


class Settings(RedisSettings):
    pass


def get_settings() -> Settings:
    """
        Cache the settings, this allows the settings to be used in dependencies
        and for overwriting in tests
    """
    return Settings()
