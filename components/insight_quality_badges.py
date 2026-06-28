import streamlit as st


class InsightQualityBadges:

    """
    =======================================================
    Quality Badges

    Muestra insignias ejecutivas sobre el estado
    del conjunto de datos.

    =======================================================
    """

    @staticmethod
    def render(

        analysis

    ):

        resultado = analysis["resultado"]

        score = resultado.score

        insights = resultado.insights

        badges = []

        # ==========================================
        # SCORE
        # ==========================================

        if score >= 95:

            badges.append(

                ("🟢", "Dataset Certificado")

            )

        elif score >= 80:

            badges.append(

                ("🟡", "Dataset Aprobado")

            )

        else:

            badges.append(

                ("🔴", "Requiere Preparación")

            )

        # ==========================================
        # DUPLICADOS
        # ==========================================

        if any(

            "duplicado" in i.mensaje.lower()

            and "no" in i.mensaje.lower()

            for i in insights

        ):

            badges.append(

                ("🟢", "Sin Duplicados")

            )

        else:

            badges.append(

                ("🟠", "Duplicados Detectados")

            )

        # ==========================================
        # NULOS
        # ==========================================

        if any(

            "no existen valores nulos" in i.mensaje.lower()

            or "no existen valores faltantes" in i.mensaje.lower()

            for i in insights

        ):

            badges.append(

                ("🟢", "Sin Valores Nulos")

            )

        else:

            badges.append(

                ("🟡", "Revisar Valores Nulos")

            )

        # ==========================================
        # MADUREZ
        # ==========================================

        madurez = analysis["madurez"]

        if madurez["nivel"] >= 4:

            badges.append(

                ("🤖", "Listo para Machine Learning")

            )

        if madurez["nivel"] == 5:

            badges.append(

                ("🚀", "Listo para Producción")

            )

        # ==========================================
        # VISUALIZACIÓN
        # ==========================================

        st.subheader(

            "🏅 Quality Badges"

        )

        cols = st.columns(

            min(

                len(badges),

                4

            )

        )

        for idx, badge in enumerate(

            badges

        ):

            col = cols[

                idx % len(cols)

            ]

            with col:

                st.success(

                    f"{badge[0]} {badge[1]}"

                )