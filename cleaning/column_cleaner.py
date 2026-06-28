import re

from cleaning.models import CleaningAction


class ColumnCleaner:

    """
    ==========================================================
    Column Cleaner

    Motor encargado del tratamiento de columnas.

    Funcionalidades

    • Eliminar columnas completamente vacías
    • Eliminar columnas constantes
    • Normalizar nombres
    • Eliminar espacios
    • Detectar columnas ID
    • Estadísticas

    ==========================================================
    """

    @staticmethod
    def remove_empty_columns(df):

        antes = len(df.columns)

        df.dropna(

            axis=1,

            how="all",

            inplace=True

        )

        despues = len(df.columns)

        eliminadas = antes - despues

        return CleaningAction(

            nombre="Eliminar Columnas Vacías",

            descripcion=(
                f"Se eliminaron "
                f"{eliminadas} columnas completamente vacías."
            ),

            registros_afectados=eliminadas

        )

    @staticmethod
    def remove_constant_columns(df):

        columnas = []

        for columna in df.columns:

            if df[columna].nunique(

                dropna=False

            ) <= 1:

                columnas.append(

                    columna

                )

        if columnas:

            df.drop(

                columns=columnas,

                inplace=True

            )

        return CleaningAction(

            nombre="Eliminar Columnas Constantes",

            descripcion=(
                f"Se eliminaron "
                f"{len(columnas)} columnas constantes."
            ),

            registros_afectados=len(columnas)

        )

    @staticmethod
    def normalize_names(df):

        nuevos = []

        cambios = 0

        for columna in df.columns:

            nuevo = str(columna)

            nuevo = nuevo.strip()

            nuevo = nuevo.lower()

            nuevo = nuevo.replace(

                " ",

                "_"

            )

            nuevo = re.sub(

                r"[^a-zA-Z0-9_]",

                "",

                nuevo

            )

            if nuevo != columna:

                cambios += 1

            nuevos.append(

                nuevo

            )

        df.columns = nuevos

        return CleaningAction(

            nombre="Normalizar Nombres",

            descripcion=(
                f"Se normalizaron "
                f"{cambios} nombres de columnas."
            ),

            registros_afectados=cambios

        )

    @staticmethod
    def trim_names(df):

        nuevos = []

        cambios = 0

        for columna in df.columns:

            nombre = str(columna).strip()

            if nombre != columna:

                cambios += 1

            nuevos.append(

                nombre

            )

        df.columns = nuevos

        return CleaningAction(

            nombre="Eliminar Espacios",

            descripcion=(
                f"Se limpiaron "
                f"{cambios} nombres de columnas."
            ),

            registros_afectados=cambios

        )

    @staticmethod
    def detect_id_columns(df):

        ids = []

        for columna in df.columns:

            nombre = columna.lower()

            if nombre.endswith("id"):

                ids.append(

                    columna

                )

                continue

            if nombre.startswith("id"):

                ids.append(

                    columna

                )

                continue

            if nombre == "id":

                ids.append(

                    columna

                )

        return ids

    @staticmethod
    def statistics(df):

        vacias = []

        constantes = []

        ids = []

        for columna in df.columns:

            if df[columna].isna().all():

                vacias.append(

                    columna

                )

            if df[columna].nunique(

                dropna=False

            ) <= 1:

                constantes.append(

                    columna

                )

        ids = ColumnCleaner.detect_id_columns(

            df

        )

        return {

            "columnas": len(df.columns),

            "vacias": vacias,

            "constantes": constantes,

            "ids": ids

        }