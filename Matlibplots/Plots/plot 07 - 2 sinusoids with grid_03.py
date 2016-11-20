import matplotlib.pyplot as plt
import numpy as np


# ax = plt.subplot(111)
t = np.arange(0.0, 45.0, 0.01)
wave1 = np.cos(2 * np.pi * t) 
wave2 = np.cos(2.03 * np.pi * t) 
resulting_wave = wave1 + wave2

line = plt.plot(t, wave1, lw=1)
line2 = plt.plot(t, wave2, lw=1)
line3 = plt.plot(t, resulting_wave, lw=1)

plt.grid()
# plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
#            arrowprops=dict(facecolor='black', shrink=0.05),
#            )

plt.ylim(-3, 3)
plt.xlim(-0.5, 45)
plt.show()
