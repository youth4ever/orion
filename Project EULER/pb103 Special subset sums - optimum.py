#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Fri, 6 Jan 2017, 16:22
#The  Euler Project  https://projecteuler.net
'''
Special subset sums: optimum        -           Problem 103

Let S(A) represent the sum of elements in set A of size n.
We shall call it a special sum set if for any two non-empty disjoint subsets, B and C, the following properties are true:

1.      S(B) ≠ S(C); that is, sums of subsets cannot be equal.
2.      If B contains more elements than C then S(B) > S(C).

If S(A) is minimised for a given n, we shall call it an optimum special sum set. The first five optimum special sum sets are given below.

                                                n = 1: {1}
                                                n = 2: {1, 2}
                                                n = 3: {2, 3, 4}
                                                n = 4: {3, 5, 6, 7}
                                                n = 5: {6, 9, 11, 12, 13}

                                                n = 6 : {11, 18, 19, 20, 22, 25}

It seems that for a given optimum set, A = {a1, a2, ... , an}, the next optimum set is of the form B = {b, a1+b, a2+b, ... ,an+b},
where b is the "middle" element on the previous row.

By applying this "rule" we would expect the optimum set for n = 6 to be A = {11, 17, 20, 22, 23, 24}, with S(A) = 117.
However, this is not the optimum set, as we have merely applied an algorithm to provide a near optimum set.
The optimum set for n = 6 is A = {11, 18, 19, 20, 22, 25}, with S(A) = 115 and corresponding set string: 111819202225.

Given that A is an optimum special sum set for n = 7, find its set string.

NOTE: This problem is related to Problem 105 and Problem 106.


'''
import time
from itertools import combinations, permutations, combinations_with_replacement
import itertools
from operator import itemgetter

def unique_permutations(lst):       # VERY EFFECTIVE
    ''':Description: Takes a list and makes ONLY Unique Permutations of a list with repeated elements.
        If one tries itertools.permutations on a list with 14 elements ==> BANG, computer freezes
    :param lst: type list
    :return:    a list of lists containing all the permutations
    '''
    if len(lst) == 1:
        yield (lst[0],)
    else:
        unique_lst = set(lst)
        for first_element in unique_lst:
            remaining_lst = list(lst)
            remaining_lst.remove(first_element)
            for sub_permutation in unique_permutations(remaining_lst):
                yield (first_element,) + sub_permutation


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


one = {1:1}
A = set([11, 17, 20, 22, 23, 24])
seven = set([22]) |  set([ 22+i for i in sorted(A)])
print(A)
print('sevens :\t',sorted(seven))

Tt = [  11, 17, 20, 21, 22, 24 ]

# print(list(combinations(Tt, 2)) )


print('\n----------- Finding consecutive numbers in a list -----------------')

L = set([ 12, 13, 14, 15, 18, 19 ])
def consecutive_terms( lst) :
# Find runs of consecutive numbers using groupby.  The key to the solution
# is differencing with a range so that consecutive numbers all appear in
# same group.
    R =[]
    for k, g in itertools.groupby( enumerate(L), lambda x: x[1]-x[0] ) :
        lst = list(map(itemgetter(1),g ))
        if len(lst) > 1 :
            R.append(lst)
    return R

print('consecutive_terms Function Test : ',consecutive_terms(L) )

print('\n------- How many Equal SubSets -----------')


