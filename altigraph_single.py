# Frankly, I have no idea why you'd ever use this, since it auto-scales
# the data, and you should never, ever, please, have altitude and temperature
# on the same scaling for a good reason. However, I'm including it since it took
# less time to make than this message did.

import matplotlib.pyplot as plt
import numpy as np

y1 = np.loadtxt('alti_p.txt', delimiter=',', unpack=True)
y2 = np.loadtxt('alti_t.txt', delimiter=',', unpack=True)
x1 = range(0,len(y1))
x2 = range(0,len(y2))

# plt.legend()

plt.title('Module Data')

plt.plot(x1, y1, 'r.-')
plt.ylabel('Pressure/Altitude')

plt.plot(x2, y2, 'b.-')
plt.ylabel('Temperature')

plt.show()
