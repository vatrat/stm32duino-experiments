import matplotlib.pyplot as plt
import numpy as np

y1 = np.loadtxt('alti_p.txt', delimiter=',', unpack=True)
y2 = np.loadtxt('alti_t.txt', delimiter=',', unpack=True)
x1 = range(0,len(y1))
x2 = range(0,len(y2))

# plt.legend()

plt.subplot(2, 1, 1)
plt.plot(x1, y1, 'o-')
plt.title('Module Data')
plt.ylabel('Pressure/Altitude')

plt.subplot(2, 1, 2)
plt.plot(x2, y2, '.-')
plt.ylabel('Temperature')

plt.show()
