"""
pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
built on top of the Python programming language. 
"""

# https://pandas.pydata.org/

import pandas as pd

# Creating Data 
# There are two core objects in pandas: the DataFrame and the Series.

# -------------------------------------------------------------------------- #

# Dataframe
"""
A DataFrame is a table. It contains an array of individual entries, each of which has a certain value. Each entry corresponds to a row (or record) and a column.
"""

"""
# Create a dataframe with integers
records = pd.DataFrame({'Yes': [50, 120], 'No': [20, 100]})
print(records)
"""

"""
# Create a dataframe with strings
ratings = pd.DataFrame({'Bob': ['I liked it', 'It was awful'], 'Sue': ['Pretty good', 'Bland']})
print(ratings)
"""

"""
# Create a dataframe with custom index
productRatings = pd.DataFrame({'Bob': ['I liked it', 'It was awful'], 'Sue': ['Pretty good', 'Bland']}, index=['Product A', 'Product B'])
print(productRatings)
"""

# -------------------------------------------------------------------------- #

# Series
"""
A Series, by contrast, is a sequence of data values. If a DataFrame is a table, a Series is a list. And in fact you can create one with nothing more than a list:
"""

"""
myList = pd.Series([1, 2, 3, 4, 5])
print(myList)
"""

"""
A Series is, in essence, a single column of a DataFrame. So you can assign row labels to the Series the same way as before, using an index parameter. However, a Series does not have a column name, it only has one overall name (run this code to see the name):
"""

"""
sales = pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
print(sales)
"""

# -------------------------------------------------------------------------- #

# Reading data files

"""
Most of the time, we won't actually be creating our own data by hand. Instead, we'll be working with data that already exists.

Data can be stored in any of a number of different forms and formats. By far the most basic of these is the humble CSV file :)
"""

"""
# How a CSV file looks like:

Product A,Product B,Product C
30,21,9
35,34,1
41,11,11

So a CSV file is a table of values separated by commas. Hence the name: "Comma-Separated Values", or CSV.
"""

"""
# To read a CSV file:
products = pd.read_csv('./Pandas-Course/data.csv')    

# Print the read file
print(products)

# To check how large the resulting dataframe is
print(products.shape)

# Prints the first 5 rows (handy when your data is too large!)
print(products.head())
"""

"""
The pd.read_csv() function is well-endowed, with over 30 optional parameters you can specify. For example, you can see in the dataset (second_data.csv) that the CSV file has a built-in index (Index column), which pandas did not pick up on automatically. To make pandas use that column for the index (instead of creating a new one from scratch), we can specify an index_col.
"""

fruits = pd.read_csv('./Pandas-Course/second_data.csv', index_col=0)
print(fruits)
