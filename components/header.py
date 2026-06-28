import streamlit as st

from datetime import datetime

from analytics.quality import DataQuality


# =====================================================
# HEADER ENTERPRISE V3
# =====================================================

def render_header(

    title,

    subtitle,

    df=None,

    icon="📊"

):

    fecha = datetime.now().strftime("%d/%m/%Y")

    registros = "-"

    variables = "-"

    estado = "Sin Dataset"

    score = "-"

    if df is not None:

        resumen = DataQuality.resumen(df)

        registros = f"{resumen['filas']:,}"

        variables = resumen["columnas"]

        estado = resumen["estado"]

        score = resumen["score"]

    with st.container():

        c1, c2 = st.columns(

            [6,1]

        )

        with c1:

            st.markdown(

                f"""
### {icon} {title}

{subtitle}

""")

        with c2:

            st.markdown(

                """
### 🚀

Enterprise
""")

        st.divider()

        k1,k2,k3,k4,k5 = st.columns(5)

        k1.metric(

            "📅 Fecha",

            fecha

        )

        k2.metric(

            "📂 Estado",

            estado

        )

        k3.metric(

            "📄 Registros",

            registros

        )

        k4.metric(

            "📊 Variables",

            variables

        )

        k5.metric(

            "🎯 Score",

            score

        )

    st.markdown("<br>",unsafe_allow_html=True)
    import streamlit as st

from datetime import datetime

from analytics.quality import DataQuality


# =====================================================
# HEADER ENTERPRISE V3
# =====================================================

def render_header(

    title,

    subtitle,

    df=None,

    icon="📊"

):

    fecha = datetime.now().strftime("%d/%m/%Y")

    registros = "-"

    variables = "-"

    estado = "Sin Dataset"

    score = "-"

    memoria = "-"

    if df is not None:

        resumen = DataQuality.resumen(df)

        registros = f"{resumen['filas']:,}"

        variables = resumen["columnas"]

        estado = resumen["estado"]

        score = resumen["score"]

        memoria = f"{resumen['memoria']} MB"

    st.markdown(
        """
        <style>

        .hero{

            background:linear-gradient(135deg,#0F172A,#1E3A8A);

            border-radius:22px;

            padding:28px;

            margin-bottom:20px;

            color:white;

        }

        .hero-title{

            font-size:34px;

            font-weight:700;

            margin-bottom:6px;

        }

        .hero-subtitle{

            color:#CBD5E1;

            font-size:16px;

        }

        .hero-version{

            float:right;

            background:rgba(255,255,255,.12);

            padding:8px 16px;

            border-radius:999px;

            font-size:13px;

        }

        </style>
        """,

        unsafe_allow_html=True

    )

    st.markdown(

        f"""

<div class="hero">

<div class="hero-version">

🚀 Enterprise Edition

</div>

<div class="hero-title">

{icon} {title}

</div>

<div class="hero-subtitle">

{subtitle}

</div>

</div>

""",

        unsafe_allow_html=True

    )

    c1,c2,c3,c4,c5,c6 = st.columns(6)

    c1.metric(

        "📄 Registros",

        registros

    )

    c2.metric(

        "📊 Variables",

        variables

    )

    c3.metric(

        "💾 Memoria",

        memoria

    )

    c4.metric(

        "🎯 Calidad",

        score

    )

    c5.metric(

        "📂 Estado",

        estado

    )

    c6.metric(

        "📅 Fecha",

        fecha

    )

    st.divider()
    import streamlit as st

from datetime import datetime

from analytics.quality import DataQuality


# =====================================================
# HEADER ENTERPRISE V3
# =====================================================

def render_header(

    title,

    subtitle,

    df=None,

    icon="📊"

):

    fecha = datetime.now().strftime("%d/%m/%Y")

    registros = "-"

    variables = "-"

    estado = "Sin Dataset"

    score = "-"

    memoria = "-"

    if df is not None:

        resumen = DataQuality.resumen(df)

        registros = f"{resumen['filas']:,}"

        variables = resumen["columnas"]

        estado = resumen["estado"]

        score = resumen["score"]

        memoria = f"{resumen['memoria']} MB"

    st.markdown(
        """
<style>

.hero{

    background:linear-gradient(
        135deg,
        #0F172A,
        #1E3A8A
    );

    border-radius:22px;

    padding:30px;

    margin-bottom:25px;

    box-shadow:0 12px 30px rgba(15,23,42,.18);

}

.hero-title{

    color:white;

    font-size:34px;

    font-weight:700;

}

.hero-subtitle{

    color:#CBD5E1;

    font-size:16px;

    margin-top:6px;

}

.hero-chip{

    display:inline-block;

    margin-top:16px;

    padding:8px 14px;

    border-radius:999px;

    background:rgba(255,255,255,.12);

    color:white;

    font-size:12px;

    font-weight:600;

    margin-right:8px;

}

.hero-version{

    float:right;

}

</style>
""",
        unsafe_allow_html=True
    )

    st.markdown(

        f"""

<div class="hero">

<div class="hero-version">

<span class="hero-chip">

🚀 Enterprise Edition

</span>

</div>

<div class="hero-title">

{icon} {title}

</div>

<div class="hero-subtitle">

{subtitle}

</div>

<div>

<span class="hero-chip">

🤖 AI Ready

</span>

<span class="hero-chip">

📂 {estado}

</span>

<span class="hero-chip">

📅 {fecha}

</span>

</div>

</div>

""",

        unsafe_allow_html=True

    )

    c1,c2,c3,c4 = st.columns(4)

    with c1:

        st.metric(

            "📄 Registros",

            registros

        )

    with c2:

        st.metric(

            "📊 Variables",

            variables

        )

    with c3:

        st.metric(

            "💾 Memoria",

            memoria

        )

    with c4:

        st.metric(

            "🎯 Calidad",

            score

        )

    st.divider()
    import streamlit as st

