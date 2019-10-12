import json
from base64 import b64encode

import urllib.request
import urllib.error
from typing import Dict, Any, Optional

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
        :param url: highcarts server url. You can run your own server for unlimited usage
        """
        self._image_type: str = image_type
        self._url: str = url
        self._chart_data: Dict[str, Any] = options.data
        self._chart_raw_data: Optional[bytes] = None

    def get_data_image(self) -> str:
        """ Return string for embedded to <img> tag. """
        return 'data:image/{0};charset=utf-8;base64,{1}'.format(self._image_type, self._decoded_chart())

    @property
    def chart_raw_data(self) -> bytes:
        if self._chart_raw_data is None:
            self._chart_raw_data = self._make_request()
        return self._chart_raw_data

    def save_to_file(self, path: str):
        try:
            f = open(path, 'wb+')
        except OSError as e:
            raise SaveFileError(e)

        f.write(self.chart_raw_data)
        f.close()

    def _get_prepared_request(self) -> urllib.request.Request:
        req = urllib.request.Request(self._url)

        req.add_header('Content-Type', 'application/json; charset=utf-8')
        req.add_header('User-Agent', 'python-urllib')
        req.add_header('Accept-Encoding', 'gzip, deflate')
        req.add_header('Accept', '*/*')
        req.add_header('Connection', 'keep-alive')

        return req

    def _prepared_request_data(self) -> bytes:
        data: Dict[str, Any] = {
            'type': self._image_type,
            'options': self._chart_data
        }

        return json.dumps(data).encode('utf-8')

    def _make_request(self) -> bytes:
        try:
            response = urllib.request.urlopen(self._get_prepared_request(), self._prepared_request_data())
        except (urllib.error.HTTPError, urllib.error.URLError) as e:
            raise HTTPError(e)
        return response.read()

    def _decoded_chart(self) -> str:
        return b64encode(self.chart_raw_data).decode()
