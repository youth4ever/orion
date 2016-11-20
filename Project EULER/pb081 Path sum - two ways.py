#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Thu, 13 Oct 2016, 20:53
#The  Euler Project  https://projecteuler.net
'''
Path sum: two ways      -       Problem 81
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right,
by only moving to the right and down, is indicated in red and is equal to 2427.

                           131 673 234 103 18
                           201 96  342 965 150
                           630 803 746 422 111
                           537 699 497 121 956
                           805 732 524 37  331

Find the minimal path sum, in matrix.txt, a 31K text file containing a 80 by80 matrix,
from the top left to the bottom right by only moving right and down.
'''
import time
from math import factorial
# import pandas as pd
# matrix=pd.read_csv('pb081_matrix.txt', sep=',',header=None)
# print(matrix.values)
#print(matrix)

def load_file(filename="pb081_matrix.txt"):
    with open(filename) as f:
        matrix = [list(map(int, line.split(","))) for line in f.readlines()]
    f.close()
    return matrix

from numpy import genfromtxt
def load(filename):
    M = genfromtxt(filename, delimiter=',')
    rows = M.shape[0]
    cols = M.shape[1]
    return M

print(load("pb081_matrix.txt"))

#   Get the file into the python matrix
f = open ( 'pb081_matrix.txt' , 'r')
text = f.read()
#print(text)
f.close()
matrix=[]
for row in text.split('\n'):
    matrix.append(list(map(int, row.split(','))))         # This maps the strings into ints on the run, SMART TECHNIQUE


def combinations(n , k):
    result = factorial(n)//(factorial(k)*factorial(n-k))
    return result

print('Path possibilities , huge huge number ',combinations(79*2,79),' ;  ' ,len(str(combinations(79*2,79))), 'digits')

print('\n----------------- TEST FOR Smaller MaTriX -----------------------\n')

# m =[[150, 650, 250, 100, 50], \
#        [200, 100,  350, 950, 150],\
#        [650, 800, 750, 400, 100],\
#        [550, 700, 500, 150, 950],\
#        [800, 750, 500, 50,  350]]

m=[[131, 673, 234, 103, 18], \
   [201, 96,  342, 965, 150],\
   [630, 803, 746, 422, 111],\
   [537, 699, 497, 121, 956],\
   [805, 732, 524, 37,  331]]


for i in range(0,len(m)):
    for j in range(0, len(m)):
        if i ==0 and j==0 :
            #print(m[i][j])
            continue
        elif i == 0 and j > 0 :
            #print ( m[i][j-1] )
            m[i][j] += m[i][j-1]
        elif j == 0 and i > 0 :
            #print(m[i][j])
            m[i][j] += m[i-1][j]
        else:
            #print(m[i][j-1], m[i-1][j])
            m[i][j] += min( m[i][j-1], m[i-1][j] )
    print(m[i])

print('\nThe minimum path sum is : ',m[-1][-1])



print ('\n-------------------------- MY SOLUTION, DYNAMIC PROGRAMMING , pb67--------------------------------------\n')

t1  = time.time()

for i in range(0,len(matrix)):
    for j in range(0, len(matrix)):
        if i ==0 and j==0 :
            #print(matrix[i][j])
            continue
        elif i == 0 and j > 0 :
            #print ( matrix[i][j-1] )
            matrix[i][j] += matrix[i][j-1]
        elif j == 0 and i > 0 :
            #print(matrix[i][j])
            matrix[i][j] += matrix[i-1][j]
        else:
            #print(matrix[i][j-1], matrix[i-1][j])
            matrix[i][j] += min( matrix[i][j-1], matrix[i-1][j] )
    #print(matrix[i])

print('\nThe minimum path sum is : ',matrix[-1][-1])        # 427337

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1 , VERY NICE , ELEGANT way to load a file, mmanimath, England --------------------------')

t1  = time.time()

from numpy import genfromtxt

