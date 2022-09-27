import pandas as pd

# read parameters in csv file

d = pd.read_csv('./samples/airtravel.csv')
print(d)
print(d.columns)
d = pd.read_csv('./samples/airtravel.csv', nrows=5)
print(d)
d = pd.read_csv('./samples/airtravel.csv', nrows=5, usecols=[0,1])
print(d)
d = pd.read_csv('./samples/airtravel.csv', skiprows=1)
print(d)
d = pd.read_csv('./samples/airtravel.csv', skiprows=[2,8])
print(d)
d = pd.read_csv('./samples/airtravel.csv', index_col="Month")
print(d)
d = pd.read_csv('./samples/airtravel.csv', index_col=2)
print(d)
d = pd.read_csv('./samples/airtravel.csv', index_col=0)
print(d)