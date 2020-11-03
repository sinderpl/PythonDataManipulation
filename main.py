# -*- coding: utf-8 -*-
"""
@author: A00209408
"""
import math

# Program loop
keep_running = True

#Data sets
filenames = ("dataSets/updatedDataSet/securities.csv",
              "dataSets/updatedDataSet/fundamentals.csv",
              "dataSets/updatedDataSet/prices.csv",
              "dataSets/updatedDataSet/prices-split-adjusted.csv"
             )
original_data_set = 
columns_securities = list()
rows_securities = list()
user_input = -1



print("Welcome to the stock analysis program")
while keep_running:
    print("List of available actions: ")
    print("1.Display available columns \n")
    input("Please choose an action or choose 0 to cancel")
    
    if user_input == 0:
        keep_running == False
        break

def load_file(filename):
    try:
        with open(filename, encoding='cp1252') as file_content:
            print("file loaded", filename )
            #Get column names
            column_names = (file_content.readline()) #[1:] #Remove initial id column
            for column in column_names.split(","):
                columns.append(column.strip("\n"))
            #Load rows into memory
            for line in file_content.readlines():
                rows.append(line.strip("\n"))
    except FileNotFoundError:
        print("File could not be found")



    # user_choice = input("")
    # if user_choice == 1:
for filename in filenames:
    load_file(filename)

# for column in columns:
print(columns)

for row in rows[1:2]: #List of lists for this
    print(row.split(","))
    print(len(row.split(","))) # City and state are being split into two because delimiter is ,



    

