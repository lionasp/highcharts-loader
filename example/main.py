from src.options import Options

from src.chart_loader import ChartLoader

options = Options(from_file='options.json')
chart = ChartLoader(options)
chart.save_to_file('result.png')
