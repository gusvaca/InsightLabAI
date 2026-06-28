import pandas as pd


def calcular_score(df):

    score = 100

    porcentaje_nulos = (
        df.isnull()
        .sum()
        .sum()
    ) / (df.shape[0] * df.shape[1])

    duplicados = df.duplicated().sum()

    if porcentaje_nulos > .10:
        score -= 30

    elif porcentaje_nulos > .05:
        score -= 15

    if duplicados > 0:
        score -= 10

    return max(score, 0)