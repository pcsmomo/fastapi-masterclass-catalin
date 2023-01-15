from redis_om import get_redis_connection
from app.config import get_settings

config = get_settings()


redis = get_redis_connection(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    password=config.REDIS_PASSWORD
)
