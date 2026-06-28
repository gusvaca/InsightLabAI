from datetime import datetime

from analytics.insights.report_model import ExecutiveReport


class ReportBuilder:

    """
    =======================================================
    Constructor del Reporte Ejecutivo

    Convierte el resultado del Insight Engine en un
    ExecutiveReport.

    =======================================================
    """

    @staticmethod
    def build(

        analysis

    ):

        report = ExecutiveReport()

        resultado = analysis["resultado"]

        report.fecha = datetime.now().strftime(

            "%d/%m/%Y %H:%M"

        )

        report.score = resultado.score

        report.estado = resultado.estado

        report.data_maturity = analysis["madurez"]["nombre"]

        # ==========================================
        # RESUMEN EJECUTIVO
        # ==========================================

        report.add_section(

            "Resumen Ejecutivo",

            analysis["resumen"]

        )

        # ==========================================
        # HISTORIA DEL DATASET
        # ==========================================

        report.add_section(

            "Historia del Dataset",

            analysis["historia"]

        )

        # ==========================================
        # INTERPRETACIÓN DE NEGOCIO
        # ==========================================

        negocio = "\n".join(

            analysis["negocio"]

        )

        report.add_section(

            "Interpretación de Negocio",

            negocio

        )

        # ==========================================
        # RECOMENDACIONES
        # ==========================================

        for item in analysis[

            "resultado"

        ].recomendaciones:

            report.add_recommendation(

                item

            )

        # ==========================================
        # SIGUIENTES PASOS
        # ==========================================

        for paso in analysis[

            "siguientes_pasos"

        ]:

            report.add_next_step(

                paso["titulo"]

            )

        return report