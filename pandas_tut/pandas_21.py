import pandas as pd

# melt()
d = pd.DataFrame({'Gener':['action','history','mythology','sci-fi','thriller'], 'Year':[2020,2021,2022,2019,2019], 'Budget(mn$)':[25,53,2,54,900], 'Rating(stars)':[4.9,5.0,4.8,4.7,4.5]})
print(d)

print(pd.melt(d))
print(pd.melt(d, id_vars=['Gener'], value_vars=['Year']))
print(pd.melt(d, id_vars=['Year'], value_vars=['Gener'], var_name='Category'))
print(pd.melt(d, id_vars=['Year'], value_vars=['Gener'], var_name='Category', value_name='Category_val'))