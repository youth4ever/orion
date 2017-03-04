#!/usr/bin/python                   ( ͡° ͜ʖ ͡°)
# Solved by Bogdan Trif @       Completed on Thu, 16 Feb 2017, 12:22
#The  Euler Project  https://projecteuler.net
'''
Largest integer divisible by two primes     -       Problem 347

The largest integer ≤ 100 that is only divisible by both the primes 2 and 3 is 96, as 96 = 32*3 = 25*3.

For two distinct primes p and q let M(p, q, N) be the largest positive integer ≤N
only divisible by both p and q and M(p, q, N)=0 if such a positive integer does not exist.

E.g. M(2, 3, 100) = 96.
M(3, 5, 100) = 75 and not 90 because 90 is divisible by 2 ,3 and 5.
Also M(2, 73, 100) = 0    because there does not exist a positive integer ≤ 100 that is divisible by both 2 and 73.

Let S(N) be the sum of all distinct M(p, q, N).
S(100)=2262.

Find S(10 000 000).                                S(10**7) = ?

'''
import time, gmpy2
import sympy.ntheory
from math import log, floor, ceil

def sieve(n):       # SECOND FASTEST
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]


def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    from pyprimes import factorise
    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]






def largest_integer(a, b ,lim):
    l1 = log(lim,a)
    l2 = log(lim,b)
    closest = 0
    for i in range(1, ceil(l1)):
#         if a**i > lim : break
        for j in range(1, ceil(l2)):
            y = a**i*b**j
            if y > lim : break
            if y > closest :
                closest = y
            # print('i,j =',i,j,' a,b=',a,b ,', powrs=',a**i, b**j,'  ', y)
    return closest


