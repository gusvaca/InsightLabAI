import pandas as pd
import numpy as np


class DataProfiler:

    @staticmethod
    def profile(df):

        resultado = []

        for columna in df.columns:

            serie = df[columna]

            tipo = str(serie.dtype)

            nulos = serie.isna().sum()

            porcentaje_nulos = round(
                (nulos / len(df)) * 100,
                2
            )

            unicos = serie.nunique()

            memoria = round(
                serie.memory_usage(deep=True) / 1024,
                2
            )

            minimo = None
            maximo = None
            promedio = None

            if pd.api.types.is_numeric_dtype(serie):

                minimo = serie.min()
                maximo = serie.max()
                promedio = round(
                    serie.mean(),
                    2
                )

            recomendacion = ""

            if porcentaje_nulos > 30:

                recomendacion = "Muchos valores nulos"

            elif unicos == len(df):

                recomendacion = "Posible clave primaria"

            elif unicos == 1:

                recomendacion = "Columna constante"

            resultado.append({

                "Columna": columna,

                "Tipo": tipo,

                "% Nulos": porcentaje_nulos,

                "Únicos": unicos,

                "Memoria KB": memoria,

                "Mínimo": minimo,

                "Máximo": maximo,

                "Promedio": promedio,

                "Recomendación": recomendacion

            })

        return pd.DataFrame(resultado)