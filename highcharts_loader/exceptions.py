class HighChartsLoaderError(Exception):
    """ Base exception for the library. Other library exceptions are inherited from it """
    pass


class EmptyParams(HighChartsLoaderError):
    pass


class TooManyParams(HighChartsLoaderError):
    pass


class HTTPError(HighChartsLoaderError):
    pass


class SaveFileError(HighChartsLoaderError):
    pass


class ReadFileError(HighChartsLoaderError):
    pass
