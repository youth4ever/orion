#!/usr/bin/python                   ( ͡° ͜ʖ ͡°)
# Solved by Bogdan Trif @       Completed on Wed, 1 Feb 2017, 20:31
#The  Euler Project  https://projecteuler.net
'''
                Totient Chains      -       Problem 214

Let φ be Euler's Totient function, i.e. for a natural number n,
φ(n) is the number of k, 1 ≤ k ≤ n, for which gcd(k,n) = 1.

By iterating φ, each positive integer generates a decreasing chain of numbers ending in 1.
E.g. if we start with 5 the sequence 5,4,2,1 is generated.
Here is a listing of all chains with length 4:

5,4,2,1
7,6,2,1
8,4,2,1
9,6,2,1
10,4,2,1
12,4,2,1
14,6,2,1
18,6,2,1
Only two of these chains start with a prime, their sum is 12.

What is the sum of all primes less than 40.000.000 which generate a chain of length 25?


'''
import time, gmpy2
import sympy
from pyprimes import factorise

def sieve(n):       # SECOND FASTEST
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def prime_generator(lower, upper):      #THIRD FASTEST
    """  Sieve of Eratosthenes              !!!!!!!!! THE FASTEST SIEVE. It won the battle with sieve
    Create a candidate list within which non-primes will be marked as None.         """
    cand = [i for i in range(3, upper + 1, 2)]
    end = int(upper ** 0.5) // 2

    # Loop over candidates (cand), marking out each multiple.
    for i in range(end):
        if cand[i]:
            cand[cand[i] + i::cand[i]] = [None] * ( (upper // cand[i]) - (upper // (2 * cand[i])) - 1 )

    # Filter out non-primes and return the list.
    return [2] + [ i for i in cand if i and i > lower ]

def Euler_totient(n):   # o(^_^)o  @2017-01-23, 10:30 by Bogdan Trif
    ''':Works without errors !
        https://en.wikipedia.org/w/index.php?title=Euler%27s_totient_function&action=edit&section=3
    :param n: int
    :return: int, Euler Phi, Euler Totient
    '''
    def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
        ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
        return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]
    F = set(get_factors(n))
    for i in F :
        n*=(1-1/i)
    return round(n)


print('\n--------------------------TESTS------------------------------')
t1  = time.time()

NR = list(range( 31455263372, 31455263372+10) )

for i in NR :
    print( sympy.totient(i), end='  ' )

print(sympy.totient(1))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

R = {1:1}
def totient_chain(n):
    n0 = n
    cnt = 1
    while n != 1 :
        if n  in R :
            R[n0] = R[n]+cnt-1
            # print('print\t ',n0,'     R[n0]: ' ,R[n0] ,'     R[n]=' ,R[n], cnt, R[n]+cnt , R )
            return R[n]+cnt-1
        else :
            # print(n,'  ---')
            n = sympy.totient(n)
            cnt+=1
    R[n0] = cnt

    return cnt



def totient_chain1(n):
    if n==1 : return 1
    cnt = 1
    while n != 1 :
        n = sympy.totient(n)
        cnt+=1
    return cnt

# print('\ntotient_chain : \t ', totient_chain1(18) )

print('\n================  My BRUTE FORCE SOLUTION, VERY SLOW, 1 hour  ===============\n')
t1  = time.time()

primes = prime_generator(9.5*10**6, 4*10**7)           # 40.000.000
print(len(primes), primes[:50] , '\n\n')


def brute_force():
    S, cnt =0, 0
    for p in primes:
        # b = totient_chain1(i)
        a = totient_chain(p)
        if a == 25:
            S+=p
        if a >=25 :
            cnt+=1
            print(str(cnt)+'.       ', p ,'          length: ',  a  )

    return print('\nAnswer : \t', S , '\n\n')       #Answer : 	 1677366278943

print('\n', R)


# for i in primes: print(i)

t2  = time.time()
print('\nCompleted in :', round((t2-t1), 6), 's\n\n')


print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()







t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,   --------------------------')
t1  = time.time()

# === Mon, 6 May 2013, 12:10, tom.wheldon, England
# I calculate phi(n) and chain length with a single pass through a sieve.
# Runs in ~84s, which seems reasonable for Python.
# This was my 200th problem - thanks to all at Project Euler for the fun I've had solving them.

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,  40 sec --------------------------')
t1  = time.time()

# ==== Wed, 3 Aug 2016, 05:16, j123, Canada
# We only have to compute phi values up to half the limit, since for a prime p, we have
# ϕ(ϕ(p))=ϕ((p−1)/2)∗ { 2 , if p ≡ 1(mod 4)
#                                   {1 , otherwise
# Here's clean Python code that runs in about 30 seconds on my ancient laptop (interpreted);
# adapting to pypy (using Animus's code for computing phi values and replacing itertools calls with explicit loops)
# gives a program that runs about 30% faster than his.
# There is a redundant calculation of primes up to 20,000,000 but it only takes a fraction of a second.

try: #i.e. if using Python2
    range=xrange
except Exception:
    pass

from array import array
from itertools import chain, compress, count

#adapted from the pypy code of Animus
def phi_values(N):
    phi = array('l', [0]) * 2 + array('l', [1]) * (N - 1)
    for p, ph in enumerate(phi):
        if ph != 1: continue
        p_pow, multiple = p, p-1
        while p_pow <= N:
            for i in range(p_pow, N + 1, p_pow):
                phi[i] *= multiple
            multiple = p
            p_pow *= p
    return phi

def primes(N):
    '''Iterator of primes up to and including N'''
    b = N - 1 >> 1
    if b <= 0: return iter(())
    B = bytearray([0]) + bytearray([1]) * b
    for c in count(1, 2):
        if B[c >> 1]:
            a = c * c >> 1
            if a > b: return chain([2], compress(count(1, 2), B))
            B[a::c] = bytearray([0]) * ((b - a) // c + 1)

def do(N=4*10**7, k=25):
    phi = phi_values(N // 2) #It sets phi(0)=phi(1)=0
    x = bytearray([0]) * (N // 2 + 1)
    for i in range(1, N // 2 + 1): x[i] = x[phi[i]] + 1
    return sum(p for p in primes(N)
               if x[phi[p // 2] * (2 if p & 3 == 1 else 1)] == k - 2)

# print(do())


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,  30 sec --------------------------')
t1  = time.time()

# ==== Fri, 11 Nov 2016, 13:22, mbh038, England
# bout 13 s with this (after a lot of effort to get it within 1 minute, never mind that low!), in Python 3.
# About 8 s of the  time is spent in the euler totient sieve for n=20,000,000.
# The prime sieve, on the other hand, takes 250 ms for n=40,000,000.
# Animus says his/her code runs in 4 s using PyPy. Without PyPy, that code runs in 53 s on my machine.
#
# I create an array of totient values and, starting from each prime, iterate my way through this until I arrive at a power of two.
# So far, when I have tried to memoise this part of the task beyond dipping out when I hit a power of two,
# I have not been able to get the overhead down to the point where it was worth the effort.


import numpy as np

def pe214(n,length):

    t=time.clock()

    primes=primesieve(n)
    lowprimes=primes[primes[:] <=n//2]
    highprimes=primes[primes[:] > n//2]
    ets=etsieve(n//2,lowprimes)
    lowprimes=lowprimes[lowprimes[:] >2**(length-2)]
    chains2={2**x:x+1 for x in range(25)}

    csum=0
    def clength(pos,ets,count,required):
        while 1:
            if pos in chains2:
                count+=chains2[pos]
                break
            count+=1
            pos=ets[pos]
        return count==required

    for prime in lowprimes:
        if clength(prime-1,ets,1,length): csum+=prime

    tf={0:2,2:1}
    for prime in highprimes:
        if clength((prime-1)//2,ets,tf[(prime-1)%4],length): csum+=prime

    print(csum,time.clock()-t)

def primesieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]

def etsieve(n,primes):
    """return array of totient(x) for x from 2 to n"""
    sieve=np.array(range(n+1),dtype=float)
    for i in primes:
        if sieve[i]==i:
            sieve[i::i]*=(1-1/i)
    return sieve.astype(int)

# pe214(40000000, 25)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4, SIEVING ,  120 sec --------------------------')
t1  = time.time()

# === Sat, 10 Aug 2013, 19:59, Animus, Germany
# Just 2 seconds in Python (using PyPy) due to an efficient totient sieve.
def animus():
    n = 4 * 10 ** 7

    # fill totient sieve
    phi = [1] * (n + 2)
    p = 2
    while p <= n:
        off = p
        while off <= n:
            phi[off] *= p - 1
            off += p
        pot = p * p
        while pot <= n:
            off = pot
            while off <= n:
                phi[off] *= p
                off += pot
            pot *= p
        p += 1
        while phi[p] > 1:
            p += 1

    # build chains
    su = 0
    ch = [1] * n
    ch[1] = 1
    for i in range(2, n):
        ch[i] = 1 + ch[phi[i]]
        if ch[i] == 25 and phi[i] == i - 1:
            su += i

    return print (su)

# animus()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5,  2.2 min  --------------------------')
t1  = time.time()

# === Thu, 19 Apr 2012, 20:13, ving, USA
# Calculating phi, lengths of chains, and the required sum all in one short sieve:

def problem214(n, chainlength):
    nums = n*[1]
    s = 0
    for p in range(2, n):
        c = nums[p]
        if c == 1:  # p is a prime
            c = nums[p-1] + 1
            if c == chainlength:
                s += p
            nums[p] = c
            for i in range(2*p, n, p):  # update phi
                nums[i] *= p-1
                ii = i // p
                while ii % p == 0:
                    nums[i] *= p
                    ii //= p
        else:
            nums[p] = nums[c] + 1
    return s

# problem214(4*10**7, 25 )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6,   --------------------------')
t1  = time.time()



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

