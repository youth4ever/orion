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
import copy

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
    for s in primes_7 :                 #    (7,2), (7,1,1)
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

# get_sevens()

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

### Now it remains to solve the problem of the SETS with elements of max 5 elements


print('\n------------ SET INTERSECTION of a list of numbers -------------------------')
# We have a list of numbers and we have a test number.
# We want to make the intersection of the test number with every number from the list
# and return only the numbers which have no common digits with the test number
# lst = {257, 641, 643, 769, 389, 263, 647, 137, 521, 139, 523, 269, 397, 271, 653, 659, 149}
# print('The initial list to of elements :\t',lst)
# test_nr = 324
# set_nr = set([int(i) for i in str(test_nr)])
# print('Test number :\t', test_nr, set_nr)
# INTERSECTION = [ s for s in lst if len(set_nr& set([int(i) for i in str(s)]) )==0 ]
# print(' Intersection of the test_nr with every element of the list yields :\n', INTERSECTION )




print()
PART = []
for i in partitions(9):
    if 1 < len(i) <= 5 :
        Prt = tuple(i[::-1])
        if Prt < (6,) :
            print(Prt)
            PART.append(Prt)

print('\n',PART,'\n')

primes = primesieve(10**5)
D ={}                   # We separate length of primes in a dictionary
for p in primes :
    l = len(str(p))
    if l not in D :
        D[l]=set([])
        if len(str(p)) == len(set (str(p)) ) :
            if str(p).count('0') == 0 :
                D[l].add(p)
    else :
        if len(str(p)) == len(set (str(p)) ) :
            if str(p).count('0') == 0 :
                D[l].add(p)


print(D)
DI = copy.deepcopy(D)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n----------------------------')
t1  = time.time()

P = set( [i for i in range(1,10)] )
W=set()
#                     W.add(''.join(str(i)for i in SET))
itr, cnt, scnt= 0, 0, 1
T = ( 3, 2, 2, 2 )

# i = 1
# while i < len(T) :
L1 = D[T[0]]
print(L1)
for p1 in L1 :
    set_p1 = set([int(a) for a in str(p1)])
    L2 = list(D[T[1]])
    I = [ s for s in L2 if len(set_p1 & set([int(a) for a in str(s)]) )==0 ]
    # print(p1, I)
    for p2 in I :
        SET1 = {p1, p2}
        # print(SET1, )
        SET1={}
        if len(T) >2 :
            SET1 = {p1, p2}
            L3 = list(D[T[2]])
            set_p1p2 = set([int(i) for i in ''.join( str(i) for i in  SET1 )])
            I1 = [ s for s in L3 if len(set_p1p2 & set([int(a) for a in str(s)]) )==0 ]
            # print(L3, set_p1p2, I1 )
            for p3 in I1 :
                SET2= {p1, p2, p3}
                # print(SET2)
                SET2 = {}
                if len(T) > 3 :
                    SET3= {p1, p2, p3}
                    L4 = list(D[T[3]])
                    set_p1p2p3 = set([int(i) for i in ''.join( str(i) for i in  SET3 )])
                    I2 = [ s for s in L3 if len(set_p1p2p3 & set([int(a) for a in str(s)]) )==0 ]
                    # print(L4, set_p1p2p3, I2)
                    for p4 in I2 :
                        SET3 = {p1, p2, p3, p4}
                        print(SET3)
                        SET3 = {}

                        if len(T) > 4 :
                            SET4= {p1, p2, p3, p4}
                            L5 = list(D[T[4]])
                            set_p1p2p3p4 = set([int(i) for i in ''.join( str(i) for i in  SET4 )])
                            I3 = [ s for s in L3 if len(set_p1p2p3p4 & set([int(a) for a in str(s)]) )==0 ]
                            # print(L5, set_p1p2p3p4, I3)



@ 2017 -01-19 I can do it with recursion,

