# -*- coding: utf-8 -*-
"""
Tests for the calculationFunctions  library suite

@author: A00029408
"""

import calculationFunctions as stat

test_set = [-12, 9, 10, 13, 13, 13, 15, 15, 16, 16, 18, 22, 23, 24, 24, 25]

def test_calculate_mean():
    """
    Test the mean function from stat module

    Returns
    -------
    None.

    """
    assert(stat.calculate_mean(test_set)) == 15.25
    
def test_calculate_median():
    """
    Tests the median from the stat module

    Returns
    -------
    None.

    """
    assert(stat.calculate_median(test_set)) == 15.5
    
def test_calculate_mode():
    """
    Tests the mode from the stat module
    
    Returns
    -------
    None.

    """
    assert(stat.calculate_mode(test_set)) == 13
    
def test_calculate_standard_deviation():
    """
    Tests the standard deviation from the stat module
    
    Returns
    -------
    None.

    """
    assert(stat.calculate_standard_deviation(test_set, stat.calculate_mean(test_set))) == 8.61
    
def test_calculate_quartiles():
    """
    
    Tests the quartile calculations from the stat module.

    Returns
    -------
    None.

    """
    
    q1, q3 = stat.calculate_quartiles(test_set)
    assert(q1 == 13)
    assert(q3 == 22.5)
    
def test_calculate_outliers():
    """
    Tests the outlier identification from the stat module

    Returns
    -------
    None.

    """
    
    assert(stat.calculate_outliers(test_set) == {-12})
    
