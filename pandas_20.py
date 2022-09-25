import pandas as pd

# pivot table
d = pd.DataFrame({'Gener':['action','history','mythology','sci-fi','thriller'], 'Year':[2020,2021,2022,2019,2019], 'Budget(mn$)':[25,53,2,54,900], 'Rating(stars)':[4.9,5.0,4.8,4.7,4.5]})
print(d)

print(d.pivot_table(index='Year')) # mean
print(d.pivot_table(index='Year', columns='Gener'))
print(d.pivot_table(index='Year', columns='Gener', aggfunc='count'))
print(d.pivot_table(index='Year', columns='Gener', aggfunc='max'))
print(d.pivot_table(index='Year', columns='Gener', aggfunc='sum'))

print(d.pivot_table(index='Year', columns='Gener', aggfunc='sum', fill_value='-')) # fill NaN value
print(d.pivot_table(index='Year', columns='Gener', aggfunc='sum', fill_value='-' , margins=True)) # give the net value as per the aggfunc