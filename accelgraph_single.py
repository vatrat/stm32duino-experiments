import matplotlib.pyplot as plt
import numpy as np

y1 = np.loadtxt('accel_x.txt', delimiter=',', unpack=True)
y2 = np.loadtxt('accel_y.txt', delimiter=',', unpack=True)
y3 = np.loadtxt('accel_z.txt', delimiter=',', unpack=True)
x1 = range(0,len(y1))
x2 = range(0,len(y2))
x3 = range(0,len(y3))

# plt.legend()

plt.title('Module Data')

plt.plot(x1, y1, 'r.-')
plt.ylabel('X accel')

plt.plot(x2, y2, 'g.-')
plt.ylabel('Y accel')

plt.plot(x3, y3, 'b.-')
plt.ylabel('Z accel')

plt.show()
