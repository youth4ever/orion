from numpy import *
from matplotlib.pyplot import *

x = linspace(-2, 2, 200)

y = (x**5 + 4*x**4 + 3*x**3 + 2*x**2 + x + 1)*exp(-x**2)

figure()   # Make a new figure
#Out[5]: <matplotlib.figure.Figure at 0x3636250>

plot(x, y)   # Plot some data
#Out[6]: [<matplotlib.lines.Line2D at 0x36e5550>]


grid(True)   # Set the thin grid lines

show()   # Save the figure to a file "png",
                                # "pdf", "eps" and some more file types are valid