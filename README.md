highcharts-loader
=================

It is a small library that can load charts from [highcharts](http://highcharts.com/) on server side. 
After loading chart you can save it to file or embed it into your html page in base64 format. 

```python
from highcharts_loader import ChartLoader, Options

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

## Unlimited usage
For unlimited usage you should to run own server rather than relying on the public 
export.highcharts.com server which is rate limited. You can use solution from this 
[repo](https://github.com/ONSdigital/highcharts-export-docker)

**How to use:**

1. Run export server with docker

   * Without docker-compose (run next command in terminal for expose the service on port 8080):
    ```bash
    docker run -d --name highcharts -p 8080:8080 onsdigital/highcharts-export-node
    ```

   * With docker-compose (paste next command to docker-compose.yml file):
    
    ```yml
    highcharts:
        image: onsdigital/highcharts-export-docker
        ports:
          - "8080"
    
    ```
    
2. Send url param to ChartLoader instance
    ```python
    chart = ChartLoader(options, url='http://localhost:8080')
    ```

## todo
* Add tests
* Add typing
