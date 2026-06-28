import streamlit as st


def kpi_card(
    titulo,
    valor,
    icono="📊",
    color="#2563EB",
    descripcion=""
):
    with st.container(border=True):

        st.markdown(f"#### {icono} {titulo}")

        st.metric(
            label="",
            value=valor
        )

        if descripcion:
            st.caption(descripcion)