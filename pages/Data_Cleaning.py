import streamlit as st
import pandas as pd

from components.layout import Layout

from cleaning.service import CleaningService


Layout.render(

    "🧹 Data Cleaning Center"

)

st.write(

    "Centro inteligente para la preparación y limpieza de datos."

)

# ==========================================================
# DATASET
# ==========================================================

if "df" not in st.session_state:

    st.warning(

        "Primero cargue un conjunto de datos."

    )

    st.stop()

df = st.session_state["df"]

# ==========================================================
# INFORMACIÓN GENERAL
# ==========================================================

st.subheader(

    "📊 Dataset"

)

c1, c2, c3, c4 = st.columns(4)

c1.metric(

    "Registros",

    len(df)

)

c2.metric(

    "Columnas",

    len(df.columns)

)

c3.metric(

    "Duplicados",

    int(

        df.duplicated().sum()

    )

)

c4.metric(

    "Nulos",

    int(

        df.isna().sum().sum()

    )

)

st.divider()

# ==========================================================
# PREVIEW
# ==========================================================

st.subheader(

    "Vista previa"

)

st.dataframe(

    df,

    use_container_width=True,

    height=350

)

st.divider()

# ==========================================================
# AUTO CLEAN
# ==========================================================

st.subheader(

    "✨ Limpieza Inteligente"

)

st.write(

    "Ejecuta automáticamente el pipeline completo de limpieza."

)

if st.button(

    "🚀 Ejecutar Auto Clean",

    use_container_width=True,

    type="primary"

):

    with st.spinner(

        "Limpiando dataset..."

    ):

        resultado = CleaningService.auto_clean(

            df

        )

    st.session_state["clean_df"] = resultado.dataframe

    st.session_state["clean_result"] = resultado

# ==========================================================
# RESULTADOS
# ==========================================================

if "clean_result" in st.session_state:

    resultado = st.session_state["clean_result"]

    clean_df = resultado.dataframe

    st.success(

        "Proceso de limpieza finalizado."

    )

    st.subheader(

        "📈 Calidad"

    )

    c1, c2, c3 = st.columns(3)

    c1.metric(

        "Antes",

        f"{resultado.score_before:.2f}%"

    )

    c2.metric(

        "Después",

        f"{resultado.score_after:.2f}%"

    )

    c3.metric(

        "Mejora",

        f"{resultado.score_after - resultado.score_before:.2f}%"

    )

    st.progress(

        resultado.score_after / 100

    )

    st.divider()

    # ======================================================
    # HISTORIAL
    # ======================================================

    st.subheader(

        "📜 Historial"

    )

    history = resultado.history.to_dataframe()

    if history is not None:

        st.dataframe(

            history,

            use_container_width=True,

            hide_index=True

        )

    st.divider()

    # ======================================================
    # REPORTE
    # ======================================================

    st.subheader(

        "📄 Resumen Ejecutivo"

    )

    st.info(

        resultado.report["resumen"]

    )

    if resultado.report["recommendations"]:

        st.subheader(

            "💡 Recomendaciones"

        )

        for recomendacion in resultado.report["recommendations"]:

            st.success(

                recomendacion

            )

    st.divider()

    # ======================================================
    # DATASET LIMPIO
    # ======================================================

    st.subheader(

        "✅ Dataset Limpio"

    )

    st.dataframe(

        clean_df,

        use_container_width=True,

        height=350

    )

    st.divider()

    # ======================================================
    # EXPORTAR CSV
    # ======================================================

    csv = clean_df.to_csv(

        index=False

    ).encode(

        "utf-8"

    )

    st.download_button(

        "⬇ Descargar CSV",

        csv,

        "dataset_clean.csv",

        "text/csv",

        use_container_width=True

    )

    # ======================================================
    # REEMPLAZAR DATASET ACTUAL
    # ======================================================

    if st.button(

        "✅ Usar Dataset Limpio",

        use_container_width=True

    ):

        st.session_state["df"] = clean_df

        st.success(

            "El dataset limpio ahora es el dataset activo."

        )