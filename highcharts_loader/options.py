import json

from .exceptions import EmptyParams, ToManyParams


class Options:
    data = {}

    def __init__(self, *, from_file=None, from_dict=None):
        if not from_file and not from_dict:
            raise EmptyParams('You should pass "from_file" or "from_dict" param.')
        if from_file and from_dict:
            raise ToManyParams('You should pass only one param: "from_file" or "from_dict".')

        self.data = json.loads(open(from_file).read()) if from_file else from_dict
