# -*- coding: utf-8 -*-
"""
@author: A00209408
"""
import preProcessing

import math

# Program loop
keep_running = True

#Data sets
file_path = "dataSets/updatedDataSet/"
file_extensions = ".csv"
filenames = ("dataSets/updatedDataSet/securities.csv",
              "dataSets/updatedDataSet/fundamentals.csv",
              "dataSets/updatedDataSet/prices.csv",
             )
file+data = (  # filename   #Columns #Rows 
              ("securities", list(), list()),
              ("fundamentals", list(), list()),
              ("prices", list(), list())
            )
user_input = -1


print("Welcome to the stock analysis program")
while keep_running:
    print("List of available actions: ")
    print("\t1.File viewer \n")
    user_input = int(input("Please choose an action or choose 0 to cancel: "))
    
    if user_input == 0:
        keep_running == False
        break
    elif user_input == 1:
        print("Select file to display available columnns:")
        for i in range(len(user_friendly_filenames)):
            print(str(i)+".",user_friendly_filenames[i])
        input("Please select filename number to display columns: ")
        
    
        

# def load_file(filename):
#     try:
#         with open(filename, encoding='cp1252') as file_content:
#             print("file loaded", filename )
#             #Get column names
#             column_names = (file_content.readline()) #[1:] #Remove initial id column
#             for column in column_names.split(","):
#                 columns.append(column.strip("\n"))
#             #Load rows into memory
#             for line in file_content.readlines():
#                 rows.append(line.strip("\n"))
#     except FileNotFoundError:
#         print("File could not be found")



#     # user_choice = input("")
#     # if user_choice == 1:
# for filename in filenames:
#     load_file(filename)

# # for column in columns:
# print(columns)

# for row in rows[1:2]: #List of lists for this
#     print(row.split(","))
#     print(len(row.split(","))) # City and state are being split into two because delimiter is ,



    

