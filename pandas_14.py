import pandas as pd

# loc[] and iloc[]
d = pd.read_csv('./samples/airtravel.csv')
print(d)

print(d.loc[0])
print(d.loc[[2,3]])
print(d.loc[0, 'Month'])
print(d.loc[0:3, 'Month'])
# print(d.loc[2]<500, ['Month'])
# print(d.loc[[False, False]])
print(d.iloc[0])
print(d.iloc[[0]])
print(d.iloc[[1,0]])
# print(d.iloc[[True, False, True]])

