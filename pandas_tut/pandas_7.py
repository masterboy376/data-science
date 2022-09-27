import pandas as pd

#handeling missing values- 1
d = pd.read_csv('./samples/airtravel.csv' , na_values=['not available'])
print(d)
d = pd.read_csv('./samples/airtravel.csv' , na_values={3:'not available'})
print(d)
d = pd.read_csv('./samples/airtravel.csv' , keep_default_na=False)
print(d)
d = pd.read_csv('./samples/airtravel.csv' , na_filter=False) # fast but make sure there is no missing data
print(d)