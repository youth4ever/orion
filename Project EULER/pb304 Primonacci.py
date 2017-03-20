#!/usr/bin/python                   ( ͡° ͜ʖ ͡°)
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
            Primonacci      -       Problem 304

For any positive integer n the function next_prime(n) returns the smallest prime p
such that p>n.

The sequence a(n) is defined by:
a(1)=next_prime(1014) and a(n)=next_prime(a(n-1)) for n>1.

The fibonacci sequence f(n) is defined by:
f(0)=0, f(1)=1 and f(n)=f(n-1)+f(n-2) for n>1.

The sequence b(n) is defined as f(a(n)).

Find ∑b(n) for 1≤n≤100 000. Give your answer mod 1234567891011.


'''
import time, gmpy2
from decimal import *
getcontext().prec = 100


def Fibonacci_Binet(n_th) :
    ''':Description:    Returns the Fibonacci corresponding to the number  and uses the Binet Formula.
        http://mathworld.wolfram.com/BinetsFibonacciNumberFormula.html
        :param n_th: F_nth Fibonacci in sequence
        :return: str, first 9 digits of the Fibonacci number
    '''
    # phi = Decimal((5**(1/2)+1)/2)
    # phi_ = Decimal((1- 5**(1/2))/2)
    m = 1234567891011
    phi = (1+5**(1/2))/2
    phi_ = (1-5**(1/2))/2
    a =  (  (phi**n_th)% m  - ( phi_**n_th)% m  ) / ( phi % m - phi_ %m )
    # a = str(((phi**n_th)-(phi_)**n_th)/( phi - (phi_)))[0:10].replace( '.' , '')
    # b =   ( (( 1 + np.sqrt(5))/2)**n_th - ((1 - np.sqrt(5))/2)**n_th  ) /np.sqrt(5)
    return a

def fibonacci_gen():
    """Fibonacci numbers generator"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# def fib(x) :
#     a = matrix(GF, [0, 1])
#     b = matrix(GF, [[0, 1],
#                     [1, 1]])
#     return (a * b88(x - 1))[0][1]

# http://www.topcoder.com/tc?module=Static&d1=features&d2=010408
# b(1)=428,562,224,098 mod 1234567891011

t1  = time.time()


test = gmpy2.next_prime(10**14)
print('\ngmpy2 next prime : \t', test)
print('\ngmpy2 next prime : \t',gmpy2.next_prime(test) )




t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------TESTS------------------------------')
t1  = time.time()


# 2017-02-26. 11:15 - Finally understood what the problem asks for :
# you take next_prime(10**14) term of the Fibonacci serie
# I think that it can be done ONLY with Binet Formula

F = fibonacci_gen()
next(F)

a= gmpy2.next_prime(10**14)
for i in range(1, 10**2):
    print( a ,'         ',  Fibonacci_Binet(a ) )
    a = gmpy2.next_prime(a)

# s=''
# for i in range(1,200) :
#     s+=str(i)
# print(s)

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
