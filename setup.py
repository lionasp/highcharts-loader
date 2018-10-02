from setuptools import setup
import highcharts_loader

setup(
    name='highcharts-loader',
    version=highcharts_loader.__version__,
    packages=[
        'highcharts_loader'
    ],
    install_requires=[
        'requests==2.19.1'
    ],
    author='Vitalii Pugach',
    author_email='lion.programmer@gmail.com',
    url='https://github.com/lionasp/highcharts-loader',
    description='''Load charts from www.highcharts.com on server side''',
    long_description=open('README.md').read(),
    include_package_data=True,
    keywords='highcharts-loader',
    zip_safe=False,
    license="MIT",
)
