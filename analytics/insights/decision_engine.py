class DecisionEngine:

    """
    =======================================================
    Decision Engine

    Determina cuál debería ser el siguiente paso del análisis
    de acuerdo con el estado del dataset.

    =======================================================
    """

    @staticmethod
    def next_steps(resumen):

        pasos = []

        score = resumen.get("score", 0)

        missing = resumen.get("porcentaje_nulos", 0)

        duplicates = resumen.get("duplicados", 0)

        constantes = resumen.get("variables_constantes", 0)

        # ==========================================
        # LIMPIEZA
        # ==========================================

        if duplicates > 0:

            pasos.append({

                "prioridad": 1,

                "titulo": "Eliminar registros duplicados",

                "estado": "Pendiente"

            })

        if missing > 0:

            pasos.append({

                "prioridad": 2,

                "titulo": "Tratar valores nulos",

                "estado": "Pendiente"

            })

        if constantes > 0:

            pasos.append({

                "prioridad": 3,

                "titulo": "Eliminar variables constantes",

                "estado": "Pendiente"

            })

        # ==========================================
        # ANALÍTICA
        # ==========================================

        if score >= 80:

            pasos.append({

                "prioridad": 4,

                "titulo": "Ejecutar Análisis Exploratorio (EDA)",

                "estado": "Recomendado"

            })

            pasos.append({

                "prioridad": 5,

                "titulo": "Analizar correlaciones",

                "estado": "Recomendado"

            })

            pasos.append({

                "prioridad": 6,

                "titulo": "Entrenar modelos de Machine Learning",

                "estado": "Recomendado"

            })

        # ==========================================
        # DATASET EXCELENTE
        # ==========================================

        if score >= 95:

            pasos.append({

                "prioridad": 7,

                "titulo": "Comparar varios algoritmos",

                "estado": "Muy recomendado"

            })

            pasos.append({

                "prioridad": 8,

                "titulo": "Realizar validación cruzada",

                "estado": "Muy recomendado"

            })

            pasos.append({

                "prioridad": 9,

                "titulo": "Generar Reporte Ejecutivo",

                "estado": "Muy recomendado"

            })

        pasos.sort(

            key=lambda x: x["prioridad"]

        )

        return pasos