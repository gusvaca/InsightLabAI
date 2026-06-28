import time
import streamlit as st


class LoadingManager:

    @staticmethod
    def simple(texto="Procesando..."):

        return st.spinner(texto)

    @staticmethod
    def progress(etapas):

        barra = st.progress(0)

        estado = st.empty()

        total = len(etapas)

        for i, etapa in enumerate(etapas):

            estado.info(f"🔄 {etapa}")

            porcentaje = int((i + 1) / total * 100)

            barra.progress(porcentaje)

            time.sleep(0.4)

        estado.success("✅ Proceso finalizado")