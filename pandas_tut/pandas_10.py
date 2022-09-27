import pandas as pd

# fillna()
d = pd.read_csv('./samples/airtravel.csv')
print(d)

print(d.fillna(2))
print(d.fillna({"1958":100 , "1959":0, "1960":90, "Date":'null'}))
print(d.fillna(method = 'ffill'))
print(d.fillna(method = 'pad'))
print(d.fillna(method = 'bfill'))
print(d.fillna(axis=1, method='bfill'))
print(d.fillna(axis=1, method='ffill'))
print(d.fillna(0, limit=1))
print(d.fillna(0, inplace=True)) # changes the variable itself
print(d)