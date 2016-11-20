'''
Setting limits:
Current limits of the figure are a bit too tight and we want to make some space in order to clearly see all data points.
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

# Set x, y limits
xlim(X.min()*1.1, X.max()*1.1)
ylim(C.min()*1.1, C.max()*1.1)


# Set x ticks
xticks(np.linspace(-4,4,9,endpoint=True))



# Set y ticks
yticks(np.linspace(-1,1,5,endpoint=True))

# Save figure using 72 dots per inch
# savefig("exercice_2.png",dpi=72)

# Show result on screen
show()