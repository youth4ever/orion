#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
                Prime generating integers       -       Problem 357

Consider the divisors of 30: 1, 2, 3, 5, 6, 10 ,15 ,30 .
It can be seen that for every divisor d of 30, d+30/d is prime.

Find the sum of all positive integers n not exceeding 100 000 000 ( 10**8 )
such that for every divisor d of n, d + n/d is prime.


'''
import time, sys
from math import sqrt
import gmpy2

def get_divisors(n):      ### o(^_^)o  FASTEST  o(^_^)o  ### !! FIRST FASTEST
    factors = set()
    for x in range(1, int(sqrt(n)) + 1):
        if n % x == 0:
            factors.add(x)
            factors.add(n//x)
    return sorted(factors)

def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    from pyprimes import factorise
    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]


def prime_generator(n):      ### o(^_^)o  FASTEST  o(^_^)o  ###  HIghly Efficient !!!
    """  Sieve of Eratosthenes              !!!!!!!!! THE FASTEST SIEVE. It won the battle with sieve
    Create a candidate list within which non-primes will be marked as None.
    """
    cand = [i for i in range(3, n + 1, 2)]
    end = int(n ** 0.5) // 2

    # Loop over candidates (cand), marking out each multiple.
    for i in range(end):
        if cand[i]:
            cand[cand[i] + i::cand[i]] = [None] * ( (n // cand[i]) - (n // (2 * cand[i])) - 1 )

    # Filter out non-primes and return the list.
    return [2] + [i for i in cand if i]


def is_357_integer(n):
    D = get_divisors(n)
    L = len(D)
    Icnt = 0
    for d in D :
        if gmpy2.is_prime( d+(n)//d )== False :
            return False
        else : Icnt+=1
    if L == Icnt :
        return True

print('\n--------------------------TESTS------------------------------')


print('Test for is_357_integer Function : ', is_357_integer(10**8))

print(get_divisors(30))
print('\n------------------------')


print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()



def solution_pb357(up_range) :
    cnt=1
    h  = 1
    S = 1
    # # METHOD 1 - VERY SLOW, CHECK ONLY
    # for n in range(2, up_range+1, 4) :
    #     D = get_divisors(n)
    #     L = len(D)
    #     Icnt = 0
    #     for d in D :
    #         if gmpy2.is_prime( d+n//d )== False :
    #             break
    #         else : Icnt+=1
    #     if L == Icnt :
    #         cnt+=1
    #         # print(n, '  ',n%2,'    ' ,get_factors(n) , '    ', get_divisors(n))

    ## METHOD 2 - Faster
    primes = prime_generator(up_range)
    # print(primes[0:300])
    for n in primes :
        if n% 4 == 3 :
            if is_357_integer(n-1) == True :
                    cnt+=1
                    S +=n-1
                    # F =  get_factors(n-1)
                    # print(n,'     ' ,n-1 ,'    ',  F, '    ', len(F) )

        if n*100 //up_range  > h-1 :        # Progress Bar #
            h += 1
            # sys.stdout.write("\r%d%%-" %h )
            sys.stdout.write('\r' + str(h)+' % ['+'#'*h+str(' ')*(220-22*h//10) +']' )   # Font Segoe UI Semibold
            # sys.stdout.write('\r' + str(h)+' % ['+'#'*h+str(' ')*(100-h) +']' )         #  Calibri, Adjust the numbers, for the font of your configuration
            # sys.stdout.flush()

    return print('\nAnswer :\t', S ,'           ' ,cnt )


# solution_pb357(10**8)



t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')          # Completed in : 4855960.745096 ms Completed in : 4935161.275148 ms


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,  1 min --------------------------')
t1  = time.time()
# ===== Sat, 5 Nov 2011, 23:36, Francky, France
#
# A Python3 solution in 27s (i5-2400 proc), I realized that my tab and the trick : (N in tab => N*k² not in tab) slow down the algo :-((
#
# So without it, I'm under the minute.
# Here we should try the simplest way first !
#
# I kept only one trick : N is 1 or 4*k+2.

def PE357(limit=10**8):
  lim = limit+2
  BA = bytearray
  prime = BA([True])*(lim+1)
  prime[:2] = BA(2)
  prime[4::2] = BA(limit >> 1)

  for i in range(3, int(lim**0.5)+1, 2):
    if prime[i]:  prime[i*i::i]=BA(lim//i-i+1)
  res = 0

  for n in range(2, limit+1, 4): # killer : step by 4
      if prime[n+1] and prime[n//2+2] and \
      all(prime[d+n//d] for d in range(3, int(n**0.5)+1) if not n%d):
        res+=n
  return 1+res

# PE357()

t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')

print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,   --------------------------')
t1  = time.time()

# =====  Mon, 22 Jun 2015, 04:17, Haroun, Algeria
# My solution took 66 secs on Python and 26 secs on Pypy (which may be considered as cheating LOL) on my old computer 1GHz *2.
# I used a fast prime sieve (it takes 10secs to sieve primes <10**8), and then checked number in the form p−1p−1 where pp is prime.


from math import sqrt;

def Haroun():
    def prime_sieve(n):

        sieve = [True] * (n//2)
        for i in range(3,int(n**0.5)+1,2):
            if sieve[i//2]:
                sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
        return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]

    def f(n):
        if n%4==0 : return 0;
        r=int(sqrt(n))+1;
        for i in range(1,r+1):
            if n%i==0:
                if i+n/i not in s:
                    return 0;
        return 1;
    L=10**8;
    l=prime_sieve(L);
    s=set(l)
    sol=sum(p-1 for p in l if f(p-1));

    return print ("the answer is " , sol)

# Haroun()

t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')        # Completed in : 100826.766968 ms

print('\n--------------------------SOLUTION 4,   --------------------------')
t1  = time.time()

# ====Sun, 6 Nov 2016, 13:28, mbh038, England
# About 31 s in Python. In the end, my solution is almost the same as Francky's


import numpy as np

def mbh038(limit):


    primes=np.ones(limit+1,dtype=bool)
    for i in range(2, int((limit+1)**0.5+1)):
        if primes[i]:
            primes[2*i::i]=False

    sf=np.ones(limit+1,dtype=bool)
    for i in range(2, int((limit+1)**0.5+1)):
        if sf[i]:
            sf[i**2::i**2]=False

    nsum=1
    for n in range(2,limit,4):
        if  primes[n+1] and primes[n//2+2] and sf[n] and all(primes[d+n//d] for d in range(3,int(n**.5)+1) if not n%d):
            nsum+=n
    print(nsum)

mbh038(10**8)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')      Completed in : 62139.554024 ms

print('\n--------------------------SOLUTION 5, SLOW  --------------------------')
t1  = time.time()

# ====== Sat, 12 Nov 2016, 00:24, aolea , Spain

import pyprimes
import sympy

def aolea () :
    sum = 0

    for i in pyprimes.primes_below(10**8):
        flag = True
        for j in sympy.divisors(i-1):
            if sympy.isprime(int(j+(i-1)/j)) == False:
                flag = False
                break
        if flag == True:
            sum = sum +i-1
    print(sum)

# aolea()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


# print('\n--------------------------SOLUTION 6,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
