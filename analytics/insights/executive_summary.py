from analytics.insights.models import InsightResult


class ExecutiveSummary:

    """
    =======================================================
    Generador de Resumen Ejecutivo

    Convierte los insights generados por el motor experto
    en un lenguaje natural comprensible para usuarios de
    negocio.

    =======================================================
    """

    @staticmethod
    def generate(

        resultado: InsightResult

    ) -> str:

        texto = []

        # ==========================================
        # INTRODUCCIÓN
        # ==========================================

        texto.append(

            "Resumen Ejecutivo"

        )

        texto.append("")

        texto.append(

            f"El conjunto de datos obtuvo una "

            f"calificación de "

            f"{resultado.score} "

            f"puntos, "

            f"clasificándose como "

            f"'{resultado.estado}'."

        )

        texto.append("")

        # ==========================================
        # FORTALEZAS
        # ==========================================

        fortalezas = [

            i for i in resultado.insights

            if i.prioridad == "Baja"

        ]

        if fortalezas:

            texto.append(

                "Fortalezas identificadas:"

            )

            texto.append("")

            for insight in fortalezas:

                texto.append(

                    f"• {insight.mensaje}"

                )

            texto.append("")

        # ==========================================
        # RIESGOS
        # ==========================================

        riesgos = [

            i for i in resultado.insights

            if i.prioridad in [

                "Media",

                "Alta"

            ]

        ]

        if riesgos:

            texto.append(

                "Aspectos que requieren atención:"

            )

            texto.append("")

            for insight in riesgos:

                texto.append(

                    f"• {insight.mensaje}"

                )

            texto.append("")

        # ==========================================
        # RECOMENDACIONES
        # ==========================================

        texto.append(

            "Recomendaciones:"

        )

        texto.append("")

        for insight in resultado.insights:

            if insight.recomendacion:

                texto.append(

                    f"• {insight.recomendacion}"

                )

        texto.append("")

        # ==========================================
        # CONCLUSIÓN
        # ==========================================

        if resultado.score >= 95:

            texto.append(

                "Conclusión:"

            )

            texto.append("")

            texto.append(

                "El conjunto de datos se encuentra "

                "en excelentes condiciones para "

                "procesos analíticos y de "

                "Machine Learning."

            )

        elif resultado.score >= 80:

            texto.append(

                "Conclusión:"

            )

            texto.append("")

            texto.append(

                "El dataset puede utilizarse "

                "para análisis avanzados, aunque "

                "se recomienda atender las "

                "observaciones identificadas."

            )

        else:

            texto.append(

                "Conclusión:"

            )

            texto.append("")

            texto.append(

                "Antes de desarrollar modelos "

                "predictivos se recomienda "

                "realizar un proceso completo "

                "de preparación y limpieza "

                "del conjunto de datos."

            )

        return "\n".join(texto)