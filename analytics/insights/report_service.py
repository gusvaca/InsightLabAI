from analytics.insights.report_builder import ReportBuilder

from analytics.insights.html_report import HTMLReport

from analytics.insights.pdf_report import PDFReport

from analytics.insights.word_report import WordReport

from analytics.insights.markdown_report import MarkdownReport


class ReportService:

    """
    ==========================================================
    Servicio central de generación de reportes.

    Unifica todos los formatos soportados por InsightLab AI.

    ==========================================================
    """

    @staticmethod
    def build(

        analysis

    ):

        return ReportBuilder.build(

            analysis

        )

    @staticmethod
    def export_html(

        analysis

    ):

        report = ReportBuilder.build(

            analysis

        )

        return HTMLReport.generate(

            report

        )

    @staticmethod
    def export_pdf(

        analysis,

        output_file

    ):

        report = ReportBuilder.build(

            analysis

        )

        return PDFReport.generate(

            report,

            output_file

        )

    @staticmethod
    def export_word(

        analysis,

        output_file

    ):

        report = ReportBuilder.build(

            analysis

        )

        return WordReport.generate(

            report,

            output_file

        )

    @staticmethod
    def export_markdown(

        analysis

    ):

        report = ReportBuilder.build(

            analysis

        )

        return MarkdownReport.generate(

            report
        )

    @staticmethod
    def save_markdown(

        analysis,

        output_file

    ):

        report = ReportBuilder.build(

            analysis

        )

        return MarkdownReport.save(

            report,

            output_file

        )