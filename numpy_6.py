import numpy as np

# array concatenation and split 
a1 = np.arange(1,17).reshape(4,4)
a2 = np.arange(17,33).reshape(4,4)

l1 = [1,2,3]
l2 = [4,5,6]
print(l1+l2) # list will be concatenated

print( np.concatenate((a1,a2)) ) # array will be concatenated -> column-wise -> axis=0 by default
print( np.vstack((a1,a2)) ) # array will be concatenated -> column-wise
print( np.split(a1,2) ) # array will be splited -> column-wise -> axis=0 by default ----> list
print( np.vsplit(a1, 2)) # array will be splited -> column-wise ----> list

print( np.concatenate((a1,a2), axis=1) ) # array will be concatenated -> row-wise -> axis=1
print( np.hstack((a1,a2)) ) # array will be concatenated -> row-wise
print( np.split(a1,2, axis=1) ) # array will be splited -> row-wise ----> list
print( np.hsplit(a1, 2)) # array will be splited -> row-wise ----> list

d1 = np.array([4,57,3,65,23,3])
print( np.split(d1, [1,3]) ) # -----> split