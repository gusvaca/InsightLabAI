from analytics.insights.knowledge_base import (

    KnowledgeRule

)


QUALITY_RULES = [

    KnowledgeRule(

        id="QLT001",

        categoria="Calidad",

        nombre="Dataset Excelente",

        descripcion="Excelente calidad.",

        prioridad="Baja",

        impacto="Muy Bajo",

        mensaje=(

            "El conjunto de datos presenta una excelente calidad."

        ),

        recomendacion=(

            "Puede continuar con el análisis exploratorio."

        ),

        condicion=lambda r:

            r.get("score",0)>=95

    ),

    KnowledgeRule(

        id="QLT002",

        categoria="Calidad",

        nombre="Dataset Bueno",

        descripcion="Buena calidad.",

        prioridad="Media",

        impacto="Bajo",

        mensaje=(

            "La calidad del conjunto de datos es adecuada."

        ),

        recomendacion=(

            "Revisar aspectos menores antes del modelado."

        ),

        condicion=lambda r:

            80<=r.get("score",0)<95

    ),

    KnowledgeRule(

        id="QLT003",

        categoria="Calidad",

        nombre="Dataset Deficiente",

        descripcion="Calidad insuficiente.",

        prioridad="Alta",

        impacto="Alto",

        mensaje=(

            "La calidad puede afectar los resultados."

        ),

        recomendacion=(

            "Ejecutar limpieza antes del entrenamiento."

        ),

        condicion=lambda r:

            r.get("score",0)<80

    ),

    KnowledgeRule(

        id="QLT010",

        categoria="Duplicados",

        nombre="Sin duplicados",

        descripcion="No existen duplicados.",

        prioridad="Baja",

        impacto="Ninguno",

        mensaje=(

            "No se detectaron registros duplicados."

        ),

        recomendacion=(

            "No se requieren acciones."

        ),

        condicion=lambda r:

            r.get("duplicados",0)==0

    ),

    KnowledgeRule(

        id="QLT011",

        categoria="Duplicados",

        nombre="Duplicados",

        descripcion="Existen registros duplicados.",

        prioridad="Alta",

        impacto="Alto",

        mensaje=(

            "Se detectaron registros duplicados."

        ),

        recomendacion=(

            "Eliminar registros duplicados."

        ),

        condicion=lambda r:

            r.get("duplicados",0)>0

    ),

    KnowledgeRule(

        id="QLT020",

        categoria="Completitud",

        nombre="Sin valores nulos",

        descripcion="Dataset completo.",

        prioridad="Baja",

        impacto="Ninguno",

        mensaje=(

            "No existen valores faltantes."

        ),

        recomendacion=(

            "No requiere imputaciones."

        ),

        condicion=lambda r:

            r.get("porcentaje_nulos",0)==0

    ),

    KnowledgeRule(

        id="QLT021",

        categoria="Completitud",

        nombre="Valores nulos",

        descripcion="Existen valores faltantes.",

        prioridad="Media",

        impacto="Medio",

        mensaje=(

            "Se detectaron valores nulos."

        ),

        recomendacion=(

            "Aplicar técnicas de imputación."

        ),

        condicion=lambda r:

            r.get("porcentaje_nulos",0)>0

    )

]