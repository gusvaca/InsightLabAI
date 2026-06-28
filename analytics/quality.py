import pandas as pd


class DataQuality:

    @staticmethod
    def score(df):

        score = 100

        total = df.shape[0] * df.shape[1]

        if total == 0:
            return 0

        nulos = df.isna().sum().sum()

        duplicados = df.duplicated().sum()

        porcentaje_nulos = (nulos / total) * 100

        if porcentaje_nulos > 20:
            score -= 40

        elif porcentaje_nulos > 10:
            score -= 25

        elif porcentaje_nulos > 5:
            score -= 10

        if duplicados > 0:
            score -= min(10, duplicados)

        return max(score, 0)

    @staticmethod
    def estado(score):

        if score >= 90:
            return "🟢 Excelente"

        elif score >= 75:
            return "🟡 Bueno"

        elif score >= 60:
            return "🟠 Regular"

        else:
            return "🔴 Crítico"

    @staticmethod
    def resumen(df):

        return {

            "filas": len(df),

            "columnas": len(df.columns),

            "nulos": int(df.isna().sum().sum()),

            "duplicados": int(df.duplicated().sum()),

            "memoria": round(
                df.memory_usage(deep=True).sum()
                / 1024
                / 1024,
                2
            ),

            "score": DataQuality.score(df),

            "estado": DataQuality.estado(
                DataQuality.score(df)
            )

        }

    @staticmethod
    def recomendaciones(df):

        recomendaciones = []

        porcentaje_nulos = (
            df.isna().sum() / len(df)
        ) * 100

        for columna, valor in porcentaje_nulos.items():

            if valor > 40:

                recomendaciones.append(
                    f"Eliminar o imputar '{columna}' ({valor:.1f}% de nulos)"
                )

        if df.duplicated().sum() > 0:

            recomendaciones.append(
                "Existen registros duplicados."
            )

        if len(recomendaciones) == 0:

            recomendaciones.append(
                "No se encontraron problemas importantes."
            )

        return recomendaciones