import streamlit as st


class InsightDecisionPanel:

    """
    =======================================================

    Decision Panel

    Presenta las decisiones propuestas por el
    Decision Engine organizadas por prioridad.

    =======================================================
    """

    @staticmethod
    def render(

        analysis

    ):

        pasos = analysis.get(

            "siguientes_pasos",

            []

        )

        st.subheader(

            "🧭 Decision Center"

        )

        if not pasos:

            st.success(

                "No existen decisiones pendientes."

            )

            return

        pendientes = []
        recomendados = []
        muy_recomendados = []

        for paso in pasos:

            estado = paso.get(

                "estado",

                ""

            ).lower()

            if estado == "pendiente":

                pendientes.append(

                    paso

                )

            elif estado == "recomendado":

                recomendados.append(

                    paso

                )

            elif estado == "muy recomendado":

                muy_recomendados.append(

                    paso

                )

        c1, c2, c3 = st.columns(3)

        with c1:

            st.metric(

                "Pendientes",

                len(

                    pendientes

                )

            )

        with c2:

            st.metric(

                "Recomendados",

                len(

                    recomendados

                )

            )

        with c3:

            st.metric(

                "Muy Recomendados",

                len(

                    muy_recomendados

                )

            )

        st.divider()

        InsightDecisionPanel._render_section(

            "🔴 Acciones Pendientes",

            pendientes,

            "error"

        )

        InsightDecisionPanel._render_section(

            "🟡 Acciones Recomendadas",

            recomendados,

            "warning"

        )

        InsightDecisionPanel._render_section(

            "🟢 Acciones Muy Recomendadas",

            muy_recomendados,

            "success"

        )

    @staticmethod
    def _render_section(

        titulo,

        acciones,

        tipo

    ):

        if not acciones:

            return

        st.markdown(

            f"### {titulo}"

        )

        for accion in acciones:

            texto = f"""
**{accion['titulo']}**

Estado: **{accion['estado']}**
"""

            if tipo == "error":

                st.error(

                    texto

                )

            elif tipo == "warning":

                st.warning(

                    texto

                )

            else:

                st.success(

                    texto

                )