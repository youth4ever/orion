'''
Setting tick labels:
Ticks are now properly placed but their label is not very explicit.
We could guess that 3.142 is π but it would be better to make it explicit.
When we set tick values, we can also provide a corresponding label in the second argument list.
Note that we'll use latex to allow for nice rendering of the label.
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


# Save figure using 72 dots per inch
# savefig("exercice_2.png",dpi=72)

# Show result on screen
show()