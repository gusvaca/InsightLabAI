import streamlit as st


class InsightHealthPanel:

    """
    =======================================================

    Dataset Health Panel

    Presenta un diagnóstico ejecutivo del estado
    general del conjunto de datos.

    =======================================================
    """

    @staticmethod
    def render(

        analysis

    ):

        resultado = analysis["resultado"]

        score = resultado.score

        estado = resultado.estado

        madurez = analysis["madurez"]

        salud = InsightHealthPanel._health(score)

        color = InsightHealthPanel._color(score)

        st.subheader(

            "🩺 Dataset Health"

        )

        st.markdown(

            f"""
<div style="
background:{color};
padding:22px;
border-radius:12px;
color:white;
margin-bottom:20px;
">

<h2 style="margin:0;">

{salud}

</h2>

<p style="margin-top:12px;font-size:17px;">

Estado: <b>{estado}</b>

<br>

Score: <b>{score:.1f}/100</b>

<br>

Nivel de Madurez:
<b>{madurez["nombre"]}</b>

</p>

</div>
""",

            unsafe_allow_html=True

        )

        c1, c2 = st.columns(2)

        with c1:

            st.markdown(

                "### ✔ Fortalezas"

            )

            fortalezas = [

                i

                for i in resultado.insights

                if i.prioridad.lower() == "baja"

            ]

            if fortalezas:

                for item in fortalezas:

                    st.success(

                        item.mensaje

                    )

            else:

                st.info(

                    "No existen fortalezas registradas."

                )

        with c2:

            st.markdown(

                "### ⚠ Aspectos a Mejorar"

            )

            mejoras = [

                i

                for i in resultado.insights

                if i.prioridad.lower() != "baja"

            ]

            if mejoras:

                for item in mejoras:

                    st.warning(

                        item.mensaje

                    )

            else:

                st.success(

                    "No se identificaron observaciones."

                )

    @staticmethod
    def _health(

        score

    ):

        if score >= 95:

            return "Excelente"

        elif score >= 85:

            return "Muy Buena"

        elif score >= 70:

            return "Buena"

        elif score >= 50:

            return "Regular"

        return "Crítica"

    @staticmethod
    def _color(

        score

    ):

        if score >= 95:

            return "#16A34A"

        elif score >= 85:

            return "#2563EB"

        elif score >= 70:

            return "#D97706"

        return "#DC2626"