import pandas as pd

from cleaning.models import CleaningAction


class DatatypeCleaner:

    """
    ==========================================================
    Datatype Cleaner

    Motor encargado de detectar y convertir
    automáticamente los tipos de datos.

    Funcionalidades

    • Convertir números
    • Convertir fechas
    • Convertir booleanos
    • Optimizar memoria
    • Estadísticas

    ==========================================================
    """

    @staticmethod
    def convert_numeric(df):

        convertidas = 0

        for columna in df.columns:

            if df[columna].dtype == object:

                try:

                    serie = pd.to_numeric(

                        df[columna],

                        errors="raise"

                    )

                    df[columna] = serie

                    convertidas += 1

                except Exception:

                    pass

        return CleaningAction(

            nombre="Conversión Numérica",

            descripcion=(
                f"Se convirtieron "
                f"{convertidas} columnas numéricas."
            ),

            registros_afectados=convertidas

        )

    @staticmethod
    def convert_dates(df):

        convertidas = 0

        for columna in df.columns:

            if df[columna].dtype == object:

                try:

                    serie = pd.to_datetime(

                        df[columna],

                        errors="raise"

                    )

                    if serie.notna().sum() > 0:

                        df[columna] = serie

                        convertidas += 1

                except Exception:

                    pass

        return CleaningAction(

            nombre="Conversión de Fechas",

            descripcion=(
                f"Se convirtieron "
                f"{convertidas} columnas a fecha."
            ),

            registros_afectados=convertidas

        )

    @staticmethod
    def convert_boolean(df):

        convertidas = 0

        valores = {

            "true": True,
            "false": False,
            "yes": True,
            "no": False,
            "si": True,
            "sí": True,
            "0": False,
            "1": True

        }

        for columna in df.columns:

            if df[columna].dtype != object:

                continue

            serie = (

                df[columna]

                .astype(str)

                .str.lower()

                .str.strip()

            )

            unicos = set(

                serie.unique()

            )

            if unicos.issubset(

                valores.keys()

            ):

                df[columna] = serie.map(

                    valores

                )

                convertidas += 1

        return CleaningAction(

            nombre="Conversión Booleana",

            descripcion=(
                f"Se convirtieron "
                f"{convertidas} columnas booleanas."
            ),

            registros_afectados=convertidas

        )

    @staticmethod
    def optimize_memory(df):

        optimizadas = 0

        for columna in df.select_dtypes(

            include=["int64"]

        ).columns:

            df[columna] = pd.to_numeric(

                df[columna],

                downcast="integer"

            )

            optimizadas += 1

        for columna in df.select_dtypes(

            include=["float64"]

        ).columns:

            df[columna] = pd.to_numeric(

                df[columna],

                downcast="float"

            )

            optimizadas += 1

        return CleaningAction(

            nombre="Optimización de Memoria",

            descripcion=(
                f"Se optimizaron "
                f"{optimizadas} columnas."
            ),

            registros_afectados=optimizadas

        )

    @staticmethod
    def statistics(df):

        tipos = {}

        for columna in df.columns:

            tipo = str(

                df[columna].dtype

            )

            tipos[tipo] = tipos.get(

                tipo,

                0

            ) + 1

        return tipos