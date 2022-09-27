import numpy as np

# random sampling
a = np.random.random()
print(a)

a1 = np.random.random(3)
print(a1)

a2 = np.random.random((3,3))
print(a2)

i= np.random.randint(1,4)
print(i)

i1= np.random.randint(1,4, 1)
print(i1)

i2= np.random.randint(1,4,(4,4))
print(i2)

i3= np.random.randint(1,4,(4,4,2))
print(i3)

np.random.seed(10) # 2**32 - 1  ---->  pattern
s1i3= np.random.randint(1,4,(4,4,2))
print(s1i3)

np.random.seed(10)
s2i3= np.random.randint(1,4,(4,4,2))
print(s2i3)

a1 = np.random.rand(3)
print(a1)

a2 = np.random.rand(3,3)
print(a2)

a1 = np.random.randn(3)
print(a1)

a2 = np.random.randn(3,3)
print(a2)

l = [1,2,3,4,56,7,9]
c = np.random.choice(l)
print(c)
for i in range (10):
    c = np.random.choice(l)
    print(c)

p = np.random.permutation(l)
print(p)
p = np.random.permutation(l)
print(p)
