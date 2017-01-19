#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Sun, 25 Dec 2016, 21:31
#The  Euler Project  https://projecteuler.net
'''
The prime factorisation of binomial coefficients        -           Problem 231

The binomial coefficient C{10,2} = 120.

120 = 2**3 × 3 × 5 = 2 × 2 × 2 × 3 × 5, and 2 + 2 + 2 + 3 + 5 = 14.

So the sum of the terms in the prime factorisation of  C{10, 3} is 14.

Find the sum of the terms in the prime factorisation of  C{ 20.000.000, 15.000.000}  .

'''
import time, gmpy2
import functools, operator


def prime_generator(lower, upper):      ### o(^_^)o  FASTEST  o(^_^)o  ###  HIghly Efficient !!!
    """  Sieve of Eratosthenes              !!!!!!!!! THE FASTEST SIEVE. It won the battle with sieve
    Create a candidate list within which non-primes will be marked as None.         """
    cand = [i for i in range(3, upper + 1, 2)]
    end = int(upper ** 0.5) // 2

    # Loop over candidates (cand), marking out each multiple.
    for i in range(end):
        if cand[i]:
            cand[cand[i] + i::cand[i]] = [None] * ( (upper // cand[i]) - (upper // (2 * cand[i])) - 1 )
    # Filter out non-primes and return the list.
    return  [ i for i in cand if i and i > lower ]

def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    from pyprimes import factorise
    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]

print('\n--------------------------TESTS------------------------------')




# 2016-12-23, 12:33
# IDEA : is to Eliminate from the Numerator list the multiples of the Denominator list, progressively until we are no longer left
# with the list Denominator, and only with the Numerator list which will consist of primes and leftovers from the simplifications
# Must do first for a smaller list and do a correct algorithm, and practice with it !!!!
# For example you could practice with C{200, 150}

t1  = time.time()


comb_test = gmpy2.comb(200, 150)
# print( 'We will practice with this list of C{200, 150} for which the algorithm elimination should work :\n' ,comb_test, end='\t  '*3 )
# print('As you see this C{200,150} is already a huge huge number')
gf = get_factors( comb_test )
# print('Insane but we just test it:\n', gf )
print('\n\nTotal sum of the factors: \t', sum(gf) )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n================  My Initial SOLUTION,   ===============\n')
t1  = time.time()
#
# #############       200 / 150 TEST ##############
# Num1 = set(i for i in range(151, 201))        # STEP 1 Initialization only the needed numbers
#
# N1 = set(i for i in range(152, 201, 4))       # Multiple of 4 numbers
# Num = Num1 - N1                                         # We eliminate the multiple of 4
# Den = set(i for i in range(2, 38))         # In the Denominator we put only the numbers which remained after first step
# # Num = Num1
# # Den = set(i for i in range(2, 51))         # In the Denominator we put only the numbers which remained after first step
# print(len(Num) ,Num)
# print(len(Den) , Den)
#
# # #############       20.000.000  ######################
# # Num1 = set(i for i in range(15000001, 20000001))        # Initialization only the needed numbers
# # N1 = set(i for i in range(15000004, 20000001, 4))       # Multiple of 4 numbers
# # Num = Num1 - N1                                         # We eliminate the multiple of 4
# #
# # Den = set(i for i in range(2, 3750001))         # In the Denominator we put only the numbers which remained after first step
# # print('Num length :\t' ,len(Num), '\nDen length :\t', len(Den),'\n')
#
#
# S_tot = 4*len(N1)      # How many four multiples are in the upper range
# # S_tot = 0
#
# print('---------------STEP 1 ------ Eliminate primes --------------')
# N2 = set()
# for i in Num :                    # Step 2 : Eliminate directly the primes from the Num Top Range, add them to S_tot
#     if gmpy2.is_prime(i) == True :
#         N2.add(i)
#         S_tot+=i
# Num = Num - N2
#
# print('\nS_tot = \t',S_tot,'\n' )
# print('Num length :\t' ,len(Num), '\nDen length :\t', len(Den),'\n')
#
#
# print('---------------- STEP 2 ----------- Eliminate the multiple in the Numerator list ------------ ')
# for i in range(5, 5000) :         # Here we eliminate all the multiples of the Numerator list
#     a = min(Num)
#     b = max(Num)
#     # print(a, a//i+1, b, b//i -1 )
#     for j in range(a//i+1, b+1  ):
#         if (j*i) in Num and j in Den:
#             Num.remove(j*i)
#             g = get_factors(i)
#             S_tot += sum(g)
#             Den.remove(j)
#     # print(Num)
#     # print( i,j, i*j,  Den)
#
# print('\nS_tot = \t',S_tot,'\n' )
# print('Num length :\t' ,len(Num), '\nDen length :\t', len(Den),'\n')
#
# print('-------------STEP 3 --------Eliminate Multiples ---------------------')
#
# N3 = list(Num)[:]
# D3 = list(Den)[:]
# for i in range(len(N3)) :           # Step 3, we get rid of the multiples of the Den in the Numerator
#     for j in range(len(D3)) :
#         if D3[j] !=1 and N3[i]%D3[j] == 0 :
#             N3[i] = N3[i]//D3[j]
#             D3[j] = 1
# print(N3[:100],'\n' ,D3[:100])
#
# print('----------------- STEP 4 , CLEANING --------------------')
#
# N4 =[]              # Step 4, Cleaning
# for i in N3 :       # we clean the Numerator of the ones
#     if i !=1 :
#         N4.append(i)
#
# D4 = []
# for i in D3 :       # we clean the Denominator  of the zeroes in Denominator
#     if i !=1 :
#         D4.append(i)
#
# Num = N4[:]
# Den = D4[:]
# print('\nS_tot = \t',S_tot,'\n' ,Num[:100], '\n', Den[:100],'\n')
#
# print('--------STEP 5 ---Factorise all the Denominator list -----Correct-----')
#
# D5 = []        # Step 5 : Here we transform the Den list into just basic prime factors
# for i in Den :
#     if gmpy2.is_prime(i) : D5 .append(i)
#     if gmpy2.is_prime(i) == False :
#         f = get_factors(i)
#         D5.extend(f)
#
# # Simple check of the factors of D5 with the original list Den
# # print(D5, functools.reduce( operator.mul, D5) , Den, functools.reduce( operator.mul, Den))
#
# Den = D5[:]
# #Status
# print('\nS_tot = \t',S_tot,'\n' ,Num[:100], '\n', Den[0:100],'\n')
#
# print('--------------STEP 6 ---Clean Out the Denominator List -------------------')
#
# N6 = list(Num)[:]                      # Step 6 : We want to completely clean out the Denominator list, remain only the Numerator
# D6 = Den[:]
# for i in range(len(N6)) :
#     for j in range(len(D6)) :
#         if D6[j] !=0 and N6[i]%D6[j] == 0 :
#             N6[i] = N6[i]//D6[j]
#             D6[j] = 0
# print(N6[0:100],'\n' ,D6[0:100])
#
# S_tot -= sum(D6)
#
# print('\n-------------STEP 7 -- FINAL STEP, Factor all the remaining terms in the Numerator : --------------------')
# # Step 7 - FINAL STEP, Factor all the remaining terms in the Numerator :
#
# N7=[]
# for i in N6 :      # Add the terms to S_tot
#     if i != 1 :
#         if gmpy2.is_prime(i) == True  : N7.append(i)
#         elif gmpy2.is_prime(i) == False :
#             f = get_factors(i)
#             N7.extend(f)
#
# S_tot+=sum(N7)
#
# print('Final Numerator List : \n',N7[:100])
#
#
#
# print('\n\nFinal Answer :\t',S_tot)

up , down = 200, 150
P = prime_generator(down, up)
# print(P)
S = sum(P)

print('Total S : ',S)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

up , down = 200, 150
bot = up //4


UP = set(range(down+1, up+1))
DO = set(range( 2, bot+1,  ))

# print(UP)
# print(DO)

# S=0
# while len(UP) > 0 :
#     i = min(UP)
#     if gmpy2.is_prime(i) == True :
#         S+=i
#         UP.remove(i)
#         print(i)
    # elif gmpy2.is_prime(i) == False :
    #     for j in DO:
    #         # print(UP, DO, i, j )
    #         if i % j == 0 :
    #             k = i / j
    #             DO.remove(j)
    #             S+= sum(get_factors(k))
    #             UP.remove(i)
    #             # print('     ', i, j )
    #             break
    #     if i in UP :
    #         # print(i,'    none divisors found in  Denominator')
    #         S+= sum(get_factors(i))
    #         UP.remove(i)



# print('\n',UP)
# print(DO)
# do_f = [  sum(get_factors(i)) for i in list(DO)]
# print((do_f ))
# S-=sum(do_f)

# print('\n\nFinal Answer :\t', int(S))           #  Total sum of the factors: 	 7526965179680

t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')

# ==== GENERAL IDEA, Legendre's Theorem from Number Theory allows to ...
# http://mathbmt.com/legendretheo

print('\n--------------------------SOLUTION 0, SIMPLEST & FASTEST  --------------------------')
t1  = time.time()

# ==== Sat, 8 Oct 2016, 20:34 , Arvind Ganesh, USA
# Using Legendre's Theorem.

import numpy as np
def primesieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]

