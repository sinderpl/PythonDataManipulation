# -*- coding: utf-8 -*-
"""
    A script that allows the user to analyse stock market data
@author: A00209408
"""
import preProcessing
import math

# Program loop
keep_running = True
user_input = -1

#Data sets
file_path = "dataSets/updatedDataSet/"
file_extension = ".csv"
file_data = (# filename[0] #Columns[1] #Rows[2] 
              ("securities", list(), list()),
              ("fundamentals", list(), list()),
              ("prices", list(), list())
            )

# Load the data sets into memory
for file_index in range(len(file_data)):
    try:
        filename = file_path + file_data[file_index][0] + file_extension
        with open(filename, encoding='cp1252') as file_content:
            #Parse in the columns
            for column_name in file_content.readline().split(","):
                file_data[file_index][1].append(column_name.rstrip())
            #Parse in the rows
            for row in file_content.readlines():
                file_data[file_index][2].append(row)
    except FileNotFoundError:
        print("File could not be found", filename)

# Simple user based search
stocks_found = set()
for row in file_data[1][2]:
    stock_ticker = row.split(",")[0]
    if "BA" in stock_ticker:
        stocks_found.add(stock_ticker)
print(stocks_found)
    
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
        for i in range(len(file_data)):
            print(str(i)+".",file_data[i][0])
        input("Please select filename index to display columns: ")
        
        
    
        

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



    

