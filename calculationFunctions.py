# -*- coding: utf-8 -*-
"""

This file contains any statistical calculation methods


@author: A00209408

"""
import math


# Calculation functions
def calculate_mean(data: []) -> float:
    """
    Calculates the mean based on the input array
    
    Parameters
    ----------
    data : [] data values to perform mean
    analysis on

    Returns
    -------
    float
        The mean of the values
    """
    try:
        return round(sum(data) / len(data), 2)
    except ZeroDivisionError:
        return 0.0

def calculate_median(data: []) -> float:
    """
    Calculates the median based on the input array
    
    Parameters
    ----------
    data : [] 
        data values to perform median analysis on

    Returns
    -------
    float
        Median of the values
    """
    length = len(data)
    if length > 0 and length % 2 == 0:
        median_upper  = data[math.ceil(length / 2)]
        median_lower = data[math.ceil(length / 2) - 1]
        return round((median_upper + median_lower)/2, 2)
    elif length > 0 and not length % 2 == 0:
        return round(data[math.ceil(length / 2)])
    
def calculate_mode(data: []) -> float:
    """
    Calculates the mode based on the input array
    
    Parameters
    ----------
    data : []
        data values to perform mode analysis on

    Returns
    -------
    float
        Mode of the values

    """
    return float(f'{max(set(data), key=data.count):.2f}')
    

def calculate_standard_deviation(data: [], mean: float) -> float:
    """
    Calculates the standard deviation based on the input array
    
    Parameters
    ----------
    data : []
        data values to perform standard deviation analysis on

    Returns
    -------
    float
        standard deviation of the values

    """
    standard_deviation_total = 0.0    
    standard_deviation_count = 0
    standard_deviation = 0.0
    for value in data:
        standard_deviation_total += (value - mean)**2
        standard_deviation_count += 1
    return round((math.sqrt(standard_deviation_total/standard_deviation_count)), 2)

def calculate_pearsons_coefficient():
    
    