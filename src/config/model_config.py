"""
This module sets up the ML model configuration.

It utilizes Pydantic's BaseSettings for configuration management,
allowing settings to be read from environment variables and a .env file.
"""

# data_file_name - path to our csv file in collection.py
# model_path - the folder containing model config files
# model_name - the name of the model we should use

from pydantic import DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict


class ModelSettings(BaseSettings):
    """
    ML Model Configuration settings for the application.

    Attributes:
        model_config (SettingConfigDict): Model config, loaded from .env file.
        model_path (DirectoryPath): Filesystem path to the model.
        model_name (str): Name of the model.
    """

    model_config = SettingsConfigDict(
        env_file="config/.env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    model_path: DirectoryPath
    model_name: str


# Initializing settings and configure logging
model_settings = ModelSettings()
