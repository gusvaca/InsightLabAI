import streamlit as st

from components.insight_summary_card import InsightSummaryCard
from components.insight_kpi_panel import InsightKPIPanel
from components.insight_quality_badges import InsightQualityBadges
from components.insight_health_panel import InsightHealthPanel
from components.insight_decision_panel import InsightDecisionPanel
from components.insight_recommendations import InsightRecommendations
from components.insight_business_view import InsightBusinessView


class InsightOverview:

    """
    =======================================================

    Insight Overview

    Vista ejecutiva principal del Insight Intelligence
    Engine.

    Integra todos los componentes ejecutivos en un
    único panel reutilizable.

    =======================================================
    """

    @staticmethod
    def render(

        analysis

    ):

        st.header(

            "🧠 Insight Intelligence"

        )

        # ==========================================
        # RESUMEN EJECUTIVO
        # ==========================================

        InsightSummaryCard.render(

            analysis

        )

        # ==========================================
        # KPIs
        # ==========================================

        InsightKPIPanel.render(

            analysis

        )

        st.divider()

        # ==========================================
        # BADGES
        # ==========================================

        InsightQualityBadges.render(

            analysis

        )

        st.divider()

        # ==========================================
        # HEALTH
        # ==========================================

        InsightHealthPanel.render(

            analysis

        )

        st.divider()

        # ==========================================
        # DECISIONES
        # ==========================================

        InsightDecisionPanel.render(

            analysis

        )

        st.divider()

        # ==========================================
        # RECOMENDACIONES
        # ==========================================

        InsightRecommendations.render(

            analysis

        )

        st.divider()

        # ==========================================
        # NEGOCIO
        # ==========================================

        InsightBusinessView.render(

            analysis
        )