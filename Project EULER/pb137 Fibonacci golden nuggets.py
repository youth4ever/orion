#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
Arithmetic expressions      -       Problem 93

Consider the infinite polynomial series A_F(x) = x*F_1 + x**2*F_2 + x**3 *F_3 + ...,
where F_k is the k-th term in the Fibonacci sequence: 1, 1, 2, 3, 5, 8, ... ;
that is, F_k = F_(k−1) + F_(k−2),   F_1 = 1 and F_2 = 1.

For this problem we shall be interested in values of x for which A_F(x) is a positive integer.

Surprisingly A_F(1/2)	 = 	(1/2)*1 + (1/2)**2*1 + (1/2)**3*2 + (1/2)**4*3 + (1/2)**5*5 + ...
 	 = 	1/2 + 1/4 + 2/8 + 3/16 + 5/32 + ...
 	 = 	2

The corresponding values of x for the first five natural numbers are shown below.

                                                    x	                AF(x)
                                                √2−1	             1
                                                1/2	                 2
                                                (√13−2)/3	         3
                                                (√89−5)/8	         4
                                                (√34−3)/5	         5

We shall call A_F(x) a golden nugget if x is rational, because they become increasingly rarer;
for example, the 10th golden nugget is 74049690.

Find the 15th golden nugget.

'''
import time
from math import sqrt
import  gmpy2
from decimal import *
getcontext().prec = 100

def Fibonacci_Binet(n_th) :
    ''':Description:    Returns the Fibonacci corresponding to the number  and uses the Binet Formula.
        http://mathworld.wolfram.com/BinetsFibonacciNumberFormula.html
        :param n_th: F_nth Fibonacci in sequence
        :return: str, first 9 digits of the Fibonacci number
    '''

    phi = Decimal((1+5**(1/2))/2)
    phi_ = Decimal((1- 5**(1/2))/2)
    # phi = (1+5**(1/2))/2
    # phi_ = (1-5**(1/2))/2
    # a = ( ( phi**n_th-phi_**n_th ) / ( phi - phi_) )%(10**9)
    a = str(((phi**n_th)-(phi_)**n_th)/( phi - (phi_)))[0:10].replace( '.' , '')
    # b =   ( (( 1 + np.sqrt(5))/2)**n_th - ((1 - np.sqrt(5))/2)**n_th  ) /np.sqrt(5)
    return str(a)

def Fibo_gen():
    #   Fibonacci GENERATOR , while loop
    a1, a2 = 0, 1
    while True:
        a = a1 + a2
        yield a
        a1, a2 = a2, a

def Fibonacci_kth( k ):
    return (1/5**(1/2) )*( ((1+ 5**(1/2)) /2 )**k - ((1- 5**(1/2))/2 )**k )

print('Fibonacci_kth : ',Fibonacci_kth (541))

print('Test for the Fibonacci_Binet : ', Fibonacci_Binet(50))
print('gmpy2.fib : \t\t\t\t\t\t\t' ,gmpy2.fib(50) )



A_F = lambda x : x/(1-x-x**2)

print('A_F :\t', A_F(1/2))



print('\n--------------------------TESTS------------------------------')
t1  = time.time()

epsilon = 10**-9
FG = Fibo_gen()
f1=1
for i in range(1, 500):
    f2 = next(FG)
    f3 = f1**2+f2**2
    x = (pow(f3, 0.5) - f1 )/f2
    A = A_F(x)
    if (A-round(A)) < epsilon :
        print(str(i)+'.    ', f1, f2,'    ' ,f3,'       ' , round(A) )

    f1 = f2


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
