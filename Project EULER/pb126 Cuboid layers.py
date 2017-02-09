#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
                        Cuboid layers     -    Problem 126

The minimum number of cubes to cover every visible face on a cuboid measuring 3 x 2 x 1 is 22.

- If we then add a second layer to this solid it would require 46 to cover every visible face,
- the third layer would require 78 cubes,
- and the fourth layer would require  118 cubes to cover every visible face.

- However, the first layer on a cuboid measuring 5 x 1 x 1 also requires 22 twenty-two cubes;
- similarly the first layer on cuboids measuring 5 x 3 x 1, 7 x 2 x 1, and 11 x 1 x 1 all contain forty-six cubes.

We shall define C(n) to represent the number of cuboids that contain n cubes in one of its layers.
So C(22) = 2, C(46) = 4, C(78) = 5, and C(118) = 8.

It turns out that 154 is the least value of n for which C(n) = 10.

Find the least value of n for which C(n) = 1000.

'''
import time, gmpy2
from itertools import combinations
from math import gcd
import operator, functools

# print(sympy.npartitions( 5 ))


def partition_in_three(n):     #2017-02-06 Some minor losses, but no time to fix it now
    ''':Usage:  >>> for i in P :  print( i )
    :param n: int, number
    :return: generator, tuple with partitions : (9, 1, 1), (8, 2, 1), (7, 3, 1) ....            '''
    a, b, c = n-1, 0, 1
    bc = b+c
    while a > n/3+1 :
        a-=1
        bc+=1
        for i in range( 1, bc//2+1):
            b=bc-i ; c=bc-b
            if a>=b :
                yield a, b, c
    if n%3 == 0 :
        yield n//3, n//3, n//3

# must use partition of a number to find cuboid shapes --> reverse engineering, complicated # 2016-12-02 - we'll solve it later
print('\n--------------------------TESTS------------------------------')

P = partition_in_three(11)
cnt=0
for i in P :
    cnt+=1
    print( str(cnt)+'.    ',  i )

print('\n---------------------------------------------\n')

def get_cuboid_layer( P ):
    C = list( combinations(P, 2 ))
    # F =[]
    # for i in C :
    #     F.append(gcd ( i[0], i[1] ) )
    # C2 = list( combinations(F, 2 ))
    S = 0
    for I in C :
        S+= functools.reduce( operator.mul, I )

    return 2*S

print('make_cuboid : \t ', get_cuboid_layer(  [3,2,1 ]) )

D = {}
for n in range(4, 30) :
    P = partition_in_three(n)
    for i in P :
        g = get_cuboid_layer(i)
        print(str(n)+'.     ', i, get_cuboid_layer(i))
        if g not in D : D[g] =1
        else : D[g]+=1

print('\n', D)

# @2017-02-07. I must also count the other layers.
# Doesn't suffice to count only the firts layer of a partition configuration. Must go until the limit



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
