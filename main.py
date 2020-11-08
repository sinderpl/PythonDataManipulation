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
"""I realised later we can use sets, I thought it would be a more 
   interesting challenge to use multi dimmensional arrays.
"""
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

print("Welcome to the stock analysis program")
while keep_running:
    user_input = -1
    print("List of available actions: ")
    print("\t1.View stock information \n")
    print("\t2.File viewer \n")
    try:
        user_input = int(input("Please choose an action or choose -1 to cancel: \n"))
    except ValueError:
        print("Invalid input, please try again \nd")
       
        
    # Main program loop
    if user_input == -1:
        keep_running == False
        break
    elif user_input == 1: # View stock information
        print("Choose a ticker symbol to display company info")
        tickers = list()
        for row in range(len(file_data[0][2])):
            tickers.append(file_data[0][2][row].split(",")[0].replace('"',''))
        ticker_output = ""
        for row in range(len(tickers)):
            ticker_output += "\t|" + tickers[row] + "|"
            if row % 8 == 0:
                ticker_output += "\n"
        print(ticker_output) 
        stock_choice = (input("\nPlease enter the stock you are interested in: \n")).upper()
        if stock_choice in tickers:
            print("Stock Found, displaying statistical data on the daily closing prices: ")
            median = 0.0
            mean = 0.0
            mode = 0.0
            standard_deviation = 0.0
            stock_close_values = list()
            stock_volumes = list()
            for row in file_data[2][2]:
                try:
                   date, symbol, open_col, close, low, high, volume =  row.split(",")
                   if symbol == stock_choice and close and volume: # We dont want null values in either field
                       stock_close_values.append(close)
                       stock_volumes.append(volume)
                except ValueError:
                    print("error")
                    pass # if we are missing a value we skip it
            #Print out statistics
                # Min and Max
            print("Minimnum value: ", f'{float(min(stock_close_values)):.2f} $')
            print("Maximum value: ",  f'{float(max(stock_close_values)):.2f} $')
        else:
            print("The stock does not exist, please try again")
    elif user_input == 2: # View any columns in the data
        print("Select file to display available columnns:")
        for file_index in range(len(file_data)):
            print("\t",str(file_index)+".",file_data[file_index][0])
            print("\t\tTotal Available columns: ", len(file_data[file_index][1]))
        try:
            file_choice = int(input("Please select filename index to display columns: \n"))
            if file_choice in range(len(file_data)):
                print("Columns in file: \n")
                for column_index in range(len(file_data[file_choice][1])):
                    print("\t",str(column_index)+".",file_data[file_choice][1][column_index])
                try:
                    column_choice = int(input("Please select a column to display data"))
                    if column_choice in range(len(file_data[file_choice][1])):
                        print("Viewing rows for column", file_data[file_choice][1][column_choice], ":\n")
                        for row in file_data[file_choice][2]:
                          row_corresponding_column = row.split(",")[column_choice]
                          #No need to display empty columns
                          if row_corresponding_column:
                              print(row_corresponding_column)
                    else:
                        print("Invalid column selected")
                except ValueError:
                    print("Invalid column selected")
            else:
                print("Invalid file choice")
        except ValueError:
            print("Invalid input, please try again \n")
    
        




# Simple  search code for later
# stocks_found = set()
# for row in file_data[1][2]:
#     stock_ticker = row.split(",")[0]
#     if "BA" in stock_ticker:
#         stocks_found.add(stock_ticker)
# print(stocks_found)
    

    

