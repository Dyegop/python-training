"""
BASIC CONCEPTS:
-Pandas is a library built on top of numpy.
-It allows for fast analysis and data cleaning and preparation.
-It can work with data from a wide variety of resources.
-The main data types in Pandas are Series and Dataframes.

DATATYPES EQUIVALENCE (PANDAS-PYTHON:
-object       -> str or mixed - Text or mixed numeric and non-numeric values
-int64	      -> int - Integer numbers
-float64      -> float - Floating point numbers
-bool         -> bool - True/False values
-datetime64	  -> datetime - Date and time values
timedelta[ns] -> NA - Differences between two datetimes
category	  -> NA	- Finite list of text values

SERIES:
-Series are similar to a NumPy array (it is built on top of the NumPy array object).
-Series admits accessing data (ser[0]), slicing (ser1[1:3]) and sum (ser1 + ser2)
-Properties:
    -Series can hold any arbitrary Python Object, even functions.
    -List, arrays, or dictionary can be converted to Series.
    -Series will use numbers as indexes by default for list or arrays if no label is set.
    -Series will use keys as indexes for dictionaries.

DATAFRAMES:
-Dataframes are a bunch of series that shares the same indexes.
-Properties:
    -To apply changes permanently, we must set Inplace=True.
    -Conditional selection = dataframe[conditions][['columns']]
    -All the operations available in numpy are also available in Pandas(mean, max, min, etc.)
"""

import numpy as np
import pandas as pd


# -----------------PANDAS - BASICS-----------------

# Create series
# data  -> input data, it can be lists, arrays or dictionaries
# index -> a list of index values
ser1 = pd.Series(data=[1, 2, 3, 4], index=['USA', 'Germany', 'USSR', 'Japan'])
ser2 = pd.Series(data=[1, 2, 3, 4], index=['USA', 'Germany', 'Italy', 'Japan'])
serie_from_list = pd.Series(data=[10, 20, 30], index=['a', 'b', 'c'])
serie_from_dict = pd.Series({'a': 10, 'b': 20, 'c': 30})
serie_from_array = pd.Series(np.array([10, 20, 30]), ['a', 'b', 'c'])

