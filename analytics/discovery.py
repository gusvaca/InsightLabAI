import pandas as pd
import numpy as np

from analytics.statistics import Statistics
from analytics.quality import DataQuality


class DiscoveryEngine:

    @staticmethod
    def generar(df):

        descubrimientos = []

        # ===================================
        # Calidad
        # ===================================

        score = DataQuality.score(df)

        descubrimientos.append({

            "tipo": "info",

            "titulo": "Calidad del Dataset",

            "mensaje": f"El dataset obtuvo un Data Health Score de {score}/100."

        })

        # ===================================
        # Correlaciones
        # ===================================

        corr = Statistics.correlation(df)

        if not corr.empty:

            columnas = corr.columns

            for i in range(len(columnas)):

                for j in range(i + 1, len(columnas)):

                    valor = corr.iloc[i, j]

                    if abs(valor) >= 0.85:

                        descubrimientos.append({

                            "tipo": "success",

                            "titulo": "Correlación Fuerte",

                            "mensaje": f"{columnas[i]} y {columnas[j]} tienen una correlación de {valor:.2f}"

                        })

        # ===================================
        # Skewness
        # ===================================

        skew = Statistics.skewness(df)

        for _, fila in skew.iterrows():

            if abs(fila["Skewness"]) > 1:

                descubrimientos.append({

                    "tipo": "warning",

                    "titulo": "Distribución Sesgada",

                    "mensaje": f"{fila['Variable']} presenta un sesgo importante ({fila['Skewness']:.2f})"

                })

        # ===================================
        # Outliers
        # ===================================

        outliers = Statistics.outliers(df)

        for _, fila in outliers.iterrows():

            if fila["Outliers"] > 0:

                descubrimientos.append({

                    "tipo": "warning",

                    "titulo": "Valores Atípicos",

                    "mensaje": f"{fila['Variable']} contiene {fila['Outliers']} outliers."

                })

        return descubrimientos