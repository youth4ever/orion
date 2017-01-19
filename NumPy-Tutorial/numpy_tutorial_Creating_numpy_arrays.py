#           Creating numpy arrays
'''There are a number of ways to initialize new numpy arrays, for example from

a Python list or tuples
using functions that are dedicated to generating numpy arrays, such as arange, linspace, etc.
reading data from files'''
#For example, to create new vector and matrix arrays from Python lists we can use the numpy.array function.
from numpy import *
# a vector: the argument to the array function is a Python list
v = array([1,2,3,4])
print(v, type(v))
#---------------------------------------------------------
# a matrix: the argument to the array function is a nested Python list
M = array([[1, 2], [3, 4]])
print(M, '--> type: ', type(M))
''' The v and M objects are both of the type ndarray that the numpy module provides.
The difference between the v and M arrays is only their shapes.
 We can get information about the shape of an array by using the ndarray.shape property.'''
print(v.shape)
print(M.shape)
#The number of elements in the array is available through the ndarray.size property:
print('M size: ', M.size)
#Equivalently, we could use the function numpy.shape and numpy.size
print('M shape: ',shape(M), '  M size: ',size(M))

'''
So far the numpy.ndarray looks awefully much like a Python list (or nested list).
 Why not simply use Python lists for computations instead of creating a new array type?

There are several reasons:

Python lists are very general. They can contain any kind of object.
They are dynamically typed. They do not support mathematical functions such as matrix and dot multiplications, etc.
Implementing such functions for Python lists would not be very efficient because of the dynamic typing.
Numpy arrays are statically typed and homogeneous. The type of the elements is determined when array is created.
Numpy arrays are memory efficient.
Because of the static typing, fast implementation of mathematical functions such as multiplication
and addition of numpy arrays can be implemented in a compiled language (C and Fortran is used).

Using the dtype (data type) property of an ndarray, we can see what type the data of an array has:'''
print('Data type of M:    ',M.dtype)

#We get an error if we try to assign a value of the wrong type to an element in a numpy array:
#M[0,0] = 'hello'
#If we want, we can explicitly define the type of the array data when we create it, using the dtype keyword argument:
M = array([[1, 2], [3, 4]], dtype=complex)
print(M)
'''Common type that can be used with dtype are: int, float, complex, bool, object, etc.

We can also explicitly define the bit size of the data types, for example: int64, int16, float128, complex128.'''