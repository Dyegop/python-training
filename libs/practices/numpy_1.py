import numpy as np


# EXERCISE 1:

# Dataset:
country = np.array(
    ['Great Britain', 'China', 'Russia', 'United States', 'Korea', 'Japan', 'Germany']
)
country_code = np.array(['GBR', 'CHN', 'RUS', 'US', 'KOR', 'JPN', 'GER'])
country_medal_gold = np.array([29, 38, 24, 46, 13, 7, 11])
country_medal_silver = np.array([17, 28, 25, 28, 8, 14, 11])
country_medal_bronze = np.array([19, 22, 32, 29, 7, 17, 14])

# Find the country with maximum gold medals
# Find the countries with more than 20 gold medals
print(country[country_medal_gold.argmax()])
print(country[country_medal_gold > 20])

# Evaluate the dataset and print the name of each country with its gold medals and total number
# of medals
for i in range(len(country)):
    n_medals = country_medal_gold[i]
    sum_medals = country_medal_gold[i] + country_medal_silver[i] + country_medal_bronze[i]
    print(f"Country: {country[i]}\nGold medals: {n_medals}\nTotal of medals: {sum_medals}\n")






# EXERCISE 2:

# Dataset:
countries = np.array(
    ['Algeria', 'Angola', 'Argentina', 'Australia', 'Austria', 'Bahamas', 'Bangladesh', 'Belarus',
     'Belgium', 'Bhutan', 'Brazil', 'Bulgaria', ' Cambodia', 'Cameroon', 'Chile', 'China',
     'Colombia', 'Cyprus', 'Denmark', 'El Salvador', 'Estonia', 'Ethiopia', 'Fiji', 'Finland',
     'France', 'Georgia', 'Ghana', 'Grenada', 'Guinea', 'Haiti', 'Honduras', 'Hungary',
     'India', 'Indonesia', 'Ireland', 'Italy', 'Japan', 'Kenya', 'South Korea', 'Liberia',
     'Malaysia', 'Mexico', 'Morocco', 'Nepal', 'New Zealand', 'Norway', 'Pakistan', 'Peru',
     'Qatar', 'Russia', 'Singapore', 'South Africa', 'Spain', 'Sweden', 'Switzerland', 'Thailand',
     'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Venezuela', 'Vietnam',
     'Zimbabwe']
)
gdp_values = np.array(
    [2255.225482, 629.9553062, 11601.63022, 25306.82494, 27266.40335, 19466.99052, 588.3691778,
     2890.345675, 24733.62696, 1445.760002, 4803.398244, 2618.876037, 590.4521124, 665.7982328,
     7122.938458, 2639.54156, 3362.4656, 15378.16704, 30860.12808, 2579.115607, 6525.541272,
     229.6769525, 2242.689259, 27570.4852, 23016.84778, 1334.646773, 402.6953275, 6047.200797,
     394.1156638, 385.5793827, 1414.072488, 5745.981529, 837.7464011, 1206.991065, 27715.52837,
     18937.24998, 39578.07441, 478.2194906, 16684.21278, 279.2204061, 5345.213415, 6288.25324,
     1908.304416, 274.8728621, 14646.42094, 40034.85063, 672.1547506, 3359.517402, 36152.66676,
     3054.727742, 33529.83052, 3825.093781, 15428.32098, 33630.24604, 39170.41371, 2699.123242,
     21058.43643, 28272.40661, 37691.02733, 9581.05659, 5671.912202, 757.4009286, 347.7456605]
)

# Find the highest and lowest GDP
print(countries[gdp_values.argmax()])
print(countries[gdp_values.argmin()])

# Print out text ('evaluating country') and input value ('country name') iteratively
for country in countries:
    print("evaluating country " + country)

# Print out the entire list of the countries with their GDPs
for i in range(len(countries)):
    country = countries[i]
    country_gdp = gdp_values[i]
    print(f"{country} {country_gdp}")

# Print highest, lowest, mean, standardized and sum for GPD values
print(gdp_values.max())
print(gdp_values.min())
print(np.mean(gdp_values))
print(np.std(gdp_values))
print(gdp_values.sum())
