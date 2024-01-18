"""
A dataset in CSV format is given for the Fire Department of New York City. Analyze the dataset to determine:

The total number of fire department facilities in New York city
The number of fire department facilities in each borough
The facility names in Manhattan
"""

# Import necessary libraries
import pandas as pd

# Import the dataset and
input_file = "resources/FDNY.csv"
df_dataset_raw = pd.read_csv(input_file)

# View the content of the data and the first five records
print(df_dataset_raw.describe())
print("\n")
print(df_dataset_raw.head())
print("\n")

# Skip the duplicate header row and verify if the dataset is fixed
df_dataset_raw_fixed = pd.read_csv(input_file, skiprows=1)
print(df_dataset_raw_fixed.head())
print("\n")

# View the data statistics (Hint: use describe() method)
print(df_dataset_raw_fixed.describe())
print("\n")

# View the attributes of the dataset (Hint: view the column names)
print(df_dataset_raw_fixed.columns)
print("\n")

# View the index of the dataset
print(df_dataset_raw_fixed.index)
print("\n")

# Find the total number of fire department facilities in New York city
# Count number of records for each attribute
print(df_dataset_raw_fixed.count())
print("\n")

# View the datatypes of all three attributes
print(df_dataset_raw_fixed.dtypes)
print("\n")

# Find the total number of fire department facilities in each borough
# Select FDNY information boroughwise
df_dataset_borough = df_dataset_raw_fixed.groupby('Borough')
print("\n")

# View FDNY informationn for each borough
print(df_dataset_borough.size())

# Find the total number of fire department facilities in Manhattan
# Select FDNY information for Manhattan
df_dataset_manhattan = df_dataset_raw_fixed.get_group('Manhattan')

# View FDNY information for Manhattan
print(df_dataset_manhattan.size())
