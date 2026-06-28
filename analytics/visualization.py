import pandas as pd
import numpy as np


class VisualizationEngine:

    @staticmethod
    def numericas(df):

        return df.select_dtypes(include=np.number).columns.tolist()

    @staticmethod
    def categoricas(df):

        return df.select_dtypes(
            include=["object", "category"]
        ).columns.tolist()

    @staticmethod
    def todas(df):

        return df.columns.tolist()