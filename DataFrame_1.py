import pandas as pd
from pandas import DataFrame, Series

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
dataframe3 = DataFrame(data, columns=["state", "year", "pop", "debt"], index=["one", "two", "three", "four", "five"])
print(dataframe3.columns)


# Get value of column as Series
print(type(dataframe3.state))
print(type(dataframe3.loc["three"]))

print(dataframe3)
dataframe3.debt = [0, 0, 0, 0, 100]
print(dataframe3["state"].value_counts())





