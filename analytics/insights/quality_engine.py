from analytics.insights.models import (

    Insight,

    InsightResult

)

from analytics.insights.knowledge_base import (

    KnowledgeBase

)

from analytics.insights.knowledge_loader import (

    KnowledgeLoader

)


class QualityEngine:

    """
    =====================================================

    Motor de interpretación de Calidad.

    Evalúa el Knowledge Base y genera un
    InsightResult.

    =====================================================
    """

    _loaded = False

    @classmethod
    def initialize(cls):

        if not cls._loaded:

            KnowledgeLoader.load()

            cls._loaded = True

    @classmethod
    def analyze(

        cls,

        resumen

    ) -> InsightResult:

        cls.initialize()

        resultado = InsightResult()

        resultado.score = resumen.get(

            "score",

            0

        )

        resultado.estado = resumen.get(

            "estado",

            "Desconocido"

        )

        reglas = KnowledgeBase.evaluate(

            resumen

        )

        for regla in reglas:

            insight = Insight(

                titulo=regla.nombre,

                categoria=regla.categoria,

                prioridad=regla.prioridad,

                icono="💡",

                mensaje=regla.mensaje,

                recomendacion=regla.recomendacion,

                impacto=regla.impacto

            )

            resultado.agregar(

                insight

            )

        resultado.resumen = (

            f"Se evaluaron "

            f"{len(reglas)} "

            f"reglas del Knowledge Base."

        )

        return resultado