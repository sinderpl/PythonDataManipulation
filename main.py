# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 20:16:31 2020

@author: alann
"""

filenames = ("dataSet/securities.csv",
             "dataSet/fundamentals.csv",
             "dataSet/prices.csv",
             "dataSet/prices-split-adjusted.csv")
try:
    with open(filenames[0], encoding='cp1252') as securities:
        print("file loaded")
        # for security in securities:
            # print(security)
except FileNotFoundError:
    print("File could not be found")