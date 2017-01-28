#!/usr/bin/python
# Solved by Bogdan Trif @       Completed on Tue, 10 Jan 2017, 10:06
#The  Euler Project  https://projecteuler.net
'''
                Composites with prime repunit property      -       Problem 130

A number consisting entirely of ones is called a repunit.
We shall define R(k) to be a repunit of length k; for example, R(6) = 111111.

Given that n is a positive integer and GCD(n, 10) = 1, it can be shown that there always exists a value, k,
for which R(k) is divisible by n, and let A(n) be the least such value of k;
for example, A(7) = 6 and A(41) = 5.

You are given that for all primes, p > 5, that p − 1 is divisible by A(p).
For example, when p = 41, A(41) = 5, and 40 is divisible by 5.

However, there are rare composite values for which this is also true;
the first five examples being 91, 259, 451, 481, and 703.

Find the sum of the first twenty-five composite values of n for which
GCD(n, 10) = 1 and n − 1 is divisible by A(n).

'''
# 1 2          [11]                n - is a prime,   A(n) - numbers of 1's in the repunit
# 1 3          [3, 37]                      n = 7 , 41,  5363222357
# 1 4          [11, 101]
# 1 5          [41, 271]                --> A(n) = 5 ,   A(41) = 5
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
# 1 16          [11, 17, 73, 101, 137, 5882353]         --> A(17) = 16,
# 1 17          [2071723, 5363222357]
# 1 18          [3, 3, 7, 11, 13, 19, 37, 52579, 333667]

# 2137.     [1000117]        1000117 1000117
# 30306.     [1000099]        1000099 1000099
# 38463.     [1000039]        1000039 1000039
# 166667.     [1000003]        1000003 1000003

import time
from pyprimes import factorise
from itertools import combinations
import functools, operator

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

print('\n--------------------------TESTS------------------------------')
t1  = time.time()




t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


################        GENERAL IDEA      ####################
# GOOD INFO : http://stdkmd.com/nrr/repunit/tm.cgi?p=100
# GENERAL IDEA :
# Since R(k)=(10**k−1) / 9, to show that p is a factor of R(k), it suffices to show that
# (10**k−1)/9 ≡ 0 (mod p), or  10**k ≡ 1 (mod 9p)
# Example: If 11111 has factor 41 => pow(10, 5, 9*41) = 1   !!!!!!!!!!!!!!!!!!!!!!!!!!!!
print('\nTherefore we can test this idea with 11111 which has 41 as a factor : ', pow(10,5 ,41* 9)  )   # with 3 args pow makes modulo


print('\n--------------------------TESTS------------------------------')



print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

def composite_primes_repunits( how_many ) :
    primes = prime_generator(2, 10**3)

    C = set()              # Composites List
    for n in range(2, 10**3) :
        # if gcd (n, 10 ) == 1 :
            P=[]
            for i in primes:
                if pow(10, n , 9*int(i) ) == 1:    # If R(k)=(10**k-1)/9  => R(k)=(10**k)%(9*prime_nr) == 1   IIF 10**k is divisible with prime_nr
                    P.append(i)
            if len(P) > 1 :
                # print(str(n)+'.    ' ,P)
                comb = set()
                for j in range(2, 4 ):
                    c = set(combinations( P , j) )
                    comb.update(c)
                comb_prod = list(functools.reduce(operator.mul, k) for k in comb)
                # print( comb, comb_prod )
                for p in comb_prod :
                    if (p-1) % n == 0:
                        C.add(p)
                        # print(str(n)+'.    ' ,P, '     p=',p)
    C = sorted(C)
    C = C[ 0: how_many]
    return print('\nAnswer : \t', sum(C), '\n' , len(C)   ,C)

composite_primes_repunits(25)

# Answer : 	 149253
# [91, 259, 451, 481, 703, 1729, 2821, 2981, 3367, 4141, 4187, 5461, 6533, 6541, 6601, 7471, 7777, 8149, 8401, 8911, 10001, 11111, 12403, 13981, 14701]


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')          #   Completed in : 759.043455 ms


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,   --------------------------')
t1  = time.time()

# ==== Fri, 2 Dec 2016, 15:31, mbh038, England
# About 1.4s in Python. As for problem 129, except that this time I did use a sieve to create an array of composite n values
# for which gcd(n,10)=1 and which were not multiples of 3.
# I thought that would be quicker than generating the nn values one by one and testing each nn for primality.

import numpy as np

def p130_mhb038(limit, nvals):
    ncs=ncsieve(limit)
    results=[]
    for n in ncs:
        k=1
        R=1
        while R%n:
            k+=1
            R=(10*R+1)%n
        if not (n-1)%k:
            print(n,k)
            results.append(n)
            if len(results)==nvals:
                break

    print(sum(results))

