"""Lambdata - a collection of Data Science helper functions"""


# accessing libraries through pipenv
import pandas as pd
import numpy as np


class MyDataFrame(pd.DataFrame):
    def null_count(self):

        """
        Checks dataframe for null values.
        Returns the number of missing values.
        """

        return self.isna().sum().sum()

    def list_2_series(self, list_2_add):

        """
        Takes in a list and pandas dataframe.
        List is converted to pandas series and added to pandas dataframe.
        Returns the dataframe with list added as a series/column.
        """

        as_series = pd.Series(list_2_add)
        self['list'] = as_series
        return self
