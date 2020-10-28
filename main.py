# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 20:16:31 2020

@author: alann
"""

filenames = ("dataSet/securities.csv",
             # "dataSet/fundamentals.csv",
             # "dataSet/prices.csv",
             # "dataSet/prices-split-adjusted.csv"
             )

rows = list()
columns = list()
keep_running = True

def load_file(filename):
    try:
        with open(filename, encoding='cp1252') as file_content:
            print("file loaded", filename )
            #Get column names
            column_names = (file_content.readline()) #[1:] #Remove initial id column
            for column in column_names.split(","):
                columns.append(column)
            #Load rows into memory
            for line in file_content.readlines():
                rows.append(line)
    except FileNotFoundError:
        print("File could not be found")


print("Welcome to the stock analysis program")
# while keep_running:
print("List of available actions: ")
print("1.Display available columns \n")
    # user_choice = input("")
    # if user_choice == 1:
    
    
for filename in filenames:
    load_file(filename)



    
