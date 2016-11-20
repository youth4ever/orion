"""
A simple example of an animated plot
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

x = np.arange(0, 6, 0.01)  # x-array
line, = ax.plot(x, np.sin(x))

def animate(i):
    line.set_ydata(np.sin(x + i / 10.0))  # update the data SPEED
    return line,
# Init only required for blitting to give a clean slate.
'''
def init():
    line.set_ydata(np.ma.array(x, mask=True))
    return line,
'''
# The simpler way to animate
ani = animation.FuncAnimation(fig, animate, np.arange(1, 200))
'''
# The more clear way to animate
ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), init_func=init,
    interval=225, blit=True)
'''
plt.xlim(-2, 10)
plt.ylim(-2, 2)
plt.grid()
plt.show()
