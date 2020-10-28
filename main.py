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
    with open(filenames[1], encoding='cp1252') as securities:
        print("file loaded")
        
        
        #Get column names
        # print(securities.readline().split(","))
        column_names = (securities.readline())
        for column in column_names.split(","):
            print(column)
        
        #Print all
        # for security in securities:
            # print(security)
except FileNotFoundError:
    print("File could not be found")