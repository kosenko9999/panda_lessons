import pandas as pd
from pandas import Series, DataFrame


obj = Series([1, 2, 3, 4, 5])
print(obj.name)
print(obj.index.name)


obj2 = Series([6, 7, 8], ["f", "a", "a"])
print(obj2)

print(obj2*3)
print(obj[obj > 4])


#Creating Series from dict
dict_test = {1: "11", 2: "22", 3: "33"}
obj3 = Series(dict_test)
print(obj3)
test_index = [5, 2, 1, 6, 7, 3]

obj4 = Series(dict_test, test_index)
print(obj4)

#Working with missing data. Function isnull, notnull
print(pd.isnull(obj4))
print(pd.notnull(obj4))

# Sum Series with different index
obj4.name= "String numbers"
obj4.index.name = "Numbers"

print(obj4)



