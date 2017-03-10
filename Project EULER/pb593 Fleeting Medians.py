#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @     Completed on Sun, 5 Mar 2017, 05:13
#The  Euler Project  https://projecteuler.net
'''
Fleeting Medians            -       Problem 593
We define two sequences S={S(1),S(2),...,S(n)}S={S(1),S(2),...,S(n)}
and S2={S2(1),S2(2),...,S2(n)}S2={S2(1),S2(2),...,S2(n)}:

S(k)=(p_k)**k mod 10007    where p_k is the k-th prime number.

S2(k)=S(k)+S(⌊k10000⌋+1) where ⌊⋅⌋ denotes the floor function.

Then let M(i,j)  be the median of elements S2(i)  through S2(j), inclusive.
For example, M(1,10)=2021.5 and M(102,103)=4715.0.

Let F(n,k)=∑{n−k+1, i=1} = M (i, i+k−1)

For example, F(100,10)=463628.5
and F(10**5,10**4)=675348207.5

Find F(10**7,10**5)F(10**7,10**5).
If the sum is not an integer, use .5.5 to denote a half. Otherwise, use .0.0 instead.


'''
import time, math
import gmpy2
import numpy as np

def prime_sieve(n):       # SECOND FASTEST        o(^_^)o
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[ i*i :: 2*i ] = [False] * ( (n-i*i-1) // (2*i) +1 )
    return [2] + [i for i in range(3, n , 2) if sieve[i] ]


def numpy_prime_sieve(n):          ### o(^_^)o  FASTEST  o(^_^)o  ###  Highly Efficient !!!
    import numpy as np
    """return array of primes 2<=p<=n"""
    sieve=np.ones( n+1, dtype=bool )
    for i in range( 2, int((n+1)**0.5+1) ) :
        if sieve[i] :
            sieve[2*i :: i] = False
    return np.nonzero(sieve)[0][2:]

t1  = time.time()




# primes up to 2.2*10**9 - there are   107540122                     Completed in : 43 sec



lim = 10**6             ### !!!!!!!!!!!!!!

primes = numpy_prime_sieve(int( lim * math.log(lim)*1.2 ) )
print(len(primes), primes[:50]  )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

# cnt = 5761455
# pr = 10**8
# while cnt <= LIM+1 :
#     pr = gmpy2.next_prime(pr)
#     primes = np.append(primes, pr )
#     cnt+=1
#     if cnt % 10**6 == 0 : print(cnt)

print('All the primes were added to the primes sieve\n')


def S(k, primes):
    p_k = primes[k-1]
    # print(primes[k-1], type(primes[k-1]) )
    return pow( int(p_k), int(k), 10007)


def S2(k, primes) :
    # return S(int(k), primes ) + S( math.floor(int(k)/10000)+1 , primes  )
    return S(int(k), primes ) + S( int(k)//10000+1 , primes  )
# S2_sieve = {    }
# for k in range(1, 10**5+1  ) :
#     S2_sieve[k] = S2(k)
#     if k%10**6 ==0 : print(k)

t1  = time.time()

### Here we build the s2_sieve
S2_sieve = np.array([  S2(k, primes) for k in range(1, lim+1  ) ])

print('\nS2_sieve was built ....\n')

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

def M(i, j) :
    L = np.array([ S2_sieve[h-1] for h in range(i, j+1) ])
    # print(L)
    # L = np.array([ S2_sieve[h] for h in range(i, j+1) ])
    # print('numpy median ' ,np.median(L) )
    # L.sort()
    # if len(L) %2 == 0 :
    #     # print(len(L)//2-1 , len(L)//2 )
    #     e1, e2 =  L[len(L)//2-1] ,  L[len(L)//2]
    #     return (e1+e2)/2
    #
    # if len( L )%2 == 1 :
    #     e = L[ len(L)//2 ]
    #     return e
    return np.median(L)


def F(n, k, S2_sieve):
    SUM = 0
    L = np.array([ S2_sieve[h-1] for h in range(1, k+1) ])
    # print(L)
    SUM += np.median(L)
    # print( str(k)+'.      ', np.median(L) )
    for i in range(2, n-k+2 ) :
        L = np.delete(L, 0)
        L = np.append(L, S2_sieve[i+k-2] )
        med = np.median(L)
        print(str(i)+'.      ' , med, len(L), L )
        SUM += med
        if (i+k-1) % 10**5 == 0 :
            # print(str(i+k-1)+'.     ' , med , '     '  )
    return SUM


# def F1(n, k):
#     SUM = 0
#     for i in range(1, n-k+2 ) :
#         SUM += M(i, i+k-1)
#         print(str(i+k-1)+'.     ' ,M(i, i+k-1)  )
#     return SUM

print(' M(1, 10) test  :\t', M(1, 10))

# print( '\n S2 test : \t', S2(2), S2(10) )

print('\nM(10**2, 10**3) test : ', M(10**2, 10**3),'\n\n')

print('\n---------------------------')
# print('\nF(100, 10) test : ', F1(100, 10) )

print('\nF(100, 10) test : ', F(100, 10, S2_sieve) )


print('\n--------------------------TESTS------------------------------')
t1  = time.time()



# @2017-03-04 22:30  Basically this problem is solved. BUT PYTHON is OVERPOWERED.
# Not solves even the last example # in reasonable amount of time.

# print('\nF(10**5, 10**4) test : ', F(10**5, 10**4, S2_sieve) )





t2  = time.time()
print('\nCompleted in :', round((t2-t1)/60, 6), 'min\n\n')

print('\n====== My FIRST SOLUTION, 4 hours, S2_Sieve MUST BE improved  to keep only 2*10007 elements =====\n')
t1  = time.time()

def solution(LIM, b ):
    a = LIM
    primes = numpy_prime_sieve(int( LIM * math.log(LIM)*1.2) )
    print(len(primes), primes[:50]  )
    ### Here we build the s2_sieve
    S2_Sieve = np.array([  S2(k, primes ) for k in range(1, LIM+1  ) ])
    print('\nS2_sieve was built ....\n')


    return print('\nF(10**7, 10**5) solution : ', F(a , b, S2_Sieve) )

solution(10**7, 10**5)             #       F(10**7, 10**5) solution :  96632320042.0



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,  3 min, VERY GOOD INDEED  --------------------------')
t1  = time.time()


# ===== Sat, 4 Mar 2017, 21:53, urimend, Israel
# I maintained the distribution of values in an array of size 2∗10007, which is the maximal value for S2.
# For each step of "i" in the sum I updated the distribution and performed a local search for the new median,
# or actually two medians: the value below it and the value above it.
# 42.0 seconds in PyPy.


from math import log

def get_sequence(N, MOD):
    S = [pow(p, k+1, MOD) for k, p in enumerate(prime_sieve(int(N*log(N)*2)))][:N]
    assert len(S) == N
    S2 = [S[k] + S[(k+1)//10000] for k in range(N)]
    return S2

def find_ith_place(count, i, median = 0, smaller_than_median = 0):
    while smaller_than_median > i:
        median -= 1
        smaller_than_median -= count[median]
    while smaller_than_median <= i:
        smaller_than_median += count[median]
        median += 1
    return median - 1, smaller_than_median - count[median-1]

def p593(N = 10**6, K = 10**5, MOD = 10007):
    count = [0] * MOD * 2
    S2 = get_sequence(N+1, MOD)
    for j in range(K):
        count[S2[j]] += 1
    median0, smaller_than_median0 = find_ith_place(count, K/2-1)
    median1, smaller_than_median1 = find_ith_place(count, K/2)

    res = 0
    for i in range(N-K+1):
        res += 0.5 * (median0+median1)

        x = S2[i]
        count[x] -= 1
        smaller_than_median0 -= (x < median0)
        smaller_than_median1 -= (x < median1)

        x = S2[i+K]
        count[x] += 1
        smaller_than_median0 += (x < median0)
        smaller_than_median1 += (x < median1)

        median0, smaller_than_median0 = find_ith_place(count, K/2-1, median0, smaller_than_median0)
        median1, smaller_than_median1 = find_ith_place(count, K/2  , median1, smaller_than_median1)

    return print('\nAnswer : \t',res)


p593( N = 10**7, K = 10**5, MOD = 10007 )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)/60, 6), 'min\n\n')


# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 3,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
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
#
# print('\n--------------------------SOLUTION 6,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 7,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 8,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 9,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 10,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 11,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 12,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

