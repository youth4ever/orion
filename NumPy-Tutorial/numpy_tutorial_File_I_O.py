#                               Comma-separated values (CSV)

from numpy import *


data = genfromtxt('Stockolm.dat')
print(data.shape)



M = random.rand(3,4)
print(M)
# Using numpy.savetxt we can store a Numpy array to a file in CSV format:
savetxt("random-matrix.csv", M)
print('-------'*10,'MATRIX OPERATIONS','-------'*10)
print('Describe the shape of the Matrix:  ',M.shape)
print('Describe the number of object within the matrix:  ',M.size)
print('Print the MIN value of each row: ', amin(M,axis=1))
print('Print the minimum value of each column: ',amin(M,axis=0))
print('Print the max value of each row: ', amax(M,axis=1))
print('Print the MAX value of each column: ',amax(M,axis=0))
print('Print the MEAN value of each column: ',mean(M,axis=0))
print('Print the SUM value of each column: ',sum(M,axis=0))
N = random.rand(3,3)
print(N)
print('Print the TRACE : ', trace(N))
print('Print the diagonal : ', diagonal(N))
print('Print the TRANSPOSE matrix : ', transpose(N))
print('Print how many bytes has an elemnt: ',N.itemsize)
print('Print total number of bytes of the MaTriX: ',N.nbytes)
print('Print total number of dimensions the MaTriX: ',N.ndim)
print('-------'*10,'END','-------'*10)
savetxt("random-matrix_2.csv", M, fmt='%.5f') # fmt specifies the format

#           Numpy's native file format
#Useful when storing and reading back numpy array data. Use the functions numpy.save and numpy.load:
save("random-matrix_3.npy", M)
load("random-matrix_3.npy")