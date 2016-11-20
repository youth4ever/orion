'''
Eigenvector and Eigenvalues of a matrix:
Given a matrix M, the eigenvalues b and eigenvectors V of the
matrix are defined by the equation:
MV = bV
If you multiply a matrix with a vector, the result is again a vector.
If this vector is a multiple of the original vector, the vector is said
to be an eigenvector. The eigenvalue b of a vector is defined as
above. Note that there might be more than one vector solving the
equation above and we are interested in solutions for which V is a
non–zero vector.
Finding the eigenvalues of a matrix can be a lot of work, in
particular if the matrix is big. Python makes it easy to find the
eigenvector and the eigenvalue of a matrix.
'''
import numpy as np

a= np.array([[0, -7, 2, 0], [-7, 0 ,0, 2], [2, 0, 0, -7], [0, 2, -7, 0]])
print(a)
print('-----'*15)

# Returns the EIGENVALUES and EIGENVECTORS of an array (matrix) M
vals, vecs = np.linalg.eig(a)
print('EIGENVALUES: \n', vals)
print('EIGENVECTOR: \n',vecs)
print('-----'*15)
b = np.array([[6, -3, -8, -4], [0, 10, 6, 7], [0, 0 ,6, -3], [0, 0, 0, 6]])
print(b)
vals, vecs = np.linalg.eig(b)
print('EIGENVALUES: \n', vals)
print('EIGENVECTOR: \n',vecs)
print('-----'*15)
'''
Watch the notation! The first eigenvector is given by the first
elements of the vecs–object: (1,0,0,0). The second eigenvector is
(-0.6,0.8,0,0) etc. Note that the command
'''
print('___'*10,'CHECKING CALCULATIONS:','___'*10)
#We can check that our calculations are correct. Take the last example:
vec1 = np.array([1, 0, 0, 0])
vec2 = np.array([-0.6,  0.8, 0, 0])
print('Dot Product of b with vec1: \n',np.dot(b,vec1))
print('Eigenvalue * vec1: \n',6*vec1)
print('Dot Product of b with vec2: \n',np.dot(b,vec2))
print('Eigenvalue * vec2: \n',10*vec2)

