import numpy as np
import matplotlib.pyplot as plt

# trignometric functions
print(np.sin(180)) 
print(np.sin(90)) 
print(np.cos(180)) 
print(np.cos(90)) 
print(np.tan(45)) 

x_sin = np.arange(0, 3*np.pi, 0.1)
y_sin = np.sin(x_sin)
print(x_sin)
print(y_sin)

plt.plot(x_sin, y_sin)
plt.show()

