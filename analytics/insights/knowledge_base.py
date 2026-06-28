from dataclasses import dataclass


@dataclass
class KnowledgeRule:

    id: str

    categoria: str

    nombre: str

    descripcion: str

    condicion: callable

    prioridad: str

    impacto: str

    mensaje: str

    recomendacion: str


class KnowledgeBase:

    """
    ======================================================

    Knowledge Base

    Repositorio central del conocimiento de
    InsightLab AI.

    Todas las reglas expertas vivirán aquí.

    ======================================================
    """

    rules = []

    @classmethod
    def register(cls, rule):

        cls.rules.append(rule)

    @classmethod
    def evaluate(cls, resumen):

        resultados = []

        for rule in cls.rules:

            try:

                if rule.condicion(resumen):

                    resultados.append(rule)

            except Exception:

                continue

        return resultados