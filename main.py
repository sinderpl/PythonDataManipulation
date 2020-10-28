# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 20:16:31 2020

@author: alann
"""

filenames = ("dataSet/securities.csv",
             "dataSet/fundamentals.csv",
             "dataSet/prices.csv",
             # "dataSet/prices-split-adjusted.csv"
             )

def load_file(filename):
    try:
        with open(filename, encoding='cp1252') as file_content:
            print("file loaded", filename )
            
            #Get column names
            column_names = (file_content.readline()) #[1:] #Remove initial id column
            for column in column_names.split(","):
                print(column)
    except FileNotFoundError:
        print("File could not be found")
    


for filename in filenames:
    load_file(filename)



    
