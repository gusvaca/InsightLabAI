from cleaning.facade import CleaningFacade


class CleaningService:

    @staticmethod
    def auto_clean(df):

        return CleaningFacade.auto_clean(df)