import pandas as pd

# functions and more parameters in pandas for csv data
d = pd.read_csv('./samples/airtravel.csv')
print(d.head())
print(d.head(6))
print(d.tail())
print(d.tail(6))

d = pd.read_csv('./samples/airtravel.csv', dtype={2:float, 1:float, 3:float})
print(d)
d = pd.read_csv('./samples/airtravel.csv', true_values=['Yes'])
print(d)
d = pd.read_csv('./samples/airtravel.csv', true_values=["Yes"], false_values=["No"])
print(d)