import matplotlib.pyplot as plt
from pylab import *
import matplotlib.animation as animation
import numpy as np

#plt.plot([1, 2, 3, 4], linestyle='--', color='m')
#plt.plot([3, 1.2, 1, 3], linestyle='--',  linewidth=4.5)

#plt.plot([8, 3, 1, 5], 'ro-.')
fig, ax = plt.subplots()

x = np.arange(0, 6, 0.01)  # x-array
dot, = ax.plot([2], 'ro')

#Label

def animate(i):
    dot.set_ydata(np.sin(x + i / 10.0))  # update the data SPEED
    return dot,

ani = animation.FuncAnimation(fig, animate, np.arange(1, 200))

plt.axis([-1, 6, -2, 6])
plt.ylabel('some numbers')
plt.title("Simple DOTS")
plt.grid()

plt.show()
