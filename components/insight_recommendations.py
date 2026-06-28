import streamlit as st


class InsightRecommendations:

    """
    =======================================================
    Recomendaciones Inteligentes

    Visualiza las recomendaciones generadas por el
    Insight Intelligence Engine.

    =======================================================
    """

    @staticmethod
    def render(

        analysis

    ):

        resultado = analysis["resultado"]

        recomendaciones = resultado.recomendaciones

        if not recomendaciones:

            st.success(

                "No existen recomendaciones pendientes."

            )

            return

        st.subheader(

            "💡 Recomendaciones Inteligentes"

        )

        for i, recomendacion in enumerate(

            recomendaciones,

            start=1

        ):

            st.markdown(

                f"""
<div style="
padding:16px;
margin-bottom:12px;
border-left:6px solid #2563EB;
background:#F8FAFC;
border-radius:8px;
">

<b>Recomendación {i}</b>

<br><br>

{recomendacion}

</div>
""",

                unsafe_allow_html=True

            )