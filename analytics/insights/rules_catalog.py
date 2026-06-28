from analytics.insights.knowledge_base import (

    KnowledgeBase,

    KnowledgeRule

)


# ==========================================================
# REGLAS DE CALIDAD
# ==========================================================

KnowledgeBase.register(

    KnowledgeRule(

        id="QLT001",

        categoria="Calidad",

        nombre="Dataset Excelente",

        descripcion="El dataset posee una excelente calidad.",

        prioridad="Baja",

        impacto="Muy Bajo",

        mensaje=(

            "El conjunto de datos presenta una calidad "

            "excelente para procesos analíticos."

        ),

        recomendacion=(

            "Puede continuar con el análisis "

            "exploratorio y Machine Learning."

        ),

        condicion=lambda r:

            r.get("score",0)>=95

    )

)


KnowledgeBase.register(

    KnowledgeRule(

        id="QLT002",

        categoria="Calidad",

        nombre="Dataset Bueno",

        descripcion="La calidad es adecuada.",

        prioridad="Media",

        impacto="Bajo",

        mensaje=(

            "La calidad general del conjunto de datos "

            "es adecuada."

        ),

        recomendacion=(

            "Revisar aspectos menores antes "

            "del entrenamiento."

        ),

        condicion=lambda r:

            80<=r.get("score",0)<95

    )

)


KnowledgeBase.register(

    KnowledgeRule(

        id="QLT003",

        categoria="Calidad",

        nombre="Dataset Deficiente",

        descripcion="La calidad requiere mejoras.",

        prioridad="Alta",

        impacto="Alto",

        mensaje=(

            "La calidad del conjunto de datos "

            "puede afectar los resultados."

        ),

        recomendacion=(

            "Realizar un proceso completo "

            "de limpieza."

        ),

        condicion=lambda r:

            r.get("score",0)<80

    )

)


# ==========================================================
# DUPLICADOS
# ==========================================================

KnowledgeBase.register(

    KnowledgeRule(

        id="QLT010",

        categoria="Integridad",

        nombre="Sin duplicados",

        descripcion="No existen duplicados.",

        prioridad="Baja",

        impacto="Ninguno",

        mensaje="No se detectaron registros duplicados.",

        recomendacion="No se requieren acciones.",

        condicion=lambda r:

            r.get("duplicados",0)==0

    )

)


KnowledgeBase.register(

    KnowledgeRule(

        id="QLT011",

        categoria="Integridad",

        nombre="Duplicados",

        descripcion="Existen registros duplicados.",

        prioridad="Alta",

        impacto="Alto",

        mensaje="Se detectaron registros duplicados.",

        recomendacion="Eliminar duplicados antes del análisis.",

        condicion=lambda r:

            r.get("duplicados",0)>0

    )

)


# ==========================================================
# VALORES NULOS
# ==========================================================

KnowledgeBase.register(

    KnowledgeRule(

        id="QLT020",

        categoria="Completitud",

        nombre="Sin nulos",

        descripcion="Dataset completo.",

        prioridad="Baja",

        impacto="Ninguno",

        mensaje="No existen valores nulos.",

        recomendacion="No requiere imputaciones.",

        condicion=lambda r:

            r.get("porcentaje_nulos",0)==0

    )

)


KnowledgeBase.register(

    KnowledgeRule(

        id="QLT021",

        categoria="Completitud",

        nombre="Valores nulos",

        descripcion="Existen valores faltantes.",

        prioridad="Media",

        impacto="Medio",

        mensaje="Se detectaron valores nulos.",

        recomendacion=(

            "Aplicar técnicas de imputación."

        ),

        condicion=lambda r:

            r.get("porcentaje_nulos",0)>0

    )

)