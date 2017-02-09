#!/usr/bin/python                   ( ͡° ͜ʖ ͡°)
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
                Exploring Pascal's pyramid      -       Problem 154

A triangular pyramid is constructed using spherical balls so that each ball rests on exactly three balls of the next lower level.


Then, we calculate the number of paths leading from the apex to each position:

A path starts at the apex and progresses downwards to any of the three spheres directly below the current position.

Consequently, the number of paths to reach a certain position is the sum of the numbers
immediately above it (depending on the position, there are up to three numbers above it).

The result is Pascal's pyramid and the numbers at each level n are the coefficients of the trinomial expansion (x + y + z)**n.

How many coefficients in the expansion of (x + y + z)**200000 are multiples of 10**12?


'''
import time
import sympy
from math import factorial


from sympy import symbols, expand_mul, exp, log, sin, expand

x, y, z = symbols('x,y,z', positive=True)
print(sympy.expand( (x+y+z)**2 ) ,'\n\n')


print( sympy.binomial_coefficients_list(10) )


def calculate_trinomial_coefficient(n, m, k) :
    '''Description: (x+y+z)**n . The coefficients of (x+y+z)**4 are :
        1, 4, 4, 6, 12, 6, 4, 12, 12, 4, 1, 4, 6, 4, 1
                       1
                    4     4
                 6     12     6
              4    12   12     4
           1     4     6     4     1
    :param n: the power of the expansion
    :param m: is the row of the triangle
    :param k: is the column of the triangle
    :return: int, the coefficient of the trinomial expansion
    :Observations : n >= m, n>=k, m >=k
    :Formula: :   C{n,m} *C{m,k} = n! / [ (n-m)! * (m-k)! * k! ]
    '''
    return factorial(n) // ( factorial(n-m)*factorial(m-k)* factorial(k) )

print('calculate_trinomial_coefficient :\t', calculate_trinomial_coefficient(4, 2, 2 ))




print('\n--------------------------TESTS------------------------------')
t1  = time.time()

def brute_force(n) :
    cnt=0
    for m in range(n+1):
        tmp=[]
        for k in range(m+1):
            c = calculate_trinomial_coefficient(n, m, k)
            # tmp.append( c %10**8 )
            if c %10**6 == 0 : cnt+=1
        print('m= ',m ,'      ', )

    return print('\nBrute Force  Soln: \t', cnt )

# brute_force(20)

#           Brute Force  Soln: 	 32835 ---> 2000 %10**8 ;

print('\n----------------------------------')

def sympy_coeff(n_max) :
    for i in range(2, n_max+1) :
        l = sympy.expand( (x+y+z)**i )
        print(str(i)+'.     ' , l )

for i in range(0, 2*10**5+1) :
    c = calculate_trinomial_coefficient(200000 , i, 0 )%(10**12)
    if c==0 :
        print(str(i)+'.            trinom_coeff :\t', c )


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
