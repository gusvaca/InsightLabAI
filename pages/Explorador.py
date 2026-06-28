import streamlit as st

from core.session import obtener_dataset

from analytics.visualization import VisualizationEngine

from components.charts import *
from components.layout import Layout


df = obtener_dataset()
Layout.render(

    "📈 Explorador Visual",df

)

if df is None:

    st.warning("Primero carga un dataset.")

    st.stop()

tipo = st.selectbox(

    "Tipo de gráfico",

    [

        "Barras",

        "Líneas",

        "Scatter",

        "Bubble",

        "Pie",

        "Treemap",

        "Sunburst",

        "Boxplot",

        "Violin"

    ]

)

columnas = VisualizationEngine.todas(df)

numericas = VisualizationEngine.numericas(df)

categoricas = VisualizationEngine.categoricas(df)

if tipo=="Pie":

    col=st.selectbox(

        "Variable",

        categoricas

    )

    st.plotly_chart(

        pie(df,col),

        use_container_width=True

    )

elif tipo=="Treemap":

    col=st.selectbox(

        "Variable",

        categoricas

    )

    st.plotly_chart(

        treemap(df,col),

        use_container_width=True

    )

elif tipo=="Sunburst":

    col=st.selectbox(

        "Variable",

        categoricas

    )

    st.plotly_chart(

        sunburst(df,col),

        use_container_width=True

    )

elif tipo=="Boxplot":

    y=st.selectbox(

        "Variable",

        numericas

    )

    st.plotly_chart(

        box(df,y),

        use_container_width=True

    )

elif tipo=="Violin":

    y=st.selectbox(

        "Variable",

        numericas

    )

    st.plotly_chart(

        violin(df,y),

        use_container_width=True

    )

else:

    x=st.selectbox(

        "Eje X",

        columnas

    )

    y=st.selectbox(

        "Eje Y",

        numericas

    )

    if tipo=="Barras":

        fig=barras(df,x,y)

    elif tipo=="Líneas":

        fig=lineas(df,x,y)

    elif tipo=="Scatter":

        fig=scatter(df,x,y)

    else:

        size=st.selectbox(

            "Tamaño",

            numericas

        )

        fig=bubble(df,x,y,size)

    st.plotly_chart(

        fig,

        use_container_width=True

    )