import json
from typing import Optional, Dict, Any

from .exceptions import EmptyParams, TooManyParams


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

        self.data: Dict[str, Any] = json.loads(open(from_file).read()) if from_file else from_dict
