from highcharts_loader.chart_loader import ChartLoader
from highcharts_loader.options import Options

chart_options = {
    'title': {
        'text': 'Solar Employment Growth by Sector, 2010-2016'
    },

    'subtitle': {
        'text': 'Source: thesolarfoundation.com'
    },

    'yAxis': {
        'title': {
            'text': 'Number of Employees'
        }
    },
    'legend': {
        'layout': 'vertical',
        'align': 'right',
        'verticalAlign': 'middle'
    },

    'plotOptions': {
        'series': {
            'label': {
                'connectorAllowed': False
            },
            'pointStart': 2010
        }
    },

    'series': [{
        'name': 'Installation',
        'data': [43934, 52503, 57177, 69658, 97031, 119931, 137133, 154175]
    }, {
        'name': 'Manufacturing',
        'data': [24916, 24064, 29742, 29851, 32490, 30282, 38121, 40434]
    }, {
        'name': 'Sales & Distribution',
        'data': [11744, 17722, 16005, 19771, 20185, 24377, 32147, 39387]
    }, {
        'name': 'Project Development',
        'data': [None, None, 7988, 12169, 15112, 22452, 34400, 34227]
    }, {
        'name': 'Other',
        'data': [12908, 5948, 8105, 11248, 8989, 11816, 18274, 18111]
    }]
}

options = Options(from_dict=chart_options)
chart = ChartLoader(options)
# save to file
chart.save_to_file('result2.png')
