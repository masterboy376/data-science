import matplotlib.pyplot as plt

# line plot

days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temperature = [23,24,30,32,28,29,29,34,33,32,30,27,30,31,32]

plt.plot(days, temperature)
plt.axis([0, 30, 0, 35])
plt.title('Delhi Temperature')
plt.xlabel('day')
plt.ylabel('temperature')
plt.show()