

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

# def main(): # I should try and create some type of test data; still don't know how the data will be passed though


class QueriedData:
    'Class to encompass the transition from database queries to Json dictionaries.'
    # isDefault = "true"
    jsonDict = {}
    organizedData = []
       
    def __init__(self, title, sType, queriedData, **kwargs): #insert other arguments
        'Constructor. **kwargs will be a dictionary of specified chart options'
                        
        self.queriedData = queriedData
        self.title = title
        self.sType = sType
        
        # debugging code to show the **kwargs (chart options)
        if kwargs is not None:
            # indicate that we are not using the default format (ie we are specifying chart options)
            # self.isDefault = false
            
            for key, value in kwargs.iteritems():
                print "%s == %s" %(key,value)
        
        
    def creatDict(self): #insert other arguments
        'Create a Json dictionary incorporating queried data and the Highcharts functions.'
        
        # organize 2-D list into a 1-D list
        #=======================================================================
        # orgDataIndex = 0
        # for col in queriedData:
        #     for row in queriedData: # this may be inverted order to organize by
        #         organizedData[orgDataIndex].add(queriedData[row][col])
        #         orgDataIndex += 1
        #=======================================================================
        
        # create chart object--set appropriate chart options using the Highcharts functions (ie add_data_set) based on what options were passed to QueriedData constructor
        chart = Highchart()
        chart.title(self.title)
        
        for row in self.queriedData:
            orgDataIndex = 0
            for element in range(1, len(row)): # access individual elements of the list that is within the outer list (how the 2d list is build)
                # ^ skip first column because it has the name of the variable, not a value
                self.organizedData[orgDataIndex].append(element)
                orgDataIndex += 1
            chart.add_data_set(self.organizedData, series_type=self.sType, name=self.queriedData[row][0]) # name is assumed to be in the 0th column of each row
        
        chart.set_options(EXAMPLE_CONFIG) # add further configs
                                          # current EXAMPLE_CONFIG provides default visual options; can be found in examples.py
        
        # Using chart.__export_options__(), create a Json dictionary (member variable)
        return chart.__export_options__() # return new json dictionary
        
        
    def exportDict(self): #insert other arguments
        'Send the dictionary to the appropriate location to be displayed on the web. Could be implemented using PyHighcharts.highcharts.charts.show()'
        
        # self-explanatory
        