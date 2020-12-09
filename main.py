# -*- coding: utf-8 -*-
"""
    A script that allows the user to analyse stock market data
    
    The user is given a output containg the stocks he can view the data for.
    Statistical analysis is then performed on certain columns in the files.
    Afterwards, the data is written to a text file for further reference
    
@author: A00209408
"""
import preProcessing
import calculationFunctions as stat
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


        
# User menu choices
def main_menu_user_choice_1():
    """
    Main user menU choice, displays the
    data specific to a company
    Returns
    -------
    None.
    """
    print("Choose a ticker symbol to display company info")
    tickers = list()
    for row in range(len(file_data[0][2])):
        tickers.append(file_data[0][2][row].split(",")[0].replace('"',''))
    ticker_output = ""
    # The output was very long so I have attempted to put it into a simple table
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
                # We dont want null values in either field, if either is null we dont consider it
                if symbol == stock_choice and close and volume: 
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
        
            # Min, Max, range
        min_closing_price = min(stock_close_values)
        max_closing_price = max(stock_close_values)
        range_closing_price = round(max_closing_price - min_closing_price,2)
            
        print("Minimnum value: ", min_closing_price, "$")
        print("Maximum value: ", max_closing_price, "$")
        print("Range value: ",  range_closing_price, "$")
        
            # Mean
        mean_closing_price = stat.calculate_mean(stock_close_values)
        print("Mean is:", mean_closing_price ,'$')
        
            # Median
        median = stat.calculate_median(stock_close_values)
        print("Median is:", median ,'$')
            
            # Mode
        mode = stat.calculate_mode(stock_close_values)
        print("Mode is:", mode, "$")
        
            # Standard deviation
        standard_deviation = stat.calculate_standard_deviation(stock_close_values, mean_closing_price)
        print("Standard deviation:", standard_deviation,'$')
        
            # Mean of volume
        mean_volume =  stat.calculate_mean(stock_volumes)
        
            # Correlation calculation
        correlation, skewness, kurtosis, total_closing_price_square = stat.calculate_correlation_skewness_kurtosis(stock_values_unsorted, mean_closing_price, stock_volumes, mean_volume)
    
        print("The Correlation coefficient value is: ", correlation)
        
        # Variance of entire population
        try:
            population_variance = float(f'{total_closing_price_square / len(stock_values_unsorted):.2f}')
            print("Population variance is: ", population_variance)
        except ZeroDivisionError:
            print("The population variance could not be calculated as the data source is empty")
        
        # Skewness
        try:
            skew = float(f'{skewness / standard_deviation**3:.2f}')
            print("Skewness value: ", skew)
        except ZeroDivisionError:
            print("The skew could not be calculated as the data source is empty")
            
        # Kurtosis
        try:
            kurtosis = float(f'{kurtosis / standard_deviation**4:.2f}')
            print("Kurtosis value: ", kurtosis)
        except ZeroDivisionError:
            print("The kurtosis could not be calculated as the data source is empty")
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
                new_file.write("Kurtosis : "+ str(skew) + "\n")
            print("The data has been written to:", file_name)
        except FileExistsError:
            pass
    else:
        print("The stock does not exist, please try again.")
        # Simple suggestion system
        stocks_found = set()
        for row in file_data[1][2]:
            stock_ticker = row.split(",")[0]
            if stock_choice in stock_ticker:
                stocks_found.add(stock_ticker)
        if stocks_found:
            print("Some stock suggestions you could have meant: ")
            print(stocks_found)

def main_menu_user_choice_2():
    """
    Main user menu choice, allows to search the files for specific
    columns and info inside of them
    Returns
    -------
    None.

    """
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
        

if __name__ == "__main__":
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
            main_menu_user_choice_1()
        elif user_input == 2: # View any columns in the data
            main_menu_user_choice_2()

