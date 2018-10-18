import json
from base64 import b64encode

import requests


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
        self.url = url
        self.image_type = image_type

        response = requests.post(self.url, data={
            'type': image_type,
            'options': json.dumps(options.data)
        })

        if response.status_code == requests.codes.ok:
            self.raw_chart_data = response.content
        else:
            response.raise_for_status()

    def _decoded_chart(self):
        return b64encode(self.raw_chart_data).decode()

    def get_data_image(self):
        """ Return string for embedded to <img> tag. """
        return 'data:image/{0};charset=utf-8;base64,{1}'.format(self.image_type, self._decoded_chart())

    def get_raw_data(self):
        return self.raw_chart_data

    def save_to_file(self, path):
        f = open(path, 'wb+')
        f.write(self.raw_chart_data)
        f.close()
