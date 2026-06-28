import pandas as pd


class CleaningStatistics:

    """
    ==========================================================
    Cleaning Statistics

    Calcula indicadores antes y después del proceso
    de limpieza.

    ==========================================================
    """

    @staticmethod
    def calculate(

        original_df,

        clean_df,

        history

    ):

        before = CleaningStatistics._dataset_metrics(

            original_df

        )

        after = CleaningStatistics._dataset_metrics(

            clean_df

        )

        improvement = CleaningStatistics._calculate_improvement(

            before,

            after

        )

        return {

            "before": before,

            "after": after,

            "improvement": improvement,

            "actions": history.summary()

        }

    @staticmethod
    def _dataset_metrics(

        df

    ):

        rows = len(df)

        columns = len(df.columns)

        nulls = int(

            df.isna().sum().sum()

        )

        duplicates = int(

            df.duplicated().sum()

        )

        memory = round(

            df.memory_usage(

                deep=True

            ).sum()

            / 1024

            / 1024,

            2

        )

        constant_columns = sum(

            df[col].nunique(

                dropna=False

            ) <= 1

            for col in df.columns

        )

        empty_columns = sum(

            df[col].isna().all()

            for col in df.columns

        )

        quality_score = CleaningStatistics._quality_score(

            rows,

            columns,

            nulls,

            duplicates,

            constant_columns,

            empty_columns

        )

        return {

            "rows": rows,

            "columns": columns,

            "nulls": nulls,

            "duplicates": duplicates,

            "memory_mb": memory,

            "constant_columns": constant_columns,

            "empty_columns": empty_columns,

            "quality_score": quality_score

        }

    @staticmethod
    def _quality_score(

        rows,

        columns,

        nulls,

        duplicates,

        constants,

        empty

    ):

        total_cells = max(

            rows * columns,

            1

        )

        penalty = 0

        penalty += (

            nulls / total_cells

        ) * 40

        penalty += (

            duplicates / max(rows, 1)

        ) * 30

        penalty += (

            constants / max(columns, 1)

        ) * 20

        penalty += (

            empty / max(columns, 1)

        ) * 10

        score = max(

            0,

            100 - penalty

        )

        return round(

            score,

            2

        )

    @staticmethod
    def _calculate_improvement(

        before,

        after

    ):

        score_gain = round(

            after["quality_score"]

            - before["quality_score"],

            2

        )

        duplicates_removed = (

            before["duplicates"]

            - after["duplicates"]

        )

        nulls_removed = (

            before["nulls"]

            - after["nulls"]

        )

        memory_saved = round(

            before["memory_mb"]

            - after["memory_mb"],

            2

        )

        return {

            "score_gain": score_gain,

            "duplicates_removed": duplicates_removed,

            "nulls_removed": nulls_removed,

            "memory_saved_mb": memory_saved

        }