n, r, s = 20000000, 15000000, 0
primes = primesieve(n)
for p in primes:
    pj = p
    while pj <= n:
        s += p * (n//pj - r//pj - (n - r)//pj)
        pj *= p
print (s)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 1,  Legendre s Theorem 20 secs --------------------------')

# ==== Mon, 21 Nov 2016, 15:00, aolea, Spain
# C(20⋅106,15⋅10620⋅106,15⋅106) = 20*10**6!/(15*10**6!*5*10**6!)
# so:
# 1.- For primes bigger than 15*10**6 add them multiplied by its exponent in 20*10**6! factorization.
# 2.- For primes smaller than 15*10**6 check if the exponent in the 20*10**6! factorization is bigger than
# the sum of the exponents of that prime in the 5*10**6! and 15*10**6! factorizations,
# if yes add them multiplied by de exponent of 20*10**6 minus de exponent of 15*10**6 and the exponent of 5*10**6
#
# The exponent of each prime in the n! factorization  is computed using the Legendre's theorem



t1  = time.time()

def aolea():
    import pyprimes
    import math

    def p_in_factorial(p,n):
        '''
        Computes the exponent of a given prime in the n! factorization using the Legendre´s theorem

        Parameters:
        -----------
        n : integer that defines the factorial.Integer
        p: prime whose exponent in the n! factorization is computed.Integer.

        Returns:
        -------
        v : exponent of the prime number p in the n! factorization.Integer
        '''
        k = 1
        v = 0
        while n >= p ** k:
            v += math.floor(n / p ** k)
            k += 1
        v = int(v)
        return v
    '''
    C(20*10**6,15*10**6) = 20*10**6!/(15*10**6!*5*10**6!)
    so:
    1.- For primes bigger than 15*10**6 add them multiplied by its exponent in 20*10**6! factorization.
    2.- For primes smaller than 15*10**6 check if the exponent in the 20*10**6! factorization is bigger
        than the sum of the exponents of that prime in the 5*10**6! and 15*10**6! factorizations, if yes
        add them
    '''
    sum = 0
    for i in pyprimes.primes_below(20*10**6):

        if i > 15*10**6:
            sum += i*p_in_factorial(i,20*10**6)
        elif i < 15*10**6:
            if p_in_factorial(i,20*10**6) - p_in_factorial(i,15*10**6) - p_in_factorial(i,5*10**6) > 0 :
                sum +=i*(p_in_factorial(i,20*10**6) - p_in_factorial(i,15*10**6) - p_in_factorial(i,5*10**6))
        # print(i, sum)
    print('solution problem 231:', sum)

# aolea()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n--------------------------SOLUTION 2,  SLOW --------------------------')
t1  = time.time()

# ======Sun, 20 Nov 2016, 09:57, mbh038, England
# 4.6 s in Python, using the fact that if p is a prime factor of nCm,
# then its exponent is the number of integer values of j≥0j for which frac(m/pj)>frac(n/pj)

import numpy as np


def primesieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]

