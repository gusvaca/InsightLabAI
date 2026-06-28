from copy import deepcopy

from cleaning.models import CleaningResult

from cleaning.duplicate_cleaner import DuplicateCleaner
from cleaning.null_cleaner import NullCleaner
from cleaning.column_cleaner import ColumnCleaner
from cleaning.datatype_cleaner import DatatypeCleaner
from cleaning.text_cleaner import TextCleaner
from cleaning.outlier_cleaner import OutlierCleaner

from cleaning.cleaning_history import CleaningHistory
from cleaning.cleaning_statistics import CleaningStatistics
from cleaning.cleaning_report import CleaningReport


class CleaningEngine:

    """
    =======================================================

    Data Cleaning Engine

    Motor principal encargado de ejecutar el proceso
    completo de limpieza.

    =======================================================
    """

    @staticmethod
    def auto_clean(df):

        original_df = deepcopy(df)

        clean_df = deepcopy(df)

        history = CleaningHistory()

        result = CleaningResult()

        result.dataframe = clean_df

        # ==========================================
        # DUPLICADOS
        # ==========================================

        action = DuplicateCleaner.clean(

            clean_df

        )

        history.add(action)

        result.add_action(action)

        # ==========================================
        # NOMBRES DE COLUMNAS
        # ==========================================

        action = ColumnCleaner.trim_names(

            clean_df

        )

        history.add(action)

        result.add_action(action)

        action = ColumnCleaner.normalize_names(

            clean_df

        )

        history.add(action)

        result.add_action(action)

        # ==========================================
        # COLUMNAS
        # ==========================================

        action = ColumnCleaner.remove_empty_columns(

            clean_df

        )

        history.add(action)

        result.add_action(action)

        action = ColumnCleaner.remove_constant_columns(

            clean_df

        )

        history.add(action)

        result.add_action(action)

        # ==========================================
        # NULOS
        # ==========================================

        action = NullCleaner.fill_mode(

            clean_df

        )

        history.add(action)

        result.add_action(action)

        # ==========================================
        # TIPOS
        # ==========================================

        action = DatatypeCleaner.convert_numeric(

            clean_df

        )

        history.add(action)

        result.add_action(action)

        action = DatatypeCleaner.convert_dates(

            clean_df

        )

        history.add(action)

        result.add_action(action)

        action = DatatypeCleaner.convert_boolean(

            clean_df

        )

        history.add(action)

        result.add_action(action)

        action = DatatypeCleaner.optimize_memory(

            clean_df

        )

        history.add(action)

        result.add_action(action)

        # ==========================================
        # TEXTO
        # ==========================================

        action = TextCleaner.trim(

            clean_df

        )

        history.add(action)

        result.add_action(action)

        action = TextCleaner.normalize_spaces(

            clean_df

        )

        history.add(action)

        result.add_action(action)

        action = TextCleaner.remove_accents(

            clean_df

        )

        history.add(action)

        result.add_action(action)

        # ==========================================
        # OUTLIERS
        # ==========================================

        action = OutlierCleaner.replace_by_median(

            clean_df

        )

        history.add(action)

        result.add_action(action)

        # ==========================================
        # ESTADÍSTICAS
        # ==========================================

        statistics = CleaningStatistics.calculate(

            original_df,

            clean_df,

            history

        )

        report = CleaningReport.generate(

            statistics,

            history

        )

        result.dataframe = clean_df

        result.statistics = statistics

        result.score_before = statistics[
            "before"
        ][
            "quality_score"
        ]

        result.score_after = statistics[
            "after"
        ][
            "quality_score"
        ]

        result.history = history

        result.report = report

        return result