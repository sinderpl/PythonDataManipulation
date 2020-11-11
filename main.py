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
file_path_statistics = "dataSets/statisticalCalculations/"
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

print("Welcome to the stock analysis program\n")
while keep_running:
    user_input = -2
    print("\nList of available actions: ")
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
            stock_close_values = list()
            stock_volumes = list()
            stock_volumes_temp = list()
            for row in file_data[2][2]:
                try:
                    date, symbol, open_col, close, low, high, volume =  row.split(",")
                    if symbol == stock_choice and close and volume: # We dont want null values in either field
                        stock_close_values.append(float(f'{float((close)):.2f}'))
                        stock_volumes_temp.append(volume.rstrip())
                except ValueError:
                    pass # if we are missing a value we skip it
            #Print out statistics
            stock_values_unsorted = stock_close_values.copy()
            for volume in stock_volumes_temp:
                try:
                    stock_volumes.append(int(volume))
                except ValueError:
                    stock_volumes.append(float(volume))
            stock_close_values.sort()
            
                # Min and Max
            min_closing_price = min(stock_close_values)
            max_closing_price = max(stock_close_values)
            range_closing_price = max_closing_price - min_closing_price
            print("Minimnum value: ", min_closing_price, "$")
            print("Maximum value: ", max_closing_price, "$")
            print("Range value: ",  range_closing_price, "$")
            
                # Mean
            total = 0.0    
            count = 0
            mean_closing_price = 0.0
            mean_closing_price = 0.0
            for stock_value in stock_close_values:
                total += stock_value
                count += 1
            try:
                mean_closing_price = float(f'{(total / count):.2f}')
                print("Mean is:", mean_closing_price ,'$')
            except ZeroDivisionError:
                print("The mean could not be calculated as the data source is empty")
                
                # Median
            length = len(stock_close_values)
            median = 0.0
            if length > 0 and length % 2 == 0:
                median_upper  = stock_close_values[math.ceil(length / 2)]
                median_lower = stock_close_values[math.ceil(length / 2) - 1]
                median = float(f'{(median_upper + median_lower)/2:.2f}')
                print("Median is:", median ,'$')
            elif length > 0 and not length % 2 == 0:
                median = float(f'{stock_close_values[math.ceil(length / 2)]:.2f}') 
                print("Median is : ", median, '$')
                
                # Mode
            mode = float(f'{max(set(stock_close_values), key=stock_close_values.count):.2f}')
            print("Mode is:", mode, "$")
            
            standard_deviation_total = 0.0    
            standard_deviation_count = 0
            standard_deviation = 0.0
                # Standard deviation
            if mean_closing_price > 0.0:
                for stock_value in stock_close_values:
                    standard_deviation_total += (stock_value - mean_closing_price)**2
                    standard_deviation_count += 1
                    standard_deviation = float(f'{math.sqrt(standard_deviation_total/standard_deviation_count):.2f}')
                print("Standard deviation:", standard_deviation,'$')
            else:
                print("No Mean available so can't calculate standard deviation")
                
                #Pearson's Correlation coefficient
                
                # Mean of volume
            mean_volume = 0.0
            total_volume = 0.0
            count_volume = 0.0
            for volume in stock_volumes:
                total_volume += volume
                count_volume += 1
            mean_volume = float(f'{(total_volume / count_volume):.2f}')
            
            # Correlation calculation
            total_closing_price_multiply_volume = 0.0
            total_closing_price_square = 0.0
            total_volume_square = 0.0
            for index in range(len(stock_values_unsorted)):
                # Calculations
                #  A
                close_price_minus_mean = stock_values_unsorted[index] - mean_closing_price
                # B
                volume_minus_mean = stock_volumes[index] - mean_volume
                # A x B
                close_multiply_volume = close_price_minus_mean * volume_minus_mean
                #  A^2
                close_price_minus_mean_square = close_price_minus_mean ** 2
                #  B^2
                volume_minus_mean_square = volume_minus_mean ** 2 
                # Totals
                total_closing_price_multiply_volume += close_multiply_volume
                total_closing_price_square += close_price_minus_mean_square
                total_volume_square += volume_minus_mean_square
            correlation = 0.0
            try:
                correlation = float(f'{total_closing_price_multiply_volume / math.sqrt(total_closing_price_square * total_volume_square):.2f}')
                print("The Correlation coefficient value is: ", correlation)
            except ZeroDivisionError:
                print("The correlation could not be calculated as the data source is empty")
            
            # Variance of entire population
            population_variance = 0.0
            try:
                population_variance = float(f'{total_closing_price_square / len(stock_values_unsorted):.2f}')
                print("Population variance is: ", population_variance)
            except ZeroDivisionError:
                print("The population variance could not be calculated as the data source is empty")
            
            # Skewness 
            skew = 0.0
            print(mean_closing_price)
            print(median)
            print(standard_deviation)
            try:
                skew = float(f'{((mean_closing_price - median) **3) / standard_deviation:.2f}')
                print("Skewness value: ", skew)
            except ZeroDivisionError:
                print("The skew could not be calculated as the data source is empty")
            # Save values to a text file
            try:
                file_name = file_path_statistics +stock_choice+".txt"
                with open(file_name, "w") as  new_file:
                    new_file.write("Minimum value: " + str(min_closing_price) +"\n")
                    new_file.write("Maximum value: " + str(max_closing_price) +"\n")
                    new_file.write("Range value: " + str(range_closing_price) +"\n")
                    new_file.write("Mean: "+ str(mean_closing_price) + "\n")
                    new_file.write("Median: "+ str(median) + "\n")
                    new_file.write("Mode: " + str(mode) + "\n")
                    new_file.write("Standard Deviation: "+ str(standard_deviation) +"\n")
                    new_file.write("Correlation coefficient: "+ str(correlation) + "\n")
                    new_file.write("Population variance: "+ str(population_variance) + "\n")
                    new_file.write("Skew : "+ str(skew) + "\n")
                print("The data has been written to:", file_name)
            except FileExistsError:
                pass
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
    

    

