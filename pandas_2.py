import pandas as pd

# pandas data frames 

t = pd.DataFrame()
print(t)

t = pd.DataFrame([1,2,3])
print(t)

t = pd.DataFrame([[1,2,3],['a','b','c'],[True, False, True]])
print(t)

t = pd.DataFrame({"id": [1,2,3]})
print(t)

t = pd.DataFrame({"id": [1,2,3], "name": ['a','b','c'], "isGood": [True, False, True]}) # only equal dict
print(t)

t = pd.DataFrame([ {'a':1, 'b':2}, {'a':3, 'b':4 , 'c':5} ]) # unequal dict is ok
print(t)

t = pd.DataFrame({"id": pd.Series([12,23,34]), "s.no": pd.Series([1,2,3,4])}) # dictionar of series - enequal is ok
print(t)
print(t['id'][0]) # access




