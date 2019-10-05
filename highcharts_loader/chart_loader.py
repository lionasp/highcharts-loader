import json
from base64 import b64encode

import urllib.request
import urllib.error

from .exceptions import HTTPError, SaveFileError


class ChartLoader:
    """
        Take Options object and load chart from highcharts API in specified format.
    """
    raw_chart_data = None
    image_type = None

    def __init__(self, options, image_type='image/png', url='http://export.highcharts.com/'):
        """
        :param options: Options object
        :param image_type: Available types: image/png, image/jpeg, image/svg+xml, application/pdf
        """
        self.image_type = image_type

        req = urllib.request.Request(url)

        req.add_header('Content-Type', 'application/json; charset=utf-8')
        req.add_header('User-Agent', 'python-urllib')
        req.add_header('Accept-Encoding', 'gzip, deflate')
        req.add_header('Accept', '*/*')
        req.add_header('Connection', 'keep-alive')

        data = {
            'type': image_type,
            'options': options.data
        }

        data = json.dumps(data).encode('utf-8')

        try:
            response = urllib.request.urlopen(req, data)
        except (urllib.error.HTTPError, urllib.error.URLError) as e:
            raise HTTPError(e)
        self.raw_chart_data = response.read()

    def _decoded_chart(self):
        return b64encode(self.raw_chart_data).decode()

    def get_data_image(self):
        """ Return string for embedded to <img> tag. """
        return 'data:image/{0};charset=utf-8;base64,{1}'.format(self.image_type, self._decoded_chart())

    def get_raw_data(self):
        return self.raw_chart_data

    def save_to_file(self, path):
        try:
            f = open(path, 'wb+')
        except OSError as e:
            raise SaveFileError(e)
        f.write(self.raw_chart_data)
        f.close()
