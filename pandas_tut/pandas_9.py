import pandas as pd

#handling missing values- 3
d = pd.read_csv('./samples/airtravel.csv' , na_values=['not available'])
print(d)

print(d.dropna())

print(d.dropna(axis=1)) # 1->column, 0->row => default = 0

print(d.dropna(how = 'any')) # default = any
print(d.dropna(how = 'all'))
print(d.dropna(thresh = 4)) # default = 1
# print(d.dropna(subset = ['Date'])) # only check date column for NaN value

d.dropna(inplace = True) # updates the data set
print(d)


