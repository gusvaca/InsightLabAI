import streamlit as st


class InsightTimeline:

    """
    =======================================================
    Timeline del proceso analítico

    Muestra el estado de avance del dataset dentro del
    flujo de analítica de InsightLab AI.

    =======================================================
    """

    @staticmethod
    def render(

        analysis

    ):

        resultado = analysis["resultado"]

        score = resultado.score

        pasos = [

            ("📥", "Carga del Dataset"),

            ("🧹", "Calidad de Datos"),

            ("📊", "Análisis Exploratorio"),

            ("🤖", "Machine Learning"),

            ("📑", "Reporte Ejecutivo")

        ]

        estado = InsightTimeline._status(

            score

        )

        columnas = st.columns(

            len(pasos)

        )

        for i, (icono, titulo) in enumerate(

            pasos

        ):

            with columnas[i]:

                st.markdown(

                    f"""
<div style="text-align:center;padding:10px;">

<div style="font-size:34px;">

{icono}

</div>

<b>{titulo}</b>

<br><br>

<span style="color:{estado['color']};
font-weight:bold;">

{estado['texto']}

</span>

</div>
""",

                    unsafe_allow_html=True

                )

    @staticmethod
    def _status(

        score

    ):

        if score >= 95:

            return {

                "texto": "Completado",

                "color": "#16A34A"

            }

        if score >= 80:

            return {

                "texto": "En progreso",

                "color": "#D97706"

            }

        return {

            "texto": "Pendiente",

            "color": "#DC2626"

        }