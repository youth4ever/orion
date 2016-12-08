#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Sun, 4 Dec 2016, 01:14
#The  Euler Project  https://projecteuler.net
'''
            Investigating a Prime Pattern       -       Problem 146

The smallest positive integer n for which the numbers n**2+1, n**2+3, n**2+7, n**2+9, n**2+13, and n**2+27
are consecutive primes is 10.
The sum of all such integers n below one-million is 1242490.

What is the sum of all such integers n below 150 million ( 1.5e8 )  ?

'''
import time
import gmpy2
from gmpy2 import mpz

def prime_generator(n):         # HIghly Efficient !!!!         THE FASTEST, The BEST , The ONE
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

primes = prime_generator(10**5)

def get_prime_pattern(n):
    m = n**2
    P = [m+1, m+3, m+7, m+9, m+13, m+27]
    cnt=0
    for i in P:
        if gmpy2.is_prime(i) :   cnt += 1
        else : break
    if cnt == 6 :
        itr = 0
        for j in range(P[0], P[0]+27) :      # Here we want to make sure that there are no other primes in between range (n+1, n+27)
            if gmpy2.is_prime(j) : itr += 1
        if itr == 6 :
            return P
    return 0

print('\n--------------------------TESTS------------------------------')

print('Test for the function get_prime_pattern :  ', get_prime_pattern(11),'\n\n')


print('\n================  My FIRST SOLUTION, SLOW  ===============\n')
t1  = time.time()

def solve_pb146():
    S=0
    for i in range(10, int(1.5e8), 10):
        n = get_prime_pattern(i)
        if n != 0 :
            S += i
            print(i, n)
        if i % 1e7 == 0: print(i)
    return  print("\nThe Sum of n's is : ", S)

# solve_pb146()               # The Sum of n's is:  676333270




t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')      # Completed in : 96838.538647 ms


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
#               !!!!!!!!!        IMPORTANT REMARKS          !!!!!!!!!!!!!!!!!!
# ===========  Fri, 7 Jun 2013, 13:26 , Sika, Croatia
# This can be solved with simple code, you don't need to use probabalistic primality tests.
# Also, you don't need to realize that n % 30 = +/-10, or that only 1, 3, 7, 9 13, 19, 21 and 27 are interesting.
#
# The main idea is that it's much, much faster to check if :
#     (n^2 + 1) * (n^2 + 3) * (n^2 + 7) * (n^2 + 9) * (n^2 + 13) * (n^2 + 27) is divisible by an integer 2 <= k <= n,
# than to check for primality of every given sum (n^2 + k) individually.
# The first approach takes a long time only if every sum (n^2 + k) is prime, while the second approach takes a long time
# if first of the checked sums is prime.

# ============= Sun, 16 Jun 2013, 17:07, Oren, USA
# Incorporates all ideas already mentioned by others: Chinese remainder theorem to get n=210q+[10|80|130|200];
# tabulate permissible n (mod p) for small p; probable primality test for remaining candidates.

# ========= Fri, 30 Jan 2009, 15:23 , laune, Austria
# For n2+ d for d = 1, 3, 7, 9, 13, 27 to be prime, n2 must be congruent 1 mod 3, and congruent 2|3 mod 7,
# and congruent 1|3|4|7 mod 9, and congruent 1|2|3|5|7|8|9|11 mod 13, and congruent 1-13|15-17|19|21-23|25 mod 27.
#
# If n passes these tests, I used division by primes p, considering that (for p > 27) if r = n2 + 1) rem p, then r must not be zero,
# and r-p must not be -2|-6|-8|-12|-26.
# Analysis courtesy Lufthansa, due to a 90 minute delay in Munich ;-)

# ======= Tue, 14 Apr 2009, 01:12 , Konstantin Tenzin, Russia
# Nice task. 2 key ideas:
# 1. Reduce to (10,80,130,200) mod 210
# 2. Check prime numbers together

