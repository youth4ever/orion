#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Thu, 15 Dec 2016, 21:35
#The  Euler Project  https://projecteuler.net
'''
Generalised Hamming Numbers     -       Problem 204

A Hamming number is a positive number which has no prime factor larger than 5.
So the first few Hamming numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15.
There are 1105 Hamming numbers not exceeding 10**8.

We will call a positive number a generalised Hamming number of type n, if it has no prime factor larger than n.
Hence the Hamming numbers are the generalised Hamming numbers of type 5.

How many generalised Hamming numbers of type 100 are there which don't exceed 10**9?


'''
import time

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


print('\n--------------------------INITIAL TESTS------------------------------')
t1  = time.time()

# Must take combinations of [2,3,5] up to 2**29
# There are 2: [0,6] --total 27,  2 powers up to 10**8
# There are 3: [1,16] --total 16,  3 powers up to 10**8
# There are 5: [1,11] --total 11,  5 powers up to 10**8
#  ...  and then take combinations of them  ...

def test_pb204(up_range) :
    primes = [ 2, 3 ,5 ]
    Nrs = [[1]]
    tmp=[1]
    while  up_range  : #while tmp[-1] < up_range  :
        wk=tmp[:]
        tmp=[]
        for i in range(len(primes)) :
            for j in range(len(wk)):
                o = wk[j]*primes[i]
                if o <= up_range :
                    tmp.append( o )
        print(tmp)
        tmp = list(set(tmp))
        if len(tmp) == 0 : break
        Nrs.append(tmp)

    Nrs = [val for sublist in Nrs for val in sublist]
    return print('\nFinal List of Numbers : \t',len(Nrs), '\n',Nrs )

test_pb204(10**8)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()


def generalised_Hamming_numbers_type_100(up_range) :
    primes = prime_generator(100)
    Nrs = [[1]]
    tmp=[1]
    while  up_range  : #while tmp[-1] < up_range  :
        wk=tmp[:]
        tmp=[]
        for i in range(len(primes)) :
            for j in range(len(wk)):
                o = wk[j]*primes[i]
                if o <= up_range :
                    tmp.append( o )
        # print(tmp)
        tmp = list(set(tmp))
        if len(tmp) == 0 : break
        Nrs.append(tmp)

    Nrs = [val for sublist in Nrs for val in sublist]
    return print('\nFinal List of Generalised Hamming Numbers of type 100 : \t',len(Nrs))#   , '\n', sorted(Nrs) )

# generalised_Hamming_numbers_type_100(10**9)         # Answer : 2944730



t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')          # Completed in : 31007.773638 ms



print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')

print('\n--------------------------SOLUTION 0, THE FASTEST, VERY CLEVER & INGENIOUS  --------------------------')
t1  = time.time()
# ====== Wed, 16 Oct 2013, 11:23, Zweedeend, Netherlands
# I decided to work with the logarithms of numbers. My code runs as follows:
# 1) start with the number 0 ( = log(1))
# 2) take a prime number (e.g. 97), and take it's logarithm: ~ 1.987
# 3) for each hamming number already found, add multiples of this logarithm until you hit the limit, 9.
#     e.g. after the first number I have a list: [0, 1.987, 3.974, 5.96, 7.947]
# 4) repeat for all prime numbers

# This code runs in about a second.

import pyprimes
from math import log

def solve(n, lim):
    primestack = list(log(prime) for prime in pyprimes.primes_below(n))
    hamming = [log(1)]
    loglim = log(lim)
    while primestack:
        prime = primestack.pop()
        for number in hamming[:]:
            number += prime
            while number < loglim:
               hamming.append(number)
               number += prime
    return len(hamming)

print(solve(100, 10**9))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 1,   --------------------------')
t1  = time.time()

# ===== Mon, 11 Jan 2016, 20:57, cwkoo, Singapore
# This simple backtracking solution runs in ~10 sec.


primes = prime_generator(100)

# Initialize at 1 since 1 should be counted
COUNT = 1

def backtrack(c, product, primes):
    global COUNT
    if len(c) == 0:
        for p in primes:
            backtrack([p], p, primes)
    else:
        COUNT += 1
        for p in primes:
            new_product = product * p
            if new_product > 10 ** 9:
                break
            if p >= c[-1]:
                backtrack(c + [p], new_product, primes)

def main():
    primes = prime_generator(100)
    backtrack([], 1, primes)
    print (COUNT)


# main()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2, BRUTE FORCE, 1 min,  --------------------------')
t1  = time.time()
# ==== Fri, 3 Oct 2014, 15:07, NeatMonster, France
# Bruteforcing in Python:

def NeatMonster():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    def rec(index=0, total=1):
        if (index >= len(primes)):
            return [total]
        i, ham = 0, []
        while total * primes[index] ** i <= 10 ** 9:
            ham.extend(rec(index + 1, total * primes[index] ** i))
            i += 1
        return ham
    return print (len(rec()))

# NeatMonster()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,   --------------------------')
t1  = time.time()
# ======== Mon, 20 Oct 2014, 13:06, fioi, France

U = 10 ** 9
N = 100

def genprimes():
	isprime = [True] * N
	primes = []
	for i in range(2, N):
		if isprime[i]:
			primes.append(i)
			for j in range(2 * i, N, i):
				isprime[j] = False
	return primes

primes = genprimes()
n = len(primes)

def genhamming(c = 1, i = 0):
	if i >= n:
		return 1
	else:
		ans = 0
		if c * primes[i] <= U:
			ans += genhamming(c * primes[i], i)
		return ans + genhamming(c, i + 1)

# print(genhamming())

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
