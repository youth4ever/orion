#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
                            Idempotents     -       Problem 407

If we calculate a**2 mod 6 for 0 ≤ a ≤ 5 we get: 0,1,4,3,4,1.

The largest value of a such that    :   a**2 ≡ a (mod 6)        is = 4.
Let's call M(n) the largest value of a < n such that            :       a**2 ≡ a (mod n).
So M(6) = 4.

Find ∑M(n) for 1 ≤ n ≤ 10**7.


'''
import time, gmpy2
from math import log, gcd

def primesieve(n):          ### o(^_^)o  FASTEST  o(^_^)o  ###  Highly Efficient !!!
    import numpy as np
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]

def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    from pyprimes import factorise
    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]


Sm = 0
for n in range(1, 1000) :
    if gmpy2.is_prime(n) : Sm +=1

    # else :
    #     for n in primes :
    else :
        for a in range(n-1, -1, -1):
            if pow(a, 2, n  ) == a%n :
                print(str(n)+'.     ', a ,a**2,  '    ', a%n  ,'    modulo:\t' , pow(a, 2, n), pow(a, 3, n), (a*(a-1))%n , '   gcd=',gcd(n,a), ' ',get_factors(n) )
                break
    print('-----------')

print('math log function :\t', log(11**5, 11))
print('math log function :\t', log(11**5, 11) %1 == 0 )




# @2017-01-22 , 22:45
# http://www.math.stonybrook.edu/~moira/mat331-spr10/papers/1978%20McLeanGroups%20in%20Modular%20Arithmetic.pdf
# https://en.wikipedia.org/wiki/Idempotent_(ring_theory)#Types_of_ring_idempotents
# http://www.mersenneforum.org/showthread.php?t=21717
# https://crypto.stanford.edu/pbc/notes/numbertheory/exp.html







print('\n--------------------------TESTS------------------------------')
t1  = time.time()

Lim = 10**6
primes = primesieve( int( Lim**(1/2)) )
print(len(primes), primes)


print('\n-----Interesting test. See the regularity of 1*2, 2*3, 3*4, 4*5 ... ----------------')
n=155
for i in range(n-1,0,-1):
    print(i,  (i*(i-1))%n ,'   ', n-i, n-i+1   )

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
