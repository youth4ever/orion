#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
                Pandigital prime sets       -       Problem 118

Using all of the digits 1 through 9 and concatenating them freely to form decimal integers, different sets can be formed.

Interestingly with the set {2, 5, 47, 89, 631 }, all of the elements belonging to it are prime.

How many distinct sets containing each of the digits one through nine exactly once contain only prime elements?

'''
import time
import eulerlib
import gmpy2, functools, operator
from itertools import  combinations, permutations

# Rules :
# 4,6,8 must be within a number AND not at the end
# 2 free or within a number AND NOT at the end

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
    return [ i for i in cand if i and i > lower ]

def partitions(n):
    '''     Taken from http://code.activestate.com/recipes/218332-generator-for-integer-partitions/
            Created by David Eppstein on Wed, 27 Aug 2003
    :What it is:    A generator of number partition
    :Usage:     Example:    >>>             for i in partitions(5):    print(i)
    :param n:   the number you want the partitions
    :return:    set of lists with all the possible combinations                              '''
    # base case of recursion: zero is the sum of the empty list
    if n == 0:
        yield []
        return

    # modify partitions of n-1 to form partitions of n
    for p in partitions(n-1):
        yield [1] + p
        if p and (len(p) < 2 or p[1] > p[0]):
            yield [p[0] + 1] + p[1:]

def primesieve(n):          ### o(^_^)o  FASTEST  o(^_^)o  ###  Highly Efficient !!!
    import numpy as np
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]

print('\n--------------------------TESTS------------------------------')

t1  = time.time()

# primes_8 = [i for i in sieve(10**7, 10**8) if  len(set(list(str(i)))) == 8 and list(str(i)).count('0') ==0  ]
# print(len(primes_8) ,  primes_8)

# 23082 [12345769, 12346589, 12346597, 12348659, 12354689, 12354967,            Completed in : 58071.321487 ms

# primes_8 = [i for i in prime_generator( 10**7, 10**8 ) if  len(set(list(str(i)))) == 8 and list(str(i)).count('0') ==0  ]
# print(len(primes_8) ,  primes_8)
#
# Eights = 0
# P = set('2357')
# for s in primes_8 :
#     A= set(str(s))
#     if len(P - A) >= 1  :
#         Eights +=1
#         print( s , P-A )
#
# print('\nThere are Eighths: \t', Eights )     #   There are Eigths: 	 11483

Eigths =  11483

print('\n--------------- SEVENS--------------')

def get_sevens():
    primes_7 = [i for i in prime_generator( 10**6, 10**7 ) if  len(set(list(str(i)))) == 7 and list(str(i)).count('0') ==0  ]
    print(len(primes_7) ,  primes_7)

    Sevens = 0
    P = set(list(int(i) for i in str(123456789)))        #set('12357')
    # # primes_7 = [ 9854231 ,9854261 , 9854371 , 9854623, 9854627 ]

    cnt = 0
    for s in primes_7 :
        A= set(list(int(i) for i in str(s)))
        B = list(P-A)
        if B[0]%2 == 1 or B[1]%2 == 1  :
            if gmpy2.is_prime( B[0]) and gmpy2.is_prime( B[1]) :
                cnt +=1
                Sevens +=1         # Both are primes :
                print(str(cnt)+'.    ', s ,A, P-A)
            d2_1, d2_2 = int(str(B[0])+str(B[1])) , int(str(B[1])+str(B[0]))            # forming two digits nrs : 23, 32
            if gmpy2.is_prime(d2_1) :                # if  23 is prime
                cnt+=1
                Sevens +=1
                print(str(cnt)+'.    ', s ,A, d2_1)
            if gmpy2.is_prime(d2_2) :                   # if  32 is prime
                cnt+=1
                Sevens +=1
                print(str(cnt)+'.    ', s ,A, d2_2)
    return Sevens

# print('\nThere are Sevens: \t', get_sevens() )     #   There are Sevens: 10896            Completed in : 3595.205545 ms
Sevens = 10896

print('\n--------------- SIXES--------------')

# primes_6 = [i for i in prime_generator( 10**5, 10**6 ) if  len(set(list(str(i)))) == 6 and list(str(i)).count('0') ==0  ]
# print(len(primes_6) ,  primes_6)
#
#
# # primes_6 = [ 9854231 ,9854261 , 9854371 , 9854623, 9854627 ]
# Sixes = 0
# P = set(list(int(i) for i in str(123456789)))
#
# cnt = 0
# for s in primes_6 :
#     A= set(list(int(i) for i in str(s)))
#     B = list(P-A)
#     # print(A, B)
#     itr=0
#     for p in B :                # Check if all are primes :  only 1 digit  (1, 1, 1) partition
#         if gmpy2.is_prime(p) :             itr +=1
#     if itr ==3 :        Sixes+=1
#     c = list(combinations(B, 2))               # Check if all are primes :  only 1 digit  (2 , 1) partition
#     for j in c :
#         d1 = list(set(B) - set(j))
#         if  gmpy2.is_prime( int(str(j[0])+str(j[1])) ) and gmpy2.is_prime( d1[0] ) :
#             Sixes +=1
#             print(B, str(j[0])+str(j[1]) ,d1)
#         if  gmpy2.is_prime( int(str(j[1])+str(j[0])) ) and gmpy2.is_prime( d1[0] ) :
#             Sixes +=1
#             print(B, str(j[1])+str(j[0]) ,d1)
#     p = list(permutations(B))
#     print(p)
#
#



# print('\nThere are Sixes: \t', Sixes )     #   There are Sevens: 19871
# Sixes = 19871

print()
Part = []
for i in partitions(9):
    if 1 < len(i) <= 5 :
        Prt = tuple(i[::-1])
        if Prt < (6,) :
            print(Prt)


primes = primesieve(10**5)
D={}
for p in primes :
    l = len(str(p))
    if l not in D :
        D[l]=set([])
        if len(str(p)) == len(set (str(11)) ) :
            D[l].add(p)
    else : D[l].add(p)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n----------------------------')
t1  = time.time()

P = set( [i for i in range(1,10)] )

itr, cnt, scnt= 0, 0, 1
T = ( 2, 2, 2, 2, 1 )
a1 = D[T[0]]
# while scnt < 4 :
for p1 in a1 :
    A= set(list(int(p1) for p1 in str(p1)))
    B = P - A
    print(p1, A, B)
    # scnt+=1
    C = B
    for i in range(1, 2 ) :        # len(T)
        SET = set()
        comb = list(combinations(C, T[i]))
        # print(comb)
        Z = []
        if T[i] > 1 :
            for j in comb :
                perm = [ int(''.join([str(k) for k in s ])) for s in  list(permutations(j)) ]
                Z = Z + perm
        print(i,'    ',Z)
        # for p2 in Z :
        #     SET.add(p1)
        #     C = B
        #     if p2 in D[T[i]]:
        #         SET.add(p2)
        #         A = set(list(int(p2) for p2 in str(p2)))
        #         C = set(C) - A
        #         print( A, C  ,SET)
        #         SET=set()






print('\n------------------------------')

# T = list(( 2, 2, 2, 2, 1 ))
#
# def form_sets( T ):
#     T2=T[:]
#     Dg1 = set( [i for i in range(1,10)] )
#     SET = set()
#     for p1 in D[T2[0]] :
#         SET.add(p1)
#         A = set(list(int(p1) for p1 in str(p1)))
#         Dg2 = Dg1 - A
#         print(p1, A, Dg2, SET  )
#         SET=set()
#         while len(T2) > 3 :
#             A = set(list(int(j) for j in str(p1)))
#             # for p2 in D[T[0]] :
#
#
#
#
#             print(T2, D[T2[0]])
#             T2.pop(0)
# form_sets(T)

# print('\n-------------- BENCHMARK TEST ----------------')
# # for i in D:     print(D[i])
# test_list = [i for i in range(9*10**6+1, 9*10**6+1000, 2)]

# t1  = time.time()
# cnt=0
# for p in test_list:
#     if gmpy2.is_prime(p) :
#         cnt+=1
#         print(str(cnt)+  '.    Yes' , end=' ')
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# t1  = time.time()
# cnt=0
# for p in test_list:
#     if p in D[len(str(p))] :
#         cnt+=1
#         print(str(cnt)+ '.   Yes', end=' ')
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()

















# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


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
