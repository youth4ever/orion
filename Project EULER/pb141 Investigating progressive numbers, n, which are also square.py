#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
Investigating progressive numbers, n, which are also square         -       Problem 141

A positive integer, n, is divided by d and the quotient and remainder are q and r respectively.

In addition d, q, and r are consecutive positive integer terms in a geometric sequence, but not necessarily in that order.

For example, 58 divided by 6 has quotient 9 and remainder 4.
It can also be seen that 4, 6, 9 are consecutive terms in a geometric sequence (common ratio 3/2).
We will call such numbers, n, progressive.

Some progressive numbers, such as 9 and 10404 = 102**2, happen to also be perfect squares.
The sum of all progressive perfect squares below one hundred thousand is 124657.

Find the sum of all progressive perfect squares below one trillion (10**12).

'''
import time
from itertools import combinations
import functools, operator

print('\n--------------------------TESTS------------------------------')

import numpy, cmath

# SUMS as checks
#                 10^5: 124657
#                 10^6: 700738
#                 10^8: 171436696

t1  = time.time()

# a= numpy.complex(3,3 ) - numpy.complex(1,4)
# print(a)

# squares = [i*i for i in range(1, int((10**5)**(1/2) )) ]
# print(len(squares), squares)

# Just some naive search !
x = 124657- 9 - 10404

L = (9, 10404, 16900, 97344)

print(sum(L), [ i**(1/2) for i in L ])

# L = list(combinations (squares , 2 ))
# for i in L :
#     P = functools.reduce( operator.add , i  )
#     if P == x :
#         print('other two numbers : \t', i)
#         break


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

################
t1  = time.time()


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------TESTS------------------------------')



print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()

















# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 3,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 4,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 5,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 6,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#