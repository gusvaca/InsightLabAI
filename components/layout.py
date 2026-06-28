import streamlit as st

from components.sidebar import sidebar
from components.header import render_header


class Layout:

    @staticmethod
    def load_css():

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

    @staticmethod
    def render(

        title,

        df=None,

        subtitle="Intelligent Data Analytics Platform",

        icon="📊"

    ):

        Layout.load_css()

        sidebar()

        render_header(

           title=title,

            subtitle=subtitle,

            df=df,

            icon=icon

        )