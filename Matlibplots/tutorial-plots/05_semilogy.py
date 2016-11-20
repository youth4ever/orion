from numpy import *
from matplotlib.pyplot import *

''' Work only in Command Line '''
x = linspace(-2, 2, 200)


figure()

semilogy(x, 2**x, "r-", label=r"$2^x$",  linewidth=5.5)
semilogy(x, 3**x, "g-", label=r"$3^x$")
semilogy(x, 4**x, "b-", label=r"$4^x$",  linewidth=2.5)
semilogy(x, 5**x, "c-", label=r"$5^x$")
semilogy(x, 6**x, "m-", label=r"$6^x$",  linewidth=2.5,  linestyle="--")
semilogy(x, 7**x, "y-", label=r"$7^x$")

grid(True)

legend(loc="lower right")

show()