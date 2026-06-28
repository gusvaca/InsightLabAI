import streamlit as st


def guardar_dataset(df):
    st.session_state["dataset"] = df


def obtener_dataset():
    return st.session_state.get("dataset", None)


def existe_dataset():
    return "dataset" in st.session_state


def limpiar_dataset():
    if "dataset" in st.session_state:
        del st.session_state["dataset"]