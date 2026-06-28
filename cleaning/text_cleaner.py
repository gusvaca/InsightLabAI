import re
import unicodedata

from cleaning.models import CleaningAction


class TextCleaner:

    """
    ==========================================================
    Text Cleaner

    Motor especializado en limpieza de texto.

    Funcionalidades

    • Eliminar espacios
    • Eliminar múltiples espacios
    • Convertir a minúsculas
    • Convertir a mayúsculas
    • Eliminar acentos
    • Eliminar caracteres especiales
    • Eliminar tabulaciones
    • Eliminar saltos de línea
    • Limpiar HTML
    • Limpiar URLs
    • Limpiar correos electrónicos

    ==========================================================
    """

    @staticmethod
    def trim(df):

        columnas = df.select_dtypes(

            include="object"

        ).columns

        afectadas = 0

        for columna in columnas:

            df[columna] = (

                df[columna]

                .astype(str)

                .str.strip()

            )

            afectadas += 1

        return CleaningAction(

            nombre="Eliminar Espacios",

            descripcion=(
                f"Se limpiaron "
                f"{afectadas} columnas."
            ),

            registros_afectados=afectadas

        )

    @staticmethod
    def normalize_spaces(df):

        columnas = df.select_dtypes(

            include="object"

        ).columns

        afectadas = 0

        for columna in columnas:

            df[columna] = (

                df[columna]

                .astype(str)

                .str.replace(

                    r"\s+",

                    " ",

                    regex=True

                )

            )

            afectadas += 1

        return CleaningAction(

            nombre="Normalizar Espacios",

            descripcion=(
                f"Se normalizaron "
                f"{afectadas} columnas."
            ),

            registros_afectados=afectadas

        )

    @staticmethod
    def lower(df):

        columnas = df.select_dtypes(

            include="object"

        ).columns

        afectadas = 0

        for columna in columnas:

            df[columna] = (

                df[columna]

                .astype(str)

                .str.lower()

            )

            afectadas += 1

        return CleaningAction(

            nombre="Convertir a Minúsculas",

            descripcion=(
                f"Se transformaron "
                f"{afectadas} columnas."
            ),

            registros_afectados=afectadas

        )

    @staticmethod
    def upper(df):

        columnas = df.select_dtypes(

            include="object"

        ).columns

        afectadas = 0

        for columna in columnas:

            df[columna] = (

                df[columna]

                .astype(str)

                .str.upper()

            )

            afectadas += 1

        return CleaningAction(

            nombre="Convertir a Mayúsculas",

            descripcion=(
                f"Se transformaron "
                f"{afectadas} columnas."
            ),

            registros_afectados=afectadas

        )

    @staticmethod
    def remove_accents(df):

        columnas = df.select_dtypes(

            include="object"

        ).columns

        afectadas = 0

        for columna in columnas:

            df[columna] = (

                df[columna]

                .astype(str)

                .apply(

                    TextCleaner._strip_accents

                )

            )

            afectadas += 1

        return CleaningAction(

            nombre="Eliminar Acentos",

            descripcion=(
                f"Se procesaron "
                f"{afectadas} columnas."
            ),

            registros_afectados=afectadas

        )

    @staticmethod
    def remove_special_characters(df):

        columnas = df.select_dtypes(

            include="object"

        ).columns

        afectadas = 0

        for columna in columnas:

            df[columna] = (

                df[columna]

                .astype(str)

                .str.replace(

                    r"[^A-Za-z0-9\s]",

                    "",

                    regex=True

                )

            )

            afectadas += 1

        return CleaningAction(

            nombre="Eliminar Caracteres Especiales",

            descripcion=(
                f"Se procesaron "
                f"{afectadas} columnas."
            ),

            registros_afectados=afectadas

        )

    @staticmethod
    def remove_html(df):

        columnas = df.select_dtypes(

            include="object"

        ).columns

        patron = re.compile(r"<.*?>")

        afectadas = 0

        for columna in columnas:

            df[columna] = (

                df[columna]

                .astype(str)

                .apply(

                    lambda x:

                    re.sub(

                        patron,

                        "",

                        x

                    )

                )

            )

            afectadas += 1

        return CleaningAction(

            nombre="Eliminar HTML",

            descripcion=(
                f"Se limpiaron "
                f"{afectadas} columnas."
            ),

            registros_afectados=afectadas

        )

    @staticmethod
    def remove_urls(df):

        columnas = df.select_dtypes(

            include="object"

        ).columns

        patron = re.compile(

            r"https?://\S+|www\.\S+"

        )

        afectadas = 0

        for columna in columnas:

            df[columna] = (

                df[columna]

                .astype(str)

                .apply(

                    lambda x:

                    re.sub(

                        patron,

                        "",

                        x

                    )

                )

            )

            afectadas += 1

        return CleaningAction(

            nombre="Eliminar URLs",

            descripcion=(
                f"Se limpiaron "
                f"{afectadas} columnas."
            ),

            registros_afectados=afectadas

        )

    @staticmethod
    def remove_emails(df):

        columnas = df.select_dtypes(

            include="object"

        ).columns

        patron = re.compile(

            r"\S+@\S+\.\S+"

        )

        afectadas = 0

        for columna in columnas:

            df[columna] = (

                df[columna]

                .astype(str)

                .apply(

                    lambda x:

                    re.sub(

                        patron,

                        "",

                        x

                    )

                )

            )

            afectadas += 1

        return CleaningAction(

            nombre="Eliminar Correos",

            descripcion=(
                f"Se limpiaron "
                f"{afectadas} columnas."
            ),

            registros_afectados=afectadas

        )

    @staticmethod
    def _strip_accents(texto):

        texto = unicodedata.normalize(

            "NFKD",

            texto

        )

        return "".join(

            c

            for c in texto

            if not unicodedata.combining(c)

        )