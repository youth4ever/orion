#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Sat, 28 Jan 2017, 11:41
#The  Euler Project  https://projecteuler.net
'''
Maximum product of parts        -       Problem 183

Let N be a positive integer and let N be split into k equal parts, r = N/k, so that N = r + r + ... + r.
Let P be the product of these parts, P = r × r × ... × r = rk.

For example, if 11 is split into five equal parts, 11 = 2.2 + 2.2 + 2.2 + 2.2 + 2.2, then P = 2.25 = 51.53632.

Let M(N) = Pmax for a given value of N.

It turns out that the maximum for N = 11 is found by splitting eleven into four equal parts
which leads to Pmax = (11/4)4; that is, M(11) = 14641/256 = 57.19140625, which is a terminating decimal.

However, for N = 8 the maximum is achieved by splitting it into three equal parts,
so M(8) = 512/27, which is a non-terminating decimal.

Let D(N) = N if M(N) is a non-terminating decimal and D(N) = -N if M(N) is a terminating decimal.

For example, ΣD(N) for 5 ≤ N ≤ 100 is 2438.

Find ΣD(N) for 5 ≤ N ≤ 10000.


'''
import time
from math import gcd, e, log
import gmpy2
from decimal import *
getcontext().prec = 100
from fractions import Fraction
from pyprimes import factorise
print(Decimal(2/5))


print(Fraction (2,7) )

def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''

    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]

def M(n):
    k = round(n/e)
    A = [int(i) for i in str(gmpy2.mpq(n, k)).split('/') ]
    # print(A)
    K = set(get_factors(A[-1]))
    if (n/k) % 1  == 0 : return -n
    if len(K) == 1:
        if 2 in K or 5 in K :
            return -n
    if len(K) ==2 :
        # print(K)
        if 2 in K and 5 in K :
            return -n
        else : return n
    else  :
        return n











print('\n---------------------     My First SOLUTION,  0.5 sec     -----------------------')
t1  = time.time()


def Product_of_parts_sum( limit ) :
    S=0
    for n in range(5, limit + 1) :
        k = round(n/e)
        m = M(n)
        # if m  < 0 :
        #     print(str(n)+'.       '  ,n/e,'    ', k ,'     ',  n/k ,'      ' , m , '               ', Decimal(n/k) ,'         ' )

        S+=m

    return print('\n\nAnswer :', S)

Product_of_parts_sum(10**4)                          #          Answer : 48861552

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()


# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')




print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,  FAST, 80 ms --------------------------')
t1  = time.time()

# ==== Tue, 21 Jul 2015, 09:36, arnet95, Norway
# I had some issues with this one. I found the N/e solution quite quickly,
# and checked the floor and the ceiling of N/e.
# Then I checked whether k had any prime factors other than 2 or 5.
# What I forgot was that N/k need not be in the lowest possible form,
# so I divided k by the gcd of k and N.
# This then gave the right result. Runs in about 40 ms.


#Project Euler 183: Maximum product of parts
from math import e, ceil, log, gcd

def reduced(n):
    while (n % 2) == 0:
        n = n // 2
    while (n % 5) == 0:
        n = n // 5
    return -1 if n == 1 else 1

def d(N):
    low = int(N/e)
    high = low + 1
    k = high if (low * (log(N) - log(low))) < (high * (log(N) - log(high))) else low
    k = k/(gcd(k, N))
    return reduced(k)*N

def main(n):
    return sum(d(i) for i in range(5, n+1))

print (main(10000))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,  VERY SIMPLE --------------------------')
t1  = time.time()

# ====Mon, 26 Aug 2013, 02:27, BoltonBailey, USA


import math

def d(n):
    d = int((float(n)/math.e))
    if n>(1+1./d)**d*(1+d):
        d+=1
    while d%2==0: d/=2
    while d%5==0: d/=5
    if n%d == 0:
        return -n
    else:
        return n

print (sum([d(n) for n in range(5,10001)]))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3, SLOW  --------------------------')
t1  = time.time()

# ==== Thu, 3 Oct 2013, 02:27, Josay, France
# Computing the maximum value, check finiteness by going through the divisors and return the sum.

def ptilde(n,k): # does not overflow but keeps ordering
    return k*math.log(n/k)

def get_max_k(n):
    m = n/math.e # P(x) = (N/x)^x has a maximum in x = N/e
    mf, mc = math.floor(m), math.ceil(m)
    pf, pc = ptilde(n,mf), ptilde(n,mc)
    return mf if pf > pc else mc

def fraction_is_finite(a, b, base): # computing powers does not change "finiteness"
    d = 2
    while b > 1:
        while b%d == 0:
            if a%d == 0:
                a/=d
            elif base%d:
                return False
            b/=d
        d+=1
    return True

print (sum(n * (-1 if fraction_is_finite(n,get_max_k(n),10) else 1) for n in range(5,10001)))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,   --------------------------')
t1  = time.time()


# ==== Fri, 22 Feb 2008, 19:19, zeycus, Spain
# Second! I was never so close!
# What I did was almost brute-force. For each n, I found M(n) using dichotomic search.
# I computed k * ln(n / k) instead of (n/k)^k.


import math

## ************************ SUBROUTINES ************************

def funct(n, k):
    return k * math.log(n/k)

def fun(n):
    i1 = 1
    i2 = n
    while i2 - i1 > 1:
        i3 = (i1 + i2) // 2
        if funct(n, i3) < funct(n, i3 + 1):
            i1 = i3
        else:
            i2 = i3
    return i2

def gcd2(a, b):
      if a < b: a, b = b, a
      while b:  a, b = b, a % b
      return a


def isPositive(n):
    denom = fun(n)
    gcd = gcd2(n, denom)
    denom = denom / gcd
    while denom % 2 == 0: denom = denom // 2
    while denom % 5 == 0: denom = denom // 5
    return denom != 1

## ************************ MAIN ************************

sol = 0
for n in range(5, 10001):
    if isPositive(n): sol += n
    else: sol -= n
print (sol)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5, VERY NICE  --------------------------')
t1  = time.time()

from math import e, log as ln
f=lambda N, x :  x*ln(N/x)

def gcd(a,b):
    while b: a, b = b, a%b
    return(a)

def decimal(N):
    while N%2==0:N//=2
    while N%5==0:N//=5
    return(N==1)

def D(N):
    r=int(N/e);r+=(f(N,r+1)>f(N,r))
    return(N*(1-2*decimal(r/gcd(r,N))))

sumD=lambda N:sum([D(n) for n in range(5,N+1)])

sumD(10**4)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6,   --------------------------')
t1  = time.time()

# ==== Thu, 15 Jan 2009, 01:48, tolstopuz, Russia

import math, fractions

s = 0

for n in range(5, 10001):
    k = int(n / math.exp(1))
    if k * math.log(n / k) < (k + 1) * math.log(n / (k + 1)):
        k += 1
    f = k // math.gcd(n, k)
    while f % 2 == 0:
        f //= 2
    while f % 5 == 0:
        f //= 5
    s += n if f > 1 else -n

print(s)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

