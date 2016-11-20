from numpy import *
from matplotlib.pyplot import *

x = linspace(-2, 2, 200)

y1 = -sqrt(1-x**2)
y2 = +sqrt(1-x**2)

figure()   # Make a new figure
#Out[5]: <matplotlib.figure.Figure at 0x3636250>

plot(x, y1, x, y2)   # Plot some data
#Out[6]: [<matplotlib.lines.Line2D at 0x36e5550>]


grid(True)   # Set the thin grid lines

show()   # Save the figure to a file "png",
                                # "pdf", "eps" and some more file types are valid