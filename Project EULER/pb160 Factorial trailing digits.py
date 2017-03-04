#!/usr/bin/python                   ( ͡° ͜ʖ ͡°)
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
Factorial trailing digits       -       Problem 160

For any N, let f(N) be the last five digits before the trailing zeroes in N!.
For example,

9! = 362880 so f(9)=36288
10! = 3628800 so f(10)=36288
20! = 2432902008176640000 so f(20)=17664

Find f(1,000,000,000,000)


'''
import time
from math import factorial
from gmpy2 import fac
import operator, functools

def prime_sieve(n):       # SECOND FASTEST        o(^_^)o
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[ i*i :: 2*i ] = [False] * ( (n-i*i-1) // (2*i) +1 )
    return [2] + [i for i in range(3, n , 2) if sieve[i] ]







print('\n--------------------------Preliminary TESTS------------------------------')
t1  = time.time()


# 2017-02-03, 12:06 --> Miss the idea  completely !
def factorial_non_zero(b):
    s = 1
    for i in range(1, b+1):
        s *= i
        while not s % 10:
            s //= 10
        s = s % 10**10
    return s

print('factorial_non_zero : \t' ,factorial_non_zero( 10**5 ) )

# 4109700 27753472000000
# 996.     633088
# 997.     188736
# 998.     358528
# 999.     169472
# factorial non zero digit

# f(               10)=36288
# f(              100)=16864
# f(            1,000)=53472
# f(           10,000)=79008
# f(          100,000)=56096
# f(        1,000,000)=12544
# f(       10,000,000)=28125


# http://mathforum.org/library/drmath/view/71768.html     !!!!!!!!!!!!!!!!!!
# https://www.reddit.com/r/math/comments/4fjmt1/finding_the_last_nonzero_digits_of_ginormous/
# http://math.stackexchange.com/questions/130352/last-non-zero-digit-of-a-factorial
# http://mathcentral.uregina.ca/qq/database/qq.09.07/s/mukesh1.html
# http://www.mathpages.com/home/kmath489.htm
# https://comeoncodeon.wordpress.com/2009/06/20/lastnon-zero-digit-of-factorial/


print('\n' , len(str(fac(10**4))) , str(factorial(10**4)) )                   # 27753472

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

def factorial_trailing_digits(n) :
    # primes = [2, 3, 5, 7]
    primes = prime_sieve(10**5)
    F = []
    for p in primes :
        e = 1
        pe = p**e
        f = 0
        while pe <= n :
            if p == 5 :
                F[0][1] = F[0][1]-n//pe
            else : f+= n//pe
            # print(p , 'exp=', e, '    ',p**e ,'     ',n//pe  )
            e+=1
            pe = p**e
        F .append([p,f ] )
    # print(F)
    # F[0][1] = F[0][1]-fives
    # F.pop(2)
    # print(F[:50])

    return functools.reduce( operator.mul , [ i[0]**i[1] for i in F ] ) %10**5

# print('\nfactorial_trailing_digits : \t', factorial_trailing_digits(10**2) )

g = factorial_trailing_digits(10**2)

print('g=' , g)
print('pow mod : \t' ,pow( g , 10**1, 10**5 )  )

print(factorial_trailing_digits(10**4))
print('pow mod : \t' ,pow( factorial_trailing_digits(10**4) , 10**0, 10**5 )  )
print('\n-------------')
print('10             ',factorial_non_zero(10**1))
print('100           ',factorial_non_zero(10**2))
print('1.000          ',factorial_non_zero(10**3))
print('10.000          ',factorial_non_zero(10**4))
print('100.000        ',factorial_non_zero(10**5))
print('1.000.000        ',factorial_non_zero(10**6))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


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
