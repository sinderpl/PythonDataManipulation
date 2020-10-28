# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 20:16:31 2020

@author: alann
"""

try:
    with open("dataSet/securitiess.csv", encoding='cp1252') as securities:
        for security in securities:
            print(security)
except FileNotFoundError:
    print("File could not be found")