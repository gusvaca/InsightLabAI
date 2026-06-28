import pandas as pd


class MissingAnalyzer:

    @staticmethod
    def resumen(df):

        datos = pd.DataFrame({

            "Columna": df.columns,

            "Nulos": df.isna().sum().values

        })

        datos["Porcentaje"] = round(

            datos["Nulos"] /

            len(df) * 100,

            2

        )

        datos = datos.sort_values(

            "Porcentaje",

            ascending=False

        )

        return datos