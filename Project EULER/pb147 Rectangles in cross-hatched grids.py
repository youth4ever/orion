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

def get_one_row_rectangle(a ) :
    return calc_rectangle(a, 1) +a-1


def calculate_rombs( a , b ):
    if a==1 : return b-1
    if b==1 : return a-1
    R = {}
    #######   CASE 1--> a=b    ##########
    if a == b  :
        l_max = 2*a - 2
        group = []
        for i in range(l_max, 0, -2):
            group.append( (i,2) )
        ### Generate blocks :
        BL = []
        if a%2==0 :  max_rect = ( a, a)
        if a%2==1 :  max_rect = ( a+1, a-1)
        S_rect = sum(max_rect)
        R[max_rect] =1

        for i in range(S_rect, 1 ,-1) :
            for j in range(1, i+1 ):
                if i+j > S_rect : break
                if  ( ( i%2 == 0) or (j%2 == 0) ) or ( i+j <S_rect ) :
                    # print(i, j)
                    BL.append( ( i, j) )

     #####   CASE 2  --> a != b   ########
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

    ####COMMON OPERATIONS ####
    #### Q: How many k x 1 Rectangles ?
    max_length = group[0][0]


    for i in range(max_length, 1, -1):
        F = [ b[1] for b in group if i <= b[0]  ]
        G = [ c[0]-i+1 for c in group if i <= c[0] ]
        fg = sum ( [ i*j for i,j in zip(F, G)]   )
        R[(i, 1)] = fg
        BL.remove( (i , 1) )
        # print(F, G,   fg )
    # print('\n', max(BL))
    for I in BL :
        g_s_k = [ i for i in R.keys() if sum(i)== sum(I) ][0]  # get_sum_key
        # print(g_s_k,'           ' ,I)
        if ( g_s_k[0]%2 == 1) and ( g_s_k[1]%2 == 1) :  # both ODD
            if I[0]%2 == 1 and I[1]%2 == 1 :
                # print( I,'    =    ' , R[g_s_k]  )
                R[I] = R[g_s_k]
            else :       R[I] = R[g_s_k]+1
        else :
            if I[0]%2 == 1 and I[1]%2 == 1 :
                R[I] = R[g_s_k]-1
            else :      R[I] = R[g_s_k]

    # print('group : \t', group)
    # print('Blocks : \t', BL)
    # print('dict R : \t', R)
    # print( ' blocks of equal elements  : \t',  [ v  for k, v in R.items() if ( k[0] == k[1] )  ]  )
    S = sum([ k[0]*k[1] for k in group ])
    # print( 'Blocks of  1x1 : \t', S)
    for k, v in R.items() :
        # print(S)
        if k[0] != k[1] : S += 2*v
        else : S += v

    return S




def get_squares_rombs(a, b):
    x, y = calc_rectangle(a,b), calculate_rombs(a, b)
    return x+y




print('\n--------------------------TESTS------------------------------')
t1  = time.time()

print('\ncalc_rectangle : \t',calc_rectangle(3, 1) ,'\n')
print('\nget_one_row_rectangle : \t',get_one_row_rectangle(1) ,'\n')

print('\ncalculate_rombs : \t', calculate_rombs( 6 , 3)  )

print('\nget_squares_rombs : \t', get_squares_rombs( 8, 9)  )


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n================  My FIRST SOLUTION, 3 min  ===============\n')
t1  = time.time()


def cross_hatched_grids(a, b) :
    S = 0
    for i in range(1, a+1) :
        for j in range(1, b+1) :
            mag = get_squares_rombs(i,j)
            print(i,j,'            ', mag)
            S+= mag

    return print('\nAnswer : \t', S)


# cross_hatched_grids(47, 43)             #   Answer : 	 846910284





t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1, 13 ms  INCREDIBIL --------------------------')
t1  = time.time()

# ==== Fri, 30 Jan 2015, 15:48, boondoggle, USA
# After noticing some patterns and playing around with Wolfram Alpha for a while:


from itertools import product, starmap

def grid(x, y):
    """Returns a list of vertices on a grid of given size."""
    return product(range(1, x+1), range(1, y+1) )

def combined_count(x, y):
    if y > x:
        x, y = y, x
    return int(round(1/12 * y * (3 * x**2 * y + 3 * x**2 + 16 * x * y**2 + 3 * x * y - x - 8 * y**3 + 2 * y - 6)))

def total_count(x, y):
    if y > x:
        x, y = y, x
    return sum(starmap(combined_count, grid(x, y)))

print( total_count(47,43 ) )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

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
