import matplotlib.pyplot as plt
from matplotlib import style


# line plot - 2

days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temperature = [23,24,30,32,28,29,29,34,33,32,30,27,30,31,32]
plt.plot(days, temperature, color="b", marker="o", markersize=5, linestyle="--", linewidth=2)
plt.title('Delhi Temperature')
plt.xlabel('day')
plt.ylabel('temperature')
plt.show()


days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temperature = [23,24,30,32,28,29,29,34,33,32,30,27,30,31,32]
plt.plot(days, temperature, "bo--")
plt.title('Delhi Temperature', fontsize=15)
plt.xlabel('day', fontsize=10)
plt.ylabel('temperature', fontsize=10)
plt.show()


days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temperature = [23,24,30,32,28,29,29,34,33,32,30,27,30,31,32]
plt.plot(days, temperature, "bo--")
plt.title('Delhi Temperature', fontsize=15)
plt.xlabel('day', fontsize=10)
plt.ylabel('temperature', fontsize=10)
plt.legend(["temp line"], loc=2)
plt.show()


days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temperature = [23,24,30,32,28,29,29,34,33,32,30,27,30,31,32]
plt.plot(days, temperature, "bo--", label="Temp line")
plt.title('Delhi Temperature', fontsize=15)
plt.xlabel('day', fontsize=10)
plt.ylabel('temperature', fontsize=10)
plt.legend(loc=2)
plt.show()


days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temperature = [23,24,30,32,28,29,29,34,33,32,30,27,30,31,32]
style.use("ggplot")
plt.plot(days, temperature, "bo--", label="Temp line")
plt.title('Delhi Temperature', fontsize=15)
plt.xlabel('day', fontsize=10)
plt.ylabel('temperature', fontsize=10)
plt.legend(loc=2)
plt.grid(color='k', linestyle='-', linewidth=1)
plt.show()


days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
delhi_temp = [33,34,32,32,38,39,39,34,33,32,31,37,33,37,39]
mumbai_temp = [23,24,30,32,28,29,29,34,33,32,30,27,30,31,32]
style.use("ggplot")
plt.plot(days, delhi_temp, "bo--", label="Delhi")
plt.plot(days, mumbai_temp, "ro--", label="Mumbai")
plt.title('Delhi Temperature', fontsize=15)
plt.xlabel('day', fontsize=10)
plt.ylabel('temperature', fontsize=10)
plt.legend(loc=2)
plt.grid(color='k', linestyle='-', linewidth=1)
plt.show()