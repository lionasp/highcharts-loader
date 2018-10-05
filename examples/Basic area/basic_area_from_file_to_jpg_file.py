from highcharts_loader import ChartLoader, Options

options = Options(from_file='options.json')
chart = ChartLoader(options, image_type='image/jpeg')
# save to file
chart.save_to_file('result.jpg')
