from datetime import datetime


class CleaningReport:

    """
    ==========================================================
    Cleaning Report

    Genera el reporte ejecutivo del proceso de limpieza.

    ==========================================================
    """

    @staticmethod
    def generate(

        statistics,

        history

    ):

        before = statistics["before"]

        after = statistics["after"]

        improvement = statistics["improvement"]

        acciones = history.summary()

        return {

            "fecha": datetime.now(),

            "resumen": CleaningReport._summary(

                before,

                after,

                improvement

            ),

            "before": before,

            "after": after,

            "improvement": improvement,

            "actions": acciones,

            "history": history.all(),

            "recommendations": CleaningReport._recommendations(

                after

            )

        }

    @staticmethod
    def _summary(

        before,

        after,

        improvement

    ):

        return (

            f"El dataset incrementó su calidad desde "

            f"{before['quality_score']:.2f}% "

            f"hasta "

            f"{after['quality_score']:.2f}%. "

            f"Se eliminaron "

            f"{improvement['duplicates_removed']} duplicados "

            f"y se trataron "

            f"{improvement['nulls_removed']} valores nulos."

        )

    @staticmethod
    def _recommendations(

        after

    ):

        recomendaciones = []

        if after["duplicates"] > 0:

            recomendaciones.append(

                "Persisten registros duplicados."

            )

        if after["nulls"] > 0:

            recomendaciones.append(

                "Persisten valores nulos."

            )

        if after["constant_columns"] > 0:

            recomendaciones.append(

                "Persisten columnas constantes."

            )

        if after["empty_columns"] > 0:

            recomendaciones.append(

                "Persisten columnas completamente vacías."

            )

        if not recomendaciones:

            recomendaciones.append(

                "El dataset está listo para análisis y Machine Learning."

            )

        return recomendaciones