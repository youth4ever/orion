#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
Investigating Gaussian Integers     -       Problem 153

As we all know the equation x2=-1 has no solutions for real x.
If we however introduce the imaginary number i this equation has two solutions: x=i and x=-i.
If we go a step further the equation (x-3)2=-4 has two complex solutions: x=3+2i and x=3-2i.
x=3+2i and x=3-2i are called each others' complex conjugate.
Numbers of the form a+bi are called complex numbers.
In general a+bi and a−bi are each other's complex conjugate.

A Gaussian Integer is a complex number a+bi such that both a and b are integers.
The regular integers are also Gaussian integers (with b=0).
To distinguish them from Gaussian integers with b ≠ 0 we call such integers "rational integers."
A Gaussian integer is called a divisor of a rational integer n if the result is also a Gaussian integer.
If for example we divide 5 by 1+2i we can simplify  in the following manner:
Multiply numerator and denominator by the complex conjugate of 1+2i: 1−2i.
The result is :
5/1+2i  = 5/i+2i * 1-2i/1+2i = 5(1-2i) / 1-(2i)**2 = 5(1-2i) / 1-(-4) = 5(1-2i) / 5 = (1-2i)

So 1+2i is a divisor of 5.
Note that 1+i is not a divisor of 5 because  5/1+i  = 5/2 - 5i/2
Note also that if the Gaussian Integer (a+bi) is a divisor of a rational integer n, then its complex conjugate (a−bi) is also a divisor of n.

In fact, 5 has six divisors such that the real part is positive: {1, 1 + 2i, 1 − 2i, 2 + i, 2 − i, 5}.
The following is a table of all of the divisors for the first five positive rational integers:

            +--------------------------------------------------+
           | n | Gaussian integer divisors    | Sum s(n) of      |
           |   | with positive real part        | these    divisors |
           |---+------------------------------+---------------|
           | 1 |      1                                      | 1                   |
           |---+------------------------------+---------------|
           | 2 |     1, 1+i, 1-i, 2                      | 5                   |
           |---+------------------------------+---------------|
           | 3 |     1, 3                                   | 4                  |
           |---+------------------------------+---------------|
           | 4 |     1, 1+i, 1-i, 2, 2+2i, 2-2i,4    | 13                |
           |---+------------------------------+---------------|
           | 5 |    1, 1+2i, 1-2i, 2+i, 2-i, 5      | 12                  |
           +--------------------------------------------------+

For divisors with positive real parts, then, we have: .

For 1 ≤ n ≤ 10**5, ∑ s(n)=17924657155.

What is ∑ s(n) for 1 ≤ n ≤ 10**8?

'''
import time
from math import gcd

print('\n--------------------------TESTS------------------------------')

import numpy, cmath


def divisor_sum_sieve(n):
    import numpy as np
    # sieve = np.array([0] * (n + 1) )
    sieve = [0] * (n + 1)
    # sieve[4 :: 2]= [2]*len(sieve[4 :: 2])   #### ATTENTION !!!! MODIFICATION for Gaussian Integer
    limit =  int( n**(1/2) ) + 1
    for i in range(1, limit):
        sieve[i * i] += i
        temp = i + 1
        for j in range(i * i + i, n + 1, i):
            sieve[j] += i  +  temp
            temp += 1
#     print('Divisors Sum sieve ', sieve)
    return sieve




t1  = time.time()

# a= numpy.complex(3,3 ) - numpy.complex(1,4)
# print(a)

print( numpy.complex(2342345)/numpy.complex(1234, 274754654))



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

################
t1  = time.time()

# z = 1-2j
# print(z, z.conjugate() , z.imag, abs(z)   )
# print( 5/(z) )
# print()
#
# a = 3+4j
# print(a, a.conjugate() , a.imag, abs(a)   )
# print( 25/(a) )
#
# print()
# b = 2+2j
# print(b ,b.conjugate() ,  b.real ,b.imag, abs(b)   )
# print( 4/(b) )


print()
c = 15+8j
print(c, c.conjugate() ,  c.real ,c.imag, abs(c)   )
print( 289/(c) )



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n--------------------------MY FIRST SOLUTION, 1 hour------------------------------')
t1  = time.time()

# 2016-12-18 17:48
# OBSERVATION : The problem Reduces in finding to a number n, decompose it into 2 parts a & b such that:
# a**2+b**2 = n
# You must decompose a number in two perfect squares. Must solve other problems first
# Can you predict from what kind of numbers 3+4i will be a divisor? And 3-4i    ?
# @2017-03-18,01:30 missed divisors of 10 : look in the notebook : their total sum = 38 (for 10)


def gaussian_integers_sol_1(lim = 10**2) :
    spec_value = 52
    up = int( lim**(1/2))
    GI = divisor_sum_sieve( lim )
    # print( 'Gaussian Integers init list : ' ,len(GI) ,GI[:20], GI[-20::] ,'\n' )
    print( '\nSpecial value check of the value : \t ' , spec_value , '     ' ,GI[spec_value] ,'\n' )

    for i in range(1, up+1 ):
        for j in range(1, i+1 ) :
            if gcd(i,j) ==1 :
                q = i**2+j**2
                if q > lim  : break

                factor = q
                print(' ===   q= ', q ,'       i, j =  ', i, j ,'       factor= '  ,  factor ,'=======')
                while q <= lim :

                    for k in range(q  ,lim+1, q ) :
                        if i == j :
                            add = (i+j) * k//q
                        if i != j :
                            add = 2*(i+j) * k//q

                        GI[k] +=add

                        # print('--- q = ', k,'     incr= ', k//q,'     factor = ', factor, '     i, j = ' ,i*k//q, j*k//q, '          Add : ' ,   add )

                    q += factor

    print( '\nGaussian Integers final list : ' ,len(GI) ,GI[:20],'\n' ,GI[-20::] ,'\n' )
    # print( '\nSpecial value check of the value : \t ' , spec_value , '      ' ,GI[spec_value] ,'\n' )

    return print('\nAnswer : \t', sum(GI)  )


gaussian_integers_sol_1(10**8)              #   Answer : 	 17971254122360635


# CHECK VALUES :
# 10: 161       # 100: 16749           # 1000: 1752541          # 10000: 178231226          # 100000: 17924657155


t2  = time.time()
print('\nCompleted in :', round((t2-t1)/60,6), 'min\n\n')                   #     Completed in : 3735.53666 s

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
