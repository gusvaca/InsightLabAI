import pandas as pd

from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler


class AnomalyEngine:

    @staticmethod
    def detectar(df, columnas, contaminacion=0.05):

        datos = df[columnas].dropna().copy()

        scaler = StandardScaler()

        x = scaler.fit_transform(datos)

        modelo = IsolationForest(
            contamination=contaminacion,
            random_state=42
        )

        pred = modelo.fit_predict(x)

        datos["Anomaly"] = pred

        datos["Anomaly"] = datos["Anomaly"].map({
            1: "Normal",
            -1: "Anomalía"
        })

        return datos