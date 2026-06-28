"""
=========================================================
InsightLab AI Enterprise
Archivo : excel_report.py
=========================================================
"""

from io import BytesIO

import pandas as pd


class ExcelReport:

    @staticmethod
    def generar(df):

        output = BytesIO()

        with pd.ExcelWriter(
            output,
            engine="openpyxl"
        ) as writer:

            df.to_excel(
                writer,
                sheet_name="Dataset",
                index=False
            )

        output.seek(0)

        return output