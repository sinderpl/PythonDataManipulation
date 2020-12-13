# -*- coding: utf-8 -*-
"""

Utilises the power of matplotlib / seaborn to visualise data sets

@author: A00209408
"""

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import calculationFunctions as stat


def apply_boxplot(ax: plt.Axes, data: [], title, y_label) -> plt.Axes:
    """
    Creates and returns a boxplot of the data for the user to 
    show or save at his leisure

    Parameters
    ----------
    ax : TYPE
        The Axes to draw on
    data : []
        The data to visualise
    title : TYPE
        Title of the visualisation
    y_label : TYPE
        Title for the Y label

    Returns
    -------
    ax : Axis with the new box plot created 
    
    """
    x_offset = .2
    y_offset = 1.5
    ax.set_title(title)
    ax.set_ylabel(y_label)
    box_plot = ax.boxplot(data)
    
    for i, line in enumerate(box_plot['medians']):
        x, y = line.get_xydata()[1]
        text = ' Median = {:.2f}\n '.format(stat.calculate_median(data))
        ax.annotate(text, xy=(x + .05, y))
        
    q1 , q3 = stat.calculate_quartiles(data)
    for line in box_plot['boxes']:
        
        # Right top corner 
        x, y = line.get_xydata()[4]
        text = x,y, '%.2f' % x,
        text = ' Q1 = {:.2f}\n '.format(q1)
        ax.annotate(text, xy=(x+ x_offset, y - y_offset))     
             
        # Right bottom corner
        x, y = line.get_xydata()[3] 
        text = ' Q3 = {:.2f}\n '.format(q3)
        ax.annotate(text, xy=(x + x_offset, y-y_offset))     
    return ax

def visualise_by_time(ax: plt.Axes, data_time: list(), data_values: list(), title, y_label) -> plt.Axes:
    """
    Visualises the data_values by the timeline month minor year major X axis

    Parameters
    ----------
    ax : plt.Axes
        The Axes to draw on.
    data_time : list()
        Time values for the diagram.
    data_values : list()
        Values to map.
    title : TYPE
        title of the diagram.
    y_label : TYPE
        y axis label description for the mapped data.

    Returns
    -------
    ax : Axis with the new box plot created 
    
    """
    ax.set_title(title)
    
    # Set up dates for X axis
    dates = mdates.datestr2num(data_time)
    months = mdates.MonthLocator()
    ax.xaxis.set_minor_locator(months)
    ax.set_xlabel("Timeline")
    
    # Set up Y axis values
    ax.set_ylabel(y_label)
    
    #Plot the data
    ax.plot_date(dates, list(data_values), marker = ",", linestyle="-")
    return ax
    
def visualise_scatter_plot_correlation(ax: plt.Axes, data_values_x: list(), data_values_y: list(), title, x_label, y_label) -> plt.Axes:
    """
    Visualises the correlation between two parameters

    Parameters
    ----------
    ax : plt.Axes
        The Axes to draw on.
    data_values_x : list()
       value for the x axis
    data_values_y : list()
        value for the y axis
    title : TYPE
        title for the graph
    x_label : TYPE
        label for the x axis
    y_label : TYPE
        label for the y axis        
        
    Returns
    -------
    ax : axes

    """
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    
    ax.scatter(data_values_x, data_values_y, marker =".")
    
    return ax
