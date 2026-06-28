class DataMaturity:

    """
    ==========================================================
    DATA MATURITY INDEX (DMI)

    Evalúa la madurez analítica del dataset.

    Nivel 1 -> Datos Crudos

    Nivel 2 -> Datos Preparados

    Nivel 3 -> Listo para Analítica

    Nivel 4 -> Listo para Machine Learning

    Nivel 5 -> Listo para Producción
    ==========================================================
    """

    @staticmethod
    def evaluate(resumen):

        score = resumen.get("score", 0)

        duplicados = resumen.get("duplicados", 0)

        nulos = resumen.get("porcentaje_nulos", 0)

        constantes = resumen.get("variables_constantes", 0)

        resultado = {

            "nivel": 1,

            "nombre": "Datos Crudos",

            "color": "#DC2626",

            "descripcion": "",

            "recomendacion": ""

        }

        # =====================================================

        if score >= 60:

            resultado = {

                "nivel": 2,

                "nombre": "Datos Preparados",

                "color": "#EA580C",

                "descripcion": (

                    "El dataset presenta una estructura adecuada "

                    "pero requiere tareas adicionales de preparación."

                ),

                "recomendacion": (

                    "Continuar con limpieza y validación."

                )

            }

        # =====================================================

        if score >= 80:

            resultado = {

                "nivel": 3,

                "nombre": "Listo para Analítica",

                "color": "#CA8A04",

                "descripcion": (

                    "El conjunto de datos puede utilizarse "

                    "para análisis descriptivos y exploratorios."

                ),

                "recomendacion": (

                    "Realizar EDA y análisis estadístico."

                )

            }

        # =====================================================

        if (

            score >= 90

            and duplicados == 0

            and nulos < 5

        ):

            resultado = {

                "nivel": 4,

                "nombre": "Listo para Machine Learning",

                "color": "#16A34A",

                "descripcion": (

                    "El dataset cumple condiciones "

                    "adecuadas para entrenamiento "

                    "de modelos predictivos."

                ),

                "recomendacion": (

                    "Entrenar varios algoritmos "

                    "y comparar resultados."

                )

            }

        # =====================================================

        if (

            score >= 98

            and duplicados == 0

            and nulos == 0

            and constantes == 0

        ):

            resultado = {

                "nivel": 5,

                "nombre": "Listo para Producción",

                "color": "#2563EB",

                "descripcion": (

                    "El conjunto de datos presenta "

                    "un excelente nivel de madurez "

                    "para ambientes productivos."

                ),

                "recomendacion": (

                    "Proceder con despliegue "

                    "y monitoreo continuo."

                )

            }

        return resultado