Tt = [39, 59, 70, 77, 78, 79, 81, 84]
cnt , scnt = 0, 0
l = len(Tt)
if l%2 == 0 : r = l//2
if l%2 == 1 : r = l//2+1
print(l, l//2, r, sum(Tt))
for i in range(1, r+1):
    c1 = list(combinations(Tt, i))
    for i2 in c1 :
        T2 = set(Tt)-set(i2)
        for j in range(i, i+2):
            c2 = list(combinations(T2, j))
#             print(i,j, end=' ;  ' )
            for j2 in c2 :
                cnt+=1
                # print( str(cnt)+'.   ' ,i2, '  ; ',j2, '    ', sum(Tt))
                if sum(i2) == sum(j2) :
                    scnt+=1
                    print(str(scnt)+ '.   False : ', i2, j2, '      ', Tt, sum(Tt))
                if len(j2) > len(i2)   :
                    if sum(j2) < sum(i2):
                        print('False')
                if len(j2) < len(i2)   :
                    if sum(j2) > sum(i2):
                        print('False')

print('\n-------- Function Building -------------')

# my_list = [ 1, 2, 3, 4, 5, 6 ]
# my_list = [ 11, 17, 23, 24, 25, 26 ]
# my_set = set([11, 17, 20, 22, 23, 24])
my_set = set([624,596,391,605,529,610,607,568,604,603,453])
print(my_set,'\n')

def modify_set(my_set) :
    cnt , scnt = 0, 0
    for i in range(2, 4):
        c1 = list(combinations(my_set, i))
        for i2 in c1 :
            T2 = set(my_set)-set(i2)
            for j in range(1, i+2):
                c2 = list(combinations(T2, j))
                for j2 in c2 :
                    if sum(i2) == sum(j2) :
                        m = min( set(i2) | set(j2) )
                        print('   ' ,i2, '  ; ',j2,'   ',m ,'    ', sum(my_set))
                        if m+1 not in my_set :
                            my_set.remove(m)
                            my_set.add(m+1)
                            return set(sorted(list(my_set)))
                        elif m+1 in my_set :
                            R = consecutive_terms(my_set)
                            print(R, my_set)
                            for l in R :
                                if m in l :
                                    L = l
                                    plus1 = [i+1 for i in L]
                                    my_set = my_set - set(L)
                                    my_set.update(plus1)
                                    my_set = set(sorted(list(my_set)))
                                    print(m ,L , plus1, my_set)
                                    return my_set
    return True

# print('\nFunction modify_set Test : \t', modify_set(my_set),'\n' )
# print('\nFunction modify_set Test : \t', modify_set(my_set),'\n' )
# print('\nFunction modify_set Test : \t', modify_set(my_set),'\n' )
# print('\nFunction modify_set Test : \t', modify_set(my_set),'\n' )
# print('\nFunction modify_set Test : \t', modify_set(my_set),'\n' )
# print('\nFunction modify_set Test : \t', modify_set(my_set),'\n' )

# while modify_set(my_set) != True :
#     modify_set(my_set)
#     print('whike:\t',modify_set(my_set))

def check_subset(my_set) :
    l = len(my_set)
    if l%2 == 0 : r = l//2
    if l%2 == 1 : r = l//2+1
    cnt , scnt = 0, 0
    for i in range(1, r+1):
        c1 = list(combinations(my_set, i))
        for i2 in c1 :
            T2 = set(my_set)-set(i2)
            for j in range(i, i+2):
                c2 = list(combinations(T2, j))
                for j2 in c2 :
                    if sum(i2) == sum(j2) :
                        cnt+=1
                        # print(str(cnt)+'.  ' ,i2, j2, sum(i2))
                        return False
                    if len(j2) > len(i2)   :
                        if sum(j2) < sum(i2):
                            return False
                    if len(j2) < len(i2)   :
                        if sum(j2) > sum(i2):
                            return False

    return True

print('\nFunction check_subset Test : \t', check_subset(my_set),'\n' )

print('\n================  My Initial SOLUTION, Brute Force  ===============\n')

t1  = time.time()

def brute_force() :
    min_sum, itr = 1000, 0
    for a in range(19, 19+5):          # for a in range(19, 19+15):
        for b in range(a+10, a+15):
            for c in range(b+5, b+10) :
                for d in range(c+1, c+2) :
                    for e in range(d+1, d+2) :
                        for f in range(e+1, e+9) :
                            for g in range(f+1, f+10) :
                                S = { a, b, c, d, e, f, g }
                                itr += 1
                                if check_subset(S) == True :
                                    print(str(itr)  ,sorted(S),'   ' , ''.join([str(i) for i in sorted(S)]), '       ', sum(S)  )
                                    if min_sum > sum(S):
                                        min_sum = sum(S)
                                        print(sorted(S),'   ' , ''.join([str(i) for i in sorted(S)]) ,'   '  ,min_sum)
                                        s1, s2, s3 = min_sum, sorted(S), ''.join([str(i) for i in sorted(S)])
                                if itr %10**5 == 0 :
                                    print('----  '+str(itr)+'  ----')
    return print('\nAnswer:\t', s1, '   ',s2,'   ', s3 )

# brute_force()

t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')            # Completed in : 4.253243 s

#           [30, 37, 44, 47, 49, 50, 58]     37444749505830     315
#           [34, 39, 42, 44, 46, 50, 61]     34394244465061     316
#           [34, 39, 40, 44, 46, 48, 62]     34394044464862     313
#            [20, 31, 38, 39, 40, 42, 45]     38394042452031     255

#            [39, 60, 71, 78, 79, 80, 82, 85] 574      3960717879808285     21
#            [40, 61, 72, 79, 80, 81, 83, 86] 582      4061727980818386


#             [39, 62, 73, 80, 81, 82, 84, 87] 588      3962738081828487        29
#            [40, 63, 74, 81, 82, 83, 85, 88] 596      4063748182838588
#           [41, 64, 75, 82, 83, 84, 86, 89] 604      4164758283848689
#            [42, 65, 76, 83, 84, 85, 87, 90] 612      4265768384858790
#               39, 68, 79, 86, 87, 88, 90, 93] 630      3968798687889093
#               [40, 69, 80, 87, 88, 89, 91, 94] 638      4069808788899194
#                [41, 70, 81, 88, 89, 90, 92, 95] 646      4170818889909295



#            81, 120, 143, 154, 161, 162, 163, 165, 168] 1317      81120143154161162163165168       39
#            [82, 121, 144, 155, 162, 163, 164, 166, 169] 1326      82121144155162163164166169
#            [83, 122, 145, 156, 163, 164, 165, 167, 170] 1335      83122145156163164165167170
#            [79, 118, 139, 150, 157, 158, 159, 161, 164] 1285      79118139150157158159161164
#            [80, 119, 140, 151, 158, 159, 160, 162, 165] 1294      80119140151158159160162165


#           [81, 122, 145, 156, 163, 164, 165, 167, 170] 1333       41
#             [82, 123, 146, 157, 164, 165, 166, 168, 171] 1342
#                [83, 124, 147, 158, 165, 166, 167, 169, 172] 1351
#                [81, 124, 147, 158, 165, 166, 167, 169, 172] 1349
#           [82, 125, 148, 159, 166, 167, 168, 170, 173] 1358
#        [83, 126, 149, 160, 167, 168, 169, 171, 174] 1367
#       [84, 127, 150, 161, 168, 169, 170, 172, 175] 1376

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

p = [ 11, 7, 1, 1, 2, 3 ]        #   11 13 17 19 23 29 31 33 37 41 43 47
print(  len(list(unique_permutations(p)))  ,list(unique_permutations(p)),'\n')

def solution_pb103():
    min_sum, Sp = 1000, []
    # P = list(unique_permutations(p))
    for a in range(15, 30):
        # for i in range(len(P)) :
        S, s =[a], a
        for i in p :
            # for j in P[i] :
            s+= i
            S.append(s)
            #     s+=j
            #     S.append(s)
        # print(S, p)
        S =  sorted(set(S ))

        # if check_subset( S ) == True :
        if isSpecialSumSet( S ) == True :
            print( S ,'   ' ,sum(S) , '    ', "".join( [str(i) for i in S] ) )
            if min_sum > sum(S):
                min_sum, Sp, S2 = sum(S) , "".join([str(i) for i in S]), S
        # print(str(a)+'.   ')

    return print('\nAnswer : ', Sp,'     ', min_sum, '    ', S2 )

solution_pb103()        #       Answer :  20313839404245       255      [20, 31, 38, 39, 40, 42, 45]

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')          #   Completed in : 33.0019 ms


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,   --------------------------')
t1  = time.time()

# ==== Sat, 26 Nov 2016, 08:15, mbh038, England
# I have been all around the houses with this one, and have come to it after solving 105 and 106.
# In the process I wrote a very neat solution to 106, which turned out to be of little use here!
# In the end, I constructed strictly increasing sets {a.....g}, with the ranges chosen such that ∑a,b,c,d>∑e,f,g∑
# so that rule 2 is necessarily met, then tested each candidate for compliance with rule 1.
# If I judiciously choose the allowed ranges of values of a.....ga.....g I find a solution in about 0.8 s.
# The first solution is necessarily the optimal solution.
# I played a bit with trying algebraically to better tie down the set element ranges,
# but in the end just looked at the valid n=7 solutions from the file that goes with p105 and guessed from those.
# If I use riffraff11235's really rather good  isSpecialSumSet() function instead of my rule 1 tester,
# the time comes down to about 0.3 s.


import itertools as it

def p103():
    t=time.clock()
    for A in ((a,b,c,d,e,f,g) for a in range(20,30) for b in range(a+1,45)
        for c in range(b+1,45) for d in range(c+1,50) for e in range(d+1,50)
            for f in range(e+1,50) for g in range(f+1,60 ) if a+b+c+d>e+f+g):
        if rule1(A):
            print (A,sum(A),time.clock()-t)
            return ''.join([str(x) for x in A])

    print("No special sum set found")

def rule1(L):
    powerset=[[x for x in it.compress(L,binLst)] for binLst in it.product([0,1],
              repeat=len(L)) if sum (binLst) in range(2,len(L)//2+1)]
    powersum=[sum(x) for x in powerset]
    return len(set(powersum))==len(powerset)

#riffraff11235 wrote this
def isSpecialSumSet(s):
    uSet = set(s)
    for i in range(2,len(s)):
        maxSet = max(uSet)
        for a in it.combinations(s, i):
            ss = sum(a)
            if ss <= maxSet or ss in uSet: return False
            else: uSet.add(ss)
    return True

# p103()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()

import itertools

def check (s):
    ss = [ list (itertools.combinations (s, i)) for i in range (1, len (s)+1) ]
    sum_ss = [ [ sum (y) for y in x ] for x in ss ]
    for i in range (len (ss)):
        if len (set (sum_ss[i])) != len (sum_ss[i]):
            return False
    for i in range (len (sum_ss)-1):
        if max (sum_ss[i]) >= min (sum_ss[i+1]):
            return False
    return True

def rcheck (s, d, c, e=2):
    if d == len (s):
        return [c] if check (c) else []
    t = []
    for i in range (-e, e, 1):
        if s[d] + i > c[-1]:
            r = rcheck (s, d+1, c + [s[d] + i])
            t = t + r if r != [] else t
    return t

base = [ 20, 33, 40, 41, 42, 44, 47 ] # first guess
rc = rcheck (base, 1, [base[0]])
print (''.join (str (y) for y in sorted (rc, key=lambda x: sum (x))[0]))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,   --------------------------')
t1  = time.time()

from itertools import combinations

def isSpeciaSumSet(s):
    uSet = set(s)
    for i in range(2,len(s)):
        maxSet = max(uSet)
        for a in combinations(s, i):
            ss = sum(a)
            if ss <= maxSet or ss in uSet: return False
            else: uSet.add(ss)
    return True

def problem103():
    for a in range(20,23):
        for b in range(30,35):
            for c in range(b,40):
                for d in range(c,44):
                    for e in range(d,45):
                        for f in range(e,46):
                            for g in range(f,47):
                                if isSpeciaSumSet([a,b,c,d,e,f,g]):
                                    return (a,b,c,d,e,f,g)

print (problem103())

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n---------BENCHMARK TESTING --------------')

TEST = [81, 124, 146, 157, 164, 165, 166, 168, 171]

##### MY FUNCTION
t1  = time.time()

print( check_subset(TEST) )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

#### Second FUNCTION

t1  = time.time()

print( isSpecialSumSet(TEST) )

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
