import pandas as pd

#append()
df1 = pd.DataFrame({'A': [1,2,3],
                   'B': [10,20,30]})
 
 
df2 = pd.DataFrame({'A': [4,5,6],
                   'B': [40,50,60]})
 
print(df1)
print(df2)
print(df1.append(df2))
print(df1.append(df2, ignore_index = True))
print(df2.append(df1, ignore_index = True))

df1 = pd.DataFrame({'A': [1,2,3],
                   'B': [10,20,30]})
 
 
df2 = pd.DataFrame({'C': [4,5,6],
                   'B': [40,50,60]})
print(df1)
print(df2)

# deprecated
print(df2.append(df1, ignore_index = True)) # Error due to different column name
print(df2.append(df1, ignore_index = True, sort=False))