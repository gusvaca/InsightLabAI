import numpy as np
import pandas as pd

from cleaning.models import CleaningAction


class OutlierCleaner:

    """
    ==========================================================
    Outlier Cleaner

    Motor encargado del tratamiento de valores atípicos.

    Funcionalidades

    • Detección mediante IQR
    • Detección mediante Z-Score
    • Eliminación de outliers
    • Winsorización
    • Reemplazo por mediana
    • Estadísticas

    ==========================================================
    """

    @staticmethod
    def detect_iqr(df):

        resultado = {}

        columnas = df.select_dtypes(

            include="number"

        ).columns

        for columna in columnas:

            q1 = df[columna].quantile(0.25)

            q3 = df[columna].quantile(0.75)

            iqr = q3 - q1

            inferior = q1 - 1.5 * iqr

            superior = q3 + 1.5 * iqr

            mascara = (

                (df[columna] < inferior)

                |

                (df[columna] > superior)

            )

            resultado[columna] = int(

                mascara.sum()

            )

        return resultado

    @staticmethod
    def detect_zscore(

        df,

        threshold=3

    ):

        resultado = {}

        columnas = df.select_dtypes(

            include="number"

        ).columns

        for columna in columnas:

            serie = df[columna]

            std = serie.std()

            if std == 0:

                resultado[columna] = 0

                continue

            z = (

                serie - serie.mean()

            ) / std

            resultado[columna] = int(

                (np.abs(z) > threshold).sum()

            )

        return resultado

    @staticmethod
    def remove_iqr(df):

        antes = len(df)

        columnas = df.select_dtypes(

            include="number"

        ).columns

        mascara = pd.Series(

            True,

            index=df.index

        )

        for columna in columnas:

            q1 = df[columna].quantile(0.25)

            q3 = df[columna].quantile(0.75)

            iqr = q3 - q1

            inferior = q1 - 1.5 * iqr

            superior = q3 + 1.5 * iqr

            mascara &= (

                (df[columna] >= inferior)

                &

                (df[columna] <= superior)

            )

        df.drop(

            df.index[~mascara],

            inplace=True

        )

        eliminados = antes - len(df)

        return CleaningAction(

            nombre="Eliminar Outliers (IQR)",

            descripcion=(
                f"Se eliminaron "
                f"{eliminados} registros."
            ),

            registros_afectados=eliminados

        )

    @staticmethod
    def winsorize(df):

        columnas = df.select_dtypes(

            include="number"

        ).columns

        afectadas = 0

        for columna in columnas:

            q1 = df[columna].quantile(0.25)

            q3 = df[columna].quantile(0.75)

            iqr = q3 - q1

            inferior = q1 - 1.5 * iqr

            superior = q3 + 1.5 * iqr

            df[columna] = df[columna].clip(

                inferior,

                superior

            )

            afectadas += 1

        return CleaningAction(

            nombre="Winsorización",

            descripcion=(
                f"Se aplicó winsorización "
                f"a {afectadas} columnas."
            ),

            registros_afectados=afectadas

        )

    @staticmethod
    def replace_by_median(df):

        columnas = df.select_dtypes(

            include="number"

        ).columns

        afectadas = 0

        for columna in columnas:

            q1 = df[columna].quantile(0.25)

            q3 = df[columna].quantile(0.75)

            iqr = q3 - q1

            inferior = q1 - 1.5 * iqr

            superior = q3 + 1.5 * iqr

            mediana = df[columna].median()

            mascara = (

                (df[columna] < inferior)

                |

                (df[columna] > superior)

            )

            cantidad = int(

                mascara.sum()

            )

            if cantidad:

                df.loc[

                    mascara,

                    columna

                ] = mediana

                afectadas += cantidad

        return CleaningAction(

            nombre="Reemplazar Outliers",

            descripcion=(
                f"Se reemplazaron "
                f"{afectadas} valores "
                f"por la mediana."
            ),

            registros_afectados=afectadas

        )

    @staticmethod
    def statistics(df):

        return {

            "iqr": OutlierCleaner.detect_iqr(

                df

            ),

            "zscore": OutlierCleaner.detect_zscore(

                df

            )

        }