up_lim = 10**2
primes = sieve( up_lim//2 )

print('\nsympy.ntheory.prevprime : \t\t' ,sympy.ntheory.prevprime(100//3) )
p1 = sympy.ntheory.prevprime(int(100**(1/2) ))
print('sympy.ntheory.prevprime : \t\t' , primes.index(p1)+1 , primes[:primes.index(p1)+1] ,'\n' )



print('\n-----------------------     BRUTE FORCE TESTS    ---------------------------')
t1  = time.time()

def brute_force(up_lim) :       # not working properly because strings like 2 331 and 23 31 losses info on concatenation
    D = {}
    for i in range(2, up_lim+1):
        if gmpy2.is_prime(i) == False :
            g = get_factors(i)
            if len(set(g)) == 2 :
                d = str(g[0])+'-'+str(g[-1])
                print(str(i)+'.    ',g , '   ', d   )
                if d not in D : D[d] = i
                if d in D :
                    if D[d] < i :
                        D[d] = i

    print('\n' ,sorted(D.values()) )
    print( D )
    return print('\nSoln : \t' ,sum( D.values() ))

brute_force(10**3)
# 2017-02-02, 22:15 - Not difficult but I need a good IDEA !!!
# Example : Unde 10.000
# get_factors(9996), get_factors(9826),
# Justify how to get to 9826 which is the number [2, 17, 17, 17]) that we are looking for !

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n================  My FIRST SOLUTION, 1 min   ===============\n')
t1  = time.time()

def solution_pb347(up_lim) :
    up_lim
    primes = sieve( up_lim//2 )
    G = []
    S = 0
    p1 = sympy.ntheory.prevprime(int(up_lim**(1/2) ))
    ind_i = primes.index(p1)+1
    for i in range( ind_i+1 ):
        if  gmpy2.is_prime( up_lim//primes[i] ) :
            j_ind = primes.index( up_lim//primes[i])
        else :
            lim = sympy.ntheory.prevprime(up_lim//primes[i])
            j_ind = primes.index(lim)
        # print('i-th prime   lim  - j_ind ,  ', primes[i]  , lim, j_ind, up_lim//primes[i])
        for j in range(i+1, j_ind +1 ):
            a, b, c = primes[i], primes[j],  largest_integer(primes[i], primes[j], up_lim  )
            # print(a, b, '.      ',  c,'       '  )
            S+=c
            # G.append(c)
            if c > up_lim : break
        print(a)
    # print('\n',sum(G),'\n' ,sorted(G))

    return print('\nAnswer : \t', S)



# solution_pb347(10**7)                     # Answer : 	 11109800204052

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

# Tried : 11109240252318
#  1414000891

print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1, 12 sec  --------------------------')
t1  = time.time()

# === Mon, 6 Feb 2017, 11:42, Khalid, Saudi Arabia
# Straight forward problem. I generate all possible prime pairs below the target,
# and find the highest possible power for one of the primes (The other would be 1),
# and keep increasing the primes and checking what would the value be. Runs in 12 seconds.

def khalid() :
    from math import log
    target = 10**7
    primes = list(sieve(target//2))

    s = 0
    for p1 in primes:
        for p2 in primes:
            if p1 == p2 or p1 * p2 > target:
                break
            pp1 = 1
            pp2 = int(log(float(target) / p1, p2))
            r = p1**pp1 * p2**pp2
            while True:
                pp1 += 1
                if target <= p1**pp1:
                    break
                pp2 = int(log(float(target) / p1**pp1, p2))
                r_new = p1**pp1 * p2**pp2
                if r_new > target or pp2 == 0:
                    break
                if r_new < r:
                    continue
                r = r_new
            s += r

    return print (s)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()

# ==== Mon, 7 Nov 2016, 08:00, mbh038, England
# About 15 s in Python. I generate primes using a sieve, then for each pair of primes p, q, such that p<q and pq<10**7.
# I find the highest number less than 10**7 that is divisible only by p and q, by trying pq(10**7//pq−k) for k=0,1,2...
#
# Yet again I find that use of a standard library of functions can make a Project Euler solution much slower
# than it need be, because it does more work than is necessary.
# To get this one solved inside a minute I had to realise that I did not need to use my standard function
# to find the prime factors of pq(10**7//pq−k), but merely to determine whether p and q were the only prime factors,
# which is an easier task.

import numpy as np

def p347(limit):
    primesieve=np.ones(limit//2+1,dtype=bool)
    for i in range(2, int((limit+1)**0.5+1)):
        if primesieve[i]:
            primesieve[2*i::i]=False
    primes=np.nonzero(primesieve)[0][2:]

    S=0
    for i in range(len(primes)):
        for j in range(i+1,len(primes)):
            p,q=primes[i],primes[j]
            prod=p*q
            if prod>limit:
                break
            k=0
            while 1:
                ul=prod*(limit//prod-k)
                n=ul
                while not n%p:
                    n//=p
                while not n%q:
                    n//=q
                if n==1:
                    S+=ul
                    break
                k+=1
    print(S)

# p347(10**7)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,  10 sec --------------------------')
t1  = time.time()

# === Mon, 5 Sep 2011, 21:50, glingl, Austria
# I have a very unsophisticated solution in Python (3.2), which I hope to be easy to read.
# Here is the full code (including the generation of primes), so it runs without using any libs.

def primes(N):
    L = round(N**.5) + 1
    p = set(range(3, N+1, 2)).union({2})
    k = 3
    while k <= L:
        p.difference_update(set(range(k*k, N+1, k)))
        k += 2
    return p

def M(p, q, N):
    pq = p*q
    if pq > N:
        return 0
    cands = {pq}
    while cands:
        curr = min(cands)
        cands.remove(curr)
        u = curr * p
        if u <= N:
            cands.add(u)
        v = curr * q
        if v <= N:
            cands.add(v)
    return curr

N = 10000000
PRIMES = sorted(primes(N//2))
s = 0
l = len(PRIMES)
for i in range(l-1):
    pi = PRIMES[i]
    j = i+1
    while j < l:
        pj = PRIMES[j]
        if pi * pj > N:
            break
        s += M(pi, pj, N)
        j += 1

print("Sum:", s)

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
