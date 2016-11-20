'''
Adding a legend:
Let's add a legend in the upper left corner.
This only requires adding the keyword argument label (that will be used in the legend box) to the plot commands.
'''

# Import everything from matplotlib (numpy is accessible via 'np' alias)
from pylab import *

# Create a new figure of size 8x6 points, using 80 dots per inch
figure(figsize=(10,6), dpi=80)

# Create a new subplot from a grid of 1x1
subplot(1,1,1)

X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
Y = np.linspace(1.5, 1.5, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)

# Setting spines (orthogonal axes)
ax = gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

# Plot cosine
plot(X, C, color="blue", linewidth=2.5, linestyle="-")

# Plot sine 
plot(X, S, color="red",  linewidth=2.5, linestyle="-")

# Set x, y limits
xlim(X.min()*1.1, X.max()*1.1)
ylim(C.min()*1.1, C.max()*1.1)



# Set x, y ticks
xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
       [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

yticks([-1, 0, +1],
       [r'$-1$', r'$0$', r'$+1$'])

# Adding a legend

plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="cosine")
plot(X, S, color="red",  linewidth=2.5, linestyle="-", label="sine")

legend(loc='upper left')

# Save figure using 72 dots per inch
# savefig("exercice_2.png",dpi=72)

# Show result on screen
show()