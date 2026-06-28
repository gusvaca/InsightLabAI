import streamlit as st


class InsightPanel:

    """
    =====================================================
    Insight Intelligence Panel

    Componente visual utilizado por toda la plataforma
    para mostrar interpretaciones inteligentes.

    =====================================================
    """

    @staticmethod
    def render(resultado):

        st.divider()

        st.subheader("🧠 Insight Intelligence")

        # ==========================================
        # RESUMEN
        # ==========================================

        if resultado.get("resumen"):

            with st.expander(

                "📖 Resumen Ejecutivo",

                expanded=True

            ):

                st.markdown(

                    resultado["resumen"]

                )

        # ==========================================
        # HISTORIA
        # ==========================================

        if resultado.get("historia"):

            with st.expander(

                "📘 Interpretación del Dataset"

            ):

                st.markdown(

                    resultado["historia"]

                )

        # ==========================================
        # NEGOCIO
        # ==========================================

        if resultado.get("negocio"):

            with st.expander(

                "💼 Interpretación de Negocio"

            ):

                for item in resultado["negocio"]:

                    st.info(item)

        # ==========================================
        # MADUREZ
        # ==========================================

        if resultado.get("madurez"):

            madurez = resultado["madurez"]

            st.success(

                f"🏆 Data Maturity Index "

                f"Nivel {madurez['nivel']} - "

                f"{madurez['nombre']}"

            )

            st.caption(

                madurez["descripcion"]

            )

        # ==========================================
        # SIGUIENTES PASOS
        # ==========================================

        if resultado.get(

            "siguientes_pasos"

        ):

            st.markdown(

                "### 🎯 Próximos pasos"

            )

            for paso in resultado[

                "siguientes_pasos"

            ]:

                st.checkbox(

                    paso["titulo"],

                    value=False,

                    disabled=True

                )