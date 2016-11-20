import matplotlib.pyplot as plt
from pylab import *

plt.plot([1, 2, 3, 4], linestyle='--', color='m')
plt.plot([1, 3, 2, 4])
plt.plot([3, 1.2, 1, 3], linestyle='--',  linewidth=4.5)
plt.plot([8, 3, 1, 5], 'ro-.')
plt.ylabel('some numbers')
plt.show()
