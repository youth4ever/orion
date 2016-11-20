from numpy import *

from matplotlib.pyplot import *

x = linspace(-2, 2, 200)

figure()   # Make a new figure
#Out[5]: <matplotlib.figure.Figure at 0x3636250>

plot(x, y)   # Plot some data
#Out[6]: [<matplotlib.lines.Line2D at 0x36e5550>]


grid(True)   # Set the thin grid lines

savefig("plot_1.png")   # Save the figure to a file "png",
                                # "pdf", "eps" and some more file types are valid