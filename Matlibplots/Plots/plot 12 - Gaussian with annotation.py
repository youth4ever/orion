from pylab import *
#import matplotlib.pyplot as plt
import math

x = arange(-4, 5.2, 0.01)

y = 2 * math.e**( -(x - 1 / 4)**2)

plt.xlim(-4, 4)
plt.ylim(-0.5, 3)
plt.grid()

plot(x, y)
xlabel('x-axis')
ylabel('y-axis')
title(r'$y=2\ e^-(x-1/4)^2$')

show()
