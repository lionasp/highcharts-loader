import json
from base64 import b64encode

import urllib.request
import urllib.error
from typing import Dict, Any

from .options import Options
from .exceptions import HTTPError, SaveFileError


class ChartLoader:
    """
        Take Options object and load chart from highcharts API in specified format.
    """

    def __init__(self, options: Options, image_type: str = 'image/png', url: str = 'http://export.highcharts.com/'):
        """
        :param options: Options object
        :param image_type: Available types: image/png, image/jpeg, image/svg+xml, application/pdf
        """
        self._image_type = image_type

        req = urllib.request.Request(url)

        req.add_header('Content-Type', 'application/json; charset=utf-8')
        req.add_header('User-Agent', 'python-urllib')
        req.add_header('Accept-Encoding', 'gzip, deflate')
        req.add_header('Accept', '*/*')
        req.add_header('Connection', 'keep-alive')

        data: Dict[str, Any] = {
            'type': image_type,
            'options': options.data
        }

        binary_data: bytes = json.dumps(data).encode('utf-8')

        try:
            response = urllib.request.urlopen(req, binary_data)
        except (urllib.error.HTTPError, urllib.error.URLError) as e:
            raise HTTPError(e)
        self.raw_chart_data: bytes = response.read()

    def _decoded_chart(self) -> str:
        return b64encode(self.raw_chart_data).decode()

    def get_data_image(self) -> str:
        """ Return string for embedded to <img> tag. """
        return 'data:image/{0};charset=utf-8;base64,{1}'.format(self._image_type, self._decoded_chart())

    def get_raw_data(self) -> bytes:
        return self.raw_chart_data

    def save_to_file(self, path: str):
        try:
            f = open(path, 'wb+')
        except OSError as e:
            raise SaveFileError(e)
        f.write(self.raw_chart_data)
        f.close()
