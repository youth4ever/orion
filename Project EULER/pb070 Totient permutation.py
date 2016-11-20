#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Sat, 15 Oct 2016, 00:16
#The  Euler Project  https://projecteuler.net
'''
Totient permutation     -       Problem 70
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of
positive numbers less than or equal to n which are relatively prime to n.
For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 10**7, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.
'''
import time
from itertools import combinations
from numpy import prod

class Bogdan_Totient_algorithm :
    # def __init__(self, nr):
    #     self.nr = nr

    def is_prime(self, nr):
    # Function which checks if a number is prime
        for i in range(2, int(pow(nr,1.0/2))+1):
            if nr%i==0:
                return 0
        return 1

    def factor_split(self, nr): ##outputs a list of the unique prime factors of its input
        b = 2
        d = []
        f = nr
        while f > 1:
            while f % b != 0:
                b = b + 1
            d = d + [b]
            f = f / d[-1]
        if len(d) >1:
            return d
        #else: print(a,' is prime')

    def count_elements(self, nr):
            #my_method = self.factor_split(nr=4)

            if self.is_prime(nr) == True :
                return nr-1
            else:
                A = list(set(self.factor_split(nr)))
                cnt = 0
                for k in range(len(A)):
                    #print(A[k], A[0:k+1])
                    for q in  range(len(A)) :
                        Comb = list(combinations(A[0:k],q))
                        #print(Comb)
                        for l in range(len(Comb)):
                            if q % 2 == 1 :
                                cnt+= (nr-1) // (prod(Comb[l])*A[k])
                            else :              # q % 2 ==0 :
                                cnt -= (nr-1) // (prod(Comb[l])*A[k])
                return int(nr+cnt-1)          # print (nr+cnt-1)


def sieve(lower, upper_bound):         # THE FASTEST  SIEVE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # SIEVE OF ERATOSTHENES
    n = upper_bound + 1
    check = [True] * n
    check[0] = check[1] = False
    for i in range(2, int(upper_bound**0.5) + 1):
        if check[i]:
            for j in range(i**2, upper_bound + 1, i):
                check[j] = False
    primes = [i for i, flag in enumerate(check) if flag and i > lower ]
    return primes

primes = sieve(2000, 5000)

x = 9175463
y = int(''.join(sorted(list(str(x)))))
print(y)
z = int(y)
print(z)


algo = Bogdan_Totient_algorithm()

a = algo.count_elements(10)
print(a)

#
# minv = 10
# for i in primes :
#     for j in primes:
#             # P = primes[n] * primes[m]
#             n = i*j
#             if n < 10**7 :
#                 phi = algo.count_elements(n)
#                 #print(i, j,'  ;    n= ' ,n, '      phi(n)= ' ,phi , '       n/phi(n) =  ',n/phi )
#                 p = ''.join(sorted(str(phi)))
#                 q = ''.join(sorted(str(n)))
#                 if p == q and n/phi < minv:
#                     minv = n/phi
#                     print('YES ! A Permutation!  ------   >',  i, j, p , q ,'  ;    n= ' ,n, '      phi(n)= ' ,phi , '       n/phi(n) =  ',n/phi )

# Answer : 8319823

# Take 2 sieves of primes such that their product < 10**7 and make combinations between them
# sqrt of 10.000.000 = 3162.277
# the range must be something like [1000:5000] the two sieves

# 223*7919
# 1765937
# 1765937/1757796
# 1.0046313679175514


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1 ,  the KING, VERY FAST, mbh038 , England --------------------------')
# After first posting here my original solution which took 400s, here is an update that gets the answer in 0.75 s or so.
# It guesses that the minimal ratio of nϕ(n)nϕ(n), if nn cannot be prime (since then ϕ(n)ϕ(n) would be n−1n−1
# and it would not have the same digits as nn) occurs when nn has two distinct prime factors,
# these both being around n√n. I search for factors within a factor 3 of n√n and use the fact that,
# where a number nn has two distinct prime factors, p1p1 and p2p2, then ϕ(n)=(p1−1)(p2−1)ϕ(n)=(p1−1)(p2−1).

t1  = time.time()

import math
import numpy as np

def primesfrom2to(n):
    """ Input n>=6, Returns array of primes, 2 <= p < n """
    sieve = np.ones(n//3 + (n%6==2), dtype=np.bool)
    for i in range(1,int(n**0.5/3)+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3   ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0][1:]+1)|1)]

def p70(n):
    primes=set(primesfrom2to(int(math.sqrt(n)*2))).difference(set(primesfrom2to(int(math.sqrt(n)/2))))
    minratio=10
    for p1 in primes:
        for p2 in primes.difference([p1]):
            if p1*p2<n:
                pp=p1*p2
                phi=(p1-1)*(p2-1)
                if pp/phi < minratio:
                    if sorted(str(phi))==sorted(str(pp)):
                        minratio=pp/phi
                        print (pp,phi,pp/phi,p1,p2)

p70(10**7)
t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2 ,  FAST, nopria , Italy --------------------------')
## http://codegolf.stackexchange.com/a/26753/53996  modified as generator
# I found here a very interesting and fast algorithm to calculate totien(n) for all n under a certain limit,
# and then used it to find the lowest ratio required. It runs in less than 20 seconds with plain Python 3:

t1  = time.time()
#
# TOTIENT GENERATOR VERY FAST
# def totient_gen(limit):
#     phi = (limit+1)*[0]
#     phi[1] = 1
#     yield 1
#     for n in range(2,limit):
#         if phi[n] == 0:
#             phi[n] = n - 1
#             for j in range(2,int(limit/n)):
#                 if phi[j] != 0:
#                     q = j
#                     f = n - 1
#                     while q % n == 0:
#                         f *= n
#                         q //= n
#                     phi[n * j] = f * phi[q]
#         yield phi[n]
# # for i in totient_gen(100):     print(i, end=' ')
#
# min_ratio = 10 # big initial value
# n=0
# for phi in totient_gen(10000000):
#     n += 1
#     if n/phi < min_ratio:
#         if sorted(str(phi)) == sorted(str(n)):
#             if n > 1:
#                 min_ratio = n/phi
#                 print('{:9d}{:9d}{:12.8f}'.format(n,phi,min_ratio))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3 ,  INTERESTING but SLOWER, fioi , France --------------------------')
t1  = time.time()

UPPER_BOUND = 10 ** 7

def is_permutation(n, m):
    s1, s2 = list(str(n)), list(str(m))
    s1.sort()
    s2.sort()
    return s1 == s2

print("Generating primes...")
prime = [True] * UPPER_BOUND
prime_list = []

for i in range(2, UPPER_BOUND):
    if prime[i]:
        prime_list.append(i)
        for j in range(i + i, UPPER_BOUND, i):
            prime[j] = False

totient = [1] * UPPER_BOUND

print("Computing totient function...")
for p in prime_list:
    for i in range(1, (UPPER_BOUND - 1) // p + 1):
        q = p
        while i * q < UPPER_BOUND:
            totient[i * q] = totient[i] * (q - q // p)
            q *= p

print("Looking for permutations...")
min_i = -1
min_ratio = float('inf')
for i in range(2, UPPER_BOUND):
    if is_permutation(i, totient[i]):
        print(i, totient[i], "found")
        curr_ratio = i / totient[i]
        if curr_ratio < min_ratio:
            min_ratio = curr_ratio
            min_i = i
print(min_i, "with", min_ratio)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')