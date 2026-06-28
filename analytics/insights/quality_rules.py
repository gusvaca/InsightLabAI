from analytics.insights.models import Insight


class QualityRules:

    """
    =====================================================
    Sistema Experto de Calidad de Datos

    Cada regla devuelve un Insight cuando se cumple
    determinada condición.

    =====================================================
    """

    @staticmethod
    def evaluate(resumen):

        insights = []

        QualityRules.rule_score(

            resumen,

            insights

        )

        QualityRules.rule_duplicates(

            resumen,

            insights

        )

        QualityRules.rule_missing(

            resumen,

            insights

        )

        return insights

    # =====================================================
    # SCORE GENERAL
    # =====================================================

    @staticmethod
    def rule_score(

        resumen,

        insights

    ):

        score = resumen.get(

            "score",

            0

        )

        if score >= 95:

            insights.append(

                Insight(

                    titulo="Excelente calidad",

                    categoria="Calidad",

                    prioridad="Baja",

                    icono="🟢",

                    mensaje=(

                        "El conjunto de datos presenta una "

                        "excelente calidad."

                    ),

                    recomendacion=(

                        "Puede continuar con EDA y "

                        "Machine Learning."

                    ),

                    impacto="Muy Bajo"

                )

            )

        elif score >= 80:

            insights.append(

                Insight(

                    titulo="Buena calidad",

                    categoria="Calidad",

                    prioridad="Media",

                    icono="🟡",

                    mensaje=(

                        "La calidad es adecuada "

                        "aunque existen aspectos "

                        "por mejorar."

                    ),

                    recomendacion=(

                        "Revisar nulos y valores "

                        "atípicos."

                    ),

                    impacto="Medio"

                )

            )

        else:

            insights.append(

                Insight(

                    titulo="Calidad insuficiente",

                    categoria="Calidad",

                    prioridad="Alta",

                    icono="🔴",

                    mensaje=(

                        "La calidad del dataset "

                        "puede afectar los modelos."

                    ),

                    recomendacion=(

                        "Ejecutar limpieza antes "

                        "de continuar."

                    ),

                    impacto="Alto"

                )

            )

    # =====================================================
    # DUPLICADOS
    # =====================================================

    @staticmethod
    def rule_duplicates(

        resumen,

        insights

    ):

        duplicados = resumen.get(

            "duplicados",

            0

        )

        if duplicados == 0:

            insights.append(

                Insight(

                    titulo="Duplicados",

                    categoria="Integridad",

                    prioridad="Baja",

                    icono="✅",

                    mensaje="No existen registros duplicados.",

                    recomendacion="No requiere acciones.",

                    impacto="Ninguno"

                )

            )

        else:

            insights.append(

                Insight(

                    titulo="Duplicados encontrados",

                    categoria="Integridad",

                    prioridad="Alta",

                    icono="⚠️",

                    mensaje=(

                        f"Se detectaron "

                        f"{duplicados} "

                        "registros duplicados."

                    ),

                    recomendacion=(

                        "Eliminar los registros "

                        "duplicados."

                    ),

                    impacto="Alto"

                )

            )

    # =====================================================
    # VALORES NULOS
    # =====================================================

    @staticmethod
    def rule_missing(

        resumen,

        insights

    ):

        nulos = resumen.get(

            "porcentaje_nulos",

            0

        )

        if nulos == 0:

            insights.append(

                Insight(

                    titulo="Valores nulos",

                    categoria="Completitud",

                    prioridad="Baja",

                    icono="✅",

                    mensaje="No existen valores nulos.",

                    recomendacion="No requiere imputación.",

                    impacto="Ninguno"

                )

            )

        elif nulos < 5:

            insights.append(

                Insight(

                    titulo="Valores nulos bajos",

                    categoria="Completitud",

                    prioridad="Media",

                    icono="🟡",

                    mensaje=(

                        f"El dataset contiene "

                        f"{nulos:.1f}% "

                        "de valores nulos."

                    ),

                    recomendacion=(

                        "Aplicar media, mediana "

                        "o moda."

                    ),

                    impacto="Bajo"

                )

            )

        else:

            insights.append(

                Insight(

                    titulo="Valores nulos elevados",

                    categoria="Completitud",

                    prioridad="Alta",

                    icono="🔴",

                    mensaje=(

                        f"El "

                        f"{nulos:.1f}% "

                        "del dataset contiene "

                        "valores nulos."

                    ),

                    recomendacion=(

                        "Analizar antes del "

                        "entrenamiento."

                    ),

                    impacto="Alto"

                )

            )