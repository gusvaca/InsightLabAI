from cleaning.models import CleaningAction


class DuplicateCleaner:

    """
    =======================================================
    Duplicate Cleaner

    Elimina registros duplicados del DataFrame.

    =======================================================
    """

    @staticmethod
    def clean(

        df,

        keep="first"

    ):

        antes = len(df)

        df.drop_duplicates(

            keep=keep,

            inplace=True

        )

        despues = len(df)

        eliminados = antes - despues

        accion = CleaningAction(

            nombre="Eliminar Duplicados",

            descripcion=(
                f"Se eliminaron "
                f"{eliminados} registros duplicados."
            ),

            registros_afectados=eliminados

        )

        return accion

    @staticmethod
    def count(

        df

    ):

        return int(

            df.duplicated().sum()

        )

    @staticmethod
    def exists(

        df

    ):

        return DuplicateCleaner.count(

            df

        ) > 0

    @staticmethod
    def duplicated_rows(

        df

    ):

        return df[

            df.duplicated(

                keep=False

            )

        ]