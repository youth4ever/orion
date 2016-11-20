from numpy import *
from matplotlib.pyplot import *

x = random.rand(10)       # Some random points
offset = random.rand(10)

y = x + 0.25 * offset

p = polyfit(x, y, 1)   # Fit a polynomial of first degree (line)

u = linspace(-0.1, 1.1, 10)   # Evaluate the polynomial at (other) points
v = polyval(p, u)

figure()
#Out[12]: <matplotlib.figure.Figure at 0x2e87f10>

plot(x, y, ".")
#Out[13]: [<matplotlib.lines.Line2D at 0x334ac10>]
plot(u, v, "--r")
#Out[14]: [<matplotlib.lines.Line2D at 0x3271e10>]
grid(True)
show()