import pandas as pd

# elaborate on interpolate()
d = pd.read_csv('./samples/airtravel.csv')
print(d)
# print(d.interpolate(axis=1)) # 0->coloumn(default) 1->row->same datatype
print(d.interpolate(limit=1))
print(d.interpolate(limit=1, limit_direction='both'))
print(d.interpolate(limit_area='inside'))
d.interpolate(limit_area='inside', implace = True)
print(d)

