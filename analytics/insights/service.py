from analytics.quality import DataQuality

from analytics.insights.facade import InsightFacade


class InsightService:

    """
    ======================================================

    Servicio principal del Insight Intelligence Engine.

    Convierte un DataFrame en un análisis inteligente.

    Todas las páginas deberán consumir este servicio.

    ======================================================
    """

    @staticmethod
    def analyze_dataset(df):

        resumen = DataQuality.resumen(df)

        return InsightFacade.quality(

            resumen

        )

    @staticmethod
    def analyze_quality(df):

        resumen = DataQuality.resumen(df)

        return InsightFacade.quality(

            resumen

        )