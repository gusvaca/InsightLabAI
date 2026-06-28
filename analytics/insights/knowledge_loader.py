from analytics.insights.knowledge_base import KnowledgeBase

from analytics.insights.quality_catalog import QUALITY_RULES


class KnowledgeLoader:

    """
    ================================================
    Cargador de reglas del Knowledge Base
    ================================================
    """

    @staticmethod
    def load():

        KnowledgeBase.rules.clear()

        for rule in QUALITY_RULES:

            KnowledgeBase.register(rule)