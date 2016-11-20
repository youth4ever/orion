import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math


def plot_dot(x,y):
    fig=plt.figure(figsize=(10 , 10))
    dot = plt.plot([ x], [y], 'mo'); plt.axis([-6, 6, -6, 6])

plot_dot(1,-5)

def sumab(a,b):
    return a+b,
    print(a+b)

sumab(4444,5)

'''

def init():
    patch.center = (5, 5)
    dot = ax.plot([3],[2], 'ro')
    return dot,


def animate(i):
#    x, y = patch.center
    x = 5 + 3 * np.sin(np.radians(i))
    y = 5 +  3 * np.cos(np.radians(i))
    return dot,

anim = animation.FuncAnimation(fig, animate,
                               init_func=init,
                               frames=360,
                               interval=20,
                               blit=True)
'''
'''
def animate(i):
    #dot.set_ydata(np.sin(x + i / 10.0))  # update the data SPEED
    dot.set_ydata(np.cos(i / 10.0))  # update the data SPEED
    return dot,
ani = animation.FuncAnimation(fig, animate, np.arange(1, 200))

'''

def toRadians(degrees):
    return (degrees / 180.0) * math.pi

def polar_to_X(theta, r):
    x = r * math.cos(theta)
    return x

def polar_to_Y(theta, r):
    y = r * math.sin(theta)
    return y


print(polar_to_X(math.pi,1))
print(toRadians(90))

plt.title("Simple DOTS"); plt.ylabel('some numbers'); plt.xlabel('only for test')
plt.grid(); plt.show()

