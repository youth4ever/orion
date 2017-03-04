#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @     Completed on Mon, 20 Feb 2017, 15:04
#The  Euler Project  https://projecteuler.net
'''
                        Pseudo-Fortunate Numbers        -       Problem 293

An even positive integer N will be called admissible,
if it is a power of 2 or its distinct prime factors are consecutive primes.
The first twelve admissible numbers are 2,4,6,8,12,16,18,24,30,32,36,48.

If N is admissible, the smallest integer M > 1 such that N+M is prime, will be called the pseudo-Fortunate number for N.

For example, N=630 is admissible since it is even and its distinct prime factors are the consecutive primes 2,3,5 and 7.
The next prime number after 631 is 641; hence, the pseudo-Fortunate number for 630 is M=11.
It can also be seen that the pseudo-Fortunate number for 16 is 3.

Find the sum of all distinct pseudo-Fortunate numbers for admissible numbers N less than 10**9.

'''
import time, gmpy2
from math import ceil, floor, sqrt, log
import functools, operator
from gmpy2 import mpz

def primesieve(n):          ### o(^_^)o  FASTEST  o(^_^)o  ###  Highly Efficient !!!
    import numpy as np
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]

#### Not very efficient yet, NOT OPTIMIZED !
def counter_generator( up_nr, elem_nr ):    # o(^_^)o   ©Bogdan Trif @ 2017 -02-20 14:00   ( ͡° ͜ʖ ͡°)
    ''':Generates a counter of a given elem_nr up to the up_nr
        Useful in finding common multiples of a list of primes numbers
    :param up_nr: int, up_power of the list
    :param elem_nr: int, nr of elements in the list
    :return: tuples, representing the   possible combinations                                             '''
    import itertools
    G=[]
    for k in itertools.product(*[range(1, up_nr+1)]*elem_nr):
        # print( k )
        G.append(k)
    return G



pseudoF = set()


print('\n--------------------------MY INITIAL SOLUTION, SLOW, 8 min------------------------------')
t1  = time.time()

def first_solution(lim = 10**9 ) :

    primes = primesieve(  100  )
    print(len(primes), '\n',primes[: 100], '\n\n')

    p=2
    print('------------',p,'-----------')
    p2 = int(p)
    N = [p2]
    n = int(p)
    while n*p2 < lim :
        p2 = int( gmpy2.next_prime(p2))
        N.append(p2)
        # print(N)
        n*=p2
        o = functools.reduce(operator.mul, N )
        np, psFn, = gmpy2.next_prime(o+1), gmpy2.next_prime(o+1) - o

        # Add first pair if it is even :
        if o < lim and o%2 == 0 :     # Admissible number
            pseudoF.add(int(psFn))
            print('\n--------first_pair : ', N, o, '   np=' ,np,  '    psFn=' , psFn ,'--------' )

        # Get MULTIPLES of the consecutive primes of N
            G = counter_generator( ceil(log( lim/o , 2)), len(N) )
            for i in G :
                aa = [ N**i for N, i in zip(N,i) ]
                a = functools.reduce(operator.mul, aa)
                if a < lim :
                    np, psFn, = gmpy2.next_prime(a+1), gmpy2.next_prime(a+1) - a
                    pseudoF.add(int(psFn))
                    print(N,'  pow=', i, ' = ',aa,'  = ', a , '        np=' ,np, '    psFn=' , psFn ,'          ',len(G))

    # Here we treat the powers of 2 :
    print('\n-----Powers of 2---------')
    a=1
    while a < lim//2 :
        a*=2
        np, psFn, = gmpy2.next_prime(a+1), gmpy2.next_prime(a+1) - a
        print(str(a)+'.     np=' , np , '     ', '    psFn=' , psFn )
        pseudoF.add(int(psFn))

    return print('\nAnswer : \t', sum(pseudoF), '\n\n',pseudoF )


# first_solution(10**9)       #   Answer : 	 2209



t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()







# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 0, VERY FAST  0.2 sec  --------------------------')
t1  = time.time()

# ==== Sat, 22 May 2010, 20:35, mastro. Italy
#
# An interesting bit of trivia about this problem: there are 6656 admissible numbers,
# but only 41 pseudo-Fortunate numbers.
#
# This means that the problem is very forgiving of bugs that miss some admissible numbers.
#
# E.g. the code below, which is a small variation of the one in my previous post,
# is buggy and finds only 5444 out of 6656 admissible numbers (it misses 6, 18, 30, 54, 90, etc.),
# but it still gets the correct answer in the end!

