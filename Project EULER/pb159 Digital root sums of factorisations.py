#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
                    Digital root sums of factorisations     -       Problem 159

A composite number can be factored many different ways.
For instance, not including multiplication by one, 24 can be factored in 7 distinct ways:

                                                    24 = 2x2x2x3
                                                    24 = 2x3x4
                                                    24 = 2x2x6
                                                    24 = 4x6
                                                    24 = 3x8
                                                    24 = 2x12
                                                    24 = 24

Recall that the digital root of a number, in base 10, is found by adding together the digits of that number,
and repeating that process until a number is arrived at that is less than 10.
Thus the digital root of 467 is 8.

We shall call a Digital Root Sum (DRS) the sum of the digital roots of the individual factors of our number.
The chart below demonstrates all of the DRS values for 24.

                                Factorisation	Digital             Root Sum
                                            2x2x2x3                        9
                                            2x3x4                           9
                                            2x2x6                          10
                                            4x6                              10
                                            3x8                              11
                                            2x12                             5
                                            24                                6

The maximum Digital Root Sum of 24 is 11.

The function mdrs(n) gives the maximum Digital Root Sum of n. So mdrs(24)=11.

Find ∑mdrs(n) for 1 < n < 1,000,000.  (10**6)


'''
import time, gmpy2
from math import sqrt

def get_divisors(n):      ### ( ͡° ͜ʖ ͡°)  FASTEST  ( ͡° ͜ʖ ͡°)  ### !! FIRST FASTEST
    factors = set()
    for x in range(1, int(sqrt(n)) + 1):
        if n % x == 0:
            factors.add(x)
            factors.add(n//x)
    return sorted(factors)

def pair_Factors(n):
    m=n
    todo, combis = [(n, 2, [])], []
    while todo:
        n, i, combi = todo.pop()
        while i * i <= n:
            if n % i == 0:
                combis += combi + [i, n//i],
                todo += (n//i, i, combi+[i]),
            i += 1
    return combis+[[m]]

def ds(n):              # Digital Sum
    ds = sum(map(int,str(n)))
    if ds < 10 : return ds
    else: return sum(map(int,str(ds)))

# For sum(mdrs(n)) for 1< n < 1000, I get 10901


def dr(n) :   # Digital Root of a number
    '''':Description: Returns the Digital Root of a number
    https://en.wikipedia.org/wiki/Digital_root#Congruence_formula    '''

    if n == 0 : return 0
    elif n%9 == 0 : return 9
    else : return n%9



print('\n--------------------------My Brute Force Solution, SLOW, 21 min------------------------------')
t1  = time.time()

def brute_force(up_lim) :
    SUM = 0
    for n in range(2, up_lim ):
        if gmpy2.is_prime(n) :
            mdrs = dr(n)
            # pF = [n]

        else :
            pF = pair_Factors(n)
            mdrs = 0                # Max digital root sum
            for J in pF :
                s = sum([ dr(j) for j in J ])
                if s > mdrs : mdrs = s

        SUM += mdrs
        # if mxx != mdrs :
        # print(str(n)+'.       mdrs = ', mdrs,   '               ', pF)

        if n%10**5 == 0 : print(n)

    return print('\nSolution :\t', SUM)            #   Solution :	 14489159

# brute_force(10**6)

t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')                #   Completed in : 1301.078417 s


print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()







# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


########## GENERAL IDEAS #############

# === Wed, 8 Jul 2015, 14:49, Arancaytar, Germany
# It's not hard to see that the DR (thinly disguised modulo 9) is compatible with multiplication and addition, ' \
#   'so that all prime factors of a number are only distinguished by their modulo 9* for this problem.
#
# (*Technically DR(9x) = 9 instead of 0, but this is irrelevant for prime numbers.)
#
# So we go from having to combine arbitrary factors of a number to combining a list of numbers between 1-8 to get the maximum sum.
#
# Next, it's apparent that nothing is ever gained by multiplying factors to a product greater than 9.
# (This can easily be checked by looking at the pairs with a sum less than 9 and
# a product greater than 9 - (2,5),(2,6),(3,4),(3,5),(4,4)(2,5),(2,6),(3,4),(3,5),(4,4) -
# to see that their product modulo nine is never greater than their sum.
#
# Therefore, all factors >4 can be added to the RDS as-is, since they will contribute most on their own.
#
# The ones that are left over are 2,3 and 4, which are a bit more complicated.
#
# 1. Pairs of 3 make 9, which is optimal. This leaves 2, 4 and at most a single 3.
#
# 2. Doubling a 4 is better than doubling a 3, and at least as good as 2∗2∗2=82∗2∗2=8,
# because 2∗2+2∗4=2∗2∗2+42∗2+2∗4=2∗2∗2+4.
#
# 3. Making an 8 from 2*2*2 is better than doubling a 3. 2∗2∗2+3>2∗2+2∗32∗2∗2+3>2∗2+2∗3
#
# 4. Doubling a 3 is better than nothing. 2∗3>2+32∗3>2+3.
#
# 5. Any remaining digits can simply be added up.
#
#
# The one pitfall here (which I only found by bruteforcing for 1...1000) is that (2) must be prioritized over (3),
# even though they look equivalent in isolation.
# The problem is that while 2∗2∗2+4=2∗2+2∗42∗2∗2+4=2∗2+2∗4 and 2∗2∗2+3>2∗2+2∗32∗2∗2+3>2∗2+2∗3,
# if there are both a 3 and a 4 we get 2+2∗3+2∗4>2∗2∗2+3+42+2∗3+2∗4>2∗2∗2+3+4.
# The first two examples for this case are 312 and 744,
# which have an mRDS of 16, but for which a flawed algorithm will get 15.


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,  23 sec --------------------------')
t1  = time.time()

