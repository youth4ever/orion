from numpy import *
from matplotlib.pyplot import *

x = linspace(-100, 700, 200000)

figure()

loglog(x, x, "r-", label=r"$x$")
loglog(x, x**2, "g-", label=r"$x^2$")
loglog(x, x**3, "b-", label=r"$x^3$")
loglog(x, x**4, "c-", label=r"$x^4$")
loglog(x, x**5, "m-", label=r"$x^5$")
loglog(x, x**6, "y-", label=r"$x^6$")

grid(True)
legend(loc="lower right")


show()