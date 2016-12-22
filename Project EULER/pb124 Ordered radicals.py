#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Fri, 9 Dec 2016, 16:21
#The  Euler Project  https://projecteuler.net
'''
                Ordered radicals        -       Problem 124

The radical of n, rad(n), is the product of the distinct prime factors of n.

For example, 504 = 2**3 × 3**2 × 7, so rad(504) = 2 × 3 × 7 = 42.

If we calculate rad(n) for 1 ≤ n ≤ 10, then sort them on rad(n), and sorting on n if the radical values are equal, we get:

                                            Unsorted            Sorted
                                             n  rad(n)          n  rad(n) k
                                             1    1                 1    1    1
                                             2    2                 2    2    2
                                             3    3                 4    2    3
                                             4    2                 8    2    4
                                             5    5                 3    3    5
                                             6    6                 9    3    6
                                             7    7                 5    5    7
                                             8    2                 6    6    8
                                             9    3                 7    7    9
                                             10   10            10   10   10


Let E(k) be the k-th element in the sorted n column; for example, E(4) = 8 and E(6) = 9.

If rad(n) is sorted for 1 ≤ n ≤ 100000, find E(10000).

'''
import time, functools, operator, gmpy2



def factorise(n):
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    from pyprimes import factorise
    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]


print('\n--------------------------TESTS------------------------------')




print('\n=============  My FIRST SOLUTION,  OK, but just a little Slow ===============\n')
t1  = time.time()


up_range = 10**5
def solve_pb124(up_range, n_th_elem):
    RAD = {}
    for i in range(1, up_range+1 ) :
        if gmpy2.is_prime(i) :
            RAD[i] = i
        else :
            f = factorise(i)
            rad = functools.reduce(operator.mul, set(f))
            RAD[i] = rad
        # print(i, set(f), rad )
    R = sorted( RAD.items(), key=operator.itemgetter(1) )
    print(len(R),R[0:1000])
    return print( '\nAnswer E['+str(n_th_elem)+'] = ', R[n_th_elem-1][0] )

# print( '\nR [4] = ',R[4-1][0], 'R [6] = ',R[6-1][0] )

# solve_pb124(10**5, 10**4)             # Answer E [10000] =  21417





t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')






print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,  GOOD & Interesting --------------------------')
t1  = time.time()
# =======  Sat, 15 Oct 2016, 08:41, mbh038, England
# Richardw93's sieve solution from 29 March 2016 is really neat. Here is my numpy version of that, which takes about 140 ms on my MBP 2015:

import numpy as np

def p124(limit, target):

    rsieve = np.ones(limit+1, dtype=int)
    for i in range(2, limit+1):
        if rsieve[i] == 1:
            rsieve[ i::i ] *= i
            # print(rsieve[ i::i ])
    print (sorted([(rsieve[x],x) for x in range(limit+1)])[target][1])

p124(10**3, 10**2)

# rsieve = np.ones(100+1, dtype=int)
# print(rsieve[0:100])

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()
# ======== Sun, 25 Oct 2015, 01:40, hornemann55, Denmark
# Pretty easy. Runs in 0.5 sec.

import pyprimes

primes = pyprimes.nprimes(10**5)
def rad(n):
    return n[1]
