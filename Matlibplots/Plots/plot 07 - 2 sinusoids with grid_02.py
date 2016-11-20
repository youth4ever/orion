import matplotlib.pyplot as plt
import numpy as np


# ax = plt.subplot(111)
t = np.arange(0.0, 45.0, 0.01)
s = np.cos(2 * np.pi * t) + np.cos(2.1 * np.pi * t)
s2 = np.cos(2 * np.pi * t) 
s3 = np.cos(2.1 * np.pi * t) 
line = plt.plot(t, s, lw=1)
line2 = plt.plot(t, s2, lw=1)
line3 = plt.plot(t, s3, lw=1)

plt.grid()
# plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
#            arrowprops=dict(facecolor='black', shrink=0.05),
#            )

plt.xlim(-0.5, 45)
plt.ylim(-3, 3)
plt.show()
