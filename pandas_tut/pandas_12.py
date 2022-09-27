import pandas as pd

# fill NaN values in data
# d = pd.read_csv('./samples/airtravel.csv', parse_dates=['Month'])
d = pd.read_csv('./samples/airtravel.csv')
print(d)
print(d.interpolate()) # only work on integer value
print(d.interpolate(method='linear'))
# print(d.interpolate(method='time')) # data type should be date-time
print(d.interpolate(method='index'))
print(d.interpolate(method='nearest'))
print(d.interpolate(method='polynomial', order=1))
print(d.interpolate(method='spline', order=1))

