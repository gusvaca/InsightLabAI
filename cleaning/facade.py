from cleaning.engine import CleaningEngine


class CleaningFacade:

    @staticmethod
    def auto_clean(df):

        return CleaningEngine.auto_clean(df)