import pandas as pd
import numpy as np

# handling missing values- 2
d = pd.read_csv('./samples/airtravel.csv')
print(d)

print(d.isnull())
print(d.isnull().sum())
print(d.isnull().sum().sum())

print(d.notnull())
print(d.notnull().sum())
print(d.notnull().sum().sum())

s = pd.Series([np.nan, 1, 2,3,4,5,np.nan,5,7,8])
print(s)
print(s.isnull())
print(s.isnull().sum()) # == print(s.isnull().sum().sum())
