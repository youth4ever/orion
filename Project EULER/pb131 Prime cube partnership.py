#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Wed, 16 Nov 2016, 23:19
#The  Euler Project  https://projecteuler.net
'''
                                                        Prime cube partnership      -       Problem 131
There are some prime values, p, for which there exists a positive integer, n, such that
the expression n**3 + n**2 p is a perfect cube.

            For example, when p = 19,   8**3 + 8**2×19 = 12**3.

What is perhaps most surprising is that for each prime with this property the value of n is unique,
and there are only four such primes below one-hundred.

How many primes below one million have this remarkable property?
'''
import time
import gmpy2
from math import gcd, sqrt,  pow
from decimal import *
getcontext().prec =100

def sieve(lower, upper_bound):
    ''':Description:        SIEVE OF ERATOSTHENES ALGORITHM  , SECOND FASTEST
    :param:      :lower: = lower_integer including
                     :upper_bound: = upper integer excluding
    :returns:   a list containing all primes between lower and upper bound
    :Usage:             Example:    primes = sieve(2, 100)                    '''

    n = upper_bound + 1
    check = [True] * n
    check[0] = check[1] = False
    for i in range(2, int(upper_bound**0.5) + 1):
        if check[i]:
            for j in range(i**2, upper_bound + 1, i):
                check[j] = False
    primes = [i for i, flag in enumerate(check) if flag and i > lower ]
    return primes


def is_perfect_cube(n):
    c = int(n**(1/3.))
    return (c**3 == n) or ((c+1)**3 == n)

def factorise(n):
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    from pyprimes import factorise
    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]

print('\nTest is_perfect_cube Function :  ', is_perfect_cube(343))
print('Test is_perfect_cube Function :  ', 17.1**3 , is_perfect_cube(17.1**3))
print('Test is_perfect_cube Function :  ', 64 , is_perfect_cube(64))

primes = sieve(1,100)

print('\n--------------------------TESTS------------------------------')

for n in range(1, 100):
    for p in primes:
        x = n**3 + n**2 * p
        x13 = round( x**(1/3.))
        if is_perfect_cube(x):
            print('p= ' , p,  '    n=',n ,   '   x13=' , round( x**(1/3.)) , '   gcd=', gcd(n , x13   ) )

print('---------------------------')

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

cubes = [i**3 for i in range(1,1001)]

def prime_cube_partners(up_range) :
    cnt=0
    for n in cubes:
        z = round(pow(n, 1/3) + 1)
        x = round(pow(n, 1/3)**2 * z )
        p = (x**3 - n**3) / (n*n)
        p = int(p)
        if p > up_range :
            break
        # print(p,  n , x , z , pow(n, 1/3) ,'   <--- TEST')
        if gmpy2.is_prime(p) == True :
            cnt+=1
            print(str(cnt)+'.    p=' , p ,  '  n=', n  , '  x=' , x  , '   gcd=', int(pow(n, 1/3)**2),'   nr_base=' , round(pow(n, 1/3)) , '  z=',z  )
    return print('\n\nAnswer:  ', cnt)

prime_cube_partners(10**6)

#
# p=  7     n= 1    x= 2
# p=  19     n= 8    x= 12
# p=  37     n= 27    x= 36
# p=  61     n= 64    x= 80
# p=  127     n= 216    x= 252
# p=  271     n= 729    x= 810
# p=  331     n= 1000    x= 1100
# p=  397     n= 1331    x= 1452
# p=  547     n= 2197    x= 2366
# p=  631     n= 2744    x= 2940
# p=  919     n= 4913    x= 5202




t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

# General formula: n^9 + n^6 * p = (n^3 + n^2)^3 where p is a prime number.
# From the above formula results that p must have the form: 3n^2 + 3n + 1.



print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')




print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()

def isPrime(n):
    if n==1:return False
    if n<4:return True
    if not n%2:return False
    if n<9:return True
    if not n%3:return False
    r=int(n**0.5)
    f=5
    while f<=r:
          if not n%f:return False
          if not n%(f+2):return False
          f+=6
    return True

M =10**6
nb = 0
for n in range(M+1):
    p =(n+1)**3 - n**3
    if p>M:break
    if isPrime(p):
       print(n,p)
       nb +=1
print("Il y en a : ",nb)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

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

print('\n--------------------------SOLUTION 4, SLOWER  ,wakkadojo, USA --------------------------')
t1  = time.time()

# I could have thought hard about this problem, but it was easy enough to just muddle through

def sieve (n):
    s, p = [ False if i % 2 == 0 else True for i in range (n) ], [2]
    s[0], s[1], s[2] = False, False, True
    for i in range (3, n):
        if s[i]:
            p += [i]
            for j in range (2*i, n, i):
                s[j] = False
    return p

iscube = lambda x: int (x**(1/3)+0.5)**3 == x

p, c, l = sieve (1000000), 0, 0
for x in p:
    for y in range (l+1, l+20):
        a = y**3
        if iscube (a**3 + a**2*x):
            l, c = y, c+1
print (c)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5, SLOW ,  aolea, Spain  --------------------------')
t1  = time.time()


# if we consider n**3+p*n**2 = (n+x)**3
# p must be p > 3*x and n | x**3 as per the rational root theorem

import pyprimes
import sympy

def solve():
    count = 0
    for x in range(1,int(10**6/3)+10):
        for n in sympy.divisors(x**3):
           p = int(((n+x)**3-n**3)/n**2)
           if  p > 3*x and p<10**6 and pyprimes.isprime(p):
                if n**3 + p*n**2 == (n+x)**3:
                    count = count + 1
                    print(count,n,'** 3 +',p,'*',n,'** 2 =',n+x,'** 3')
    print(count)

# solve()                                          # Uncoment to activate

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


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
