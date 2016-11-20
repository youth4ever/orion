import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

'''
To do this, I’m just using the equation for a point on a circle (but with the sine/ cosine flipped
from the typical — this just means it goes around in clockwise), and using the animate
function’s i argument to help compute it. This works because I’ve got 360 frames.

The init() function serves to setup the plot for animating, whilst the animate function
returns the new position of the object. Setting blit=True ensures that only the portions
of the image which have changed are updated. This helps hugely with performance.

The purpose of returning patch, from both init() and animate() is to tell the animation
function which artists are changing. Both of these except a tuple (as you can be animating
multiple different artists.) The Circle is initially created off screen as we need to initialise
it before animating. Without initialising off screen, blitting causes a bit of an artifact.
'''
fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(7, 6.5)

ax = plt.axes(xlim=(0, 10), ylim=(0, 10))
patch = plt.Circle((5, -5), 0.75, fc='y')

def init():
    patch.center = (5, 5)
    ax.add_patch(patch)
    return patch,

def animate(i):
    x, y = patch.center
    x = 5 + 3 * np.sin(np.radians(i))
    y = 5 +  3 * np.cos(np.radians(i))
    patch.center = (x, y)
    return patch,

anim = animation.FuncAnimation(fig, animate,
                               init_func=init,
                               frames=360,
                               interval=20,
                               blit=True)

plt.grid(); plt.show()

#anim.save('animation.mp4', fps=30,\
 #         extra_args=['-vcodec', 'h264',\
 #                     '-pix_fmt', 'yuv420p'])