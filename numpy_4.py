import numpy as np

a1 = np.arange(1,10).reshape(3,3)
a2 = np.arange(1,10).reshape(3,3)
print(a1)
print(a2)

add = np.add(a1, a2) # or + operator
print(add)
subtract = np.subtract(a1, a2) # or - operator
print(subtract)
divide = np.divide(a1, a2) # or / operator
print(divide)
print(a1*a2) #element wise multiplication
print( np.multiply(a1,a2) ) #element wise multiplication
print(a1 @ a2) # matrix multiplication
print(a1.dot(a2)) # matrix multiplication

print( a1.max() )
print( a1.argmax() )

print(a1.max(axis = 0)) # 0-> column wise, 1->row wise
print(a1.max(axis = 1)) # 0-> column wise, 1->row wise

# similarlly min function

sum = np.sum(a1);
print(sum)

sum = np.sum(a1, axis = 0);
print(sum)

mean = np.mean(a1)
print(mean)

sqrt = np.sqrt(a1)
print(sqrt)

std = np.std(a1)
print(std)

exp = np.exp(a1)
print(exp)

log = np.log(a1)
print(log)

log10 = np.log10(a1)
print(log10)