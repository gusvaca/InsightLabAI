import pandas as pd
import streamlit as st

from core.session import guardar_dataset


class DatasetLoader:

    FORMATOS = {
        "csv": "CSV",
        "xlsx": "Excel",
        "xls": "Excel",
        "json": "JSON",
        "parquet": "Parquet"
    }

    @staticmethod
    def cargar(archivo):

        try:

            extension = archivo.name.split(".")[-1].lower()

            if extension == "csv":

                df = pd.read_csv(archivo)

            elif extension in ["xlsx", "xls"]:

                df = pd.read_excel(archivo)

            elif extension == "json":

                df = pd.read_json(archivo)

            elif extension == "parquet":

                df = pd.read_parquet(archivo)

            else:

                st.error("Formato no soportado.")
                return None

            guardar_dataset(df)

            return df

        except Exception as e:

            st.error(f"Error al cargar el archivo: {e}")

            return None