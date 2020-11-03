# -*- coding: utf-8 -*-
"""
@author: A00209408

Reads in the original data sets and filters out unnecessary items
"""

#Data sets

original_filenames = ("dataSets/originalDataSet/securities.csv",
              "dataSets/originalDataSet/fundamentals.csv",
              "dataSets/originalDataSet/prices.csv"
             )

updated_filenames = ("dataSets/updatedDataSet/securities.csv",
              "dataSets/updatedDataSet/fundamentals.csv",
              "dataSets/updatedDataSet/prices.csv"
             )
fundamentals_columns_needed = (
    "Ticker Symbol",
    "Period Ending",
    "Accounts Payable",
    "Accounts Receivable",
    "Add'l income/expense items",
    "After Tax ROE",
    "Capital Expenditures",
    "Cash Ratio",
    "Cash and Cash Equivalents",
    "Changes in Inventories",
    "Common Stocks",
    "Cost of Revenue",
    "Current Ratio",
    "Earnings Before Interest and Tax",
    "Fixed Assets",
    "Gross Margin",
    "Gross Profit",
    "Income Tax",
    "Inventory",
    "Investments",
    "Liabilities",
    "Net Borrowings",
    "Net Cash Flow",
    "Net Income",
    "Net Income Applicable to Common Shareholders",
    "Operating Income",
    "Operating Margin",
    "Profit Margin",
    "Retained Earnings",
    "Total Assets",
    "Total Liabilities",
    "Earnings Per Share")

fundamentals_original_columns_indexing = list()
fundamentals_column_names = list()
# Rewrite the files with updates where necessary:
    
    #Securities.csv
try:
    with open(original_filenames[0], encoding='cp1252') as file_content:
        print("Securities file opened", original_filenames[0] )
        with open(updated_filenames[0], "w") as  new_file:
            new_file.write(file_content.read())
except FileNotFoundError:
    print("File could not be found", original_filenames[0])
    
    
    #Fundamentals.csv
    """
        We will filter certain columns out based on the "fundamentals_columns_needed"
        tuple found above
    """
try:
    with open(original_filenames[1], encoding='cp1252') as file_content:
        print("Fundamentals file opened", original_filenames[1] )
        # We need to filter out the columns we dont want to but we also need to do this
        # for each row record
        columns = file_content.readline().split(",")
        with open(updated_filenames[1], "w") as  new_file:
            for index in range(len(columns)):
                if columns[index] in fundamentals_columns_needed:
                    # Grab the original indexing and column names we want IF they appear in the csv
                    # Will give some protection against column corruptions
                    fundamentals_original_columns_indexing.append(index)
                    fundamentals_column_names.append(columns[index])  
            new_file.write(",".join(fundamentals_column_names))
            new_file.write("\n")
            
            # Based on the above column info we can filter out unnecessary columns in the rows
            # For now we will add empty rows too
            for line in file_content.readlines():
                line_content = ""
                row = line.split(",")
                for index in range(len(row)):
                    if index in fundamentals_original_columns_indexing:
                        line_content += (row[index]+",")
                        # line_content += (fundamentals_column_names[index]+",")
                new_file.write(line_content[:len(line_content)-1]) # Remove final comma
except FileNotFoundError:
    print("File could not be found", original_filenames[1])
    
    
    #Prices.csv
try:
    with open(original_filenames[2], encoding='cp1252') as file_content:
        print("Prices file opened", original_filenames[2] )
        with open(updated_filenames[2], "w") as  new_file:
            new_file.write(file_content.read())
except FileNotFoundError:
    print("File could not be found", original_filenames[2])