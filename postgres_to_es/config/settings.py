from pydantic import BaseSettings, Field


class PgSettings(BaseSettings):
    """Postgres connection config"""

    dbname: str = Field(..., env="DB_NAME")
    user: str = Field(..., env="DB_USER")
    password: str = Field(..., env="DB_PASSWORD")
    host: str = Field(..., env="DB_HOST")
    port: int = Field(..., env="DB_PORT")

    class Config:
        env_file = "config/.env"
        env_file_encoding = "utf-8"


class EsSettings(BaseSettings):
    """Elasticsearch connection config"""

    host: str = Field(..., env="ES_HOST")
    port: int = Field(..., env="ES_PORT")

    class Config:
        env_file = "config/.env"
        env_file_encoding = "utf-8"


class MainTimingSettings(BaseSettings):
    """Backoff config"""

    es_connect_wait_time: int = 1
    etl_refresh_time: int = 5
    backoff_start_sleep_time: float = 0.1
    backoff_factor: int = 2
    backoff_border_sleep_time: int = 10


class LoggerSettings(BaseSettings):
    """Logger config"""

    version: int = 1
    disable_existing_loggers: bool = False

    formatters: dict = {
        "default_formatter": {
            "format": '%(levelname)s\t%(asctime)s\t%(funcName)s\t"%(message)s"'
        },
    }

    handlers: dict = {
        "file_handler": {
            "class": "logging.FileHandler",
            "filename": "logs.log",
            "formatter": "default_formatter",
        },
        "stream_handler": {
            "class": "logging.StreamHandler",
            "formatter": "default_formatter",
        },
    }

    loggers: dict = {
        "my_logger": {
            "handlers": ["stream_handler"],
            "level": "DEBUG",
            "propagate": True,
        }
    }
