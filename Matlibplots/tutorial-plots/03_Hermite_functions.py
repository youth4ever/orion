from numpy import *
from matplotlib.pyplot import *

from scipy.special import gamma
from scipy.special.orthogonal import eval_hermite

x = linspace(-20, 20, 20000)


psi = lambda n,x: 1.0/sqrt((2**n*gamma(n+1)*sqrt(pi))) * exp(-x**2/2.0) * eval_hermite(n, x)

figure()		# Make a new figure
#Out[12]: <matplotlib.figure.Figure at 0x3a9be50>

		
for n in range(6):
	plot(x, psi(n,x), label=r"$\psi_"+str(n)+r"(x)$")   # The 'label' to put into the legend

grid(True)

xlim(-5,5)   # Specify the range of the x axis shown
#Out[15]: (-5, 5)
ylim(-0.8,0.8)   # Specify the range of the y axis shown
#Out[16]: (-0.8, 0.8)
xlabel(r"$x$")   # Put a label on the x axis
# Out[17]: <matplotlib.text.Text at 0x3d06210>
ylabel(r"$\psi_n(x)$")   # Put a label on the y axis
#Out[18]: <matplotlib.text.Text at 0x3d0a190>
legend(loc="lower right")   # Add a legend table
#Out[19]: <matplotlib.legend.Legend at 0x3d32e50>

title(r"Hermite functions $\psi_n$")   # And a title on top of the figure
#Out[20]: <matplotlib.text.Text at 0x3d11590>
savefig("plot_2_Hermite_functions.png")
show()