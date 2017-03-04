#!/usr/bin/python                   o(^_^)o
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
Rectangles in cross-hatched grids       -       Problem 147

In a 3x2 cross-hatched grid, a total of 37 different rectangles could be situated within that grid as indicated in the sketch.

There are 5 grids smaller than 3x2, vertical and horizontal dimensions being important,
i.e. 1x1, 2x1, 3x1, 1x2 and 2x2. If each of them is cross-hatched, the following number of different rectangles
could be situated within those smaller grids:

1x1: 1
2x1: 4
3x1: 8
1x2: 4
2x2: 18

Adding those to the 37 of the 3x2 grid, a total of 72 different rectangles could be situated within 3x2 and smaller grids.

How many different rectangles could be situated within 47x43 and smaller grids?
'''

import time
from itertools import combinations
from numpy import prod
from gmpy2 import is_prime
import functools, operator

def factors(a):
    '''Outputs a list of the unique prime factors of its input; The Second Fastest Algorithm
    This Function is splitting a number in its factors, and detects also if the number is a prime. '''
    b = 2
    d = []
    f = a
    while f > 1:
        while f % b != 0:
            b = b + 1
        d = d + [b]
        f = f / b
    if len(d) >1:
        return  d
    else: return print(a,' is prime')

def make_rectangles(n) :
    ''' Functions which transform an area into a rectangle
    :param n: is the Area which will be computed. If the number is a prime it just returns [n,1]
    :return: a list with pairs of numbers which represent sides of a rectangle    '''
    lst =[]
    if is_prime(n) == False:
        # print(i, factors(i))
        C = list(combinations(factors(n), 2))
        for k in range(len(C)):
            q = [ n//prod(C[k]),  prod(C[k]) ]
            q = sorted(q)
            if q not in lst : lst.append( q )
        for j in range( len(factors(n))):
            p = ( int(prod(factors(n)[0:j]))  , prod(factors(n)[j::]) )
            p = sorted(p)
            if p not in lst : lst.append( p  )
        return lst
    elif is_prime(n) == True :
        lst = [n , 1]
        return [lst]

# print('\nMake Rectangles Function: ',make_rectangles(2772))

def calc_rectangle(a , b):
    '''    Function which calculates the possible number of sub rectangles in an area
    :param a: is the length of the rectangle
    :param b:  the height of the rectangle
    :return:  returns the number of rectangles that can be formed inside    '''
    S = 0
    for i in range(1, a+1):
        for j in range(1, b+1):
            S += (a-i+1) * (b-j+1)
    return S

print('\ncalc_rectangles : \t',calc_rectangle(1, 2))


def get_rombs( a , b ):
    #case 1 --> a=b
    if a==b  :
        l_max = 2*a - 2
        group = []
        for i in range(l_max, 0, -2):
            group.append( (i,2) )

     #case 2 --> a != b
    if a != b  :
        l_max = (min(a, b) - 1)*2 +1
        group = []
        h = abs(a-b)        # How many max lengths
        group.append((l_max, h ))
        for i in range(l_max-1, 0, -2):
            group.append( (i,2) )
        ### Generate blocks :
            BL = []

            for i in range( l_max, min(a,b)-1, -1 ):
                for j in range( l_max-i+1, 0, -1 ):
                    BL.append( ( i, j) )
            for i in range( min(a,b)-1, 1, -1):    #we neglect (1, 1)
                for j in range(i, 0, -1):
                    BL.append( (i,j))

    return group, BL

print('\nget_rombs : \t', get_rombs(6 , 3)  )







print('\n--------------------------TESTS------------------------------')
t1  = time.time()






t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

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
