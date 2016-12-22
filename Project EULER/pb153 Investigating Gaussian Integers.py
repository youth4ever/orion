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


print('\n--------------------------TESTS------------------------------')

import numpy, cmath



t1  = time.time()

# a= numpy.complex(3,3 ) - numpy.complex(1,4)
# print(a)

print( numpy.complex(2342345)/numpy.complex(1234, 274754654))



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

################
t1  = time.time()

z = 1-2j
print(z, z.conjugate() , z.imag, abs(z)   )
print( 5/(z) )
print()

a = 3+4j
print(a, a.conjugate() , a.imag, abs(a)   )
print( 25/(a) )

print()
b = 2+2j
print(b ,b.conjugate() ,  b.real ,b.imag, abs(b)   )
print( 4/(b) )


print()
c = 15+8j
print(c, c.conjugate() ,  c.real ,c.imag, abs(c)   )
print( 289/(c) )



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------TESTS------------------------------')

# 2016-12-18 17:48
# OBSERVATION : The problem Reduces in finding to a number n, decompose it into 2 parts a & b such that:
# a**2+b**2 = n
# You must decompose a number in two perfect squares. Must solve other problems first

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
