import pandas as pd

print( pd.__version__ )

lst = [1, 2.4, "hi hello bye buffalo", -1]
s1 = pd.Series(lst)
print(s1)
print(type(s1))

s2 = pd.Series([1,2,3,4])
print(s2)

empty_s = pd.Series([])
print(empty_s)

s3 = pd.Series([1,2,3,4], index = ['a','b','c','d'], dtype=float)
print(s3)

s3 = pd.Series([1,2,3,4], index = ['a','b','c','d'], dtype=float, name="data values")
print(s3)

single_s = pd.Series(0.5, index = [1,2,3])
print(single_s)

single_s = pd.Series(0.5)
print(single_s)

single_s = pd.Series({0:3, 1:6})
print(single_s)

s2 = pd.Series([1,2,3,4])
print(s2)
print(s2[1])
print(s2[0:3])
print(max(s2))
print(min(s2))
print(s2[s2>2])

print("----------------------------------------------------------------------------")
s4= pd.Series([1,2,3,4,5])
print(s4)
s5= pd.Series([6,7,8,9,10])
print(s5)
s6= pd.Series([6,7,8])
print(s6)

print(s4+s5)
print(s4+s6)