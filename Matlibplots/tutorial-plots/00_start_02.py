'''
Changing colors and line widths:
First step, we want to have the cosine in blue and the sine in red and a slighty thicker line for both of them.
We'll also slightly alter the figure size to make it more horizontal.
'''

# Import everything from matplotlib (numpy is accessible via 'np' alias)
from pylab import *

# Create a new figure of size 8x6 points, using 80 dots per inch
figure(figsize=(10,6), dpi=80)



# Create a new subplot from a grid of 1x1
subplot(1,1,1)

X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)

# Plot cosine
plot(X, C, color="blue", linewidth=2.5, linestyle="-")

# Plot sine
plot(X, S, color="red",  linewidth=2.5, linestyle="-")

# Set x limits
xlim(-4.0,4.0)

# Set x ticks
xticks(np.linspace(-4,4,9,endpoint=True))

# Set y limits
ylim(-1.0,1.0)

# Set y ticks
yticks(np.linspace(-1,1,5,endpoint=True))

# Save figure using 72 dots per inch
# savefig("exercice_2.png",dpi=72)

# Show result on screen
show()