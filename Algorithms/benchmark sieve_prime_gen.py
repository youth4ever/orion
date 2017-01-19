
import functools, time
from math import sqrt

def sieve(n):       # SECOND FASTEST
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]


import numpy as np
def primesieve(n):          ### o(^_^)o  FASTEST  o(^_^)o  ###  HIghly Efficient !!!
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1, dtype=bool)
    print(sieve)
    for i in range(2, int((n+1)**0.5+1)):
        print(i)
        if sieve[i]:
            sieve[2*i::i] = False
            print(2*i, i, sieve[2*i::i])
    print(sieve)
    return np.nonzero(sieve)[0][2:]


def prime_generator(lower, upper):      # THIRD FASTEST
    """  Sieve of Eratosthenes
    Create a candidate list within which non-primes will be marked as None.         """
    cand = [i for i in range(3, upper + 1, 2)]
    end = int(upper ** 0.5) // 2
    # Loop over candidates (cand), marking out each multiple.
    for i in range(end):
        if cand[i]:
            cand[cand[i] + i::cand[i]] = [None] * ( (upper // cand[i]) - (upper // (2 * cand[i])) - 1 )

    # Filter out non-primes and return the list.
    return [2] + [ i for i in cand if i and i > lower ]


print('\n------------------1 ----   ----------------')
t1  = time.time()

n=10**2

primes = primesieve(n)
print(primes[-100:])


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

#################### #####################

print('\n--------------- 2 ----  ------------------')
t1  = time.time()

# primes = sieve(n)
# print(primes[-10:])

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#################### #####################

print('\n--------------- 3 ---- ------------------')
t1  = time.time()


# primes = prime_generator(2, n)
# print(primes[-10:])


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

# #################### #####################

print('\n--------------- 4 ------------------')
t1  = time.time()



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

