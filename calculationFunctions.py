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
    data.sort()
    length = len(data)
    try:
        if length > 0 and length % 2 == 0:
            median_upper  = data[math.ceil(length / 2)]
            median_lower = data[math.ceil(length / 2) - 1]
            return round((median_upper + median_lower)/2, 2)
        elif length > 0 and not length % 2 == 0:
            return round(data[math.ceil(length / 2)])
    except ZeroDivisionError:
        return 0.0
    
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
    try:
        standard_deviation_total = 0.0    
        standard_deviation_count = 0
        for value in data:
            standard_deviation_total += (value - mean)**2
            standard_deviation_count += 1
        return round((math.sqrt(standard_deviation_total/standard_deviation_count)), 2)
    except ZeroDivisionError:
        return 0.0

def calculate_correlation_skewness_kurtosis(data_first: [], mean_first: float, data_second: [], mean_second: float) -> []:
    """
    

    Parameters
    ----------
    data_first : []
        First data set to compare to
    mean_first : float
        Mean of the first data set
    data_second : []
        Second data set to correlate to first
    mean_second : float
        Mean of the second data set

    Returns
    -------
    []
        correlation value between two data sets, skewness, kurtosis and population variance of first data set

    """
    total_data_first_multiply_data_second = 0.0
    total_data_first_square = 0.0
    total_second_square = 0.0
    total_data_first_minus_mean = 0.0
    """
        We use this piece of code to calculate the Pearson coefficient but also at the same time
        piggyback on some of the calculations being done to improve performance
    """
    skewness = 0.0
    kurtosis = 0.0
    try:
        for index in range(len(data_first)):
            # Calculations
            #  A
            close_price_minus_mean = data_first[index] - mean_first
            total_data_first_minus_mean += close_price_minus_mean
            skewness += ((close_price_minus_mean) ** 3) / len(data_first)
            kurtosis += ((close_price_minus_mean) ** 4) / len(data_first)
            # B
            volume_minus_mean = data_second[index] - mean_second
            # A x B
            close_multiply_volume = close_price_minus_mean * volume_minus_mean
            #  A^2
            close_price_minus_mean_square = close_price_minus_mean ** 2
            #  B^2
            volume_minus_mean_square = volume_minus_mean ** 2 
            # Totals
            total_data_first_multiply_data_second += close_multiply_volume
            total_data_first_square += close_price_minus_mean_square
            total_second_square += volume_minus_mean_square
        return round((total_data_first_multiply_data_second / math.sqrt(total_data_first_square * total_second_square)), 2),skewness, kurtosis, total_data_first_square
    except ZeroDivisionError:
        return 0.0, 0.0, 0.0, 0.0
    
def calculate_quartiles(data: []) -> []:
    """
    Calculates quartile ranges ofa data set

    Parameters
    ----------
    data : []
        Data set from which you want the quartile ranges

    Returns
    -------
    []
        tuple of Q1 and Q3 quartile ranges (Median is Q2 and last val is Q4)

    """
    data.sort()
    lower_half = data[:len(data) // 2]
    upper_half = data[len(data) // 2 :]
    return calculate_median(lower_half), calculate_median(upper_half)

def calculate_outliers(data: []) -> {}:
    """
    Calculates the outliers and their occurence in a data set.
    This is based on a calculation of the 1.5 deviations from the
    Inter Quartile range
    Inter Quartile range is calculate by taking away Q3 - Q1

    Linear running complexity big O(n), could be improved further
    Parameters
    ----------
    data [] : TYPE
        data set from which we want to identify the outliers

    Returns
    -------
    []
        A data set possibly containing outlier values
        
    """
    data.sort()
    q1, q3 = calculate_quartiles(data)
    interquartile_range = (q3 - q1) * 1.5
    
    upper_limit = q3 + interquartile_range
    lower_limit = q1 - interquartile_range
    
    result = set()
    
    for value in data:
        if value > upper_limit or value < lower_limit:
            result.add(value)
    return result
    
    