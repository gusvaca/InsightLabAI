import pandas as pd

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


class ClusteringEngine:

    @staticmethod
    def ejecutar(df, columnas, k=3):

        datos = df[columnas].dropna()

        scaler = StandardScaler()

        x = scaler.fit_transform(datos)

        modelo = KMeans(
            n_clusters=k,
            random_state=42,
            n_init=10
        )

        clusters = modelo.fit_predict(x)

        resultado = datos.copy()

        resultado["Cluster"] = clusters

        return resultado