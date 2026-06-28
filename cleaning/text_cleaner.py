import re
import unicodedata
import pandas as pd

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
    def _text_columns(df):
        """Obtiene todas las columnas de texto compatibles con Pandas 2.x"""
        return df.select_dtypes(include=["object", "string"]).columns

    @staticmethod
    def trim(df):

        columnas = TextCleaner._text_columns(df)

        afectadas = 0

        for columna in columnas:

            df[columna] = (
                df[columna]
                .astype("string")
                .str.strip()
            )

            afectadas += 1

        return CleaningAction(
            nombre="Eliminar Espacios",
            descripcion=f"Se limpiaron {afectadas} columnas.",
            registros_afectados=afectadas
        )

    @staticmethod
    def normalize_spaces(df):

        columnas = TextCleaner._text_columns(df)

        afectadas = 0

        for columna in columnas:

            df[columna] = (
                df[columna]
                .astype("string")
                .str.replace(
                    r"\s+",
                    " ",
                    regex=True
                )
            )

            afectadas += 1

        return CleaningAction(
            nombre="Normalizar Espacios",
            descripcion=f"Se normalizaron {afectadas} columnas.",
            registros_afectados=afectadas
        )

    @staticmethod
    def lower(df):

        columnas = TextCleaner._text_columns(df)

        afectadas = 0

        for columna in columnas:

            df[columna] = (
                df[columna]
                .astype("string")
                .str.lower()
            )

            afectadas += 1

        return CleaningAction(
            nombre="Convertir a Minúsculas",
            descripcion=f"Se transformaron {afectadas} columnas.",
            registros_afectados=afectadas
        )

    @staticmethod
    def upper(df):

        columnas = TextCleaner._text_columns(df)

        afectadas = 0

        for columna in columnas:

            df[columna] = (
                df[columna]
                .astype("string")
                .str.upper()
            )

            afectadas += 1

        return CleaningAction(
            nombre="Convertir a Mayúsculas",
            descripcion=f"Se transformaron {afectadas} columnas.",
            registros_afectados=afectadas
        )

    @staticmethod
    def remove_accents(df):

        columnas = TextCleaner._text_columns(df)

        afectadas = 0

        for columna in columnas:

            df[columna] = df[columna].apply(
                TextCleaner._strip_accents
            )

            afectadas += 1

        return CleaningAction(
            nombre="Eliminar Acentos",
            descripcion=f"Se procesaron {afectadas} columnas.",
            registros_afectados=afectadas
        )

    @staticmethod
    def remove_special_characters(df):

        columnas = TextCleaner._text_columns(df)

        afectadas = 0

        for columna in columnas:

            df[columna] = (
                df[columna]
                .astype("string")
                .str.replace(
                    r"[^A-Za-z0-9\s]",
                    "",
                    regex=True
                )
            )

            afectadas += 1

        return CleaningAction(
            nombre="Eliminar Caracteres Especiales",
            descripcion=f"Se procesaron {afectadas} columnas.",
            registros_afectados=afectadas
        )

    @staticmethod
    def remove_html(df):

        columnas = TextCleaner._text_columns(df)

        patron = re.compile(r"<.*?>")

        afectadas = 0

        for columna in columnas:

            df[columna] = df[columna].apply(
                lambda x: re.sub(
                    patron,
                    "",
                    "" if pd.isna(x) else str(x)
                )
            )

            afectadas += 1

        return CleaningAction(
            nombre="Eliminar HTML",
            descripcion=f"Se limpiaron {afectadas} columnas.",
            registros_afectados=afectadas
        )

    @staticmethod
    def remove_urls(df):

        columnas = TextCleaner._text_columns(df)

        patron = re.compile(
            r"https?://\S+|www\.\S+"
        )

        afectadas = 0

        for columna in columnas:

            df[columna] = df[columna].apply(
                lambda x: re.sub(
                    patron,
                    "",
                    "" if pd.isna(x) else str(x)
                )
            )

            afectadas += 1

        return CleaningAction(
            nombre="Eliminar URLs",
            descripcion=f"Se limpiaron {afectadas} columnas.",
            registros_afectados=afectadas
        )

    @staticmethod
    def remove_emails(df):

        columnas = TextCleaner._text_columns(df)

        patron = re.compile(
            r"\S+@\S+\.\S+"
        )

        afectadas = 0

        for columna in columnas:

            df[columna] = df[columna].apply(
                lambda x: re.sub(
                    patron,
                    "",
                    "" if pd.isna(x) else str(x)
                )
            )

            afectadas += 1

        return CleaningAction(
            nombre="Eliminar Correos",
            descripcion=f"Se limpiaron {afectadas} columnas.",
            registros_afectados=afectadas
        )

    @staticmethod
    def _strip_accents(texto):

        if pd.isna(texto):
            return texto

        texto = str(texto)

        texto = unicodedata.normalize(
            "NFKD",
            texto
        )

        return "".join(
            c
            for c in texto
            if not unicodedata.combining(c)
        )