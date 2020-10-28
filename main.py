# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 20:16:31 2020

@author: alann
"""

with open("dataSet/securities.csv", encoding='cp1252') as securities:
    print(securities)
    for security in securities:
        print(security)