import pandas as pd
import numpy as np


class EDAEngine:

    @staticmethod
    def variables_numericas(df):

        return df.select_dtypes(include=np.number).columns.tolist()

    @staticmethod
    def estadisticas(df, columna):

        serie = df[columna].dropna()

        return {
            "Media": round(serie.mean(), 2),
            "Mediana": round(serie.median(), 2),
            "Desviación": round(serie.std(), 2),
            "Mínimo": round(serie.min(), 2),
            "Máximo": round(serie.max(), 2),
            "Q1": round(serie.quantile(0.25), 2),
            "Q3": round(serie.quantile(0.75), 2)
        }

    @staticmethod
    def cantidad_outliers(df, columna):

        serie = df[columna].dropna()

        q1 = serie.quantile(0.25)
        q3 = serie.quantile(0.75)

        iqr = q3 - q1

        inferior = q1 - 1.5 * iqr
        superior = q3 + 1.5 * iqr

        return len(
            serie[
                (serie < inferior) |
                (serie > superior)
            ]
        )