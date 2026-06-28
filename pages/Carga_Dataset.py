import streamlit as st

from core.loader import DatasetLoader
from components.layout import Layout


# ==========================================================
# HEADER
# ==========================================================

Layout.render(

    "🔎 Cargar Dataset"

)

st.write(
    "Carga un archivo CSV, Excel, JSON o Parquet."
)

# ==========================================================
# FILE UPLOADER
# ==========================================================

archivo = st.file_uploader(
    "Selecciona un archivo",
    type=["csv", "xlsx", "xls", "json", "parquet"]
)

# ==========================================================
# CARGAR DATASET
# ==========================================================

if archivo is not None:

    df = DatasetLoader.cargar(archivo)

    if df is not None:

        # ======================================
        # GUARDAR EN SESSION STATE
        # ======================================

        st.session_state["df"] = df
        st.session_state["dataset_loaded"] = True
        st.session_state["dataset_name"] = archivo.name
        st.session_state["rows"] = len(df)
        st.session_state["columns"] = len(df.columns)

        st.success("✅ Dataset cargado correctamente.")

# ==========================================================
# MOSTRAR DATASET SI EXISTE
# ==========================================================

if "df" in st.session_state:

    df = st.session_state["df"]

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "📄 Registros",
        len(df)
    )

    c2.metric(
        "📊 Columnas",
        len(df.columns)
    )

    memoria = (
        df.memory_usage(deep=True)
        .sum()
        / 1024
        / 1024
    )

    c3.metric(
        "💾 Memoria",
        f"{memoria:.2f} MB"
    )

    c4.metric(
        "⚠️ Nulos",
        int(df.isna().sum().sum())
    )

    st.divider()

    st.subheader("Vista previa del Dataset")

    st.dataframe(
        df,
        use_container_width=True,
        height=500
    )

else:

    st.info(
        "Seleccione un archivo para comenzar el análisis."
    )