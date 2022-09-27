import numpy as np

# string operation, comparison and information
name = "hi bros and sis"
str = "none of your bussiness"

a = np.char.add(name, str)
print(a)
a = np.char.lower(name)
print(a)
a = np.char.upper(name)
print(a)
a = np.char.center(name,60)
print(a)
a = np.char.center(name,60, fillchar="*")
print(a)
a = np.char.split(name)
print(a)
a = np.char.splitlines("l1\nl2")
print(a)
a = np.char.join([":","/"], [name,str])
print(a)
a = np.char.replace(name, "bros", "brothers")
print(a)
a = np.char.equal(name,str)
print(a)
a = np.char.count(name,'is')
print(a)
a = np.char.find(name,'o')
print(a)