def mhb038(n,m):
    factors=[]
    primes=primesieve(n)
    for p in primes:
        count=0
        j=0
        while p**j<n:
            if (m/p**j)%1>(n/p**j)%1:
                count+=1
            j+=1
        if count>0:
            factors.append((p,count))
    print( sum([x[0]*x[1] for x in factors]) )

# mhb038(2*10**7, 1.5*10**7)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,   --------------------------')
t1  = time.time()

# === Tue, 4 Oct 2011, 21:17, Francky, France
# Short 13 lines (and fast) Python3 ; 10s
# My "sieve" give the least prime for any number.
# I was ambarrassed with 1 !!! No prime in prime factorisation for 1, so empty sum, so I thought 0 !!!

def PE231(n=5*10**6, m=2*10**7):
  M=m+1
  tab=[0]*M
  for i in range(2, int(M**.5)+1):
    if not tab[i]: # ie i est premier
      tab[2*i: M: i] = [i]*(m//i-1)

  somme=[0]*M
  for i in range(2, M):
    if not tab[i]:
      somme[i]=i # i est premier
    else:
      somme[i]=tab[i]+somme[i//tab[i]]
  return sum(somme[m-n:m]) - sum(somme[:n+1]) +1 # for 1 !!!

PE231()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5,   --------------------------')
t1  = time.time()

# ===== Wed, 12 Sep 2012, 12:25, ephemeral, USA
# Short and sweet in Python! :)
# Takes about 3.6 seconds to run.

def primesieve(n):          ### o(^_^)o  FASTEST  o(^_^)o  ###  HIghly Efficient !!!
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1, dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i] = False
    return np.nonzero(sieve)[0][2:]

def factorial_factor_sum(n, primes, s = 0, i = 0):
    while i < len(primes) and n >= primes[i]:
        num = n
        while num >= primes[i]:
            num //= primes[i]
            s += primes[i] * num
        i += 1
    return s

def euler_231():
    limit = 2 * 10**7
    primes = primesieve(limit)
    return (factorial_factor_sum(limit, primes) - factorial_factor_sum(int(0.75 * limit), primes) - factorial_factor_sum(int(0.25 * limit), primes))

euler_231()

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