# Create dataframe
# data    -> input data, it can be lists, arrays or dictionaries
# index   -> a list of index values
# columns -> tags for each column
df1 = pd.DataFrame(
    data=np.random.randn(5, 4), index='A B C D E'.split(), columns='W X Y Z'.split()
)
df2 = pd.DataFrame(np.random.randn(5, 4), 'A B C D E'.split(), 'W X Y Z'.split())
df3 = pd.DataFrame(
    {'col1': [1, 2, 3, 4], 'col2': [444, 555, 666, 444], 'col3': ['abc', 'def', 'ghi', 'xyz']}
)
df4 = pd.DataFrame({'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]})
df5 = pd.DataFrame({'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
                    'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
                    'Sales': [200, 120, 340, 124, 243, 350]})

# Cast a pandas object (Serie, Dataframe, Index) to a specified dtype
df1["W"].astype(int)
ser1.astype(str)

# Atributes
# index   -> return indexes of a serie/dataframe
# values  -> return values of a serie/dataframe
# columns -> return columns of a serie/dataframe
# dtype   -> return datatype of the serie
# dtypes  -> return datatypes of every column in a dataframe
# size    -> return the number of elements in a serie/dataframe object
# shape   -> return a tuple with the shape of a dataframe

# Parameters
# inplace=True/False      - apply/discard changes
# axis='index'/0          - apply function to each column
# axis='column'/1         - apply function to each row
# label='string'          - label name to remove
# numeric_only=True/False - include only float, int or boolean
# sort=True/False         - sorted/not sorted
# ascending=True/False    - sort in ascending/descending order

# Accessors (only for series)
# Each accessor has its own properties and methods
# Check https://pandas.pydata.org/pandas-docs/stable/reference/series.html for more information
# dt     -> access data of type Datetime, Timedelta, Period
# str    -> access data of type String
# cat    -> access data of type Categorical
# sparse -> access data of type Sparse

# Options
# set_option(opt_name, value) -> set a value to an option
# reset_option(opt_name)      -> reset option to their default value. Use 'all' to reset all
# display.max_rows            -> change the max rows to be displayed (use None to display all)
# display.max_columns         -> change the max cols to be displayed (use None to display all)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)




# -----------------DATAFRAMES - DATA ACCESS-----------------

# Get basic information
# info()     -> return general information about a dataframe
# head(n)    -> return first n rows (5 by default)
# tail(n)    -> return last n rows (5 by default)
print(df1.info())
print(df1.head())
print(df1.tail())

# Access data (simplest way)
# Conditions can be applied to get data
print(df1['W'])                              # Get column 'W'
print(df1[['W', 'Z']])                       # Get columns 'W', 'Z'
print(df1.W)                                 # Get column 'W', SQL syntax
print(df1 > 0)                               # Return df1 with True/False as values
print(df1[df1 > 0])                          # Return df1 values > 0
print(df1[df1['W'] > 0])                     # Return rows where 'W' > 0
print(df1[df1['W'] > 0][['Y', 'X']])         # Return rows from ['Y', 'X'] columns if condition
print(df1[(df1['W'] > 0) & (df1['Y'] > 1)])  # Use & (and) or | (or) for more or one condition

# Access data with loc/iloc and at/iat
# loc['str'] -> return values based on labels
# iloc[int]  -> return values based on integer positon
# at['str']  -> access a single value for a row/column pair by label
# iat[int]   -> access a single value for a row/column pair by integer position
print(df1.loc['A'])                     # return all columns for row 'A'
print(df1.loc[:, 'A'])                  # return all rows for column 'A'
print(df1.loc['B', 'Y'])                # return all values in row 'B', column 'Y
print(df1.loc[['A', 'B'], ['W', 'Y']])  # return all values in rows 'A', 'B', columns 'W', 'Y'
print(df1.iloc[:, 2])                   # return all values in column at position 2
print(df1.at['A', 'W'])                 # return value in row 'A', column 'W'
print(df1.iat[0, 2])                    # return value in row at position 0, column at position 2

# Create new dataframe from selected data
df_new = df1[df1[['W', 'Z']]]  # new dataframe from columns 'W', 'Z' of df1

# Add new columns to a dataframe
df1['new1'] = df1['W'] + df1['Y']
df1['new2'] = np.random.randn(5)
df1.loc[:, 'new3'] = df1[df1['X'] > 3]  # new column with values in column 'X' > 3




# -----------------DATAFRAMES - OPERATIONS-----------------

# Return values/indexes
# unique()       -> return unique values in a column
# nunique()      -> return the number o unique values in a column
# idxmax(axis=)  -> returns index of first occurrence of maximum over requested axis
# idxmin(axis=)  -> returns index of first occurrence of minimum over requested axis
print(df3['col2'].unique())
print(df3['col2'].nunique())
print(df3.loc[df3['abc'].idxmax()])

# Count values
# value_counts(sort=)         -> return how many times each unique value occur in a column in
# descending order
# count(axis=, numeric_only=) -> count non-NA cells for each column or row
print(df3.count())
print(df3['col2'].value_counts())

# Check values
# isnull()       -> find or check null values
# isin(values)   -> check whether each element in the DataFrame is contained in values, returning
# a df of booleans
print(df3.isnull())
print(df3.loc[df3['col2'].isin(444)])  # print values in column 'col2' that are equal to 444

# Aggregate functions
# sum()       -> return the sum of selected values
# mean()      -> return the mean of selected values
# max()       -> return the max value of selected values
# min()       -> return the min value of selected values
# corr()      -> find the pairwise correlation of selected columns
# describe()  -> generate descriptive statistics.
# transpose() -> transpose index and columns
print(df3['col1'].mean())
print(df3[['col1', 'col2']].corr())

# apply(function) -> allow you to apply functions to a dataframe
# Usually, we will use lambda expressions to apply functions
def times2(x):
    return x*2
df3['col1'].apply(times2)
df3['col2'].apply(lambda x: x*2)

# sort_values(by='attr', ascending=, inplace=) -> sort values in a dataframe by given attribute
df3.sort_values('col2', inplace=True)

# agg([functions], axis=) -> aggregate using one or more operations over the specified axis
df3['col1'].agg("sum", "min")

# drop(label=, axis=, inplace=) -> remove columns or rows
df3.drop('E', axis=0, inplace=True)

# dropna(axis=, how=, thresh=, subset=, inplace=) -> remove missing values
# how='any'/'all' - remove any rows/columns with missing values or only rows/columns with all
# missing values
# thresh='value'  - determine how many missing values a row or columns must have to be removed
df4.dropna(axis="index", how="all")

# fillna(value=) -> fill missing values with the parameter given
df4.fillna(value='')
df4['A'].fillna(value=df4['A'].mean())

# groupby() -> group rows together based off of a column name
by_comp = df3.groupby("Company")
# We can call aggregate methods off the object:
print(by_comp.std())
print(by_comp.describe().transpose())




# -----------------DATAFRAMES - INDEXING-----------------

# set_index(keys) -> set dataframe indexes using existing column
# inplace=True required to apply changes
df1['States'] = 'CA NY WY OR CO'.split()  # add index column
df1.set_index('States', inplace=True)     # apply changes

# reset_index() -> reset index to default (0, 1, 2,...)
df1.reset_index()

# Multi-index dataframe
outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = pd.MultiIndex.from_tuples(list(zip(outside, inside)))
df3 = pd.DataFrame(np.random.randn(6, 2), index=hier_index, columns=['A', 'B'])
# Access multi-index
print(df3.loc['G1'].loc[1])

# Set names to multiple indexes
df3.index.names = ['Group', 'Num']

# Return cross-section of indexes with xs()
print(df3.xs(['G1', 1]))
print(df3.xs(1, level='Num'))

# Pivot tables
# pivot() -> reshaped a DataFrame organized by given index/column values
# This function does not support data aggregation
# Multiple values will result in a MultiIndex in the columns
# pivot_table() -> create a spreadsheet-style pivot table as a DataFrame
# The levels in the pivot table will be stored in MultiIndex objects
data = {'A': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'], 'B': ['one', 'one', 'two', 'two', 'one', 'one'],
        'C': ['x', 'y', 'x', 'y', 'x', 'y'], 'D': [1, 3, 2, 5, 4, 1]}
df4 = pd.DataFrame(data)
df4.pivot_table(values='D', index=['A', 'B'], columns=['C'])




# -----------------DATAFRAMES - MANAGE DATAFRAMES-----------------

# concat() -> glue together DataFrames. Dimensions should match along the axis you are
# concatenating on
df_c1 = pd.DataFrame(
    {
        'A': ['A0', 'A1', 'A2', 'A3'],
        'B': ['B0', 'B1', 'B2', 'B3'],
        'C': ['C0', 'C1', 'C2', 'C3'],
        'D': ['D0', 'D1', 'D2', 'D3']
    },
    index=[0, 1, 2, 3]
)
df_c2 = pd.DataFrame(
    {
        'A': ['A4', 'A5', 'A6', 'A7'],
        'B': ['B4', 'B5', 'B6', 'B7'],
        'C': ['C4', 'C5', 'C6', 'C7'],
        'D': ['D4', 'D5', 'D6', 'D7']
    },
    index=[4, 5, 6, 7]
)
df_c3 = pd.DataFrame(
    {'A': ['A8', 'A9', 'A10', 'A11'],
     'B': ['B8', 'B9', 'B10', 'B11'],
     'C': ['C8', 'C9', 'C10', 'C11'],
     'D': ['D8', 'D9', 'D10', 'D11']
     },
    index=[8, 9, 10, 11]
)
print(pd.concat([df_c1, df_c2, df_c3]))
print(pd.concat([df_c1, df_c2, df_c3], axis=1))

# merge(df1, df2, how=, on=) -> merge DataFrames together using a similar logic as merging SQL
# how={'left', 'right', 'outer', 'inner'} -> merge logic, default 'inner'
# on={'column', 'index'}                  -> column or index level names to join on
left = pd.DataFrame(
    {
        'key1': ['K0', 'K0', 'K1', 'K2'],
        'key2': ['K0', 'K1', 'K0', 'K1'],
        'A': ['A0', 'A1', 'A2', 'A3'],
        'B': ['B0', 'B1', 'B2', 'B3']
    }
)
right = pd.DataFrame(
    {
        'key1': ['K0', 'K1', 'K1', 'K2'],
        'key2': ['K0', 'K0', 'K0', 'K0'],
        'C': ['C0', 'C1', 'C2', 'C3'],
        'D': ['D0', 'D1', 'D2', 'D3']
    }
)
pd.merge(left, right, on=['key1', 'key2'])
pd.merge(left, right, how='outer', on=['key1', 'key2'])

# join(df1, df2, how=) -> combine columns into a single result DataFrame
# how={'left', 'right', 'outer', 'inner'} -> join logic, default 'left'
# on={'column', 'index'}                  -> column or index level names to join on
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'], 'B': ['B0', 'B1', 'B2']}, index=['K0', 'K1', 'K2'])
right = pd.DataFrame({'C': ['C0', 'C2', 'C3'], 'D': ['D0', 'D2', 'D3']}, index=['K0', 'K2', 'K3'])
left.join(right)
left.join(right, how='outer')




# -----------------PANDAS - DATA INPUT/OUTPUT-----------------

# Read data from several sources
# read_csv()   -> read data from csv files
# read_excel() -> read data from Excel files (formulas or macros can't be imported)
# read_html()  -> read tables off of a webpage and return a list of DataFrame objects
# read_sql()   -> read SQL query or database table (from string or SQLAlchemy Selectable)
# read_table() -> read general delimited file (for example, csv, url, etc.)

# Some input arguments
# dtype=dict/str - datatype for data (str) or columns (dict) | Only for csv/excel/table
# encoding=str   - encoding use to decode a web page | Only for html
# header=str     - row (or list of rows for a MultiIndex) for the columns headers
# sep=str        - delimiter to use | Only for tables/csv

# Examples
df_csv = pd.read_csv('directory/file.csv')
df_excel = pd.read_excel('directory/file.xlsx', sheet_name='Sheet1')
df_html = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')

# Write data to several sources
# Dataframes, Series and Indexes can be written to different files or datatypes (dict, list, str,
# csv, excel, etc)
# Check https://pandas.pydata.org/pandas-docs/stable/reference/io.html for more information
# about arguments
# to_csv()     -> save data to csv file
# to_excel()   -> save data to excel file
# to_json()    -> save data to json file
# to_string()  -> save data to string datatype
# to_dict()    -> save data to dict datatype
# to_list()    -> save data to list datatype

# Some input arguments
# index=True/False - save/don't save index as columns
# encoding=str     - encoding use to decode a web page
# sheetname=str    - string used for sheet name | Only for Excel
df_csv.to_csv("export.csv", index=False)
df_excel.to_excel("export.xlsx", 'Sheet1')
