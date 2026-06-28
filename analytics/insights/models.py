from dataclasses import dataclass, field


@dataclass
class Insight:

    titulo: str

    categoria: str

    prioridad: str

    icono: str

    mensaje: str

    recomendacion: str = ""

    impacto: str = ""


@dataclass
class InsightResult:

    score: float = 0

    estado: str = ""

    resumen: str = ""

    insights: list = field(default_factory=list)

    recomendaciones: list = field(default_factory=list)

    fortalezas: list = field(default_factory=list)

    riesgos: list = field(default_factory=list)

    proximos_pasos: list = field(default_factory=list)

    def agregar(self, insight: Insight):

        self.insights.append(insight)