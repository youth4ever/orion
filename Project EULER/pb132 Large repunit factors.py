#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
Large repunit factors       -       Problem 132

A number consisting entirely of ones is called a repunit. We shall define R(k) to be a repunit of length k.

For example, R(10) = 1111111111 = 11×41×271×9091, and the sum of these prime factors is 9414.

Find the sum of the first forty prime factors of R(10**9).

'''
import time
import gmpy2
import functools
import operator

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


def factors(a):
    '''Outputs a list of the unique prime factors of its input; The Second Fastest Algorithm
    This Function is splitting a number in its factors, and detects also if the number is a prime. '''
    b = 2
    d = []
    f = a
    while f > 1:
        while f % b != 0:
            b = b + 1
        d = d + [b]
        f = f / b
    if len(d) >1:
        return d
    else: return [1, a]

class GET_DIVISORS(object):
    '''Made by Bogdan Trif @ 2016-11-15, based on itertools.combinations module
    and with a little help on list(functools.reduce(operator.mul, i) for i in comb)

    :param nr:  int
    :return: a list with the divisors    '''

#     def __init__(self, nr):   # We don't want to initialize the class with a number
#     self.nr = nr

    def factorise(self, nr):
        ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
        from pyprimes import factorise
        return [val for sublist in [[i[0]]*i[1] for i in factorise(nr)] for val in sublist]

    def divisors(self, nr):
        from itertools import combinations
        import functools, operator, gmpy2
        if gmpy2.is_prime(nr) == True or nr == 1 :
            return [1]    # Must be adjusted to [1] if you change on list
        else :
            all_factors =  self.factorise(nr)
            # set_factors=list(set(all_factors))
            comb= set()
            # print(all_factors)
            for i in range(1, len(all_factors)):
                c = set(combinations(all_factors, i) )
                comb.update(c)
                comb_prod = list(functools.reduce(operator.mul, i) for i in comb)
                comb_prod.sort()
        return  comb_prod[::-1]   # sum([1]+ comb_prod)   !!!!!!!! Remember to change on  return [1]  for isprime case

primes = prime_generator(int(1.61*10**5))
print(len(primes) ,primes[0:100])

print('\n--------------------------TESTS------------------------------')

Ten =  [11, 41, 271, 9091]
t =   functools.reduce(operator.mul, Ten+ [41, 271])
print(int('1'*40)//5964848081)
print('1  * 50  :' , GET_DIVISORS().factorise(int('1'*40) // t)  )


################        GENERAL IDEA      ####################
# GOOD INFO : http://stdkmd.com/nrr/repunit/tm.cgi?p=100
# GENERAL IDEA :
# Since R(k)=(10**k−1) / 9, to show that p is a factor of R(k), it suffices to show that
# (10**k−1)/9 ≡ 0 (mod p), or  10**k ≡ 1 (mod 9p)
# Example: If 11111 has factor 41 => pow(10, 5, 9*41) = 1   !!!!!!!!!!!!!!!!!!!!!!!!!!!!
print('\nTherefore we can test this idea with 11111 which has 41 as a factor : ', pow(10,5 ,41* 9)  )   # with 3 args pow makes modulo


##########################

print('\n================  My FIRST SOLUTION,  SLOW,  2 min ===============\n')
t1  = time.time()

# L = []        # The most elementary way
# for i in range(6, 6+1):
#     x = int('1'*10**i)
#     for j in primes :
#         if x % j == 0 :
#             L.append(j)
#             print(j)
# print('\n', L)

# 1 2          [11]
# 1 3          [3, 37]
# 1 4          [11, 101]
# 1 5          [41, 271]
# 1 6          [3, 7, 11, 13, 37]
# 1 7          [239, 4649]
# 1 8          [11, 73, 101, 137]
# 1 9          [3, 3, 37, 333667]
# 1 10          [11, 41, 271, 9091]
# 1 11          [21649, 513239]
# 1 12          [3, 7, 11, 13, 37, 101, 9901]
# 1 13          [53, 79, 265371653]
# 1 14          [11, 239, 4649, 909091]
# 1 15          [3, 31, 37, 41, 271, 2906161]
# 1 16          [11, 17, 73, 101, 137, 5882353]
# 1 17          [2071723, 5363222357]
# 1 18          [3, 3, 7, 11, 13, 19, 37, 52579, 333667]

# 1 10          [11, 41, 271, 9091]
# 1 20          [11, 41, 101, 271, 3541, 9091, 27961]
# 1 30          [3, 7, 11, 13, 31, 37, 41, 211, 241, 271, 2161, 9091, 2906161]
# 1 40          [11, 41, 73, 101, 137, 271, 3541, 9091, 27961, 1676321, 5964848081]

# 10: [11, 41, 271, 9091],
# 100: [11, 41, 101, 251, 271, 3541, 5051, 9091, 21401, 25601, 27961, 60101, 7019801]
# 1000: [11, 41, 73, 101, 137, 251, 271, 401, 751, 1201, 1601, 3541, 4001, 5051, 9091, 21001, 21401, 24001, 25601, 27961, 60101, 76001, 162251, 1378001, 1610501, 1676321, 7019801],
# 10000: [11, 17, 41, 73, 101, 137, 251, 271, 401, 751, 1201, 1601, 3541, 4001, 5051, 9091, 16001, 21001, 21401, 24001, 25601, 27961, 60101, 76001, 160001, 162251, 670001, 952001, 1378001, 1610501, 1676321, 5070721, 5882353, 7019801],
# 100000: [11, 17, 41, 73, 101, 137, 251, 271, 353, 401, 449, 641, 751, 1201, 1409, 1601, 3541, 4001, 4801, 5051, 9091, 16001, 21001, 21401, 24001, 25601, 27961, 37501, 43201, 60101, 69857, 76001, 160001, 162251, 544001, 670001, 952001, 980801, 1378001, 1610501, 1634881, 1676321, 5070721, 5882353, 6600001, 7019801],
# 1000000: [11, 17, 41, 73, 101, 137, 251, 271, 353, 401, 449, 641, 751, 1201, 1409, 1601, 3541, 4001, 4801, 5051, 9091, 16001, 19841, 21001, 21401, 24001, 25601, 27961, 37501, 43201, 60101, 62501, 69857, 76001, 160001, 162251, 544001, 670001, 952001, 976193, 980801, 1378001, 1610501, 1634881, 1676321, 2800001, 5070721, 5882353, 6187457, 6576001, 6600001, 7019801]
# 10**9 : [11, 17, 41, 73, 101, 137, 251, 257, 271, 353, 401, 449, 641, 751, 1201, 1409, 1601, 3541, 4001, 4801, 5051, 9091, 10753, 15361, 16001, 19841, 21001, 21401, 24001, 25601, 27961, 37501, 40961, 43201, 60101, 62501, 69857, 76001, 76801]
# 10**9 : [11, 17, 41, 73, 101, 137, 251, 257, 271, 353, 401, 449, 641, 751, 1201, 1409, 1601, 3541, 4001, 4801, 5051, 9091, 10753, 15361, 16001, 19841, 21001, 21401, 24001, 25601, 27961, 37501, 40961, 43201, 60101, 62501, 69857, 76001, 76801]
#            [11, 17, 41, 73, 101, 137, 251, 257, 271, 353, 401, 449, 641, 751, 1201, 1409, 1601, 3541, 4001, 4801, 5051, 9091, 10753, 15361, 16001, 19841, 21001, 21401, 24001, 25601, 27961, 37501, 40961, 43201, 60101, 62501, 69857, 76001, 76801, 160001, 162251]

def repunit_factors_solution_1(n):
    X=[]
    D =  (GET_DIVISORS().divisors(n))
    D.reverse()
    print(D)
    for i in range( len(D)*2//3  )  :
        x = int('1'*D[i])
        for j in primes :
            if x%j == 0 :
                X.append(j)
                # print( D[i] ,  j)
    X=sorted(list( set(X)))
    return print('ANSWER Sum: ',sum(X[0:40]),  len(X),  X )


# print(repunit_factors_solution_1(10**9))                # Uncomment to activate                 ANSWER Sum:  843296


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n================  My SECOND SOLUTION, STILL SLOW,  RECURSIVE VERSION ===============\n')
t1  = time.time()

X, N = {}, {}
def get_repunit_factors(n):     # THE RECURSION VERSION
    # print(X)
    if n <= 2*10**5 :
        D =  (GET_DIVISORS().divisors(n))
        D.reverse()
        print(n, D)
        if n not in N :
            N[n]=n
            for i in range( len(D)  )  :
                x = int('1'*D[i])
                if D[i] in X : continue
                for j in primes :
                    if x%j == 0 :
                        if D[i] in X:
                            X[ D[i] ].append(j)
                        else :
                            X[ D[i] ] = [j]
                        # print( D[i] ,  j)
            return X
    else :
        E = (GET_DIVISORS().divisors(n))
        print('============ >', n, E)
        for k in E:
            get_repunit_factors(k)

    return X

def solve_pb132(n):
    A = get_repunit_factors(n)
    print(A)
    A = sorted({x for v in A.values() for x in v})
    print(len(A),  A)
    print('\nAnswer : ',  sum(A[0:40]))

# solve_pb132(10**9)      # My second solution        # ANSWER Sum:  843296


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n=========  My THIRD SOLUTION, IMPROVED, VERY FAST, Using formula R(k)=(10**k-1)/9   ============\n')
t1  = time.time()

primes = prime_generator(int(1.61*10**5) )
test_nr = 10**9
cnt, P  = 0, []
for i in primes:
    if pow(10, test_nr, 9*i) == 1:      # If R(k)=(10**k-1)/9  => R(k)=(10**k)%(9*prime_nr) == 1   IIF 10**k is divisible with prime_nr
        cnt+=1
        P.append(i)
    if cnt ==40 : break

print(P)
print('\nAnswer, Sum : ', sum(P) )              # 843296

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')




print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,  THE FASTEST & NICEST, brainiac1530, USA --------------------------')
t1  = time.time()
# Same process as the others here, for the most part.  The following Python script took about 120-130 ms,
# where a comparable C++ implementation took about 10 ms with self-made modular exponentiation and prime generator functions.
from pyprimes import primes

def solution_brainiac1530():
    solns, bign = [], 10**9
    for p in primes():
        if pow(10, bign, 9*p) == 1:
            solns.append(p)
            if len(solns) >= 40:
                break
    print(sum(solns),'Last prime :  ',max(solns))

solution_brainiac1530()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2, LIST COMPREHENSION, FASTEST, GNFS, USA   --------------------------')
t1  = time.time()
# Python one-liner (with a list of primes called primes):

P = prime_generator(int(1.7*10**5))

print(sum([p for p in P if pow(10, 10**9, 9*p) ==1 ][:40]) )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 3, SLOW, aolea, Spain  --------------------------')
t1  = time.time()
# Using that if a prime divides a repunit it must also divide the repunits of size the divisors of the first one's size.

import sympy
import pyprimes

def solution_aolea():
    def R(n):
        str1 = ''
        for i in range(0,n):
            str1 = str1 + '1'
        num1 = int(str1)
        return num1

    repunits = []
    prime_factors = []

    for i in sympy.divisors(10**9):
        if i != 1:
            print(i)
            num = R(i)
            repunits.append(num)
            if len(repunits)>60:
                break

    for j1 in pyprimes.primes_below(2*10**5):
        for j2 in repunits:
            if j2 % j1 == 0:
                if j1 not in prime_factors:
                    prime_factors.append(j1)
                    print(len(prime_factors),prime_factors)
                    if len(prime_factors) >= 40:
                        break
                break

        if len(prime_factors) >= 40:
            break
    sum = 0
    count = 0
    for i in prime_factors:
        sum = sum + i
        count = count +1
        print(count,i)
    return print(sum)

# solution_aolea()

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
#
# print('\n--------------------------SOLUTION 5,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
