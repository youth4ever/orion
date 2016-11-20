from numpy import *
from matplotlib.pyplot import *

x = linspace(-8,8,100)

y = linspace(-8,8,100)

X, Y = meshgrid(x, y)

f = lambda u,v: sin(u)*cos(2*v)+0.1

Z = f(X, Y)

contour(X,Y,Z)   # Plot the contour lines
#Out[7]: <matplotlib.contour.QuadContourSet instance at 0x4948b48>

colorbar()   # Make a legend for the colors
#Out[8]: <matplotlib.colorbar.Colorbar instance at 0x49574d0>

show()