# =============Wed, 30 Sep 2009, 17:39, kevinsogo, Phillippines
# As many have noticed, n % 10 = 0. I experimented with different congruences and come up with these:
# n^2 = 1 mod 3
# n^2 = 2 mod 7
# n^2 = 1,3 or 9 mod 13
# n^2 = 0,1,3 or 5 mod 11
# That's my only filter. I checked the basics when n passed that test. Code runs in ~40s.
# I used Java's built-in primality test--one using both Miller-Rabin and Lucas-Lehmer tests.

# =========== Thu, 9 Sep 2010, 23:04 - zcxvbn, USA
# I first solved this a few days ago, using the same observation of many posters above that n mod 210=10, 80, 130, or 200.
# My original solution, using Miller-Rabin primality testing, ran in about 25 minutes, which was highly unsatisfying, so I tried to optimize it.
# Using some pencil-paper analysis I found that the only possible prime between n^2+1 and n^2+27 was n^2+21
# (assuming all the given numbers were prime);
# also I went so far as to determine all possible n modulo 2*3*5*7*11*13*17*19=223092870 (i.e. all possible n, since n<150000000).
# This cut down the running time to 6 minutes, still well above the limit.
#
# Upon reading some of the posts above, I was inspired to try testing for primality using a sieve,
# but that would require storing a list of ~8000000 primes, which my paltry RAM balked at.
# I finally hit upon the idea of combining both sieve and deterministic methods of prime checking -
# initially checking primality by dividing by primes up to sqrt(150000000),
# then verifying for the resulting n that n^2+a was indeed prime (for a=1,3,7,9,13,27) and n^2+21 was composite.
# The following code runs in just 9s on my machine:


print('\n--------------------------SOLUTION 0,   --------------------------')
t1  = time.time()







t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 1,  BEST & THE FASTEST  Sandamnit, USA --------------------------')
t1  = time.time()
# I used a makeshift Chinese Remainder Theorem to generate all possible residues modulo 2*3*5*7*11*13*17*19*23
# (the first product of first primes exceeding 150,000,000) which *could* satisfy the desired condition.
# Once I had this list, it sufficed to check the conditions of the problem.
# This yields a possible 315410 numbers n to check.
#
# I then pruned this list, ensuring that n**2+1 was not divisible by any primes p < 250.
# This narrowed the list of candidates down to 15159. The only issue is that 10**2+1 = 101,
# and so we need to be careful not to exclude 10 from our list of candidate residues.
#
# All said and done, this ran in about 3.713s on my machine.

