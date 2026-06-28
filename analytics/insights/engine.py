from analytics.insights.quality_engine import QualityEngine

from analytics.insights.executive_summary import ExecutiveSummary

from analytics.insights.story_generator import StoryGenerator

from analytics.insights.business_interpreter import BusinessInterpreter

from analytics.insights.recommendation_rules import RecommendationRules

from analytics.insights.decision_engine import DecisionEngine

from analytics.insights.data_maturity import DataMaturity


class InsightEngine:

    """
    =====================================================

    Insight Intelligence Engine

    Orquestador principal de la plataforma.

    =====================================================
    """

    @staticmethod
    def quality(

        resumen

    ):

        resultado = QualityEngine.analyze(

            resumen

        )

        resultado = RecommendationRules.evaluate(

            resumen,

            resultado

        )

        madurez = DataMaturity.evaluate(

            resumen

        )

        negocio = BusinessInterpreter.interpret(

            resumen

        )

        historia = StoryGenerator.generate(

            resultado,

            madurez,

            negocio

        )

        resumen_ejecutivo = ExecutiveSummary.generate(

            resultado

        )

        siguientes_pasos = DecisionEngine.next_steps(

            resumen

        )

        return {

            "resultado": resultado,

            "madurez": madurez,

            "negocio": negocio,

            "historia": historia,

            "resumen": resumen_ejecutivo,

            "siguientes_pasos": siguientes_pasos

        }