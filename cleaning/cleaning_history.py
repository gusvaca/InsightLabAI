from datetime import datetime


class CleaningHistory:

    """
    ==========================================================

    Cleaning History

    Registro histórico de todas las acciones ejecutadas
    durante el proceso de limpieza.

    ==========================================================
    """

    def __init__(self):

        self._history = []

    def add(

        self,

        action

    ):

        self._history.append(

            {

                "fecha": datetime.now(),

                "nombre": action.nombre,

                "descripcion": action.descripcion,

                "registros": action.registros_afectados,

                "estado": action.estado

            }

        )

    def all(self):

        return self._history

    def total(self):

        return len(

            self._history

        )

    def clear(self):

        self._history.clear()

    def last(self):

        if not self._history:

            return None

        return self._history[-1]

    def to_dataframe(self):

        try:

            import pandas as pd

            return pd.DataFrame(

                self._history

            )

        except Exception:

            return None

    def summary(self):

        registros = sum(

            item["registros"]

            for item in self._history

        )

        return {

            "acciones": len(

                self._history

            ),

            "registros_afectados": registros

        }

    def __len__(self):

        return len(

            self._history

        )

    def __iter__(self):

        return iter(

            self._history

        )