def solution_Sandamnit():
    # Maximum value of n.
    N = 150000000

    # Current modulus
    modulus = 2

    # Current list of valid residues for the current modulus.
    residues = [0]

    # Values to add to n**2.
    adds = [ 1, 3, 7, 9, 13, 27 ]

    # The primes for which to apply Chinese Remainder Theorem.
    ps = [ n for n in range(250) if gmpy2.is_prime(n) and n > 2 ]

    for p in ps:
       # First, we loop over all square residues modulo p, eliminating those
       # which would make x**2+a (for a in adds) divisible by p.
       bad = set()
       for x in range(0, (p+1)//2):
          x2 = (x**2)%p
          for a in adds:
             if (a+x2)%p == 0: bad.add(x2)

       # Second, we identify the residues of x modulo p which DO NOT square to a
       # bad residue.
       good = []
       for x in range(0,p):
          if not (x**2)%p in bad:
             good += [x]

       # Third, we build a list of acceptable residues modulo the product of all
       # primes up to this point. This basically applies the Chinese Remainder
       # Theorem to the known list of good residues from the previous iteration
       # with the new list of residues modulo the current p.
       if p <= 23:
          temp = []
          for res in residues: temp += [ res+n*modulus for n in range(p) ]
          residues = [ res for res in temp if res < N ]
          modulus *= p
       residues = sorted([ x for x in residues if (x%p) in good or x == 10 ])

    def nextPrime(n):
        while gmpy2.is_prime(n+1)==False: n+=1
        return n+1

    # Lastly, the residues list now contains all possible values of n, so we
    # attempt to validate the required condition.
    total = 0
    for n in residues:
       p = n**2+1
       if gmpy2.is_prime(p) and gmpy2.is_prime(p+2) and gmpy2.is_prime(p+6) and \
          gmpy2.is_prime(p+8) and gmpy2.is_prime(p+12) and nextPrime(p+12) == p+26:
             print(n)
             total += n

    return print('\nAnswer:',total)

# solution_Sandamnit()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')      # Completed in : 5638.322353 ms

print('\n--------------------------SOLUTION 2,  nagihito, JAPAN , 32 sec--------------------------')
t1  = time.time()
# This is my solution. (Python)
# It takes about 30s on my laptop.
#
# It is obvious
# n ≡ 0 (mod 2)
# n ≡ 1,2 (mod 3)
# n ≡ 0 (mod 5)
#
# So, n is represented 10k. (10k ≡ 1,2 (mod 3))
#
# Then, I think of n modulo p (p > 5).
#
# n ≡ i (mod p) and if there is i^2 + r ≡ 0 (mod p) for r in [1, 3, 7, 9, 13, 27],
# all n^2 + r are multiple of p, and n ≡ ±i (mod p) can be omitted.
#
# If 10k ≡ i (mod p), minimum natural number k is k_min = (i * 10^(p - 2)) % p,
# because GCD(10, p) = 1 and 10^(p - 1) ≡ 1 (mod p) from Fermat's little theorem.
#
# So, omitted n are represented n ≡ 10k_min (mod 10p).
#
# I use Miller-Rabin primality test for fast primality test.
#
# Running time is the shortest when maximum of Sieve_Prime n is about lim^0.35

import random

rem = [1, 3, 7, 9, 13, 27]
other_rem = [n for n in range(1, 27, 2) if n not in rem and n % 5]

def Sieve_Prime(n):  # list of primes 7 or more but less than n
    index = [i for i in range(n)]
    for i in range(2, int(n ** 0.5) + 1):
        if index[i]:
            for m in range(i ** 2, n, i):
                index[m] = 0
    return [p for p in index if p][4:]

def Miller_Rabin(p, k = 50):  # Miller-Rabin primality test
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

def Check(n):  # check function
    if any(not Miller_Rabin(n**2 + r) for r in rem):
        return False
    if any(Miller_Rabin(n**2 + r) for r in other_rem):
        return False
    return True

lim = 150000000
s = set(n for n in range(10, lim, 10) if n % 3)
for p in Sieve_Prime(int(lim**0.35) + 1):
    for i in range(int(p/2) + 2):
        if any((i**2 + r) % p == 0 for r in rem):
            s -= set(range(10 * ((pow(10, p - 2, p) * i) % p), lim, p * 10))
            s -= set(range(10 * ((pow(10, p - 2, p) * -i) % p), lim, p * 10))

print (sum(n for n in s if Check(n)))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')      # Completed in : 32616.865635 ms

print('\n--------------------------SOLUTION 3, froycard, Venezuela  --------------------------')
t1  = time.time()

# I used Brute-Force approach to solving this problem, and using Python and this GMPY2 module,
# it computes the solution pretty fast (less than 1 min):
# froy@froy-VirtualBox:~/python > python3 testb.py

from gmpy2 import mpz
def solution_froycard():
    def nextPrime(n):
        while gmpy2.is_prime(n+1)==False: n+=1
        return n+1

    def solution():
        acc=0
        for n in range(10,150000000,10):
            tmp=mpz(n**2)
            if gmpy2.is_prime(tmp+1) == False: continue
            if gmpy2.is_prime(tmp+27) == False: continue
            if gmpy2.is_prime(tmp+13) == False: continue
            if gmpy2.is_prime(tmp+9) == False: continue
            if gmpy2.is_prime(tmp+7) == False: continue
            if gmpy2.is_prime(tmp+3) == False: continue

            prime=nextPrime(tmp)
            if tmp+1 != prime: continue
            prime=nextPrime(prime)
            if tmp+3 != prime: continue
            prime=nextPrime(prime)
            if tmp+7 != prime: continue
            prime=nextPrime(prime)
            if tmp+9 != prime: continue
            prime=nextPrime(prime)
            if tmp+13 != prime: continue
            prime=nextPrime(prime)
            if tmp+27 != prime: continue
            print(n)
            acc+=n

        return print("done:",acc)

# solution_froycard()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')      # Completed in : 165537.468195 ms

print('\n--------------------------SOLUTION 4,  tolstopuz, Russia --------------------------')
t1  = time.time()

# Miller-Rabin and autogenerated sieve for first 8 primes. 46 sec on E8400.

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

nmax = 150000000

x = [1,3,7,9,13,27]
nx = [i for i in range(1, 28, 2) if i not in x]

m = 2*3*5*7*11*13*17*19

t = m * [True]

for p in (2,3,5,7,11,13,17,19):
    for q in range(p):
        if any((q*q+xx) % p == 0 for xx in x):
            for k in range(m // p):
                t[k*p+q] = False

a = [q for q in range(m) if t[q]]

s = 0

for p in range(nmax // m + 1):
    for q in a:
        n = p * m + q
        if n > 2 and n < nmax:
            if all(isprime(n*n+xx) for xx in x) and not any(isprime(n*n+xx) for xx in nx):
                s += n

print(s)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')      # Completed in : 50658.8974 ms

print('\n--------------------------SOLUTION 5,  SLOW, Flibo, Finland  --------------------------')
t1  = time.time()

import gmpy2

# I didn't really get a solution I'd be happy with, but my code solved the problem in 378 seconds.
# It uses gmpy2 which I think utilizes the Miller-Rabin primality test.
# I quickly figured out the numbers had to be multiples of ten, but that's pretty much all the optimization I found.

def solution_Flibo() :
    total = 0
    for n in range(10, 10**8+5*10**7, 10):
        doomed = False
        doomed2 = False
        number = pow(n, 2) + 1
        if not gmpy2.is_prime(number):
            continue
        for add in [2, 4, 2, 4, 14]:
            number += add
            if not gmpy2.is_prime(number):
                doomed = True
                break

        if not doomed:
            check = pow(n, 2)
            for add in [5, 11, 15, 17, 19, 21, 23, 25]:
                if gmpy2.is_prime(check + add):
                    doomed2 = True
                    break
            if doomed2:
                continue
            else:
                print (n)
                total += n
    return print (total)

# solution_Flibo()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6,  Sika, Croatia --------------------------')
t1  = time.time()
# Fri, 7 Jun 2013, 13:26 , Sika, Croatia
# This can be solved with simple code, you don't need to use probabalistic primality tests.
# Also, you don't need to realize that n % 30 = +/-10, or that only 1, 3, 7, 9 13, 19, 21 and 27 are interesting.
#
# The main idea is that it's much, much faster to check if :
#     (n^2 + 1) * (n^2 + 3) * (n^2 + 7) * (n^2 + 9) * (n^2 + 13) * (n^2 + 27) is divisible by an integer 2 <= k <= n,
# than to check for primality of every given sum (n^2 + k) individually.
# The first approach takes a long time only if every sum (n^2 + k) is prime, while the second approach takes a long time
# if first of the checked sums is prime.

def has_divisor(n, limit):
    for p in range(2, limit + 1):
        if n % p == 0: return True
    return False

def not_prime(n):
    return has_divisor(n, int(n ** 0.5))

sm = 0
for n in range(10, 150000000, 10):
    n2 = n * n
    M = (n2 + 1) * (n2 + 3) * (n2 + 7) * (n2 + 9) * (n2 + 13) * (n2 + 27)
    if not has_divisor(M, n) and not_prime(n2 + 19) and not_prime(n2 + 21):
        print ("found: ", n)
        sm += n

print ("solution:", sm)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


