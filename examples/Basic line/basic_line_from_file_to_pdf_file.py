from highcharts_loader import ChartLoader, Options

options = Options(from_file='options.json')
chart = ChartLoader(options, image_type='application/pdf')
# save to file
chart.save_to_file('result.pdf')
