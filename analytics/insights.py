import pandas as pd


class InsightEngine:

    @staticmethod
    def generar(df):

        insights = []

        # ==========================
        # Valores nulos
        # ==========================

        total_nulos = df.isna().sum()

        columnas_nulos = total_nulos[total_nulos > 0]

        if len(columnas_nulos) == 0:

            insights.append({
                "tipo": "success",
                "titulo": "Excelente calidad",
                "mensaje": "No se encontraron valores nulos."
            })

        else:

            for columna, valor in columnas_nulos.items():

                porcentaje = (valor / len(df)) * 100

                if porcentaje > 40:

                    insights.append({
                        "tipo": "error",
                        "titulo": "Muchos valores nulos",
                        "mensaje": f"La columna '{columna}' tiene {porcentaje:.1f}% de valores nulos."
                    })

                elif porcentaje > 15:

                    insights.append({
                        "tipo": "warning",
                        "titulo": "Valores nulos",
                        "mensaje": f"La columna '{columna}' tiene {porcentaje:.1f}% de valores nulos."
                    })

        # ==========================
        # Duplicados
        # ==========================

        duplicados = df.duplicated().sum()

        if duplicados > 0:

            insights.append({

                "tipo": "warning",

                "titulo": "Duplicados",

                "mensaje": f"Se encontraron {duplicados} registros duplicados."

            })

        # ==========================
        # Columnas constantes
        # ==========================

        for columna in df.columns:

            if df[columna].nunique() == 1:

                insights.append({

                    "tipo": "info",

                    "titulo": "Columna constante",

                    "mensaje": f"La columna '{columna}' tiene un único valor."

                })

        # ==========================
        # Posibles IDs
        # ==========================

        for columna in df.columns:

            if df[columna].nunique() == len(df):

                insights.append({

                    "tipo": "info",

                    "titulo": "Posible llave primaria",

                    "mensaje": f"'{columna}' podría ser una clave primaria."

                })

        return insights