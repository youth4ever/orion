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

class DIVISORS(object):
    '''Made by Bogdan Trif @ 2016-11-15, based on itertools.combinations module
    and with a little help on list(functools.reduce(operator.mul, i) for i in comb)

    :param nr:  int
    :return: a list with the divisors    '''

#     def __init__(self, nr):   # We don't want to initialize the class with a number
#     self.nr = nr

    def factor_pyprimes(self, nr):
        ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
        from pyprimes import factorise
        return [val for sublist in [[i[0]]*i[1] for i in factorise(nr)] for val in sublist]

    def divisors(self, nr):
        from itertools import combinations
        import functools, operator, gmpy2
        if gmpy2.is_prime(nr) == True or nr == 1 :
            return [1]    # Must be adjusted to [1] if you change on list
        else :
            all_factors =  self.factor_pyprimes(nr)
            # set_factors=list(set(all_factors))
            comb= set()
            # print(all_factors)
            for i in range(1, len(all_factors)):
                c = set(combinations(all_factors, i) )
                comb.update(c)
                comb_prod = list(functools.reduce(operator.mul, i) for i in comb)
                comb_prod.sort()
        return  comb_prod[::-1]   # sum([1]+ comb_prod)   !!!!!!!! Remember to change on  return [1]  for isprime case

def factorise(n):
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    from pyprimes import factorise
    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]

print('\n--------------------------TESTS------------------------------')



REPUNIT = {}
for i in range(2, 19, 1) :      # Form a dictionary with first repunit primes
        s = int('1'*i)
        X = factorise( s )
        print('1', i  ,'        ' , X )
        REPUNIT[i] = X

print('\n', REPUNIT,'\n')




#
# # D = { 10: [11, 41, 271, 9091]}
# for i in range(20, 101, 5) :
#     if gmpy2.is_prime(i) == False :
#         s = int('1'*i)
#         print( DIVISORS().divisors(i))
#         d = DIVISORS().divisors(i)[0]
#         # if len( DIVISORS().divisors(i) ) == 1 :
#             # e = i // d
#         m = functools.reduce(operator.mul, REPUNIT[d] )
#         # n = functools.reduce(operator.mul, REPUNIT[e] )
#         # o = m*n
#         # p = s // o
#         p = s // m
#         X = factorise(p)
#         # REPUNIT[i] = sorted(X+ REPUNIT[d] + REPUNIT[e] )
#         REPUNIT[i] = sorted(X+ REPUNIT[d]  )
#         print(i,  REPUNIT[i])



Ten =  [11, 41, 271, 9091]
t =   functools.reduce(operator.mul, Ten+ [41, 271])
print(int('1'*40)//5964848081)
print('1  * 50  :' , factorise(int('1'*40) // t)  )
#
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


print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

# print('\nFunction test factors :  ' ,factors(  int( '1'*19) ))
primes = prime_generator(10**4)
print(len(primes) ,primes[0:100])

L = {}
for i in range(9, 9+1):
    x = int('1'*10**i)
    for j in primes :
        if x % j == 0 :
            if 10**i not in L :
                L[10**i] = [j]
                # x = x/j
            else :
                L[10**i].append(j)
                # x = x/j
        print(j)

print('\n',L)


# 10: [11, 41, 271, 9091],
# 100: [11, 41, 101, 251, 271, 3541, 5051, 9091, 21401, 25601, 27961, 60101, 7019801]
# 1000: [11, 41, 73, 101, 137, 251, 271, 401, 751, 1201, 1601, 3541, 4001, 5051, 9091, 21001, 21401, 24001, 25601, 27961, 60101, 76001, 162251, 1378001, 1610501, 1676321, 7019801],
# 10000: [11, 17, 41, 73, 101, 137, 251, 271, 401, 751, 1201, 1601, 3541, 4001, 5051, 9091, 16001, 21001, 21401, 24001, 25601, 27961, 60101, 76001, 160001, 162251, 670001, 952001, 1378001, 1610501, 1676321, 5070721, 5882353, 7019801],












t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 3,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
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
