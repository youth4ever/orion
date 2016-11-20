
from numpy import *
from matplotlib.pyplot import *

plot([23, 456, 676, 89, 906, 34, 2345])

#Out[9]: [<matplotlib.lines.Line2D at 0x6112f90>]

yscale('log')

grid(b=True, which='major', color='b', linestyle='-')
grid(b=True, which='minor', color='r', linestyle='--')

show()