from datetime import datetime

from analytics.quality import DataQuality


# =====================================================
# HEADER ENTERPRISE V3
# =====================================================

def render_header(

    title,

    subtitle,

    df=None,

    icon="📊"

):

    fecha = datetime.now().strftime("%d/%m/%Y")

    registros = "-"

    variables = "-"

    memoria = "-"

    estado = "Sin Dataset"

    score = "-"

    if df is not None:

        resumen = DataQuality.resumen(df)

        registros = f"{resumen['filas']:,}"

        variables = resumen["columnas"]

        memoria = f"{resumen['memoria']} MB"

        estado = resumen["estado"]

        score = resumen["score"]

    st.markdown(
        """
<style>

.hero{

    background:white;

    border-radius:20px;

    border:1px solid #E2E8F0;

    padding:28px;

    box-shadow:0 8px 24px rgba(15,23,42,.08);

    margin-bottom:20px;

}

.hero-top{

    display:flex;

    justify-content:space-between;

    align-items:center;

    margin-bottom:20px;

}

.hero-brand{

    font-size:13px;

    color:#2563EB;

    font-weight:700;

    letter-spacing:1px;

}

.hero-title{

    font-size:34px;

    font-weight:700;

    color:#0F172A;

    margin-top:6px;

}

.hero-sub{

    color:#64748B;

    font-size:16px;

    margin-top:8px;

}

.hero-chip{

    display:inline-block;

    padding:8px 14px;

    border-radius:999px;

    background:#EFF6FF;

    color:#2563EB;

    font-weight:600;

    font-size:12px;

    margin-right:8px;

    margin-top:14px;

}

</style>
""",
        unsafe_allow_html=True
    )

    st.markdown(

        f"""

<div class="hero">

<div class="hero-top">

<div>

<div class="hero-brand">

INSIGHTLAB AI ENTERPRISE

</div>

<div class="hero-title">

{icon} {title}

</div>

<div class="hero-sub">

{subtitle}

</div>

</div>

<div>

<span class="hero-chip">

🚀 Enterprise

</span>

</div>

</div>

<span class="hero-chip">

🤖 AI Ready

</span>

<span class="hero-chip">

📂 {estado}

</span>

<span class="hero-chip">

📅 {fecha}

</span>

</div>

""",

        unsafe_allow_html=True

    )

    c1,c2,c3,c4,c5 = st.columns(5)

    with c1:

        st.metric(

            "📄 Registros",

            registros

        )

    with c2:

        st.metric(

            "📊 Variables",

            variables

        )

    with c3:

        st.metric(

            "💾 Memoria",

            memoria

        )

    with c4:

        st.metric(

            "🎯 Calidad",

            score

        )

    with c5:

        st.metric(

            "📂 Estado",

            estado
        )

    st.divider()
    import streamlit as st

from datetime import datetime

from analytics.quality import DataQuality


# =====================================================
# HEADER ENTERPRISE V3
# =====================================================

def render_header(

    title,

    subtitle,

    df=None,

    icon="📊"

):

    fecha = datetime.now().strftime("%d/%m/%Y")

    registros = "-"

    variables = "-"

    memoria = "-"

    score = "-"

    estado = "Sin Dataset"

    if df is not None:

        resumen = DataQuality.resumen(df)

        registros = f"{resumen['filas']:,}"

        variables = resumen["columnas"]

        memoria = f"{resumen['memoria']} MB"

        score = resumen["score"]

        estado = resumen["estado"]

    st.markdown("""

<style>

.hero{

    background:white;

    border-radius:22px;

    overflow:hidden;

    border:1px solid #E2E8F0;

    box-shadow:0 10px 28px rgba(15,23,42,.08);

    margin-bottom:24px;

}

.hero-bar{

    height:8px;

    background:linear-gradient(
        90deg,
        #2563EB,
        #4F46E5,
        #7C3AED
    );

}

.hero-body{

    padding:28px;

}

.hero-brand{

    font-size:12px;

    font-weight:700;

    color:#2563EB;

    letter-spacing:1px;

    text-transform:uppercase;

}

.hero-title{

    font-size:34px;

    font-weight:700;

    color:#0F172A;

    margin-top:8px;

}

.hero-sub{

    color:#64748B;

    margin-top:8px;

    font-size:16px;

}

.hero-status{

    margin-top:18px;

}

.hero-pill{

    display:inline-block;

    background:#EFF6FF;

    color:#2563EB;

    border-radius:999px;

    padding:8px 16px;

    margin-right:8px;

    font-size:12px;

    font-weight:600;

}

</style>

""",unsafe_allow_html=True)

    st.markdown(f"""

<div class="hero">

<div class="hero-bar"></div>

<div class="hero-body">

<div class="hero-brand">

InsightLab AI Enterprise

</div>

<div class="hero-title">

{icon} {title}

</div>

<div class="hero-sub">

{subtitle}

</div>

<div class="hero-status">

<span class="hero-pill">

🟢 {estado}

</span>

<span class="hero-pill">

🚀 Enterprise Edition

</span>
</div>

</div>

</div>

""",unsafe_allow_html=True)

   