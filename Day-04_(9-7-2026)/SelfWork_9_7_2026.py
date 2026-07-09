import pandas as pd
import numpy as np

df = pd.read_csv("Renewable_Energy_Usage.csv")

print("\t Dataset information: \n")
print(df.info())

''' 
    ============================================================================
                              DATASET INFORMATION
    ============================================================================

    The dataset contains 1000 household records (ROWS) with 12 Features (COLUMNS).
    Most columns are complete, while a few columns contain missing values.
    Categorical columns have data type 'object'.
    Numerical columns are stored as int64 and float64.
    This information helps identify the structure of the dataset before analysis.
    
'''

print("\n")
print("\t Columns in details: \n")
print(df.columns)

"""    
    there are total 12 columns as name here one by one in order of Index:

       'Household_ID', 'Region', 'Country', 'Energy_Source',
       'Monthly_Usage_kWh', 'Year', 'Household_Size', 'Income_Level',
       'Urban_Rural', 'Adoption_Year', 'Subsidy_Received', 'Cost_Savings_USD'

    with data type dtype='object'
"""


print("\t \t \t \t Statical summary: \n")
print(df.describe())

'''
===============================================================
            STATISTICAL SUMMARY AND ANALYSIS
===============================================================

The describe() function provides statistical information
about all numerical columns in the dataset.

Monthly_Usage_kWh:
- The average monthly energy usage is about 767 kWh.
- The minimum usage is 50.74 kWh and the maximum is 1497.34 kWh.
- This indicates that energy consumption varies among households.

Year:
- The dataset contains records from 2020 to 2024.
- The average year is approximately 2022, showing that the
  dataset represents recent renewable energy usage.

Household_Size:
- Household size ranges from 1 to 8 members.
- The average household consists of about 4 to 5 people.

Adoption_Year:
- Renewable energy adoption ranges from 2010 to 2024.
- Some households adopted renewable energy earlier,
  while others adopted it recently.

Cost_Savings_USD:
- The average annual cost saving is about $248.
- Savings range from approximately $10 to $500,
  showing that financial benefits differ among households.

Overall Analysis:
- The dataset contains a good variation in household size,
  energy usage and cost savings.
- It is suitable for analysing renewable energy usage
  patterns and comparing household energy consumption.

'''

print("\n")
print("\t Missing Values: \n")
print(df.isnull().sum())

''' 
There are Total:
-3 Missing Values in Energy_Source,
-1 in monthly-usage-kwh,
-3 in Income_level and 
-3 in Cost_saving_USD 
'''


'''
===============================================================
                 NULL VALUE HANDLING
===============================================================

The dataset contains a few missing values.

Numerical columns are filled using the mean value
because it preserves the overall average of the data.

Categorical columns are filled using the mode
because it replaces missing values with the most
frequently occurring category.

'''

df["Monthly_Usage_kWh"] = df["Monthly_Usage_kWh"].fillna(
    df["Monthly_Usage_kWh"].mean()
)

df["Cost_Savings_USD"] = df["Cost_Savings_USD"].fillna(
    df["Cost_Savings_USD"].mean()
)


df["Energy_Source"] = df["Energy_Source"].fillna(
    df["Energy_Source"].mode()[0]
)

df["Income_Level"] = df["Income_Level"].fillna(
    df["Income_Level"].mode()[0]
)

print("\nMissing Values After Cleaning")
print(df.isnull().sum())

'''
===============================================================
           OVERALL DEDUCTION OF INFORMATION
===============================================================

Higher household size generally results in greater monthly energy usage.

Different renewable energy sources may provide different levels of cost savings.

Government subsidies encourage households to adopt renewable energy systems.

Households that adopted renewable energy earlier may experience greater long-term savings.

Higher monthly energy usage may lead to increased annual cost savings after adopting renewable energy.

Income level may influence the ability of households to invest in renewable energy.

Energy consumption patterns may differ between urban and rural households.

Different countries and regions show varying renewable energy usage patterns.

Renewable energy adoption helps reduce dependence on conventional energy sources.

The dataset demonstrates that household characteristics, geographical location, and renewable energy adoption collectively influence energy consumption and financial savings.
'''
