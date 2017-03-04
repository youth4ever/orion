#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Wed, 15 Feb 2017, 17:23
#The  Euler Project  https://projecteuler.net
'''
                        Repunit divisibility        -   Problem 129

A number consisting entirely of ones is called a repunit.
We shall define R(k) to be a repunit of length k;

for example, R(6) = 111111.

Given that n is a positive integer and GCD(n, 10) = 1, it can be shown that there always exists a value, k,
for which R(k) is divisible by n, and let A(n) be the least such value of k;   # R(A(n))

for example, A(7) = 6 and A(41) = 5.               #  n=7, 41,  --> n - is the prime

The least value of n for which A(n) first exceeds 10 is 17.                     #    A( n = 17 ) =  16 = A(n) = R(k)   ==> n=17

Find the least value of n for which A(n) first exceeds one-million (10**6) .   A(>10**6) = ?

Find the least n ( =17 prime) when A(n)=R(k) first exceeds 10**6

( Find a number of the repunit > 10**6 which has a factor which wasn't previously found
A(n) is the number of 1's in the repunit. You want to find the smallest n that divides a repunit with more than 1 million digits.

'''
 # 1 2          [11]                n - is a prime,   A(n) - numbers of 1's in the repunit
# 1 3          [3, 37]                      n = 7 , 41,  5363222357
# 1 4          [11, 101]
# 1 5          [41, 271]                --> A(n) = 5 ,   A(41) = 5                      A(257) = 256
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
# 1 16          [11, 17, 73, 101, 137, 5882353]             A(17) = 16
# 1 17          [2071723, 5363222357]
# 1 18          [3, 3, 7, 11, 13, 19, 37, 52579, 333667]

# 2137.     [1000117]        1000117 1000117
# 30306.     [1000099]        1000099 1000099
# 38463.     [1000039]        1000039 1000039
# 166667.     [1000003]        1000003 1000003

import time
from pyprimes import factorise
import numpy as np
from math import gcd
import gmpy2

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


def primesieve(n):          ### o(^_^)o  FASTEST  o(^_^)o  ###  Highly Efficient !!!

    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]

print('\n--------------------------TESTS------------------------------')
t1  = time.time()
#
#
# primes = primesieve( 10**6 )
# primes = set(prime_generator(6 , int(1.5*10**6) ))
# print(len(primes) )
#
# def test_lower_repunits( p , limit) :
#     for n in range(2, limit) :
#         if pow(10, n , 9*int(p) ) == 1:    # If R(k)=(10**k-1)/9  => R(k)=(10**k)%(9*prime_nr) == 1   IIF 10**k is divisible with prime_nr
#             # print('the repunit R( '+str(n)+' )  has ',p ,' as a prime   !!')
#             return n
#     return False
#
# print('\ntest_lower_repunits : \t ', test_lower_repunits(1000003, 10**6),'\n\n')
#
#




t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

# Tried :   1000003, 1000002, 1000170, 1000171
# 1002253, 1000117, 1000023

################        GENERAL IDEA      ####################
# GOOD INFO : http://stdkmd.com/nrr/repunit/tm.cgi?p=100
# GENERAL IDEA :
# Since R(k)=(10**k−1) / 9, to show that p is a factor of R(k), it suffices to show that
# (10**k−1)/9 ≡ 0 (mod p), or  10**k ≡ 1 (mod 9p)
# Example: If 11111 has factor 41 => pow(10, 5, 9*41) = 1   !!!!!!!!!!!!!!!!!!!!!!!!!!!!
print('\nTherefore we can test this idea with 11111 which has 41 as a factor : ', pow(10,5 ,41* 9)  )   # with 3 args pow makes modulo


print('\n================  My FIRST SOLUTION, 20 sec  ===============\n')
t1  = time.time()

def A(n):
    if gcd(n,10) != 1 : return 0
    x, k = 1, 1
    while k < n :
        if pow(10, k, 9*n) == 1:
            return k
        k+=1
    return 0


