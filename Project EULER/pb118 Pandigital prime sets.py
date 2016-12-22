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

# primes_7 = [i for i in prime_generator( 10**6, 10**7 ) if  len(set(list(str(i)))) == 7 and list(str(i)).count('0') ==0  ]
# print(len(primes_7) ,  primes_7)
#
# Sevens = 0
# P = set(list(int(i) for i in str(123456789)))        #set('12357')
# # primes_7 = [ 9854231 ,9854261 , 9854371 , 9854623, 9854627 ]
#
# for s in primes_7 :
#     A= set(list(int(i) for i in str(s)))
#     if P-A != {1} or P-A != {4} or P-A != {6} or P-A != {8}   :
#         if len(P - A) == 1 :
#             Sevens +=1
#             print( s , P-A )
#         if len(P - A) > 1 :
#             lst = list(P-A)
#             if gmpy2.is_prime(lst[0]) : Sevens +=1
#             if gmpy2.is_prime(lst[1]) : Sevens +=1
#             p1 = int(str(lst[0])+str(lst[1]))
#             p2 = int(str(lst[1])+str(lst[0]))
#             if gmpy2.is_prime(p1) : Sevens +=1
#             if gmpy2.is_prime(p2) : Sevens +=1
#             print( s , P-A )
#
# print('\nThere are Sevens: \t', Sevens )     #   There are Sevens: 19871            Completed in : 3595.205545 ms
Sevens = 19871

primes_6 = [i for i in prime_generator( 10**5, 10**6 ) if  len(set(list(str(i)))) == 6 and list(str(i)).count('0') ==0  ]
print(len(primes_6) ,  primes_6)


# primes_6 = [ 9854231 ,9854261 , 9854371 , 9854623, 9854627 ]
Sixes = 0
P = set(list(int(i) for i in str(123456789)))

for s in primes_6 :
    A= set(list(int(i) for i in str(s)))
    if P-A != {1} or P-A != {4} or P-A != {6} or P-A != {8}   :
        if len(P - A) == 1 :
            Sevens +=1
            print( s , P-A )
        if len(P - A) > 1 :
            lst = list(P-A)
            tmp=[]
            for i in range(1, len(lst)+1 ) :
                c = list(combinations(lst, i ))
                @ 2016-12-17, 22:15
                !! I LEFT HERE !!!! Need to construct correctly the list

                tmp.append(c)
            # lst = list(P-A)
            # if gmpy2.is_prime(lst[0]) : Sevens +=1
            # if gmpy2.is_prime(lst[1]) : Sevens +=1
            # p1 = int(str(lst[0])+str(lst[1]))
            # p2 = int(str(lst[1])+str(lst[0]))
            # if gmpy2.is_prime(p1) : Sevens +=1
            # if gmpy2.is_prime(p2) : Sevens +=1
            print( s , P-A,'    ' ,tmp )

print('\nThere are Sevens: \t', Sevens )     #   There are Sevens: 19871            Completed in : 3595.205545 ms
Sevens = 19871


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
