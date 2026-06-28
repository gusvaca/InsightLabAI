from dataclasses import dataclass, field


@dataclass
class CleaningAction:

    nombre: str

    descripcion: str

    registros_afectados: int = 0

    estado: str = "Ejecutado"


@dataclass
class CleaningResult:

    dataframe = None

    score_before: float = 0

    score_after: float = 0

    actions: list = field(default_factory=list)

    statistics: dict = field(default_factory=dict)

    def add_action(

        self,

        action: CleaningAction

    ):

        self.actions.append(action)