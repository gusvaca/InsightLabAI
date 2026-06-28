from analytics.insights.engine import InsightEngine


class InsightFacade:

    """
    Fachada principal del Insight Intelligence Engine.
    """

    @staticmethod
    def quality(resumen):

        return InsightEngine.quality(resumen)   