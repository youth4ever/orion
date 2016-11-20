#               Using array-generating functions
from numpy import *
'''For larger arrays it is inpractical to initialize the data manually,
using explicit python lists. Instead we can use one of the many functions
 in numpy that generates arrays of different forms. Some of the more common are:'''

#             arange
# create a range
print('------' * 10,'arange','------' * 10)
x = arange(0, 10, 0.4) # arguments: start, stop, step
print(x)
x = arange(-1, 1, 0.1)
print(x, type(x))

print('------' * 10,'linspace','------' * 10)

#           linspace and logspace
# using linspace, both end points ARE included
a = linspace(0, 10, 25)
print(a, type(a))
print('------' * 10,'logspace','------' * 10)
b = logspace(0, 10, 10, base=e)
print(b, type(b))


print('------' * 10,'mgrid','------' * 10)
#               mgrid
x, y = mgrid[0:5, 0:5] # similar to meshgrid in MATLAB
print(x)
print(y)

print('------' * 10,'random data','------' * 10)
#               random data
# uniform random numbers in [0,1]
c = random.rand(5,6)
print(c)
# standard normal distributed random numbers
d = random.randn(5,5)
print(d)

print('------' * 10,'diag','------' * 10)
#                           diag
# a diagonal matrix
e = diag([1,2,3])
print(e, type(e))

#       diagonal with offset from the main diagonal
f = diag([1,2,3], k=1)
print(f)

g= diag([1,-3], k=0)
print(g)

print('------' * 10,'zeros and ones','------' * 10)
#                   zeros and ones
h = zeros((3,3))
print(h)
i = ones((3,3))
print(i)