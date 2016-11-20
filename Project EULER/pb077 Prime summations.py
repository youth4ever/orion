#!/usr/bin/python3
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
                            Prime summations    -       Problem 77
It is possible to write ten as the sum of primes in exactly five different ways:

                                                        7 + 3
                                                        5 + 5
                                                        5 + 3 + 2
                                                        3 + 3 + 2 + 2
                                                        2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five thousand different ways?
'''
import time

# 2016-11-07 : Obviously this problem needs an partition algorithm but using sieve of primes instead of consecutive numbers or
# list of value of coins

# This problem will be good for solving 155, therefore I need an algorithm to make the decomposition of partirtion numbers


print('--------------------- TESTS TO DECOMPOSE A NUMBER -----------------------------')
print('Not related to this problem, but with problem 155')
n=4

partitions = [1] +  [0]* n
print(partitions)
cons = [i for i in range(1,n+1)]
print(cons)

for i in cons:
    for j in range (i, n+1):
        #print(i, j , partitions)
        partitions[j] +=  partitions[j - i]
        print(partitions)

print(partitions[-1])





print('--------------------- MY SOLUTION -----------------------------')
t1  = time.time()

def sieve(lower, upper_bound):         # THE FASTEST  SIEVE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    ''' SIEVE OF ERATOSTHENES Algorithm  , THE FASTEST  SIEVE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'''
    n = upper_bound + 1
    check = [True] * n
    check[0] = check[1] = False
    for i in range(2, int(upper_bound**0.5) + 1):
        if check[i]:
            for j in range(i**2, upper_bound + 1, i):
                check[j] = False
    primes = [i for i, flag in enumerate(check) if flag and i > lower ]
    return primes


def prime_partition(n):
    partitions = [1] +  [0]* n
    primes = sieve(1,n)
    print(primes)
    for i in primes:
        for j in range (i, n+1):
            # print(i, j , partitions)
            partitions[j] +=  partitions[j - i]
    return partitions[-1]

print('\nAnswer: ',prime_partition(71))                   #   Answer : 71

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

# print('\n--------------------- MY SECOND SOLUTION -----------------------------')
#
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')





print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1, pe_dilantha, Sri Lanka  --------------------------')
t1  = time.time()

def is_prime(n):
    if n < 2:
        return 0
    elif n == 2:
        return 1
    else:
        i = 2
        while i < int(n ** 0.5) + 1:
            if n % i == 0:
                return 0
            i += 1
        return 1

def P(n):
    primes = [k for k in range(n) if is_prime(k)]
    cnt = [0] * (n + 1)
    cnt[0] = 1
    for l in primes:
        for j in range(l, n + 1):
            cnt[j] += cnt[j - l]
    return cnt[n]

n = 1
while 1:
    if P(n) > 5000:
        print(n)
        break
    n += 1


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 2, vidoor, Hungary  --------------------------')
t1  = time.time()

# I thought at first, I have no time for a complicated algo that produces partitions.
# One and a half day later, I wrote this simple code to count partitions
#  and solved 3 problems (#76 and #31, too). Runs in 20ms.
# I really appriciate the expressive power of Python.

def list_partition_fn(maxn = 100, avalue_list = [1]):
    if len(avalue_list) < 2:
        avalue_list = list(range(1,maxn+1))
    tmplist = [1] + [0]*maxn
    for tmpval in avalue_list:
        for j in range(maxn+1-tmpval):
            tmplist[j+tmpval] += tmplist[j]
        #print(tmpval,  tmplist)
    return tmplist

plist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
print([pq for pq in enumerate(list_partition_fn(100,plist)) if pq[1] > 5000])

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 3, Oleg78, Russia  --------------------------')
t1  = time.time()

target = 5000
limit = 100
answer = 0
s = bytearray(limit)
primes = [2]
for i in range(3, limit, 2):
    if s[i] == 0:
        primes.append(i)
        for j in range(i*i, limit, 2*i):
            s[j] = 1
ways = [1 - (i & 1) for i in range(limit)]
for p in primes[1:]:
    for t in range(p, limit):
        ways[t] += ways[t - p]
for p in primes:
    ways[p] -= 1
answer = min(n for n in range(limit) if ways[n] > target)

print(answer, ways[answer])

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 4, zedyang, China  --------------------------')
t1  = time.time()

ways = [0 for i in range(0,101)]
ways[0]=1
for factor in primes:
    for i in range(0,101):
        if i-factor<0:
            pass
        else:
            ways[i] += ways[i-factor]
print ('Found',ways.index(next(x for x in ways if x>5000)) )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 5, gardener, France  --------------------------')
t1  = time.time()

# Les pkpk denotes the k-th prime (indexed from 0, computed with Eratosthenes sieve), and Rn,k
# the number of partitions of n with the k first primes. (I assume that R_(p_k,k)=1).
# Starting with the values R_(0,k)=1 ,  R_(2n,0) = 1 and R_(2n+1,0)=0, and using the relation
# R_(n,k)=R_(n,k−1) + R_(n−p_k,k)    (if n−p_k≥0), it is very easy.
#
# To get the answer, one has to stop as soon as some R_(n,k)≥5000 (or 5001 if n is prime).
# However, the computation can be made much farther:
# I find 3317888141922874534182824365438447261270459230975889 possibilities for writing 9999 as sum of primes.

N=100
T=[True]*N
T[0],T[1]=False,False
for i in range(2,N):
    if T[i]:
        for j in range(i*i,N,i):
            T[j]=False
primes=[x for x in range(N) if T[x]]
P=len(primes)
R=[[0]*P for i in range(N)]
for k in range(P):
    R[0][k]=1
for n in range(0,N,2):
    R[n][0]=1
for n in range(2,N):
    for k in range(1,P):
        R[n][k]=R[n][k-1]
        if primes[k]<=n:
            R[n][k]+=R[n-primes[k]][k]
    if R[n][-1]>=5000 and not T[n] or R[n][-1]>=5001:
        print(n)
        break

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6, aolea, Spain  --------------------------')
t1  = time.time()


import pyprimes

def P077(n,m,primes077):
    if n<0 or m<= 0:
        return 0
    if n == 0:
        return 1
    return P077(n,m-1,primes077) + P077(n-primes077[m-1],m,primes077)

n = 10
numWays = 5
while numWays < 5000 :
    n = n + 1
    m = 0
    primes077 = []
    for i in pyprimes.primes_below(n):
        primes077.append(i)
    m = len(primes077)
    numWays = P077(n,m,primes077)
    print(n,numWays)
print(n,numWays)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



