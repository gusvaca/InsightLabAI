from reportlab.lib import colors

from reportlab.lib.styles import getSampleStyleSheet

from reportlab.platypus import (

    SimpleDocTemplate,

    Paragraph,

    Spacer,

    Table,

    TableStyle

)


class PDFReport:

    """
    =======================================================
    Exportador PDF

    Genera un reporte ejecutivo en PDF a partir de un
    ExecutiveReport.

    =======================================================
    """

    @staticmethod
    def generate(

        report,

        output_file

    ):

        doc = SimpleDocTemplate(

            output_file

        )

        styles = getSampleStyleSheet()

        story = []

        # ==========================================
        # TÍTULO
        # ==========================================

        story.append(

            Paragraph(

                report.titulo,

                styles["Title"]

            )

        )

        story.append(

            Paragraph(

                report.subtitulo,

                styles["Heading2"]

            )

        )

        story.append(

            Spacer(

                1,

                20

            )

        )

        # ==========================================
        # INFORMACIÓN GENERAL
        # ==========================================

        table = Table(

            [

                [

                    "Score",

                    report.score

                ],

                [

                    "Estado",

                    report.estado

                ],

                [

                    "Data Maturity",

                    report.data_maturity

                ],

                [

                    "Fecha",

                    report.fecha

                ]

            ],

            colWidths=[140,320]

        )

        table.setStyle(

            TableStyle(

                [

                    (

                        "BACKGROUND",

                        (0,0),

                        (0,-1),

                        colors.HexColor("#2563EB")

                    ),

                    (

                        "TEXTCOLOR",

                        (0,0),

                        (0,-1),

                        colors.white

                    ),

                    (

                        "GRID",

                        (0,0),

                        (-1,-1),

                        0.5,

                        colors.grey

                    ),

                    (

                        "BOTTOMPADDING",

                        (0,0),

                        (-1,-1),

                        8

                    )

                ]

            )

        )

        story.append(

            table

        )

        story.append(

            Spacer(

                1,

                20

            )

        )

        # ==========================================
        # SECCIONES
        # ==========================================

        for section in report.sections:

            story.append(

                Paragraph(

                    section.titulo,

                    styles["Heading2"]

                )

            )

            story.append(

                Paragraph(

                    section.contenido.replace(

                        "\n",

                        "<br/>"

                    ),

                    styles["BodyText"]

                )

            )

            story.append(

                Spacer(

                    1,

                    12

                )

            )

        # ==========================================
        # RECOMENDACIONES
        # ==========================================

        if report.recomendaciones:

            story.append(

                Paragraph(

                    "Recomendaciones",

                    styles["Heading2"]

                )

            )

            for r in report.recomendaciones:

                story.append(

                    Paragraph(

                        f"• {r}",

                        styles["BodyText"]

                    )

                )

            story.append(

                Spacer(

                    1,

                    15

                )

            )

        # ==========================================
        # PRÓXIMOS PASOS
        # ==========================================

        if report.siguientes_pasos:

            story.append(

                Paragraph(

                    "Próximos pasos",

                    styles["Heading2"]

                )

            )

            for paso in report.siguientes_pasos:

                story.append(

                    Paragraph(

                        f"• {paso}",

                        styles["BodyText"]

                    )

                )

        doc.build(

            story

        )

        return output_file