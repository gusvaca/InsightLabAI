from analytics.insights.models import InsightResult


class StoryGenerator:

    """
    ==========================================================

    STORY GENERATOR

    Construye una narrativa ejecutiva del análisis realizado.

    Su objetivo es explicar el dataset en lenguaje natural.

    ==========================================================
    """

    @staticmethod
    def generate(

        resultado: InsightResult,

        madurez=None,

        negocio=None

    ):

        historia = []

        # =====================================================
        # INTRODUCCIÓN
        # =====================================================

        historia.append(

            "Durante el análisis automático realizado por InsightLab AI se evaluó la calidad, consistencia y preparación del conjunto de datos."

        )

        historia.append("")

        historia.append(

            f"La evaluación general obtuvo una puntuación de {resultado.score}, clasificándose como '{resultado.estado}'."

        )

        historia.append("")

        # =====================================================
        # HALLAZGOS
        # =====================================================

        fortalezas = [

            i for i in resultado.insights

            if i.prioridad == "Baja"

        ]

        riesgos = [

            i for i in resultado.insights

            if i.prioridad != "Baja"

        ]

        if fortalezas:

            historia.append(

                "Principales fortalezas detectadas:"

            )

            historia.append("")

            for item in fortalezas:

                historia.append(

                    f"• {item.mensaje}"

                )

            historia.append("")

        if riesgos:

            historia.append(

                "Aspectos que requieren atención:"

            )

            historia.append("")

            for item in riesgos:

                historia.append(

                    f"• {item.mensaje}"

                )

            historia.append("")

        # =====================================================
        # VISIÓN DE NEGOCIO
        # =====================================================

        if negocio:

            historia.append(

                "Interpretación desde la perspectiva de negocio:"

            )

            historia.append("")

            for mensaje in negocio:

                historia.append(

                    f"• {mensaje}"

                )

            historia.append("")

        # =====================================================
        # MADUREZ
        # =====================================================

        if madurez:

            historia.append(

                f"El nivel de madurez del conjunto de datos corresponde a '{madurez['nombre']}'."

            )

            historia.append("")

            historia.append(

                madurez["descripcion"]

            )

            historia.append("")

        # =====================================================
        # RECOMENDACIONES
        # =====================================================

        if resultado.recomendaciones:

            historia.append(

                "Próximos pasos sugeridos:"

            )

            historia.append("")

            for r in resultado.recomendaciones:

                historia.append(

                    f"• {r}"

                )

            historia.append("")

        # =====================================================
        # CIERRE
        # =====================================================

        historia.append(

            "Las conclusiones anteriores fueron generadas automáticamente utilizando el Insight Intelligence Engine, basado en reglas expertas de calidad de datos, estadística y analítica avanzada."

        )

        return "\n".join(historia)