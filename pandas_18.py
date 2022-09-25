import pandas as pd

#join()
df1 = pd.DataFrame({'A': [1,2,3],
                   'B': [10,20,30]})
 
 
df2 = pd.DataFrame({'C': [4,5,6],
                   'D': [40,50,60]})
 
print(df1)
print(df2)

print(df1.join(df2))
print(df2.join(df1))

df1 = pd.DataFrame({'A': [1,2,3],
                   'B': [10,20,30]},
                   index = ['a','b','c'])
 
df2 = pd.DataFrame({'C': [4,5],
                   'D': [40,50]},
                  index = ['a','b'])
print(df1)
print(df2)

print(df1.join(df2))
print(df1.join(df2, how = 'right'))
print(df1.join(df2, how = 'left'))
print(df1.join(df2, how = 'inner'))
print(df1.join(df2, how = 'outer'))

df1 = pd.DataFrame({'A': [1,2,3],
                   'B': [10,20,30]})
 
df2 = pd.DataFrame({'A': [4,5,6],
                   'D': [40,50,60]})
print(df1)
print(df2)

print(	df1.join(df2, lsuffix = '_1'))
print(	df1.join(df2, rsuffix = '_1'))