# ==== Thu, 24 Nov 2016, 22:56, squidaction, USA
# First I generated the mdrs of all the powers of numbers up to sqrt(N), then iterated multiplication:

from math import *

def mdrs(N):
    def drs(n):
        return (n-1)%9+1

    m = [drs(i) for i in range(0,1+N)]

    for x in range(2,floor(sqrt(N)+1)):
        Q = m.copy()
        s = x*x
        v = 2*m[x]
        while s <= N:
            if v > m[s]: Q[s] = v
            s,v = s*x,v+m[x]
        m=Q

    R = m.copy()
    for x in range(2,floor(sqrt(N)+1)):
        Q = R.copy()
        for y in range(x+1, N//x+1):
           s,v = x*y, m[x]+R[y]
           if v > R[s] : Q[s] = v
        R = Q

    return R


# print(sum(mdrs(999999)[2:]))

t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')

print('\n--------------------------SOLUTION 2,  FAST , 12 sec  --------------------------')
t1  = time.time()

# ==== Tue, 26 Mar 2013, 14:16, tom.wheldon, England
# Similar to quite a few others - uses a sieve to store a list of divisors up to √n for each n,
# then steps through again to calculate the mdrs for each n using the divisor list
# and the values already calculated.  Runs in under 7s in Python.

N = 1000000

D = {n: [] for n in range(2,N)}

for i in range(2, int((N-1)**0.5)+1):
    for j in range(i*i, N, i):
        D[j].append(i)
for n in range(2,N):
    a = n%9
    mdrs = a if a else 9
    if D[n]:
        for div in D[n]:
            mdrs = max(mdrs, D[div] + D[n//div])
    D[n] = mdrs

print(sum(D.values()))

t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')

print('\n--------------------------SOLUTION 3, 23 sec  --------------------------')
t1  = time.time()

# =====  Sat, 17 Aug 2013, 22:41, Oren, USA
# Solution similar to GrameMcCrae's 's. I instead used dynamic programming that doesn't require primes.
#
# The digital root sum of positive integer n, drs(n), is given by
#    drs(n) = n - int((n-1)/9)*9 (except n=1, where we defined it to be 0)
#
# The maximum digital root sum of a factorization of n is given by
#    mdrs(n) = max(drs(a) + mdrs(b)) for all divisors 1 < a <= n of n) <-- note difference: not mdrs(a)
#
# I perform passes over all all a, each looping over multiples of a. If mdrs(k*a) is changed for some k,
#  then we also have to update all mdrs values of l*(k*a) for all l.
# The complexity is bounded by O(N log^2 N) where N=limit.


'''The digital root of n, except for n=1, where it is defined to be 0.'''
drs = lambda n: 0 if n == 1 else n - 9 * ((n - 1) / 9)

def mdrs(N):
    '''Return the Maximum Digital Root Sum (MDRS) of all n <= N.
    n=0,1 are defined to have MDRS=0.'''
    # 0th entry is not used. 1st entry is a boundary condition. Since it's 0, it does
    # Not affect the required MDRS sum.
    m = [0] * (N + 1)
    for d in range(2, N + 1):  # Loop over divisors of x
        drsd = drs(d)
        for k in range(1, N // d + 1):  # For all numbers n=k*d divisible by d ...
            n = k * d
            mn = drsd + m[k]
            if mn > m[n]:
                m[n] = mn
                for l in range(1, N // n + 1):
                    x = l * n
                    m[x] = max(m[x], drs(l) + mn)
    return m


# print (sum(mdrs(10 ** 6 - 1)))

t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')

print('\n--------------------------SOLUTION 4, 5 sec,  THE FASTEST  --------------------------')
t1  = time.time()

# ==== Thu, 29 Sep 2011, 11:55, learnmath, India
# At first, I was terrified at the prospect of enumerating all factors of all numbers till 1M.
# Some focused thinking led to a simple sieve approach.
#
# I have not yet seen the forum posts so if someone has made the same comments,
# apologies in advance for repeating the same stuff!
#
# The idea is that we do not need to look at ALL factor combinations. If we know,
# for instance, mdrs(12)=8, we can ignore all breakups of 12 for multiples of 12.
# So, to get mdrs(24), we need to look only at 24, 2x12, 3x8, 4x6 or the normal factors.
# This leads to a natural sieve solution that I build from 2 onwards.
# For each number, I go till square of the number as higher numbers have not yet been computed.
#
# Takes 5.3s in Python. In C, we can define the sieve as a char sieve (as max mdrs is 55).
# This leads to a very fast solution (170 ms).

def p159(lim1=100) :
	l1=[0]*(lim1+1)
	for n1 in range(2,lim1) :
		n2=n1%9
		if not n2 : n2=9
		if n2>l1[n1] : l1[n1]=n2
		k1=n1+n1
		for j1 in range(2,n1+1) :
			if k1>lim1-1 : break
			n2=l1[n1]+l1[j1]
			if l1[k1]<n2 : l1[k1]=n2
			k1+=n1
	return sum(l1)

lim1=1000000
sm1=p159(lim1)

print ('\nThe sum is ',sm1)



t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')

# print('\n--------------------------SOLUTION 5,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
print('\n--------------------------SOLUTION 6, List Comprehension  --------------------------')
t1  = time.time()

# === Fri, 13 Jun 2014, 03:47, muffoosta
# Short solution, takes a minute due to dumb factorizing.

s = [0, 0] + [i % 9 + 1 for i in range(1, 999999)]
for n in range(2, len(s)):
    s[n] = max([s[i] + s[n // i] for i in range(1, int(n ** .5) + 1) if n % i == 0])
print(sum(s))

t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')

