import pandas as pd
import numpy as np


class Statistics:

    @staticmethod
    def correlation(df):

        numericas = df.select_dtypes(include=np.number)

        if numericas.empty:
            return pd.DataFrame()

        return numericas.corr()

    @staticmethod
    def skewness(df):

        numericas = df.select_dtypes(include=np.number)

        if numericas.empty:
            return pd.DataFrame()

        resultado = pd.DataFrame({
            "Variable": numericas.columns,
            "Skewness": numericas.skew().values
        })

        resultado["Interpretación"] = resultado["Skewness"].apply(
            Statistics.interpretar_skew
        )

        return resultado

    @staticmethod
    def kurtosis(df):

        numericas = df.select_dtypes(include=np.number)

        if numericas.empty:
            return pd.DataFrame()

        resultado = pd.DataFrame({
            "Variable": numericas.columns,
            "Curtosis": numericas.kurt().values
        })

        return resultado

    @staticmethod
    def interpretar_skew(valor):

        if abs(valor) < 0.5:
            return "Simétrica"

        elif valor > 0:
            return "Sesgo positivo"

        else:
            return "Sesgo negativo"

    @staticmethod
    def outliers(df):

        numericas = df.select_dtypes(include=np.number)

        resultado = []

        for columna in numericas.columns:

            q1 = numericas[columna].quantile(.25)
            q3 = numericas[columna].quantile(.75)

            iqr = q3 - q1

            inferior = q1 - 1.5 * iqr
            superior = q3 + 1.5 * iqr

            cantidad = numericas[
                (numericas[columna] < inferior) |
                (numericas[columna] > superior)
            ].shape[0]

            resultado.append({

                "Variable": columna,

                "Outliers": cantidad

            })

        return pd.DataFrame(resultado)