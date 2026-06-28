from analytics.insights.models import InsightResult


class RecommendationRules:

    """
    ===========================================================
    Recommendation Engine

    Genera recomendaciones inteligentes de los siguientes
    pasos del análisis.

    No reemplaza a los insights.

    Sugiere qué debería hacer el usuario después.
    ===========================================================
    """

    @staticmethod
    def evaluate(

        resumen,

        resultado: InsightResult

    ):

        recomendaciones = []

        # ==========================================
        # Calidad
        # ==========================================

        if resumen.get("score", 0) < 80:

            recomendaciones.append(

                "Realizar un proceso de limpieza antes de entrenar modelos."

            )

        # ==========================================
        # Valores nulos
        # ==========================================

        if resumen.get("porcentaje_nulos", 0) > 0:

            recomendaciones.append(

                "Aplicar técnicas de imputación para completar los valores faltantes."

            )

        # ==========================================
        # Duplicados
        # ==========================================

        if resumen.get("duplicados", 0) > 0:

            recomendaciones.append(

                "Eliminar los registros duplicados antes del análisis."

            )

        # ==========================================
        # Variables constantes
        # ==========================================

        if resumen.get("variables_constantes", 0) > 0:

            recomendaciones.append(

                "Eliminar variables constantes ya que no aportan información."

            )

        # ==========================================
        # Variables únicas
        # ==========================================

        if resumen.get("variables_unicas", 0) > 0:

            recomendaciones.append(

                "Excluir identificadores únicos del entrenamiento."

            )

        # ==========================================
        # Dataset listo
        # ==========================================

        if resumen.get("score", 0) >= 95:

            recomendaciones.append(

                "Continuar con Análisis Exploratorio (EDA)."

            )

            recomendaciones.append(

                "Ejecutar análisis de correlaciones."

            )

            recomendaciones.append(

                "Entrenar modelos de Machine Learning."

            )

        resultado.recomendaciones = recomendaciones

        return resultado