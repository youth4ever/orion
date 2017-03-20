
import functools, time
from math import sqrt

################################

def sieve(n):       # SECOND FASTEST
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i :: 2*i] = [False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

################################

def numpy_prime_sieve(n):          ### o(^_^)o  FASTEST  o(^_^)o  ###  Highly Efficient !!!
    import numpy as np
    """return array of primes 2<=p<=n"""
    sieve=np.ones( n+1, dtype=bool )
    for i in range( 2, int((n+1)**0.5+1) ) :
        if sieve[i] :
            sieve[2*i :: i] = False
    return np.nonzero(sieve)[0][2:]

################################

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

################################

import math
def primes_up_to(n):
    # http://code.activestate.com/recipes/576640/
    nroot = int(math.sqrt(n))
    sieve = [True] * (n + 1)# range(n + 1)
    sieve[0] = False
    sieve[1] = False

    for i in range(2, nroot+1):
        if sieve[i]:
            m = n / i - i
            # print(i,'   ', m )
            sieve[i * i: n + 1: i] = [False] * (int(m) + 1)

    return [i for i in range(n+1) if sieve[i]]

#######################


def primes2(n):             # NICE SECOND FASTEST !!!!!
    """ Input n>=6, Returns a list of primes, 2 <= p < n
    http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188"""
    n, correction = n-n%6+6, 2-(n%6>1)
    sieve = [True] * (n//3)
    for i in range(1,int(n**0.5)//3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      k*k//3 ::2*k] = [False] * ((n//6-k*k//6-1)//k+1)
        sieve[k*(k-2*(i&1)+4)//3::2*k] = [False] * ((n//6-k*(k-2*(i&1)+4)//6-1)//k+1)
    return [2,3] + [3*i+1|1 for i in range(1,n//3-correction) if sieve[i]]

##################################

import numpy
def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n
    http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188 """
    sieve = numpy.ones(n//3 + (n%6==2), dtype=numpy.bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]



##################################

import numpy
def primesfrom3to(n):
    """ Returns a array of primes, 3 <= p < n
    http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188 """
    sieve = numpy.ones(n//2, dtype=numpy.bool)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = False
    return 2*numpy.nonzero(sieve)[0][1::]+1


##################################

def primes1(n):
    """ Returns  a list of primes < n
    http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188  """
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1, 2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]


##################################

def primes0(n):
    """ Returns  a list of primes < n
    http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188 """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]



###### SET NUMBER START ##########
n = 10**7
####### -------------------- ############

print('\n------------------1 ----   ----------------')
t1  = time.time()



primes = sieve(n)
print(primes[:10], primes[-10:])


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

#################### #####################

print('\n--------------- 2 ----  ------------------')
t1  = time.time()

primes = numpy_prime_sieve(n)
print(primes[:10], primes[-10:])

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#################### #####################

print('\n--------------- 3 ---- ------------------')
t1  = time.time()


primes = prime_generator(2, n)
print(primes[:10], primes[-10:])


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

# #################### #####################

print('\n--------------- 4 ------------------')
t1  = time.time()

primes = primes_up_to(n)
print(primes[:10], primes[-10:])


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


# # #################### #####################

print('\n--------------- 5 ------------------')
t1  = time.time()

primes = primes2(n)
print(primes[:10], primes[-10:])


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

# # #################### #####################

print('\n--------------- 6 ------------------')
t1  = time.time()

primes = primesfrom2to(n)
print(primes[:10], primes[-10:])


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

# # #################### #####################

print('\n--------------- 7 ---- THE FASTEST --------------')
t1  = time.time()

primes = primesfrom3to(n)
print(primes[:10], primes[-10:])


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

# # #################### #####################

print('\n--------------- 8 ------------------')
t1  = time.time()

primes = primes1(n)
print(primes[:10], primes[-10:])


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

# # #################### #####################

print('\n--------------- 9 ------------------')
t1  = time.time()

primes = primes0(n)
print(primes[:10], primes[-10:])


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

