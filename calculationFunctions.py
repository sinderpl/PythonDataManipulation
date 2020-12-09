# -*- coding: utf-8 -*-
"""

This file contains any statistical calculation methods


@author: A00209408

"""
import math


# Calculation functions
def calculate_mean(data: []) -> float:
    """
    Simple calculate mean function based on the input array

    Parameters
    ----------
    data : data values to perform mean
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
    length = len(data)
    if length > 0 and length % 2 == 0:
        median_upper  = data[math.ceil(length / 2)]
        median_lower = data[math.ceil(length / 2) - 1]
        return round((median_upper + median_lower)/2, 2)
    elif length > 0 and not length % 2 == 0:
        return round(data[math.ceil(length / 2)])