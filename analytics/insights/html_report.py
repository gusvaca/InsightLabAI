from analytics.insights.report_model import ExecutiveReport


class HTMLReport:

    """
    ==========================================================
    Generador de Reportes HTML

    Convierte un ExecutiveReport en un documento HTML.

    ==========================================================
    """

    @staticmethod
    def generate(

        report: ExecutiveReport

    ):

        html = f"""

<!DOCTYPE html>

<html lang="es">

<head>

<meta charset="UTF-8">

<title>{report.titulo}</title>

<style>

body{{
font-family:Arial;
margin:40px;
background:#F8FAFC;
color:#1E293B;
}}

h1{{
color:#1E3A8A;
}}

h2{{
border-bottom:2px solid #E2E8F0;
padding-bottom:6px;
margin-top:30px;
}}

.card{{
background:white;
padding:20px;
border-radius:12px;
margin-bottom:20px;
box-shadow:0 2px 8px rgba(0,0,0,.08);
}}

.metric{{
display:inline-block;
margin-right:40px;
font-size:18px;
font-weight:bold;
}}

ul{{
padding-left:25px;
}}

</style>

</head>

<body>

<h1>{report.titulo}</h1>

<h3>{report.subtitulo}</h3>

<div class="card">

<div class="metric">

Score<br>
{report.score}

</div>

<div class="metric">

Estado<br>
{report.estado}

</div>

<div class="metric">

Madurez<br>
{report.data_maturity}

</div>

<div class="metric">

Fecha<br>
{report.fecha}

</div>

</div>

"""

        for section in report.sections:

            html += f"""

<div class="card">

<h2>{section.titulo}</h2>

<p>

{section.contenido.replace(chr(10),"<br>")}

</p>

</div>

"""

        if report.recomendaciones:

            html += """

<div class="card">

<h2>Recomendaciones</h2>

<ul>

"""

            for r in report.recomendaciones:

                html += f"<li>{r}</li>"

            html += """

</ul>

</div>

"""

        if report.siguientes_pasos:

            html += """

<div class="card">

<h2>Próximos pasos</h2>

<ul>

"""

            for paso in report.siguientes_pasos:

                html += f"<li>{paso}</li>"

            html += """

</ul>

</div>

"""

        html += """

</body>

</html>

"""

        return html