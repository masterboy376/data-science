import pandas as pd

# merge()
d1 = pd.DataFrame({'ID':[1,2,3,4,5], 'class':['DSA', 'Web development', 'Mobile app development', 'AI/ML', 'GUI Development']})
print(d1)
print('----------------------------------------------------------------------------------------------')
d2 = pd.DataFrame({'ID':[1,2,3,4,5,6], 'credits':[120, 100, 110, 140, 130, 1000]})
print(d2)

# only common rows will be merged
print('----------------------------------------------------------------------------------------------')
print(pd.merge(d1,d2, on=['ID']))
print('----------------------------------------------------------------------------------------------')
print(pd.merge(d1,d2, on='ID'))

print('----------------------------------------------------------------------------------------------')
print(pd.merge(d2,d1, on=['ID']))
print('----------------------------------------------------------------------------------------------')
print(pd.merge(d2,d1, on='ID'))

print('----------------------------------------------------------------------------------------------')
print(pd.merge(d1,d2, on='ID', how='outer')) # inner(default)=intersection, outer=union, right, left
print('----------------------------------------------------------------------------------------------')
print(pd.merge(d1,d2, on='ID', how='right'))
print('----------------------------------------------------------------------------------------------')
print(pd.merge(d1,d2, on='ID', how='left'))

print('----------------------------------------------------------------------------------------------')
d2 = pd.DataFrame({'ID':[6,7,8,9,10], 'credits':[120, 100, 110, 140, 130]})
print(d2)
print('----------------------------------------------------------------------------------------------')
print(pd.merge(d1,d2, on='ID', how='outer'))
print('----------------------------------------------------------------------------------------------')
print(pd.merge(d1,d2, left_index=True, right_index=True))
print('----------------------------------------------------------------------------------------------')
print(pd.merge(d1,d1, on='ID', suffixes=('_left', '_right')))