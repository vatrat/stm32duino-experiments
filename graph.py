import matplotlib.pyplot as plt
import numpy as np

y1 = np.loadtxt('accel_x.txt', delimiter=',', unpack=True)
y2 = np.loadtxt('accel_y.txt', delimiter=',', unpack=True)
y3 = np.loadtxt('accel_z.txt', delimiter=',', unpack=True)
x1 = range(0,len(y1))
x2 = range(0,len(y2))
x3 = range(0,len(y3))

# plt.legend()

plt.subplot(3, 1, 1)
plt.plot(x1, y1, 'o-')
plt.title('Module Data')
plt.ylabel('X accel')

plt.subplot(3, 1, 2)
plt.plot(x2, y2, '.-')
plt.ylabel('Y accel')

plt.subplot(3, 1, 3)
plt.plot(x3, y3, '.-')
plt.ylabel('Z accel')

plt.show()
