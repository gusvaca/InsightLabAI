from analytics.insights.report_model import ExecutiveReport


class MarkdownReport:

    """
    =======================================================

    Exportador Markdown

    Convierte un ExecutiveReport en un documento Markdown.

    Compatible con:

    - GitHub
    - GitLab
    - Azure DevOps
    - Documentación técnica

    =======================================================
    """

    @staticmethod
    def generate(

        report: ExecutiveReport

    ):

        md = []

        # ==================================================
        # TÍTULO
        # ==================================================

        md.append(

            f"# {report.titulo}"

        )

        md.append("")

        if report.subtitulo:

            md.append(

                report.subtitulo

            )

            md.append("")

        # ==================================================
        # INFORMACIÓN GENERAL
        # ==================================================

        md.append(

            "## Información General"

        )

        md.append("")

        md.append(

            f"- **Fecha:** {report.fecha}"

        )

        md.append(

            f"- **Score:** {report.score}"

        )

        md.append(

            f"- **Estado:** {report.estado}"

        )

        md.append(

            f"- **Data Maturity:** {report.data_maturity}"

        )

        md.append("")

        # ==================================================
        # SECCIONES
        # ==================================================

        for section in report.sections:

            md.append(

                f"## {section.titulo}"

            )

            md.append("")

            md.append(

                section.contenido

            )

            md.append("")

        # ==================================================
        # RECOMENDACIONES
        # ==================================================

        if report.recomendaciones:

            md.append(

                "## Recomendaciones"

            )

            md.append("")

            for item in report.recomendaciones:

                md.append(

                    f"- {item}"

                )

            md.append("")

        # ==================================================
        # SIGUIENTES PASOS
        # ==================================================

        if report.siguientes_pasos:

            md.append(

                "## Próximos Pasos"

            )

            md.append("")

            for paso in report.siguientes_pasos:

                md.append(

                    f"- {paso}"

                )

            md.append("")

        # ==================================================
        # PIE
        # ==================================================

        md.append("---")

        md.append("")

        md.append(

            "Reporte generado automáticamente por **InsightLab AI Enterprise**."

        )

        return "\n".join(md)

    @staticmethod
    def save(

        report: ExecutiveReport,

        output_file

    ):

        contenido = MarkdownReport.generate(

            report

        )

        with open(

            output_file,

            "w",

            encoding="utf-8"

        ) as f:

            f.write(

                contenido

            )

        return output_file