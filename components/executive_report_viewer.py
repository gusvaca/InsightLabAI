import streamlit as st

from analytics.insights.report_service import ReportService


class ExecutiveReportViewer:

    """
    ======================================================

    Visualizador del Reporte Ejecutivo

    Permite visualizar dentro de Streamlit el
    ExecutiveReport generado por el Insight Engine.

    ======================================================
    """

    @staticmethod
    def render(

        analysis

    ):

        report = ReportService.build(

            analysis

        )

        st.header("📑 Reporte Ejecutivo")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(

            "Score",

            report.score

        )

        c2.metric(

            "Estado",

            report.estado

        )

        c3.metric(

            "Data Maturity",

            report.data_maturity

        )

        c4.metric(

            "Fecha",

            report.fecha

        )

        st.divider()

        # =====================================
        # SECCIONES
        # =====================================

        for section in report.sections:

            with st.expander(

                section.titulo,

                expanded=True

            ):

                st.markdown(

                    section.contenido

                )

        # =====================================
        # RECOMENDACIONES
        # =====================================

        if report.recomendaciones:

            st.subheader(

                "✅ Recomendaciones"

            )

            for item in report.recomendaciones:

                st.success(

                    item

                )

        # =====================================
        # SIGUIENTES PASOS
        # =====================================

        if report.siguientes_pasos:

            st.subheader(

                "🎯 Próximos Pasos"

            )

            for paso in report.siguientes_pasos:

                st.checkbox(

                    paso,

                    value=False,

                    disabled=True

                )

        st.divider()

        # =====================================
        # EXPORTACIÓN
        # =====================================

        st.subheader(

            "📥 Exportar Reporte"

        )

        col1, col2 = st.columns(2)

        html = ReportService.export_html(

            analysis

        )

        col1.download_button(

            "🌐 HTML",

            html,

            "Executive_Report.html",

            "text/html"

        )

        md = ReportService.export_markdown(

            analysis

        )

        col2.download_button(

            "📝 Markdown",

            md,

            "Executive_Report.md",

            "text/markdown"

        )