from numpy import *
from matplotlib.pyplot import *

x = linspace(-2, 2, 100)

figure()

#Out[4]: <matplotlib.figure.Figure at 0x362b350>
subplot(2,2,1)   # Two rows and two cols of plots, select first one
#Out[5]: <matplotlib.axes.AxesSubplot at 0x362ba90>
plot(x, x)
#Out[6]: [<matplotlib.lines.Line2D at 0x27b2cd0>]
subplot(2,2,2)   # Two rows and two cols of plots, select second one
#Out[7]: <matplotlib.axes.AxesSubplot at 0x36d7b10>
plot(x, x**2)
#Out[8]: [<matplotlib.lines.Line2D at 0x38937d0>]
subplot(2,2,3)   # Two rows and two cols of plots, select third one
#Out[9]: <matplotlib.axes.AxesSubplot at 0x3893c90>
plot(x, x**3)
grid(True)
#Out[10]: [<matplotlib.lines.Line2D at 0x38b8a10>]
subplot(2,2,4)   # Two rows and two cols of plots, select fourth one
#Out[11]: <matplotlib.axes.AxesSubplot at 0x38b8e10>
plot(x, x**4)
# [<matplotlib.lines.Line2D at 0x362b8d0>]

show()