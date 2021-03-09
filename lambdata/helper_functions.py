"""Lambdata - a collection of Data Science helper functions"""

# accessing libraries through pipenv
import pandas as pd
import numpy as np

def null_count(df):
    """Checks dataframe for null values and returns the number of missing values"""
    missing = df.isna().sum()
    return missing

def list_2_series(list_2_series, df):
    """Takes in a list and dataframe, converts list to series, then adds series to dataframe"""
    as_series = pd.Series(list)
    df['list'] = as_series
    return df
