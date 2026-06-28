class BusinessInterpreter:

    """
    ==========================================================

    Business Interpreter

    Traduce resultados técnicos a lenguaje de negocio.

    No habla de algoritmos.

    Habla de riesgos, oportunidades e impacto.

    ==========================================================
    """

    @staticmethod
    def interpret(resumen):

        mensajes = []

        score = resumen.get("score", 0)

        duplicados = resumen.get("duplicados", 0)

        nulos = resumen.get("porcentaje_nulos", 0)

        # ==========================================
        # CALIDAD GENERAL
        # ==========================================

        if score >= 95:

            mensajes.append(

                "La calidad del conjunto de datos permite iniciar proyectos analíticos con un riesgo muy bajo."

            )

        elif score >= 80:

            mensajes.append(

                "El conjunto de datos es adecuado para análisis, aunque se recomienda completar tareas de preparación."

            )

        else:

            mensajes.append(

                "La calidad actual del conjunto de datos representa un riesgo para obtener resultados confiables."

            )

        # ==========================================
        # DUPLICADOS
        # ==========================================

        if duplicados > 0:

            mensajes.append(

                "Los registros duplicados pueden generar indicadores incorrectos y afectar modelos predictivos."

            )

        # ==========================================
        # VALORES NULOS
        # ==========================================

        if nulos > 10:

            mensajes.append(

                "El porcentaje de valores faltantes puede disminuir la precisión de los modelos."

            )

        elif nulos > 0:

            mensajes.append(

                "Se recomienda revisar los valores faltantes antes de continuar con el análisis."

            )

        # ==========================================
        # DATASET LISTO
        # ==========================================

        if (

            score >= 95

            and duplicados == 0

            and nulos == 0

        ):

            mensajes.append(

                "El conjunto de datos se encuentra listo para procesos avanzados de Machine Learning."

            )

        return mensajes