from gmpy2 import next_prime

def find_pseudo_fortunates(n, primes, i, target, pfs):
    pfs.add(next_prime(n + 2) - n)
    p = primes[i]
    i += 1
    n *= p
    while n < target:
        find_pseudo_fortunates(n, primes, i, target, pfs)
        n *= p

target = 10 ** 9
primes = 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
pfs = set()
find_pseudo_fortunates(2, primes, 0, target, pfs)
print(sum(pfs))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 1, VERY FAST  0.5 sec  --------------------------')
t1  = time.time()

import gmpy2, functools, operator


def pseudo_fortunate(n):
	return gmpy2.next_prime(n+1)-n


def admissible_numbers(n):
	next_prime = gmpy2.next_prime
	primes_to_use = []
	p = 2
	current_prod = 1
	current_times_next = 2
	while current_times_next < n:
		current_prod *= p
		primes_to_use.append(p)
		p = next_prime(p)
		current_times_next = current_prod*p
	number_of_primes = len(primes_to_use)
	exponents = [0]*number_of_primes
	while True:
		i = 0
		while True:
			exponents[i] += 1
			next_admissible_number = functools.reduce(lambda x,y:
                                                      x*y, [primes_to_use[x]**exponents[x] for x in range(number_of_primes)])
			if next_admissible_number < n:
				yield next_admissible_number
				break #exit innermost while-loop
			exponents[i] = 1 #reset current prime's exponent to 1, go to next prime
			i+=1
			if i >= number_of_primes:
				return


def euler_293(n):
	return print( int(sum(set([pseudo_fortunate(a) for a in admissible_numbers(n)]))) )

euler_293(10**9)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,  13 sec --------------------------')
t1  = time.time()

# ====Thu, 14 May 2015, 02:30, mmaximus, Portugal
# I generated the admissible numbers recursively, by feeding the pusher an ever-diminishing list
# of the basic primes truncated from the left, remembering how much we had 'spent' making admissible numbers so far.
#
# Then just brute-forced each one until a prime was found.
# At this order of magnitude primes are still pretty dense, to you won't have to try very hard to find one

from math import log10 as log

store_primes = [2,3,5,7,11,13,17,19,23]
L = 10**9+1
admissible = set()

def push(primes, carry_over=1):
    p = primes[0]
    max_power = int((log(L)-log(carry_over))/log(p))
    for k in range(1, max_power+1):
        admissible.add(p**k*carry_over)
        if len(primes) > 1:
            push(primes[1:], p**k*carry_over)

from math import sqrt
def is_prime(n):
    for i in range(3, int(sqrt(n))+1,2):
        if n % i == 0:
            return False
    return True

def next_prime_jump(n):
    m = 3
    while True:
        if is_prime(n+m):
            return m
        m += 2

pseudo_fortunate = set()
push(store_primes)

for n in admissible:
    pseudo_fortunate.add(next_prime_jump(n))

print(sum(pseudo_fortunate))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3, SUPER FAST  --------------------------')
t1  = time.time()

# ==== Sat, 23 Jun 2012, 03:30, ving, USA
# Same as Jon_McLean on Page 1: generate all admissible numbers (about 6500 of them),
# then use a trivial isPrime function to find m for each of them,
# throw all m's into a set, print its sum.  Another Python rendition:


from time import clock
time1 = clock()

from gmpy2 import is_prime as isPrime

def all_products(limit, primes, n):
    """ Generates all products of powers of the first n in primes
        that are divisible by primes[0] * ... * primes[n-1] """
    if n == 0:
        yield 1
    else:
        p = primes[n-1]
        for q in all_products(limit, primes, n-1):
            q *= p
            while q < limit:
                yield q
                q *= p

def all_admissible(limit, primes, n=None):
    if n is None:
        n = len(primes)
    for nn in range(1, n+1):
        for p in all_products(limit, primes, nn):
            yield p

N = 10**9
primes = [2, 3, 5, 7, 11, 13, 17]

pf = set()
for p in all_admissible(N, primes):
    m = 3
    while not isPrime(p+m):
        m += 2
    pf.add(m)

print(sum(pf))  # Answer: 2209

time2 = clock()
print("N = {0:d} Time = {1:.1f}".format(N, time2 - time1))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,   --------------------------')
t1  = time.time()