def EP_81(filename):
    M = genfromtxt(filename, delimiter=',')
    rows = M.shape[0]
    cols = M.shape[1]
    for i in range(cols - 2, -1, -1):
        M[cols-1][i] += M[cols-1][i+1]
        M[i][cols-1] += M[i+1][cols-1]
    for i in range(rows-2, -1, -1):
        for j in range(cols-2, -1, -1):
            M[i][j] += min(M[i+1][j], M[i][j+1])
    return M[0][0]

print(EP_81('pb081_matrix.txt'))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2 , NICE LOAD of file ,  jpulgarin , Columbia--------------------------')

t1  = time.time()


def get(matrix, x, y):
    if x < 0 or y < 0:
        return 9999999999
    return matrix[x][y]

matrix = []

with open('pb081_matrix.txt', 'r') as f:
    for line in f:
        matrix.append([int(n) for n in line.split(',')])

for n in range(1, len(matrix)):
    for i in range(n):
        matrix[i][n] += min(get(matrix, i-1, n), get(matrix, i, n-1))
        matrix[n][i] += min(get(matrix, n-1, i), get(matrix, n, i-1))
    matrix[n][n] += min(matrix[n-1][n], matrix[n][n-1])

print (matrix[-1][-1])

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3 , FAST, markus.obi, Germany-------------------------')


t1  = time.time()

# Almost the same algorithm as used in Maximum path sum I & II.
# Pretty straight forward and runs in 4 ms. For this algorithm c++ would be much more appropriate,
# but python is so fast to code and for this small matrix fast enough.

def solve():
    filename = "pb081_matrix.txt"
    with open(filename) as f:
        matrix = [list(map(int, line.split(","))) for line in f.readlines()]
    n_rows = len(matrix)
    n_columns = len(matrix[0])
    for i in range(n_rows):
        for j in range(n_columns):
            if i == j == 0:
                continue
            if i == 0:
                matrix[i][j] += matrix[i][j - 1]
            elif j == 0:
                matrix[i][j] += matrix[i - 1][j]
            else:
                matrix[i][j] += min(matrix[i - 1][j], matrix[i][j - 1])
    print(matrix[-1][-1])


solve()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')




print('\n--------------------------SOLUTION 4 , -------------------------')
t1  = time.time()

filename = "pb081_matrix.txt"
with open(filename) as f:
    matrix = [list(map(int, line.split(","))) for line in f.readlines()]


HEIGHT = len(matrix)
WIDTH  = len(matrix[0])

for h in range(HEIGHT - 1, -1, -1):
    for w in range(WIDTH - 1, -1, -1):
        add_list = []
        if w != WIDTH - 1:
            add_list.append(matrix[h][w + 1])
        if h != HEIGHT - 1:
            add_list.append(matrix[h+1][w])
        if len(add_list):
            matrix[h][w] += min(add_list)

print(add_list)
print ("Result: ", matrix[0][0])

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 5 , j123, Canada-------------------------')


t1  = time.time()

import numpy as np
with open('pb081_matrix.txt', 'r') as f:
    V = np.add.accumulate(np.fromstring(next(f), sep=',', dtype=int))
    n = len(V)
    for R in f:
        R = np.add.accumulate(np.fromstring(R, sep=',', dtype=int, count=n))
        np.minimum(V[:-1], V[1:] - R[:-1], V[1:])
        V += R
print(V[-1])

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6 , -------------------------')


t1  = time.time()

filename = "pb081_matrix.txt"
with open(filename) as f:
    matrix = [list(map(int, line.split(","))) for line in f.readlines()]

for i in range(1,80):
    matrix[0][i] += matrix[0][i-1]
    matrix[i][0] += matrix[i-1][0]

for i in range(1,80):
    for j in range(1,80):
            matrix[i][j] += min(matrix[i-1][j], matrix[i][j-1])

print(matrix[79][79])

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')













