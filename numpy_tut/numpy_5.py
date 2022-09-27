import numpy as np

# arry slicing(:)
a = np.arange(1,101).reshape(10,10)
print(a)
print(a[0,0].ndim)
print(a[0]) # row
print(a[0].ndim)
print(a[:,0]) # col
print(a[:,0:1]) # col 2d

print(a[ 1:4, 1:4])
print(a[:])
print(a[::])
print(a[:,:])

print(a.itemsize)
print(a.dtype) # = 64/8