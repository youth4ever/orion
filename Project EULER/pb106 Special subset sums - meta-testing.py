#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Sat, 7 Jan 2017, 21:54
#The  Euler Project  https://projecteuler.net
'''
Special subset sums: testing        -       Problem 105

Let S(A) represent the sum of elements in set A of size n.
We shall call it a special sum set if for any two non-empty disjoint subsets, B and C, the following properties are true:

1.      S(B) ≠ S(C); that is, sums of subsets cannot be equal.
2.      If B contains more elements than C then S(B) > S(C).

For this problem we shall assume that a given set contains n strictly increasing elements and it already satisfies the second rule.

Surprisingly, out of the 25 possible subset pairs that can be obtained from a set for which n = 4,
only 1 of these pairs need to be tested for equality (first rule).

Similarly, when n = 7, only 70 out of the 966 subset pairs need to be tested.

For n = 12, how many of the 261625 subset pairs that can be obtained need to be tested for equality?

NOTE: This problem is related to Problem 103 and Problem 105.

'''
import time
from itertools import combinations


def isSpecialSumSet(s):
    uSet = set(s)
    for i in range(2,len(s)):
        maxSet = max(uSet)
        for a in combinations(s, i):
            ss = sum(a)
            if ss <= maxSet or ss in uSet: return False
            else: uSet.add(ss)
    return True


print('\n--------------------------TESTS------------------------------')
t1  = time.time()




t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')         # Completed in : 226.013184 ms

# === GENERAL IDEAS ===
# https://en.wikipedia.org/wiki/Catalan_number

print('\n================  My FIRST SOLUTION, Using Sets ===============\n')
t1  = time.time()


def first_solution(n=7) :
    T = list(range(14, 14+n ))
    cnt , scnt = 0, 0
    l = len(T)//2
    print(T, ';\tLength :',len(T), '\nSet Pair Max Size :',l, ';    Sum: ' ,sum(T), '\n')

    for i in range(2 , l+1):
        Comb = list(combinations( [ e for e in range(1,2*i+1) ], i ))
        C=[]
        for m in range(len(Comb)//2):
            C.append((Comb[m], Comb[-m-1]))
        # print(len(C), C)
        X = list(combinations(T, 2*i))
        for h in range(len(X)) :
            D = {e : e for e in range(1, 2*i+1)}
            Q = dict(zip( D.keys(), X[h] ))
            # print( X ,'    ' , Q, '   ',D,'\n' ,C)
            for o in range(len(C)):
                # print(C[o])
                O1, O2 = [Q[g] for g in C[o][0]], [Q[g] for g in C[o][1]]
                itr = 0
                for k in range(len(O1)):
                    if O1[k] <O2[k] : itr +=1
                if itr < len(O1) :
                    scnt+=1
                    # print(str(scnt)+'.   ', C[o][0], C[o][1], '         ' , O1, '  ',O2, '  ',sum(O1), sum(O2) )
    return print('\nAnswer : \t', scnt )

first_solution(12)      #           Answer : 	 21384

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n======  My SECOND SOLUTION, Using Catalan Numbers & Combinatorics from Internet  ====\n')
t1  = time.time()

# Here we use the Combinatorics formula  : Found on the internet on the  :
# www.mathblog.dk/project-euler-106-minimum-comparisons-special-sum-sets/
# X(n,s) = (1/2 *C{n,s} * C{n-s,s} ) - ( 1/(s+1) * C{s,2s} * C{2s, n} )

from gmpy2 import comb

print(comb(7,3))

def using_Catalan_numbers(n=7):
    m = n//2
    f = 0
    for s in range(2, m+1) :
        f += ( (1/2) * comb(n, s) * comb(n-s, s) ) - ( (1/(s+1)) * comb( 2*s ,s) * comb(n , 2*s ) )
        # print(f)
    return print('\nAnswer : \t', int(f) )

using_Catalan_numbers(12)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')





print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,   --------------------------')
t1  = time.time()

# ==== Thu, 24 Nov 2016, 12:23, mbh038, England
# About 1.1 s in Python, and three dead puppies.
# Given that nn is a strictly increasing set of integers that satisfies rule 2, we only need to compare disjoint subsets of the same size,
# from 2 to 6 if nn has 12 elements, since none of the elements are equal and no two subsets of size 7 or more can be disjoint.
# Further, if the index in nn of every element in one subset of a pair to be compared is less than the index in n of the
# corresponding element in the other subset, then the sums of  the two subsets cannot be equal,
# so we do not need to compare these two subsets..
# There must be faster ways to do this...

import itertools as it



def p106(L):
    pset = [[x for x in it.compress(L, binLst)] for binLst in it.product([0,1], repeat=len(L)) ]
    p=[x for x in pset if len(x)<=len(L)//2]
    q={size:[x for x in p if len(x)==size] for size in range(2,len(L)//2+1)}
    count=0
    for size,sets in q.items():
        for i in range(len(sets)):
            for j in range(i+1,len(sets)):
                if set(sets[i]).intersection(set(sets[j]))==set():
                    if not all(sets[i][x]>sets[j][x] for x in range(len(sets[i]))):
                        count+=1
    print (count)

# p106(list(range(12)))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()

# ======  Fri, 15 Feb 2013, 13:09, tom.wheldon, England
# Thought about trying to derive a closed form solution, but decided it was simpler just to count.  Runs in ~330ms.

from itertools import combinations

count = 0
for i in range(2,7):
    subsets = list(combinations(range(12),i))
    for subset1 in subsets:
        complement = list(range(12))
        [complement.remove(x) for x in subset1]
        disjoints = list(combinations(complement,i))
        for subset2 in disjoints:
            diff = list(map(lambda x, y: x-y if x>y else 0, subset1,subset2))
            if any(diff) and not all(diff):
                count += 1
print(count//2)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,   --------------------------')
t1  = time.time()

===== Sat, 23 Mar 2013, 20:19, joente, NEtherlands

from itertools import combinations

def problem106(limit = 12):
    t, s = 0, [i for i in range(limit)]
    for a in range(2, limit//2 + 1):
        for c in combinations(s,a):
            for d in combinations(filter(lambda x: x not in c, s),a):
                if c[0] < d[0]:
                    for i in range(1,a):
                        if c[i] > d[i]:
                            t+=1
                            break
    return print(t)

problem106()

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