radprod = [(1,1)]*100001
for i in primes:
    for j in range(1,100000//i+1):
        radprod[i*j] = (i*j,radprod[i*j][1] *i)


print(sorted(radprod, key=rad)[10000])

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,   --------------------------')
t1  = time.time()
# ========= Tue, 29 Mar 2016, 22:55,  Richardw93
# My python solution is quite simple and runs in about 200ms. I used python for its simplicity of sorting the tuples in the last step.
#
# The method is similar to a sieve of sieve of Eratosthenes, but instead of storing True or False for each number I store the radical.
# We know when we encounter a prime because its radical will be 1 at that point,
# we then multiply its radical and the radical of all its multiples by the value of that prime.
#
# By adding a tuple of the form (rad(n), n) for each number to a list we can easily sort them and find the solution.

max = 100000
index = 10000

radicals = [(1,1)]
sieve = [1] * (max+1)

for i in range(2, max+1):
    if sieve[i] == 1 :
        for j in range(i, max+1, i):
            sieve[j] *= i

    radicals.append((sieve[i], i))


print (sorted(radicals)[index-1][1])


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,  FASTEST SOLUTION --------------------------')
t1  = time.time()
# ======= Sun, 1 Apr 2012, 14:18, inamori, Japan
# Let us generate rads ascendingly.
#
# 2, 3, 5, 6, 7, 10, ...
#
# For each rad r, count the number of the numbers n such that rad(n) = r.
# For 2, the number is 16,
#
# 2, 4, 8, ... , 65536
#
# For 3, the number is 10, 5 -> 7, ...
#
# 16 + 10 + 7 + ...
#
# Count it until the sum >= 10000.
#
# The calculation of the radicals is like Eratosthenes' sieve, and take n such that rad(n) = n.
#
# It takes 9ms,
# for N = 107 and M = N / 10, It takes 1.1s.


from itertools import *
import time

def calc_rad(n):
    if n == 1:
        return ()
    else:
        p = f[n]
        m = n // p
        if m % p == 0:
            rads[n] = None
            return None
        else:
            ps1 = rads[m]
            if ps1 is None:
                rads[n] = None
                return None
            else:
                ps = (p,) + ps1
                rads[n] = ps
                return ps

def sieve(max_n):
    a = list( range(max_n + 1))
    primes = (n for n in count(2) if a[n] == n)
    for p in takewhile(lambda p: p * p <= max_n, primes):
        for n in range(p * 2, max_n + 1, p):
            if a[n] == n:
                a[n] = p
    return a

def gen_rads():
    for n in range(2, M + 1):
        ps = calc_rad(n)
        if ps is not None:
            yield ps

def count_same_rad(ps, n):
    p = ps[-1]
    if len(ps) == 1:
        s = 0
        while n >= p:
            n /= p
            s += 1
        return s
    else:
        s = 0
        ps1 = ps[:-1]
        while n >= p:
            n /= p
            s += count_same_rad(ps1, n)
        return s

def gen_same_rad(ps, n):
    p = ps[-1]
    q = p
    if len(ps) == 1:
        while n >= p:
            yield q
            n /= p
            q *= p
    else:
        s = 0
        ps1 = ps[:-1]
        q = p
        while n >= p:
            n /= p
            for r in gen_same_rad(ps1, n):
                yield q * r
            q *= p


N = 10 ** 5
M = N // 10
f = sieve(M)
rads = [ 0, () ] + [ 0 ] * (M - 1)
counter = 1
for ps in gen_rads():
    counter += count_same_rad(ps, N)
    if counter >= M:
        a = sorted(gen_same_rad(ps, N))
        print (a[M-counter-1])
        break


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5,   --------------------------')
t1  = time.time()
# ========= Thu, 13 Mar 2014, 18:33, Nicolas Patrois, France

from math import sqrt

nb=10**5

crible=[True]*nb
crible[0:2]=False,False
n=2

while n<=sqrt(nb): # Le crible
  for i in range(2*n,nb,n):
    crible[i]=False
  n+=1
  while not crible[n]:
    n+=1

premiers=[]

for i in range(2,nb):
  if crible[i]:
    premiers.append(i)

del crible
print("crible OK")

radicaux=[[0,0]]+[[1,i] for i in range(1,nb+1)]

for i in premiers:
  for j in range(i,nb+1,i):
    radicaux[j][0]*=i

print("radicaux ok")
radicaux.sort()

print(radicaux[10**4][1])

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6,   --------------------------')
t1  = time.time()

# ========= Sun, 17 Aug 2014, 23:06, Larry, USA
# Quick once I figured out a good algorithm.
# Use the Sieve of Eratosthenes of to get the primes and then use a modified sieve of Eratosthenes t calculate Rad(n).
# This time instead of using the integers I use the primes to iterate over. runs in 0.84 seconds on my eight year old PC.

import math

def sieve2(max_nr):
    lst = [True]*(max_nr+1)
    lst[0] = False
    lst[1] = False
    stop_at = int(math.sqrt(max_nr+1)) + 1
    current = 2
    while current < stop_at:
        total = current * 2
        while total < max_nr+1:
            lst[total] = False
            total += current
        current += 1
        while not lst[current]:
            current += 1
    return [i for i in range(max_nr+1) if lst[i]]

def rad(max_nr,primes):
    rad = [0] + [1] * max_nr
    current = 0
    while primes[current] < max_nr:
#        print ('xxxxxx',current, primes[current],max_nr, max_nr/2)
        i = 0
        while i * primes[current] < max_nr+1:
            rad[i * primes[current]] *= primes[current]
            i += 1
        current += 1
    return rad

max_nr = 100000
cutoff = 10000

primes = sieve2(max_nr+20)
rad = rad(max_nr,primes)

tu_rad = [tuple([rad[i],i]) for i in range(len(rad)-1)]

tu_rad.sort()
print ('answer is the second of the two numbers')
print (tu_rad[9999])


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n--------------------------SOLUTION 7,   --------------------------')
t1  = time.time()

import pyprimes, sys, functools

iprimes = pyprimes.nprimes(40000)
primes = set(iprimes)

def factor(n):

    if n in primes:
        return [n]
    if n & 1 == 0:
        return [2] + factor(n // 2)
    for i in iprimes:
        if n % i == 0:
            return [i] + factor(n // i)
    return [n]

def rad(n):
    return functools.reduce(lambda x, y: x * y, set(factor(n)), 1)

def euler(lim ,elm):
    rads = [(n, rad(n)) for n in range(1, lim)]
    rads.sort(cmp=lambda x, y: cmp(x[1], y[1]))
    print (rads[elm])

if __name__ == "__main__":

    euler(int(10**5), int(10**4))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

