from pylab import *


x = arange(0, 2.2, 0.01)
y = 2 * sin(2 * pi * (x - 1 / 4))

plot(x, y)
xlabel('x-axis')
ylabel('y-axis')
title(r'$y=2\sin (2\pi(x-1/4))$')

show()
