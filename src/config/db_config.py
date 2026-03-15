"""
This module sets up the database configuration.

It utilizes Pydantic's BaseSettings for configuration management,
allowing settings to be read from environment variables and a .env file.
"""

# data_file_name - path to our csv file in collection.py
# model_path - the folder containing model config files
# model_name - the name of the model we should use


from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import create_engine


class DbSettings(BaseSettings):
    """
    Configuration settings for the application.

    Attributes:
        model_config (SettingConfigDict): Model config, loaded from .env file.
        db_conn_str (str): Database connection string.
        rent_apart_table_name (str): Name of the rental apartments table in DB.
    """

    model_config = SettingsConfigDict(
        env_file="config/.env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    db_conn_str: str
    rent_apart_table_name: str


db_settings = DbSettings()

engine = create_engine(db_settings.db_conn_str)
