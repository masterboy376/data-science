import pandas as pd

# DatetimeIndex
d = pd.read_csv('./samples/airtravel.csv', parse_dates=['Date'])
print(d)
print(type(d.Date[0]))