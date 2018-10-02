highcharts-loader
=================

It is a small library that can load charts from [highcharts](http://highcharts.com/) on server side. 
After loading chart you can save it to file or embed it into your html page in base64 format. 

```python
from highcharts_loader.chart_loader import ChartLoader
from highcharts_loader.options import Options

options = Options(from_file='options.json')
chart = ChartLoader(options)
# save to file
chart.save_to_file('result.png')
```

*options.json* example:
```json
{
    "chart": {
        "type": "bar"
    },
    "title": {
        "text": "Which channels are driving engagement?"
    },
    "xAxis": {
        "categories": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                       "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    },
    "series": [{
        "data": [29.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4]
    }]
}
```

Result:

![result](https://raw.githubusercontent.com/lionasp/highcharts-loader/master/result.png)

You can find more option params on [highcharts official documentation page](https://api.highcharts.com/highcharts/)

## Installation
```bash
pip install git+git://github.com/lionasp/highcharts-loader/@master
```

## todo
* Add directory with examples
* Add docker container for run own server rather than relying on the public export.highcharts.com server which is rate limited.