import json
from typing import Optional, Dict, Any

from .exceptions import EmptyParams, TooManyParams, ReadFileError


class Options:
    """
        Take chart options from dict or from json file.
        All available options you can find in official documentation https://www.highcharts.com/docs
    """

    def __init__(self, *, from_file: Optional[str] = None, from_dict: Optional[Dict[str, Any]] = None):
        if not from_file and not from_dict:
            raise EmptyParams('You have to pass "from_file" or "from_dict" parameters.')
        if from_file and from_dict:
            raise TooManyParams('You have to pass only one parameter: "from_file" or "from_dict".')

        self._from_file = from_file
        self._from_dict = from_dict
        self._data = None

    @property
    def data(self) -> Optional[Dict[str, Any]]:
        if self._data is None:
            self._data = self._init_data()
        return self._data

    def _init_data(self) -> Dict[str, Any]:
        if self._from_dict:
            return self._from_dict

        try:
            with open(self._from_file) as f:
                return json.loads(f.read())
        except (OSError, json.JSONDecodeError) as e:
            raise ReadFileError(e)
