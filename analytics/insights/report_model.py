from dataclasses import dataclass, field


@dataclass
class ReportSection:

    titulo: str

    contenido: str


@dataclass
class ExecutiveReport:

    """
    =======================================================
    Modelo del Reporte Ejecutivo
    =======================================================
    """

    titulo: str = "Executive Analytics Report"

    subtitulo: str = ""

    fecha: str = ""

    score: float = 0

    estado: str = ""

    data_maturity: str = ""

    sections: list = field(default_factory=list)

    recomendaciones: list = field(default_factory=list)

    siguientes_pasos: list = field(default_factory=list)

    def add_section(

        self,

        titulo,

        contenido

    ):

        self.sections.append(

            ReportSection(

                titulo=titulo,

                contenido=contenido

            )

        )

    def add_recommendation(

        self,

        texto

    ):

        self.recomendaciones.append(

            texto

        )

    def add_next_step(

        self,

        texto

    ):

        self.siguientes_pasos.append(

            texto

        )