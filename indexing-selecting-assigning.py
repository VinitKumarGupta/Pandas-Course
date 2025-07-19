import pandas as pd

# Load dataset
fruits = pd.read_csv('second_data.csv')

# --------------------------------------------------------------------------- #

# Native Accessors in Pandas
"""
Python native objects like lists and dictionaries already provide ways to access data. 
Pandas builds on these, making it familiar and easy to use.
"""

"""
In Python, we often access an object's property using dot notation.
For example, a book object might have a "title" property accessed via:
    book.title

Similarly, in pandas, we can access a DataFrame column like this:
"""
# print("\n", fruits.Oranges)


"""
Alternatively, just like dictionaries use square brackets to access values, 
pandas DataFrames also allow column access with the indexing operator []:
"""
# print("\n", fruits['Mangoes'])


"""
Both methods work. However, using [] is generally safer because it supports column 
names with spaces or special characters. For example, with a column named "Best Before", 
fruits.Best Before would fail, but fruits['Best Before'] would work.
"""


"""
A pandas Series (a single column) behaves like a fancy dictionary or list. 
To drill down to a specific value in a column, we can use another indexing operator:
"""
# print("\n", fruits['Mangoes'][0])

# --------------------------------------------------------------------------- #

# loc and iloc Accessors

"""
Pandas also provides its own accessors: loc and iloc. These are more powerful and 
recommended for advanced operations.

- loc uses labels (row and column names)
- iloc uses integer positions (row and column indices)

Both are row-first, column-second (opposite to native Python indexing).
"""

# Select the first row (all columns) using iloc
# print("\n", fruits.iloc[0])


# Select all rows of the second column using iloc
# print("\n", fruits.iloc[:, 1])


"""
The colon (:) means "everything" for that dimension. 
So `iloc[:, 1]` means all rows of column at index 1.
"""


# Select the first three rows of the second column using iloc
# print("\n", fruits.iloc[:3, 1])


"""
Note:
- In iloc[:3, 1], rows 0, 1, and 2 are selected (upper limit is excluded).
- The second argument selects the column (column index 1).
"""

# Or, to select just the second and third entries of fourth column, we would do:
# print("\n", fruits.iloc[1:3, 3])

"""
You may notice that headers from the csv file is automatically being excluded in the output.
This is because of pandas default property, we'll learn how to include them too in the output,
as it can cause issue if our data doesn't have any column names in the first row of the csv file.
"""

# It's also possible to pass a list:
# print("\n", fruits.iloc[[0, 1, 2, 3], 2])

# --------------------------------------------------------------------------- #

# Negative indexing 

"""
This will start counting forwards from the end of the values. 
So for example here are the last five elements of the dataset.
"""
# print("\n", fruits.iloc[-5:])

# --------------------------------------------------------------------------- #

# Label-based selection
"""
The second paradigm for attribute selection is the one followed by the `loc` operator: label-based selection. In this paradigm, it's the "data index value", not its position, which matters.
"""

# print("\n", fruits.loc[2, 'Oranges'])   # Returns: 11

# `loc` is usually easier than `iloc` due to direct value based accessing
# Here's one operation that's much easier using loc:

# print("\n", fruits.loc[:, ['Mangoes', 'Oranges', 'Apples']])    # Look carefully the column order!

"""
# Choosing between loc and iloc

When choosing or transitioning between `loc` and `iloc`, there is one "gotcha" worth keeping in mind, which is that the two methods use slightly different indexing schemes.

`iloc` uses the Python stdlib indexing scheme, where the first element of the range is included and the last one excluded. So 0:10 will select entries 0,...,9. `loc`, meanwhile, indexes inclusively. So 0:10 will select entries 0,...,10.

Why the change? Remember that `loc` can index any stdlib type: strings, for example. If we have a DataFrame with index values Apples, ..., Potatoes, ..., and we want to select "all the alphabetical fruit choices between Apples and Potatoes", then it's a lot more convenient to index df.`loc`['Apples':'Potatoes'] than it is to index something like df.`loc`['Apples':'Potatoet'] (t coming after s in the alphabet).

This is particularly confusing when the DataFrame index is a simple numerical list, e.g. 0,...,1000. In this case df.i`loc`[0:1000] will return 1000 entries, while df.`loc`[0:1000] return 1001 of them! To get 1000 elements using `loc`, you will need to go one lower and ask for df.`loc`[0:999].

Otherwise, the semantics of using `loc` are the same as those for `iloc`.
"""

# --------------------------------------------------------------------------- #

# Conditional Selection
"""
Conditional Selection with Pandas
This script demonstrates how to filter rows in a DataFrame
based on one or more conditions.
"""

# Select rows where Country is 'India'
# print(fruits.loc[fruits.Country == 'India'])

# Select rows where Country is 'Brazil' AND Mangoes > 20
# print(fruits.loc[(fruits.Country == 'Brazil') & (fruits.Mangoes > 20)])

# Select rows where Country is 'Italy' OR Apples > 30
# print(fruits.loc[(fruits.Country == 'Italy') | (fruits.Apples > 30)])

# --------------------------------------------------------------------------- #

# Built-in Conditional Selectors
"""
Pandas comes with a few built-in conditional selectors, two of which we will highlight here.

The first is `isin`, it lets you select data whose value "is in" a list of values.
"""

# Selects only rows whose "Country" has 'Italy' or 'Brazil'
# print(fruits.loc[fruits.Country.isin(['Italy', 'Brazil'])])

# The second is isnull (and its companion notnull). 
# These methods let you highlight values which are (or are not) empty (NaN)
# print(fruits.loc[fruits.Apples.isnull()])   # Prints the rows having null values in 'Apples'

# --------------------------------------------------------------------------- #


# Assigning data

# Assigning a constant value
fruits['Country'] = 'Japan'
print(fruits)

# Or with an iterable of values:
fruits['Mangoes'] = range(len(fruits), 0, -1)
print(fruits)