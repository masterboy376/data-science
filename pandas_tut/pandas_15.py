import pandas as pd

# groupBy()
d = pd.read_csv('./samples/airtravel.csv')
print(d)

print(d.groupby(by = 'Month').groups)
print(d.groupby(by = ['Month']).groups)
for Month in d:
    print(Month);
print(d.groupby(by = 'Month').get_group('JAN'))
print(d.groupby(by = 'Month').get_group('JAN').sum())
print(d.groupby(by = 'Month').get_group('JAN').mean())
print(d.groupby(by = 'Month').get_group('JAN').describe())
print(d.groupby(by = 'Month').get_group('JAN').agg(['sum', 'max']))