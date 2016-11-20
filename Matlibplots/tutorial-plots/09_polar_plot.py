from numpy import *
from matplotlib.pyplot import *

phi = linspace(0, 2*pi, 200)

figure()
#Out[149]: <matplotlib.figure.Figure at 0x5cbda50>

polar(phi, sin(-phi) *cos(phi), phi, sin(phi) *cos(phi)  )
#Out[150]: [<matplotlib.lines.Line2D at 0x67a29d0>]

grid(True)

show()