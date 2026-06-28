import streamlit as st

from core.session import existe_dataset


# =====================================================
# CARGAR CSS GLOBAL
# =====================================================

def cargar_css():

    try:

        with open(

            "style.css",

            "r",

            encoding="utf-8"

        ) as f:

            st.markdown(

                f"<style>{f.read()}</style>",

                unsafe_allow_html=True

            )

    except FileNotFoundError:

        pass


# =====================================================
# SIDEBAR
# =====================================================

def sidebar():

    cargar_css()

    with st.sidebar:

        st.image(

            "https://img.icons8.com/color/96/combo-chart--v1.png",

            width=50

        )

        st.markdown(

            """
# InsightLab AI
"""
        )

        st.caption(

            "Enterprise Edition"

        )

        st.divider()

        if existe_dataset():

            st.success(

                "🟢 Dataset cargado"

            )

        else:

            st.error(

                "🔴 Sin Dataset"

            )

        st.divider()

        st.markdown(

            "## Navegación"

        )

        st.page_link(

            "app.py",

            label="🏠 Inicio"

        )

        st.page_link(

            "pages/Carga_Dataset.py",

            label="📂 Carga"

        )

        st.page_link(

            "pages/Dashboard.py",

            label="📊 Dashboard"

        )

        st.page_link(

            "pages/Perfil_Dataset.py",

            label="📋 Perfil"

        )

        st.page_link(

            "pages/Calidad.py",

            label="🩺 Calidad"

        )

        st.page_link(

            "pages/Hallazgos.py",

            label="🧠 Hallazgos"

        )

        st.page_link(

            "pages/Estadísticas.py",

            label="📈 Estadísticas"

        )

        st.page_link(

            "pages/EDA.py",

            label="📊 EDA"

        )
        st.page_link(

    "pages/Cluster_Intelligence.py",

    label="🎯 Cluster Intelligence"

)

        st.page_link(

    "pages/Descubrimientos.py",

    label="💡 Descubrimientos"

)

        st.page_link(

            "pages/Explorador.py",

            label="📈 Explorador"

        )
        st.page_link(

            "pages/Machine_Learning.py",

            label="🤖 Machine Learning"

        )

        st.page_link(
          "pages/Data_Cleaning.py",

            label="🧹 Limpieza de Datos"

        )
        st.page_link(

            "pages/Reportes.py",

            label="📄 Reportes"

        )
        

        st.divider()

        st.caption(

            "InsightLab AI • Enterprise Edition • v1.0"

        )