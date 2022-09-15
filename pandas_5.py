import pandas as pd

# headers, prefix, names in csv
d = pd.read_csv('./samples/airtravel.csv' , header=1)
print(d)
d = pd.read_csv('./samples/airtravel.csv' , header=None , prefix="columns")
print(d)
d = pd.read_csv('./samples/airtravel.csv' , names=['a','b','c','d'])
print(d)