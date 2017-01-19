#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Tue, 10 Jan 2017, 07:31
#The  Euler Project  https://projecteuler.net
'''
                Repunit nonfactors      -       Problem 133

A number consisting entirely of ones is called a repunit.
We shall define R(k) to be a repunit of length k; for example, R(6) = 111111.

Let us consider repunits of the form R(10**n).

Although R(10), R(100), or R(1000) are not divisible by 17, R(10000) is divisible by 17.
Yet there is no value of n for which R(10**n) will divide by 19.
In fact, it is remarkable that 11, 17, 41, and 73 are the only four primes below one-hundred that can be a factor of R(10**n).

Find the sum of all the primes below one-hundred thousand (10**5) that will never be a factor of R(10**n).


'''
import time
from pyprimes import factorise
import gmpy2

def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''

    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]

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

print('\n--------------------------MY INITIAL SOLUTION, 1.5 sec------------------------------')
t1  = time.time()

def init_solution():
    primes = set(prime_generator( 10**5 ))

    for n in range(19, 20) :
        repunit_length = 10**n
        P  = []
        for i in primes:
            if pow(10, repunit_length, 9*i) == 1:    # If R(k)=(10**k-1)/9  => R(k)=(10**k)%(9*prime_nr) == 1   IIF 10**k is divisible with prime_nr
                P.append(i)
                # print(' 1*   10**',n ,'   ' ,i , '    ' )
        P = set(P)
        print(' 1*   10**',n ,'                      Length primes : ', len(primes))
        primes = primes - P

    print('Length primes : ', len(primes) )                #  Length primes :  9552
    print('\nAnswer, Sum : ', sum(primes) )              #      Answer, Sum :  453647705

# init_solution()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')          #   `Completed in : 1592.091084 ms

print('\n--------------------------TESTS------------------------------')

################        GENERAL IDEA      ####################
# GOOD INFO : http://stdkmd.com/nrr/repunit/tm.cgi?p=100
# GENERAL IDEA :
# Since R(k)=(10**k−1) / 9, to show that p is a factor of R(k), it suffices to show that
# (10**k−1)/9 ≡ 0 (mod p), or  10**k ≡ 1 (mod 9p)
# Example: If 11111 has factor 41 => pow(10, 5, 9*41) = 1   !!!!!!!!!!!!!!!!!!!!!!!!!!!!

# === Sun, 27 Nov 2016, 18:49, nonnaci, USA
# Extending problem 132,
# % large modulo-exponentiation. For prime p, if
# % p | R(10^k) =>
# % p | (10^(10^k) - 1)/9 =>
# % 10^(10^k) = 1 mod 9p
#
# To show that no k satisfies m=9p, we need only check k=0:m via the pigeon hole principle.
# A useful relation for the modulo exponentiation of this form follows
#
# 10^(10^(k+1)) = (10^(10^k))^10 mod m.
#
# Furthermore, we can shortcut the checks from k=0:m by checking if any cycles of equivalences form.
# If the cycle includes 1, then p divides R(10^n) for some n,
#     if cycle does not include 1, then p does not divide R(10^n).


print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()


primes = set(prime_generator( 10**5 ))

# F = primes = set(list( sympy.primerange(2,10**5) ))

# print( type(F), len(F)  )


repunit_length = 10**19
P  = []
for i in primes:
    if pow(10, repunit_length, 9*i) == 1:    # If R(k)=(10**k-1)/9  => R(k)=(10**k)%(9*prime_nr) == 1   IIF 10**k is divisible with prime_nr
        P.append(i)
        # print(' 1*   10**',n ,'   ' ,i , '    ' )
P = set(P)

primes = primes - P

print('\nAnswer, Sum : ', sum(primes) )              #      Answer, Sum :  453647705









t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,   --------------------------')
t1  = time.time()

# ==== Tue, 13 Dec 2016, 12:53, mbh038, England
# This cheeky code got me in here, in about 330ms, but I have not brought much real understanding to this problem.
# I have just used the handy pow() function within Python. I must now read the erudite contributions above this one...

import numpy as np
def p133(limit):
    ps = primesieve(limit)
    a = [x for x in ps if pow(10,10**100,int(x)) !=1]
    print (sum(a)+3 )

def primesieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]

p133(10**5)
############## METHOD 2 #####################

# Well that has been enlightening. Having read many of the posts here and in the forum for problem 132,
# and having mulled over Fermat's Little Theorem,
# I think I now understand what night.train is doing.
# Here's my code for doing that, which goes in 42 ms.

