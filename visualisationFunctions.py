# -*- coding: utf-8 -*-
"""

Utilises the power of matplotlib / seaborn to visualise data sets

@author: A00209408
"""

import matplotlib.pyplot as plt


def apply_boxplot(ax, data: [], title, y_label) -> plt.Axes:
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
    ax.set_title(title)
    ax.set_ylabel(y_label)
    ax.boxplot(data)
    return ax