def ncsieve(n):
    """return array n: gcd(n,10)=1, n is not a multiple of 3 and n is not prime"""

    nsieve=np.ones(n+1,dtype=bool)
    nsieve[2::2]=False
    nsieve[3::3]=False
    nsieve[5::5]=False

    psieve=np.zeros(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if not psieve[i]:
            psieve[2*i::i]=True

    return np.nonzero(np.logical_and(nsieve, psieve))[0]

# p130_mhb038(10**5 , 25)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()

# ==== Fri, 2 Dec 2016, 15:31, mbh038, England
# ..but I was wrong. It was quicker to step up through odd n and check each to see
# if each is composite and not a multiple of 5 or of 3. This goes in 0.6 s.

def p130(nvals):
    t=time.clock()
    results=[]
    n=1
    while len(results)<nvals:
        n+=2
        if not n%3 or not n%5 or is_prime(n):
            continue
        k=1
        R=1
        while R%n:
            k+=1
            R=(10*R+1)%n
        if not (n-1)%k:
            print(n,k)
            results.append(n)

    print(sum(results),time.clock()-t)

def is_prime(n):
    """Returns True if n is prime."""
    if n==2 or n==3:
        return True
    if not n%2 or not n%3:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True

# p130(25)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,   --------------------------')
t1  = time.time()

# ===== Thu, 27 Oct 2016, 13:29, aolea, Spain
# Just a variation of the previous problem.

def aolea():
    import sympy

    A = 0
    n = 50
    count = 0
    sum = 0

    while True:
        if n % 2 != 0 and n % 5 != 0 and sympy.isprime(n) == False:
            aux1 = sympy.ntheory.totient(9*n)
            for i1 in sympy.divisors(aux1):
                if 10**i1 % (9*n) == 1:
                    A = i1
                    break
            if (n-1) % A == 0:
                count = count + 1
                sum = sum + n
                print(count,n,A)
                if count == 25:
                    break
        n = n + 1
    return print(sum)

# aolea()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,  SLOW --------------------------')
t1  = time.time()

# ==== Sun, 5 Jun 2016, 23:30, azax1, USA
# Much like the last one.

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

nums = list(range(10**5))
for i in range(2, len(nums)):
    if nums[i] != i:
        continue

    m = i**2
    while m < len(nums):
        nums[m] = i
        m += i

n = 1
count = 0
sum = 0
while count < 25:
    n += 1

    if nums[n] == n or gcd(n, 10) != 1:
        continue

    x = 1
    exp = 1
    while x % n != 0:
        x = (10 * x + 1) % n
        exp += 1

    if n % exp == 1:
        sum += n
        count += 1

print (sum)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5,   --------------------------')
t1  = time.time()

# ===== Mon, 11 Mar 2013, 22:08, mantonetti, Italy
# Having found a quick method for calculating A(n) in the previous problem, this one was TOO easy! ;)
# I use miller_rabin function to test for primeness because a priori I don't know where the composite number are located... ;)

from itertools import count

def Miller_Rabin(p, k = 50):  # Miller-Rabin primality test
    import random
    if p == 2: return True
    if p < 2 or p & 1 == 0: return False

    d = (p - 1) >> 1
    while d & 1 == 0:
        d >>= 1

    for i in range(k):
        a = random.randint(1, p - 1)
        t = d
        y = pow(a, t, p)
        while t != p - 1 and y != 1 and y != p - 1:
            y = pow(y, 2, p)
            t <<= 1
        if y != p - 1 and t & 1 == 0:
            return False
    return True

def A(n):
    x = 1
    for k in count (1):
        x *= 10
        x %= 9 * n
        if x == 1:
            return k

conta = 0
somma = 0
for n in count(3, 2):
    if n % 5 != 0:
        if not Miller_Rabin(n):
            if (n - 1) % A(n) == 0:
                print(n, A(n))
                conta += 1
                somma += n
            if conta == 25:
                break

print(somma)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6,  VERY SLOW --------------------------')
t1  = time.time()

primeset = set(prime_generator(2, 10**5))

def fnA(n):
  k = 1
  while pow(10,k,9*n) != 1:
    k += 1
  return k

cnt = 0
tot = 0
for n in range(2,10**6):
  if n % 2 != 0 and n % 5 != 0 and n not in primeset:
    a = fnA(n)
    if (n-1) % a == 0:
      print (n,fnA(n))
      cnt += 1
      tot += n
      if cnt == 25:
        break
print ("Found %d candidates with sum of %d" % (cnt, tot))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