# import numpy as np
# def p133v2(limit):
#     ps=primesieve(limit)
#     psum=0
#     for p in ps:
#         m = pf25(p-1)
#         if pow( 10, m, int(p) ) != 1 :
#             psum+=p
#     print(psum+3)
#
# def pf25(n):
#     """returns 2**a x 5**b where a and b are the exponents of 2 and 5 in the
#     prime factorisation of n"""
#     m=1
#     for i in [2,5]:
#         while not n%i:
#             n//=i
#             m*=i
#     return {m>1:m, m==1:0 }
#
# def primesieve(n):
#     """return array of primes 2<=p<=n"""
#     sieve=np.ones(n+1,dtype=bool)
#     for i in range(2, int((n+1)**0.5+1)):
#         if sieve[i]:
#             sieve[2*i::i]=False
#     return np.nonzero(sieve)[0][2:]

# p133v2(10)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()

# Python - 242 ms
#
# Almost identical code to problem 132, except collated the non-factor primes instead of the factor primes.
# 1) Sieve primes
# 2) For each prime, in prime factorization of (p-1) let m = (2 ** a) * (5 ** b) where a and b
# are the respective exponents in (p-1)'s prime factorization.
# 3) If 10 ** m not equal to 1 (mod p), then p can never divide R(10 ** n)

# repunit_nonfactors.py
# Find all primes below 10 ** 5 that will never be factors of R(10 ** n)
# for all n. Return this sum
#
# import sys, os, inspect, time, operator
# from math import log
#
# #------------------------------------------------------------------------------
# # Calculate gcd of an inputted number and 10 ** n for n unbounded
# # Uses function below as well to determine max exponents
# def generate_gcd (num1, num_list, prime_set, test_factors):
#
#     num1_factors = set(num_list[num1][1])
#     common_factors = (num1_factors.intersection (set(test_factors)))
#     if len(common_factors) == 0:
#         return 1
#     prod = 1
#     for factor in list(common_factors):
#         prod = prod * (factor ** max_exponent_prime_factor (num1, factor, 1))
#     return prod
#
#
#
# # Determine the max exponent of p that divides x1
# # known is the least known exponent that satisfies
# def max_exponent_prime_factor (x1, p, known):
#
#     n = 0
#     exp = known + 2 ** n
#     while x1 % (p ** exp) == 0:
#         n += 1
#         exp = known + 2 ** n
#
#     if n == 0:
#         return known
#     if n == 1:
#         return (known + 1)
#
#     return max_exponent_prime_factor (x1, p, known + 2 ** (n-1))
# #------------------------------------------------------------------------------
#
# #-----------------------------------------------------------------------------
# # Calculate base ** exp mod mod_class
# # Handles large exponents by breaking them down into base 6
# # and constantly taking remainders of the results
# # Uses function below to determine representations in base 6
# def efficient_mod_exponentiation (base, exp, mod_class):
#     # we will use exp_base of 6 for convenience
#     rep_base = 6
#     digit_list = num2base (exp, rep_base) # puts number in base 6
#     total_prod = 1
#
#     for i in range (len(digit_list)):
#         if i == 0:
#             total_prod *= ((base ** digit_list[-i-1]) % mod_class)
#         elif i == 1:
#             base_num_exp = (base ** rep_base)
#             if base_num_exp > mod_class / 2:
#                 base_num_exp = base_num_exp - mod_class
#
#             total_prod *= ((base_num_exp ** digit_list[-i-1]) % mod_class)
#             total_prod %= mod_class
#         else:
#             base_num_exp = (base_num_exp ** rep_base)
#             if base_num_exp > mod_class / 2:
#                 base_num_exp = base_num_exp - mod_class
#
#             total_prod *= ((base_num_exp ** digit_list[-i-1]) % mod_class)
#             total_prod %= mod_class
#     return (total_prod % mod_class)
#
# # Given a base 10 number, will return a list of digits in the inputted base
# def num2base (num, base):
#     digits = []
#     while num:
#         digits = [num % base] + digits
#         num = num/base
#     return digits
# #-----------------------------------------------------------------------------
#
#
# def main():
#
#     max_prime =  10 ** 5
#     repunit_len_factors = [2, 5]
#
#     prime_list = num_list  = prime_generator (max_prime)
#     prime_set = set(prime_list)
#     prime_nonfactor_list = []
#
#     for prime in prime_list:
#         if prime < 7:
#             prime_nonfactor_list.append (prime)
#             continue
#
#         # In this case, test_gcd is the gcd between prime - 1
#         # and 10 ** n where n is unbounded.
#         test_gcd = generate_gcd (prime - 1, num_list, prime_set,
#                                  repunit_len_factors)
#
#         if efficient_mod_exponentiation (10, test_gcd, prime) != 1:
#
#             prime_nonfactor_list.append (prime)
#
#
#     print (sum(prime_nonfactor_list))
#
# main()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,   --------------------------')
t1  = time.time()



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

# print('\n--------------------------SOLUTION 4,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
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
