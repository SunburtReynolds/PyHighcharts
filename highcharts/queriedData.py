

from PyHighcharts.highcharts.options import ChartOptions, \
    ColorsOptions, CreditsOptions, ExportingOptions, \
    GlobalOptions, LabelsOptions, LangOptions, \
    LegendOptions, LoadingOptions, NavigationOptions, PaneOptions, \
    PlotOptions, SeriesData, SubtitleOptions, TitleOptions, \
    TooltipOptions, xAxisOptions, yAxisOptions
    
from PyHighcharts.highcharts.chart import Highchart 

from PyHighcharts.highcharts.highchart_types import Series, SeriesOptions, HighchartsError, MultiAxis
from PyHighcharts.highcharts.common import Formatter

# Stdlib Imports
import datetime, random, webbrowser, os, inspect
from _abcoll import Iterable

class QueriedData:
    'Class to encompass the transition from database queries to Json dictionaries.'
    # isDefault = "true"
    jsonDict = {}
    organizedData = []
       
    def __init__(self, queriedData, numSeries, **kwargs): #insert other arguments
        'Constructor. **kwargs will be a dictionary of specified chart options'
                        
        self.queriedData = queriedData
        self.numSeries = numSeries
        
        # debug code to show the **kwargs (chart options)
        if kwargs is not None:
            # indicate that we are not using the default format (ie we are specifying chart options)
            self.isDefault = false
            
            for key, value in kwargs.iteritems():
                print "%s == %s" %(key,value)
        
        
    def creatDict(self): #insert other arguments
        'Create a Json dictionary incorporating queried data and the Highcharts functions.'
        
        # organize 2-D list into a 1-D list
        orgDataIndex = 0
        for col in queriedData:
            for row in queriedData: # this may be inverted order to organize by
                organizedData[orgDataIndex].add(queriedData[row][col])
        
        
        # create chart object--set appropriate chart options using the Highcharts functions (ie add_data_set) based on what options were passed to QueriedData constructor
        
        
        # Using chart.__export_options__(), create a Json dictionary (member variable)
        
        
    def exportDict(self): #insert other arguments
        'Send the dictionary to the appropriate location to be displayed on the web. Could be implemented using PyHighcharts.highcharts.charts.show()'
        
        # self-explanatory
        