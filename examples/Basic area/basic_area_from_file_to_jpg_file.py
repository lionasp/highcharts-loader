from highcharts_loader.chart_loader import ChartLoader
from highcharts_loader.options import Options

options = Options(from_file='options.json')
chart = ChartLoader(options, image_type='image/jpeg')
# save to file
chart.save_to_file('result.jpg')
