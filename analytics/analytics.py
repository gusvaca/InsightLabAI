import pandas as pd


class DataQuality:

    @staticmethod
    def score(df):

        score = 100

        total = df.shape[0] * df.shape[1]

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
            score -= 10

        return max(score, 0)

    @staticmethod
    def estado(score):

        if score >= 90:
            return "🟢 Excelente"

        elif score >= 70:
            return "🟡 Bueno"

        return "🔴 Crítico"