"""
Analyze the Federal Aviation Authority (FAA) dataset using Pandas to do the following:
1. View
-aircraft make name
-state name
-aircraft model name
-text information
-flight phase
-event description type
-fatal flag

2. Clean the dataset and replace the fatal flag NaN with “No”
3. Find the aircraft types and their occurrences in the dataset
4. Remove all the observations where aircraft names are not available
5. Display the observations where fatal flag is “Yes”
"""

# Import necessary libraries
import pandas as pd

# Import the FAA (Federal Aviation Authority) dataset
input_file = "resources/faa_ai_prelim.csv"
df_dataset = pd.read_csv(input_file)

# View shape, first five observations and all the columns present in the dataset
print(df_dataset.shape)
print("\n")
print(df_dataset.head())
print("\n")
print(df_dataset.columns)
print("\n")

# Create a new dataframe with only the required columns
columns = ['ACFT_MAKE_NAME', 'LOC_STATE_NAME', 'ACFT_MODEL_NAME', 'RMK_TEXT', 'FLT_PHASE',
           'EVENT_TYPE_DESC', 'FATAL_FLAG']
df_new = pd.DataFrame(df_dataset[columns])

# View the type of the object and check if the dataframe contains all the required attributes
print(type(df_new))
print("\n")
print(df_new.head())
print("\n")

# Replace all Fatal Flag missing values with the required output and verify if the missing values
# are replaced
df_new['FATAL_FLAG'].fillna(value='No', inplace=True)
print(df_new.head())
print("\n")

# Check the number of observations
print(df_new.shape[-1])
print("\n")

# Drop the values/observations from the dataset where aircraft names are not available
df_new.dropna(subset=['ACFT_MAKE_NAME'], inplace=True)
print("\n")

# Check the number of observations to compare it with the original dataset and see how many values
# have been dropped
print(df_new.shape)
print("\n")

# Group the dataset by aircraft name
# View the number of times each aircraft type appears in the dataset (Hint: use the size() method)
aircraft_type = df_new.groupby('ACFT_MAKE_NAME')
print(aircraft_type)
print(aircraft_type.size())
print("\n")

# Group the dataset by fatal flag
# View the total number of fatal and non-fatal accidents
fatal_flag = df_new.groupby('FATAL_FLAG')
print(fatal_flag)
print(fatal_flag.size())
print("\n")

# Create a new dataframe to view only the fatal accidents (Fatal Flag values = Yes)
df_accidents_yes = fatal_flag.get_group('Yes')
print(df_accidents_yes)