# ==== Thu, 25 Apr 2013, 15:34, mantonetti, Italy
# Hi to all!
#
# This time the solution is very simple and a brute force attack remains largely in the 1-minute rule.
# I build the list of admissible numbers then for each of them (not more than 6230 at all!)
# find the pseudo fortunate number, which I put in a set, thus ensuring no duplicates.

from itertools import count
from gmpy2 import is_prime


limit = 10 ** 9
adm = []

primes = [3, 5, 7, 11, 13, 17, 19, 23]

exp = 1
new = 2 ** exp
while new < limit:
    adm.append(new)
    exp += 1
    new = 2 ** exp

start = 0
stop = len(adm)
for p in primes:
    for n in range(start, stop):
        exp = 1
        new_p = p ** exp
        new = adm[n] * new_p
        while new < limit:
            adm.append(new)
            exp += 1
            new_p = p ** exp
            new = adm[n] * new_p
    start = stop + 1
    stop = len(adm)

pf = set()
for i in adm:
    for c in count(3, 2):
        if is_prime(i + c):
            pf.add(c)
            break

print(sum(i for i in pf))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5,   --------------------------')
t1  = time.time()

# ==== Fri, 9 Aug 2013, 20:38, bobrovsky.serj, Russia
# Easy.

from bisect import bisect

def primesieve(n):          ### o(^_^)o  FASTEST  o(^_^)o  ###  Highly Efficient !!!
    import numpy as np
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]


def euler293(limit):
    l = [2]
    for p in 3, 5, 7, 11, 13, 17, 19, 23:
        l.append(l[-1] * p)

    for p in 2, 3, 5, 7, 11, 13, 17, 19, 23 :
        for x in [x * p for x in l if x % p == 0]:
            while x < limit:
                l.append(x)
                x *= p

    primrs = primesieve(limit)
    return sum(set(primrs[bisect(primrs, x + 1)] - x for x in l))


print(euler293(10 ** 9))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6,   --------------------------')
t1  = time.time()


# ==== Wed, 12 Oct 2011, 01:37, tolstopuz, Russia

nmax = 10 ** 9
s = set()

p = [2, 3, 5, 7, 11, 13, 17, 19, 23]

def isprime(n):
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2,3,5,7,11,13,17,19,23,29):
        if a >= n:
            return True
        def t(x, n, s):
            if x == 1 or x == n - 1:
                return True
            for r in range(1, s):
                x = pow(x, 2, n)
                if x == 1:
                    return False
                if x == n - 1:
                    return True
            return False
        if not t(pow(a, d, n), n, s):
            return False
    return True

def adm(n):
    m = n + 3
    while not isprime(m):
        m += 2
    return m - n

def test(n, i):
    global s
    s.add(adm(n))
    if n * p[i] < nmax:
        test(n * p[i], i)
        if n * p[i+1] < nmax:
            test(n * p[i+1], i + 1)

test(2, 0)

print(sum(s))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 7,   --------------------------')
t1  = time.time()


# ====Sat, 22 May 2010, 07:21, Peter de Rivaz, England
# Similar in Python

import gmpy2
def pf2(x):
   n=x+2
   while not gmpy2.is_prime(n): n+=1
   return n-x

def euler293(x,N,ps,S):
   x*=ps[0]
   if x>N: return
   S.add(pf2(x))
   euler293(x,N,ps[1:],S)
   euler293(x,N,ps,S)

ps=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
S=set()
euler293(1,10**9,ps,S)
print (sum(S))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 8,   --------------------------')
t1  = time.time()


# ====Sat, 22 May 2010, 08:13, mastro
# Was this super-easy or what? I'm embarrassed I didn't solve it faster.
#
# I used a decently optimized algorithm for finding all the admissible numbers and,
# since there are only 6656 of them, I simply brute-forced the search for the pseudo-Fortunate numbers.
#
# Somewhat verbose but fast code, 0.13 seconds:

from gmpy2 import next_prime

def find_pseudo_fortunates(n, primes, i, target, pfs):
    p = primes[i]
    i += 1
    n *= p
    while n < target:
        # finds the next prime > n + 2
        pfs.add(next_prime(n + 2) - n)
        find_pseudo_fortunates(n, primes, i, target, pfs)
        n *= p

target = 10 ** 9
primes = 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
pfs = set()
find_pseudo_fortunates(1, primes, 0, target, pfs)
print(sum(pfs))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

