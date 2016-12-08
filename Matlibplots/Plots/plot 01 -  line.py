import matplotlib.pyplot as plt
from pylab import *

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

def grid():
    # major ticks every 5, minor ticks every 1
    major_ticks = np.arange(0, 51, 5)
    minor_ticks = np.arange(0, 51, 1)

    ax.set_xticks(major_ticks)
    ax.set_xticks(minor_ticks, minor=True)
    ax.set_yticks(major_ticks)
    ax.set_yticks(minor_ticks, minor=True)

    # and a corresponding grid
    ax.grid(which='both')

    # or if you want differnet settings for the grids:
    # ax.grid(which='minor', alpha=0.2)
    ax.grid(which='minor', alpha=0.8)
    ax.grid(which='major', alpha=1)

grid()

plt.plot([1, 2, 3, 4], linestyle='--', color='m')
plt.plot([1, 3, 2, 4])
plt.plot([3, 1.2, 1, 3], linestyle='--',  linewidth=4.5)
plt.plot([8, 3, 1, 5], 'ro-.')
plt.ylabel('some numbers')
plt.show()