def solution_pb_129(lim = 10**2) :

    n = lim +1
    while True :
        # print(n , '    ',A(n))
        n+= 2
        if A(n) > lim :
            return print('\nAnswer : ',  n, '    corresponding to the Repunit ',  A(n) )

# solution_pb_129(10**6)          #       Answer :  1000023


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 's\n\n')

print('\n================  My SECOND SOLUTION, Copied  ===============\n')
t1  = time.time()



def A(n):       # Smart Function
    if gcd(n,10) != 1 : return 0
    x, k = 1, 1
    while x != 0  :
        x = (x*10+1) % n
        # print(x)
        k+=1

    return k

print('A(n) :\t', A(41) )


def solution_pb_129(lim = 10**2) :
    n = lim +1
    while True :
        # print(n , '    ',A(n))
        n+= 2
        if A(n) > lim :
            return print('\nAnswer : ',  n, '    corresponding to the Repunit ',  A(n) )

# solution_pb_129(10**6)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')          #       Answer :  1000023


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,   --------------------------')
t1  = time.time()

# ==== Fri, 2 Dec 2016, 12:30, mbh038, England
# About 410 ms in Python. I explored a bit and found that A(n)<n always,
# and that for lower limits, the value of n for which A(n) first exceeds that limit is itself only just larger than the limit.
# Hence I dispensed with sieving to generate loads of valid values of nn for which gcd(n,10)=1 and
# just started with n=999999, incremented it by two each time and ignored those n which were multiples of 5,
# in the full expectation that I would soon find the answer.
# To avoid calculating enormous R(k),
# I just worked with R(k) (mod n), and noted that R(k+1) (mod n) = 10*R(k)+1 (mod n)


def p129(limit):
    n=limit-1
    k=0
    while k<=limit:
        n+=2
        if not n%5:
            continue
        k=1
        R=1
        while R%n:
            k+=1
            R=(10*R+1)%n
    print(n,k)

p129(10**6)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()

# ==== Wed, 26 Oct 2016, 19:02, aolea, Spain
# Euler Theorem : a**phi(n)=1(mod n) with a and n coprimes.
# so:
# k = phi(9*n) --> 10**k = 1 (mod9*n) --> n | R(k) --> n | R(some_divisor_of(k))

def aolea():
    import sympy

    A = 0
    n = 10**6-1

    while True:
        if n % 2 != 0 and n % 5 != 0:
            aux1 = sympy.ntheory.totient(9*n)
            for i1 in sympy.divisors(aux1):
                if 10**i1 % (9*n) == 1:
                    A = i1
                    break
            if A != 0:
                if A > 10**6:
                    return print(n,A)
                    break
        n = n + 1

# aolea()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,   --------------------------')
t1  = time.time()

# === Mon, 20 Apr 2015, 13:27, Haroun, Algeria
# We check number in the form 10k+1,10k+3,10k+7,10k+910k+1,10k+3,10k+7,10k+9 only, this speeds up the calculations.

def f(n):
	r=1;c=1;
	while r%n:
		c+=1;
		r=(10*r+1)%n;
	return c;
limit=10**6;k=limit+1;
while True:
	if f(k)>limit :
		sol=k;
		break;
	k+=2;
	if f(k)>limit :
		sol=k;
		break;
	k+=4;
	if f(k)>limit :
		sol=k;
		break;
	k+=2;
	if f(k)>limit :
		sol=k;
		break;
	k+=2;

print ("the answser is : \t" , sol )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,  10 sec --------------------------')
t1  = time.time()

# ==== Sun, 5 Jul 2015, 03:49, hacatu, USA
# Thankful for Python's modular pow function:

def A(n):
	n *= 9
	k = 1
	while pow(10, k, n) != 1:
		k += 1
	return k

n = 999999
while True:
	n += 2
	if n%5 == 0:
		continue
	a = A(n)
	if a > 1000000:
		break
print(n)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

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
