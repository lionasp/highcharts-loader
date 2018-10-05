from highcharts_loader import ChartLoader, Options

options = Options(from_file='options.json')
chart = ChartLoader(options, image_type='application/png')
# print base64 code
print(chart.get_data_image())
