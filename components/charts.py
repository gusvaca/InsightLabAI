"""
=========================================================
InsightLab AI Enterprise
Archivo : charts.py
Modulo  : Components
Descripcion:
Gráficos reutilizables de toda la aplicación.
=========================================================
"""

import plotly.express as px
import plotly.graph_objects as go

from components.theme import ChartTheme


# =========================================================
# DASHBOARD
# =========================================================

def gauge(score):

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,
            title={"text": "Data Health Score"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "#2563EB"},
                "steps": [
                    {"range": [0, 60], "color": "#FECACA"},
                    {"range": [60, 80], "color": "#FDE68A"},
                    {"range": [80, 100], "color": "#BBF7D0"},
                ],
            },
        )
    )

    fig.update_layout(height=350)

    return ChartTheme.apply(fig)


def tipos_variables(df):

    tipos = (
        df.dtypes.astype(str)
        .value_counts()
        .reset_index()
    )

    tipos.columns = ["Tipo", "Cantidad"]

    fig = px.pie(
        tipos,
        names="Tipo",
        values="Cantidad",
        hole=0.55,
        color_discrete_sequence=ChartTheme.colors()
    )

    return ChartTheme.apply(fig)


# =========================================================
# CALIDAD
# =========================================================

def grafico_nulos(df):

    datos = df.isna().sum().reset_index()

    datos.columns = ["Columna", "Nulos"]

    fig = px.bar(
        datos,
        x="Columna",
        y="Nulos",
        color="Nulos",
        color_continuous_scale="Blues"
    )

    return ChartTheme.apply(fig)


def barra_calidad(score):

    fig = go.Figure(
        go.Indicator(
            mode="gauge",
            value=score,
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "#16A34A"},
            },
        )
    )

    fig.update_layout(height=250)

    return ChartTheme.apply(fig)


# =========================================================
# ESTADÍSTICAS
# =========================================================

def heatmap_correlation(corr):

    fig = px.imshow(
        corr,
        text_auto=".2f",
        color_continuous_scale="RdBu_r",
        aspect="auto"
    )

    return ChartTheme.apply(fig)


def grafico_outliers(df):

    fig = px.bar(
        df,
        x="Variable",
        y="Outliers",
        color="Outliers",
        color_continuous_scale="Reds"
    )

    return ChartTheme.apply(fig)


# =========================================================
# EDA
# =========================================================

def histograma(df, columna):

    fig = px.histogram(
        df,
        x=columna,
        nbins=30,
        marginal="box",
        title=f"Distribución de {columna}"
    )

    return ChartTheme.apply(fig)


def boxplot(df, columna):

    fig = px.box(
        df,
        y=columna,
        points="outliers",
        title=f"Boxplot - {columna}"
    )

    return ChartTheme.apply(fig)


def densidad(df, columna):

    fig = px.histogram(
        df,
        x=columna,
        histnorm="probability density",
        nbins=40,
        title=f"Densidad - {columna}"
    )

    return ChartTheme.apply(fig)


# =========================================================
# EXPLORADOR VISUAL
# =========================================================

def barras(df, x, y):

    fig = px.bar(
        df,
        x=x,
        y=y,
        color_discrete_sequence=ChartTheme.colors()
    )

    return ChartTheme.apply(fig)


def lineas(df, x, y):

    fig = px.line(
        df,
        x=x,
        y=y,
        color_discrete_sequence=ChartTheme.colors()
    )

    return ChartTheme.apply(fig)


def scatter(df, x, y):

    fig = px.scatter(
        df,
        x=x,
        y=y,
        color_discrete_sequence=ChartTheme.colors()
    )

    fig.update_traces(
        marker=dict(
            size=10,
            line=dict(
                width=1,
                color="white"
            )
        )
    )

    return ChartTheme.apply(fig)


def bubble(df, x, y, size):

    fig = px.scatter(
        df,
        x=x,
        y=y,
        size=size,
        color=size,
        color_continuous_scale="Blues"
    )

    return ChartTheme.apply(fig)


def box(df, y):

    fig = px.box(df, y=y)

    return ChartTheme.apply(fig)


def violin(df, y):

    fig = px.violin(
        df,
        y=y,
        box=True
    )

    return ChartTheme.apply(fig)


def pie(df, columna):

    datos = df[columna].value_counts().reset_index()

    datos.columns = ["Categoria", "Cantidad"]

    fig = px.pie(
        datos,
        names="Categoria",
        values="Cantidad",
        hole=.45,
        color_discrete_sequence=ChartTheme.colors()
    )

    return ChartTheme.apply(fig)


def treemap(df, columna):

    datos = df[columna].value_counts().reset_index()

    datos.columns = [columna, "Cantidad"]

    fig = px.treemap(
        datos,
        path=[columna],
        values="Cantidad",
        color_discrete_sequence=ChartTheme.colors()
    )

    return ChartTheme.apply(fig)


def sunburst(df, columna):

    datos = df[columna].value_counts().reset_index()

    datos.columns = [columna, "Cantidad"]

    fig = px.sunburst(
        datos,
        path=[columna],
        values="Cantidad",
        color_discrete_sequence=ChartTheme.colors()
    )

    return ChartTheme.apply(fig)


# =========================================================
# MACHINE LEARNING
# =========================================================

def scatter_cluster(df, x, y):

    fig = px.scatter(
        df,
        x=x,
        y=y,
        color="Cluster",
        title="Clusters Detectados",
        color_discrete_sequence=ChartTheme.colors()
    )

    fig.update_traces(
        marker=dict(
            size=11,
            line=dict(
                width=1,
                color="white"
            )
        )
    )

    return ChartTheme.apply(fig)


def scatter_anomaly(df, x, y):

    fig = px.scatter(
        df,
        x=x,
        y=y,
        color="Anomaly",
        symbol="Anomaly",
        title="Detección de Anomalías",
        color_discrete_sequence=["#2563EB", "#DC2626"]
    )

    fig.update_traces(
        marker=dict(
            size=11,
            line=dict(
                width=1,
                color="white"
            )
        )
    )

    return ChartTheme.apply(fig)