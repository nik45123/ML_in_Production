"""
This module sets up the logger configuration.

It utilizes Pydantic's BaseSettings for configuration management,
allowing settings to be read from environment variables and a .env file.
"""

# data_file_name - path to our csv file in collection.py
# model_path - the folder containing model config files
# model_name - the name of the model we should use

from loguru import logger
from pydantic_settings import BaseSettings, SettingsConfigDict


class LoggerSettings(BaseSettings):
    """
    Logger configuration settings for the application.

    Attributes:
        model_config (SettingConfigDict): Model config, loaded from .env file.
        log_level (str): Logging level for the application.
    """

    model_config = SettingsConfigDict(
        env_file="config/.env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    log_level: str


def configure_logging(log_level: str) -> None:
    """
    Configure the logging for the application.

    Args:
        log_level (str): The log level to be set for the logger.
    Returns:
        None
    """
    # logger.remove()
    logger.add(
        "logs/app.log",
        rotation="1 day",
        retention="2 days",
        compression="zip",
        level=log_level,
    )


configure_logging(log_level=LoggerSettings().log_level)
