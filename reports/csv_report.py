"""
=========================================================
InsightLab AI Enterprise
Archivo : csv_report.py
=========================================================
"""


class CSVReport:

    @staticmethod
    def generar(df):

        return df.to_csv(index=False).encode("utf-8")