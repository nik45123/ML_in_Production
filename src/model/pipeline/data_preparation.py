"""
This module provides functionality for preparing a dataset for ML model.

It consist of function to load data from a database.
encode categorical columns, and parse specific columns for further processing.
"""

import re

import pandas as pd
import warnings
from loguru import logger

from model.pipeline.data_collection import load_data_from_db

warnings.filterwarnings("ignore")


def prepare_data() -> pd.DataFrame:
    """
    Prepare the dataset for analysis and modelling.

    This involves loading the data, encoding categorical column,
    and parsing the 'garden' column.

    Returns:
        pd.DataFrame: The processed dataset.
    """
    logger.info("starting up preprocessing pipeline")
    dataframe = load_data_from_db()

    data_encoded = _encode_cat_cols(dataframe)
    return _parse_garden_col(data_encoded)


def _encode_cat_cols(dataframe):
    """
    Encode categorical columns into dummy variables.

    Arg:
        dataframe (pd.DataFrame): The original dataset.

    Returns:
        pd.DataFrame: Dataset with categorical columns encoded.
    """
    cols = ["balcony", "parking", "furnished", "garage", "storage"]

    logger.info(f"encoding categorical columns : {cols}")

    return pd.get_dummies(
        dataframe,
        columns=cols,
        drop_first=True,
    )


def _parse_garden_col(dataframe):
    """
    Parse the 'garden' column in the dataset.

    Args:
        dataframe(pd.DataFrame): The dataset with a 'garden' column.

    Returns:
        pd.DataFrame: The dataset with the 'garden' column parsed.
    """
    logger.info("parsing garden column")

    dataframe["garden"] = (
        dataframe["garden"].str.extract(r"(\d+)").fillna(0).astype(int)
    )

    return dataframe


# df = prepare_data()
# print(df.garden)
