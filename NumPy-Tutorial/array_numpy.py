import numpy as np

# using np to define a numpy array
from sympy.functions.combinatorial.numbers import nP

a = np.array([x for x in range(2,20)], int)
print('The numpy array is: \n', a)

b = np.array([x for x in range(2,50) if x % 2 !=0], float)
print(b)

c = np.array([x for x in range(2,50) if x % 2 !=0 and  x% 3 != 0], int)
print(c)

print('_____'*15)
d = np.array([1,2,3,4,5], float)
print(d)
e = np.array([1,2,3,4,5], int)
print(e)
# Test if a equals b:
print ('Compare two matrices if they are equal: ',d == e)
#Accesing element number from an array:
print('The element number six from array b is :',b[6])
'''
It is often useful, to create an array with the range function. With
the reshape–method you can create the object you want, if
needed:                         '''
print('-----'*20)
f = np.array(range(10), float)
print('Generate a matrix with range', f)
g =f.reshape(2,5)
print('Reshape: ', g)
print('Transpose: \n', g.transpose())
print('Flatten: ', g.flatten())
f = np.array([range(10), range(10,20), range(30,40)])
print(f)
print('_____'*15)

print('---------   Arrays of zeros and ones : -----------------')

h = np.zeros((2,3), dtype=int)
print(h)
m = np.ones((2,3), dtype=float)
print('Ones matrix: \n',m)

'''You can create a N by N identity matrix with the
identity–function. The eye–function returns matrices with ones
along the k-th diagonal:                        '''
#   Identity matrix:
print('Identity matrix: \n',np.identity(3, dtype=int))

print('__'*15,'MATHEMATICAL OPERATIONS', '___'*10)
A = np.array(([[1,2,3],[2,5,7],[7,4,2]]))
B = np.array([[8,7,4],[5,7,2],[1,6,2]])

print('\nTHE DOT PRODUCT: \n',np.dot(A,B))

print('\nTHE CROSS PRODUCT: \n',np.cross(A,B))

print('\nDETERMINANT OF MATRIX A: \n',np.linalg.det(A))

print('\nINVERSE OF MATRIX A: \n',np.linalg.inv(A))

#####################################
print('_____'*15)


A = np.array([[1,2,3,4],[5,6,7,8]])
print(A[:,2])       # Returns the third column

print('--------- Diagonals in matrix : ---------')

# Diagonals in matrix
matrix = np.array(         [[-2,   5,   3,  2],\
                                      [ 9,  -6,   5,  1],\
                                      [ 3,    2,   7,  3],\
                                      [-1,    8, -4,  8]])

diags = [matrix[::-1,:].diagonal(i) for i in range(-3,4)]
diags.extend(matrix.diagonal(i) for i in range(3,-4,-1))
print ('All the diagonals :',[n.tolist() for n in diags])
#print(diags)

print('\n------------  Product of a list using numpy--------------------')

print(np.prod([[1.,2.],[3.,4.]]))
print('Using Numpy the product of elements within Matrix is :  ',np.prod(matrix))
print('Display the maximum element :',np.max(matrix),'   ;   Display the index of the maximum element :', np.argmax(matrix))
print(np.array(matrix))
