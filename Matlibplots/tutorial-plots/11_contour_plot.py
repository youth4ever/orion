from numpy import *
from matplotlib.pyplot import *

# Data of the quadratic form
A = array([
        [2., 1.],
        [1., 2.]])

b = array([1., 1.])

# Mesh
Nx = 100
Ny = 100

X, Y = ogrid[-3.:3:Nx*1j, -3.:3:Ny*1j]   # ogrid is similar to meshgrid

z = zeros(2)
Z = zeros(Nx*Ny)

# compute values
k = 0
for x in X[:,0]:
    z[0] = x
    for y in Y[0,:]:
         z[1] = y
         Z[k] = 0.5*dot(z,dot(A,z)) - dot(z,b)
         k += 1

Z = Z.reshape(Nx,Ny)

# Plot
levels = arange(Z.min(), Z.max()+0.01, 1.0)   # How many contour levels and where
colormap = cm.get_cmap('jet', len(levels)-1)   # Add a nice color map

figure()
contourf(Z, levels, cmap=colormap)
colorbar()   # Add the color bar legend
show()