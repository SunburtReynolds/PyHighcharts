

from PyHighcharts.highcharts.options import ChartOptions, \
    ColorsOptions, CreditsOptions, ExportingOptions, \
    GlobalOptions, LabelsOptions, LangOptions, \
    LegendOptions, LoadingOptions, NavigationOptions, PaneOptions, \
    PlotOptions, SeriesData, SubtitleOptions, TitleOptions, \
    TooltipOptions, xAxisOptions, yAxisOptions 

from PyHighcharts.highcharts.highchart_types import Series, SeriesOptions, HighchartsError, MultiAxis
from PyHighcharts.highcharts.common import Formatter

# Stdlib Imports
import datetime, random, webbrowser, os, inspect
from _abcoll import Iterable

class QueriedData:
    'Class to encompass the transition from database queries to Json dictionaries.'
    
    #what member variables do I want?
    
    def __init__(self): #insert other arguments
        'Constructor.'
        
    def creatDict(self): #insert other arguments
        'Create a Json dictionary incorporating queried data and the Highcharts functions.'
        
    def exportDict(self): #insert other arguments
        'Send the dictionary to the appropriate location to be displayed on the web. Could be implemented using PyHighcharts.highcharts.charts.show()'
        