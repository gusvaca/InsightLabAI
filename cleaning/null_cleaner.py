import pandas as pd

from cleaning.models import CleaningAction


class NullCleaner:

    """
    ===========================================================
    Null Cleaner

    Motor encargado del tratamiento de valores nulos.

    Funcionalidades:

    • Detectar valores nulos
    • Estadísticas
    • Imputación por media
    • Imputación por mediana
    • Imputación por moda
    • Imputación por constante
    • Eliminar filas
    • Eliminar columnas

    ===========================================================
    """

    @staticmethod
    def statistics(df):

        total = int(df.isna().sum().sum())

        porcentaje = round(

            total /

            (len(df) * len(df.columns))

            * 100,

            2

        )

        columnas = {}

        for columna in df.columns:

            cantidad = int(

                df[columna].isna().sum()

            )

            if cantidad > 0:

                columnas[columna] = {

                    "cantidad": cantidad,

                    "porcentaje": round(

                        cantidad /

                        len(df)

                        * 100,

                        2

                    )

                }

        return {

            "total": total,

            "porcentaje": porcentaje,

            "columnas": columnas

        }

    @staticmethod
    def fill_mean(df):

        columnas = df.select_dtypes(

            include="number"

        ).columns

        afectadas = 0

        for columna in columnas:

            if df[columna].isna().any():

                df[columna].fillna(

                    df[columna].mean(),

                    inplace=True

                )

                afectadas += 1

        return CleaningAction(

            nombre="Imputación por Media",

            descripcion=f"Se imputaron {afectadas} columnas usando la media.",

            registros_afectados=afectadas

        )

    @staticmethod
    def fill_median(df):

        columnas = df.select_dtypes(

            include="number"

        ).columns

        afectadas = 0

        for columna in columnas:

            if df[columna].isna().any():

                df[columna].fillna(

                    df[columna].median(),

                    inplace=True

                )

                afectadas += 1

        return CleaningAction(

            nombre="Imputación por Mediana",

            descripcion=f"Se imputaron {afectadas} columnas usando la mediana.",

            registros_afectados=afectadas

        )

    @staticmethod
    def fill_mode(df):

        afectadas = 0

        for columna in df.columns:

            if df[columna].isna().any():

                moda = df[columna].mode()

                if len(moda):

                    df[columna].fillna(

                        moda.iloc[0],

                        inplace=True

                    )

                    afectadas += 1

        return CleaningAction(

            nombre="Imputación por Moda",

            descripcion=f"Se imputaron {afectadas} columnas usando la moda.",

            registros_afectados=afectadas

        )

    @staticmethod
    def fill_constant(

        df,

        valor="N/A"

    ):

        total = int(

            df.isna().sum().sum()

        )

        df.fillna(

            valor,

            inplace=True

        )

        return CleaningAction(

            nombre="Imputación por Constante",

            descripcion=f"Se reemplazaron {total} valores nulos por '{valor}'.",

            registros_afectados=total

        )

    @staticmethod
    def drop_rows(df):

        antes = len(df)

        df.dropna(

            inplace=True

        )

        despues = len(df)

        eliminadas = antes - despues

        return CleaningAction(

            nombre="Eliminar Filas con Nulos",

            descripcion=f"Se eliminaron {eliminadas} filas.",

            registros_afectados=eliminadas

        )

    @staticmethod
    def drop_columns(df):

        antes = len(df.columns)

        df.dropna(

            axis=1,

            inplace=True

        )

        despues = len(df.columns)

        eliminadas = antes - despues

        return CleaningAction(

            nombre="Eliminar Columnas con Nulos",

            descripcion=f"Se eliminaron {eliminadas} columnas.",

            registros_afectados=eliminadas

        )

    @staticmethod
    def exists(df):

        return bool(

            df.isna().sum().sum()

        )

    @staticmethod
    def total(df):

        return int(

            df.isna().sum().sum()

        )