#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
                        Repunit divisibility        -   Problem 129

A number consisting entirely of ones is called a repunit.
We shall define R(k) to be a repunit of length k;

for example, R(6) = 111111.

Given that n is a positive integer and GCD(n, 10) = 1, it can be shown that there always exists a value, k,
for which R(k) is divisible by n, and let A(n) be the least such value of k;   # R(A(n))

for example, A(7) = 6 and A(41) = 5.               #  n=7, 41,  --> n - is the prime

The least value of n for which A(n) first exceeds 10 is 17.                     #    A( n = 17 ) =  16 = A(n) = R(k)   ==> n=17

Find the least value of n for which A(n) first exceeds one-million (10**6) .   A(>10**6) = ?

Find the least n ( =17 prime) when A(n)=R(k) first exceeds 10**6

( Find a prime factor of the repunit > 10**6 which has a factor which wasn't previously found
A(n) is the number of 1's in the repunit. You want to find the smallest n that divides a repunit with more than 1 million digits.

'''
 # 1 2          [11]                n - is a prime,   A(n) - numbers of 1's in the repunit
# 1 3          [3, 37]                      n = 7 , 41,  5363222357
# 1 4          [11, 101]
# 1 5          [41, 271]                --> A(n) = 5 ,   A(41) = 5                      A(257) = 256
# 1 6          [3, 7, 11, 13, 37]       ---> A(n) =  6 , A(7) = 6
# 1 7          [239, 4649]
# 1 8          [11, 73, 101, 137]
# 1 9          [3, 3, 37, 333667]
# 1 10          [11, 41, 271, 9091]
# 1 11          [21649, 513239]
# 1 12          [3, 7, 11, 13, 37, 101, 9901]
# 1 13          [53, 79, 265371653]
# 1 14          [11, 239, 4649, 909091]
# 1 15          [3, 31, 37, 41, 271, 2906161]
# 1 16          [11, 17, 73, 101, 137, 5882353]             A(17) = 16
# 1 17          [2071723, 5363222357]
# 1 18          [3, 3, 7, 11, 13, 19, 37, 52579, 333667]

# 2137.     [1000117]        1000117 1000117
# 30306.     [1000099]        1000099 1000099
# 38463.     [1000039]        1000039 1000039
# 166667.     [1000003]        1000003 1000003

import time
from pyprimes import factorise
import numpy as np
from math import gcd
import gmpy2

def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]


def prime_generator(down, up):         # HIghly Efficient !!!!         THE FASTEST, The BEST , The ONE
    """  Sieve of Eratosthenes              !!!!!!!!! THE FASTEST SIEVE. It won the battle with sieve
    Create a candidate list within which non-primes will be marked as None.
    """
    cand = [i for i in range(3, up + 1, 2)]
    end = int(up ** 0.5) // 2

    # Loop over candidates (cand), marking out each multiple.
    for i in range(end):
        if cand[i]:
            cand[cand[i] + i::cand[i]] = [None] * ( (up // cand[i]) - (up // (2 * cand[i])) - 1 )

    # Filter out non-primes and return the list.
    return  [i for i in cand if i and i > down]


def primesieve(n):          ### o(^_^)o  FASTEST  o(^_^)o  ###  Highly Efficient !!!

    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]

print('\n--------------------------TESTS------------------------------')
t1  = time.time()


primes = primesieve( 10**6 )
primes = set(prime_generator(6 , int(1.5*10**6) ))
print(len(primes) )

def test_lower_repunits( p , limit) :
    for n in range(2, limit) :
        if pow(10, n , 9*int(p) ) == 1:    # If R(k)=(10**k-1)/9  => R(k)=(10**k)%(9*prime_nr) == 1   IIF 10**k is divisible with prime_nr
            # print('the repunit R( '+str(n)+' )  has ',p ,' as a prime   !!')
            return n
    return False

print('\ntest_lower_repunits : \t ', test_lower_repunits(1000003, 10**6),'\n\n')


# Just run this while enjoying tennis in the morning Federer vs Wawrinka
def step_by_step(limit):

    primes = set(prime_generator(6 , int(1.01*10**6) ))
    PRI = primes.copy()
    n_min = 10**8
    for n in range( limit, 2*10**6):             # range(10**6, 2*10**6):
        # if gcd(n, 10) == 1 :
            print(' -----------------------    A(n) repunit length : ', n ,' -------------------------- ',len(primes) )
            P = []
            for p in primes :
                if pow(10, n , 9*int(p) ) == 1:
                    PRI.remove(p)
                    P.append(p)
                    if n_min > p > limit  and n > limit :
                        if test_lower_repunits(p, limit) == False :
                            n_min = p
                            print( '\n++++++++  A('+str(n_min)+') = ', n,'   ++++++++++++     ==', n_min, '\n')

            # print('A(n)=', n , '       n = ',  P,'\n' )
            primes = PRI.copy()

# step_by_step (limit = int(10**6) )


def get_repunits( lower_limit ) :
    p_min = 10**8
    # primes = prime_generator(10**6 , int(1.1*10**6) )
    # primes = prime_generator(lower_limit-5 , lower_limit + 10000 )
    # print(len(primes))
    for n in range( lower_limit, lower_limit+1000 :
        if gmpy2.is_prime(n) == 1 or gcd(n, 10) == 1 :
            # n = test_lower_repunits(p, p)
            if n != False  :


            if n > lower_limit :
                print(p , '     repunit :',n )
                if lower_limit < p < p_min and gcd(10,n) ==1  :
                    p_min = p
                    print('---'*10,'    this is it : \t prime =',p_min,'   repunit = ', n )

    return print('\nAnswer : ', p_min)

get_repunits(10**6)



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

# Tried :   1000003, 1000002, 1000170, 1000171

################        GENERAL IDEA      ####################
# GOOD INFO : http://stdkmd.com/nrr/repunit/tm.cgi?p=100
# GENERAL IDEA :
# Since R(k)=(10**k−1) / 9, to show that p is a factor of R(k), it suffices to show that
# (10**k−1)/9 ≡ 0 (mod p), or  10**k ≡ 1 (mod 9p)
# Example: If 11111 has factor 41 => pow(10, 5, 9*41) = 1   !!!!!!!!!!!!!!!!!!!!!!!!!!!!
print('\nTherefore we can test this idea with 11111 which has 41 as a factor : ', pow(10,5 ,41* 9)  )   # with 3 args pow makes modulo


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
