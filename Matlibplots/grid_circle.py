import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

# major ticks every 5, minor ticks every 1
major_ticks = np.arange(0, 251, 5)
minor_ticks = np.arange(0, 251, 1)


ax.set_xticks(major_ticks)
ax.set_xticks(minor_ticks, minor=True)
ax.set_yticks(major_ticks)
ax.set_yticks(minor_ticks, minor=True)

# and a corresponding grid

ax.grid(which='both')

# or if you want differnet settings for the grids:
# ax.grid(which='minor', alpha=0.2)
ax.grid(which='minor', alpha=0.8)
# ax.grid(which='major', alpha=1)
ax.grid(which='major', alpha=0.4, color='b', linestyle='-')

# Here we set the right y - axis, Strange that I must use twinx and not twiny, some conflicts may be
ax1 = ax.twinx()
ax1.set_xlim([0, 250])
ax1.set_yticks(major_ticks)
ax1.set_yticks(minor_ticks, minor=True)

# Here we set the top x - axis, Strange that I must use twiny and not twinx, some conflicts may be
ax2 = ax.twiny()
ax2.set_ylim([0, 250])
ax2.set_xticks(major_ticks)
ax2.set_xticks(minor_ticks, minor=True)

circ = plt.Circle((0, 0), radius=250, color='g', fill=False)
ax.add_patch(circ)

fig = plt.gcf()
fig.set_size_inches(50, 50)
fig.savefig('C:/Users/Bogdan/Desktop/pb314_grid_circle.png', dpi=300)
# fig.savefig('pb314_grid_circle.png', dpi=300)

plt.show()