while len('.join(str(i)for i in SET)) < 9 :

    until we have all the numbers
    I can reproduce all
    i++



    # i+=1






#
# # while len(DI[T[0]]) > 0 :
# for p1 in D[T[0]] :
#     # p1= list(DI[T[0]])[0]
#     # D[T[0]].remove(p1)
#     A= set(list(int(p1) for p1 in str(p1)))
#     B = P - A
#     print(p1, A, B)
#     scnt+=1
#     C = B
#     # for i in range(1, 2 ) :        # len(T)
#     SET = set([p1])
#     comb = list(combinations(C, T[1] ))          # 2-nd element !!!!!!!
#
#     # print(comb)
#     Z = []
#
#     for j in comb :
#         perm = [ int(''.join([str(k) for k in s ])) for s in  list(permutations(j)) ]
#         Z.extend(perm)
#         # print('Z : ',Z,'    ' ,SET)
#         for p2 in Z :
#             C = B
#             if p2 in D[T[1]]:
#                 # D[T[0]].remove(p2)
#                 SET.add(p2)
#                 A = set(list(int(p2) for p2 in str(p2)))
#                 C = set(C) - A
#                 # print('A    C    SET :   ' ,A, C  ,SET)
#                 if len(T) == 2 :
#                     cnt+=1
#                     print(str(cnt)+'.       ',SET)
#                     W.add(''.join(str(i)for i in SET))
#                 SET = set([p1])     ## We set back the set to have only the first element
#
#
#                 if len(T) > 2 :                     # 3-rd element !!!!
#                     SET = set([p1,p2])
#                     Y=[]
#                     comb2 = list(combinations(C, T[2]))
#                     # print(' 3-rd term :    ',comb2)
#                     for l in comb2 :
#                         perm2 = [ int(''.join([str(k) for k in s ])) for s in  list(permutations(l)) ]
#                         Y.extend(perm2)
#                     # print(' Y   SET  C   ' ,Y, SET, C)
#                     for p3 in Y :
#                         F = C
#                         if p3 in D[T[2]] :
#                             SET.add((p3))
#                             E = set( list(int(p3) for p3 in str(p3)) )
#                             F = C - E
#                             # print(' Y   SET  C   ' ,Y, SET, F )
#                             if len(T) == 3 :
#                                 cnt+=1
#                                 print(str(cnt)+'.       ',SET)
#                                 W.add(''.join(str(i)for i in SET))
#                             SET = set([p1, p2])                # reset the set
#
#
#                             if len(T) > 3 :                     # 4-th element !!!!!
#                                 SET = set([p1,p2,p3])
#                                 X=[]
#                                 comb3 = list(combinations(F, T[3]))
#                                 # print(' 4-th term :    ',comb2 , F)
#                                 for m in comb3 :
#                                     perm3 = [ int(''.join([str(k) for k in s ])) for s in  list(permutations(m)) ]
#                                     X.extend(perm3)
#                                 # print(' X   SET  F   ' ,X, SET, F)
#                                 for p4 in X :
#                                     G = F
#                                     if p4 in D[T[3]] :
#                                         SET.add((p4))
#                                         H = set( list(int(p4) for p4 in str(p4)) )
#                                         G = F - H
#                                         # print(' X   SET  G   ' ,X, SET, G )
#                                         if len(T) == 3 :
#                                             cnt+=1
#                                             print(str(cnt)+'.       ',SET)
#                                             W.add(''.join(str(i)for i in SET))
#                                         SET=set([p1, p2, p3])
#
#
#                                         if len(T) > 4 :         # 5-th element !!!!!!!!!!
#                                             SET=set([p1, p2, p3, p4])
#                                             if list(G)[0] in D[T[4]]:       # check if it is prime
#                                                 SET.add( list(G)[0])
#                                                 cnt+=1
#                                                 print(str(cnt)+'.       ',SET)
#                                                 W.add(''.join(str(i)for i in SET))











# print('\n Length of the SETS : ', len(W),'\n',W)












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
