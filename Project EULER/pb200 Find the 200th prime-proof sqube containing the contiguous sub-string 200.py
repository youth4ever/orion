#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Tue, 14 Mar 2017, 20:32
#The  Euler Project  https://projecteuler.net
'''
Find the 200th prime-proof sqube containing the contiguous sub-string "200"         -       Problem 200

We shall define a sqube to be a number of the form, p**2*q**3, where p and q are distinct primes.
For example, 200 = 5**2 * 2**3 or 120072949 = 23**2 * 61**3.

The first five squbes are 72, 108, 200, 392, and 500.

Interestingly, 200 is also the first number for which you cannot change any single digit to make a prime;
we shall call such numbers, prime-proof.

The next prime-proof sqube which contains the contiguous sub-string "200" is 1992008.

Find the 200th prime-proof sqube containing the contiguous sub-string "200".

'''
import time, gmpy2

def sieve(n):       # SECOND FASTEST
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]





print('\n--------------------------TESTS------------------------------')
t1  = time.time()

P = sieve(100)
print(P[:100] , '\n')



print('\n----------------function ----------------------')
# @2017-01-29, Federer won today 18-th Grand Slamp title at Australian Open
# Must finish the function

def prime_proof(n) :
    l = len(str(n))
    m = int(  str(1)+ str(n)[1:] )
    if gmpy2.is_prime(m) :  return False
    # print(m,'----\n')
    for i in range(1, 9):
        m += 10**(l-1)
        if gmpy2.is_prime(m) :  return False
    o = str(n)[:-1]
    for j in [1, 3, 7 ,9] :
        m = int( o + str(j) )
        # print(m, end='   ')
        if gmpy2.is_prime(m) :      return False
    # print('\n------------')
    for k in range(2, l ):
        m =int(  str(n)[:k-1]+str(0) + str(n)[k:] )
        if gmpy2.is_prime(m) :      return False
        # print('------------')
        # print('m =   ', m )
        for q in range(0, 9) :
            m += 10**(l-k)
            if gmpy2.is_prime(m) :      return False
            # print(m, )

    return True


print('\nprime_proof : \t  ', prime_proof (200) )
print('prime_proof : \t  ', prime_proof (1992008) )

print('\n------------- Main Test ------------------')

def brute_force_test( up_prime ) :
    P = sieve(up_prime)
    print(len(P), '   ',P[:100],'\n')
    Q, cnt = [], 0
    for i in range( 1000 )  :
        if P[i]< 50 : jr = len(P)
        if 50 < P[i]< 10**3 : jr = 2500
        if 10**3 < P[i]< 10**4 : jr = 1500

        for j in range( i+1 , jr ) :
            sq1, sq2 = P[i]**2*P[j]**3 , P[i]**3*P[j]**2
            s1, s2 = str(sq1).find('200') ,  str(sq2).find('200')
            if s1 != -1 and prime_proof(sq1):
                cnt+=1
                print(str(cnt)+'.       sqube 1 : ', P[i], P[j], '      ',sq1, '       len =', len(str(sq1)) , '     Q: ', len(Q),'     indeces : ', i, j  )
                if len(str(sq1)) <= 17 :
                    Q.append(sq1)

            if  s2 != -1 and prime_proof(sq2) :
                cnt+=1
                print(str(cnt)+'.       sqube 2 : ', P[i], P[j], '      ',sq2, '      len =', len(str(sq2)) , '     Q: ', len(Q),'     indeces : ', i, j )
                if len(str(sq2)) <= 17 :
                    Q.append(sq2)

            # if cnt % 10**5 == 0 :
            #     print(str(cnt)+'.    i, j = ', i, j ,'      sqube 1 = ', sq1, '       sqube2 = ', sq2,'       ', len(Q) )
    Q.sort()
    print('\n', len(Q),'   ', Q)

    return print('\nAnswer : \t', Q[200 -1 ])

# brute_force_test(10**6)                     #       Answer : 	 229161792008

t2  = time.time()
print('\nCompleted in :', round((t2-t1)/60 ,6), 'min\n\n')      #   Completed in : 2.680353 min


print('\n================  My FIRST SOLUTION,  400 ms ===============\n')
t1  = time.time()

def optimized_solution( up_prime ) :
    P = sieve(up_prime)
    print(len(P), '   ',P[:100],'\n')
    Q, cnt = [], 0
    for i in range( 10 )  :
        if P[i]< 10 : jr = len(P)
        if 10 < P[i]< 30 : jr = len(P)//2
        for j in range( i+1 , jr ) :
            sq1, sq2 = P[i]**2*P[j]**3 , P[i]**3*P[j]**2
            s1, s2 = str(sq1).find('200') ,  str(sq2).find('200')
            if sq1 > 25*10**10 and sq2 > 25*10**10 :  break
            if s1 != -1 and prime_proof(sq1):
                cnt+=1
                # print(str(cnt)+'.       sqube 1 : ', P[i], P[j], '      ',sq1, '       len =', len(str(sq1)) , '     Q: ', len(Q),'     indeces : ', i, j  )
                if len(str(sq1)) <= 15 :  Q.append(sq1)
            if  s2 != -1 and prime_proof(sq2) :
                cnt+=1
                # print(str(cnt)+'.       sqube 2 : ', P[i], P[j], '      ',sq2, '      len =', len(str(sq2)) , '     Q: ', len(Q),'     indeces : ', i, j )
                if len(str(sq2)) <= 15 :   Q.append(sq2)
    Q.sort()
    print('\n', len(Q),'   ', Q)

    return print('\nAnswer : \t', Q[200 -1 ])

optimized_solution(2*10**5)                     #       Answer : 	 229161792008




t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,   --------------------------')
t1  = time.time()

# === Fri, 5 Sep 2014, 06:37, der_herr_g, Germany
# My solution. Found the boundaries (number of primes to pre-generate and breaking condition for x) by trial and error.
# I think it's fairly straight forward, but still runs in about 0.5s.
# In case you are a Python user and have not yet heard of PyPrimes, it is a pretty cool module that comes in handy
# for many prime-number-related problems here.

import pyprimes

def is_primeproof(n):
    zahl = str(n)
    for i in range(10):
        for position in range(len(str(n))):
            m = str(zahl[0:position])+str(i)+str(zahl[position+1:])
            if pyprimes.isprime(int(m)):
                return False
    return True

primes = list(pyprimes.primes_below(200000))
squbes = []

for p in primes:
    for q in primes:
        if p==q:
            continue
        x = p**2 * q**3
        if '200' in str(x):
            squbes.append(x)
        if x > 1000000000000:
            break

squbes.sort()
pp_squbes = []

def solution1():
    for sqube in squbes:
        if is_primeproof(sqube):
            pp_squbes.append(sqube)
    #         print (sqube)
            if len(pp_squbes) == 200:
                return print('\nAnswer : \t', pp_squbes[-1])

# solution1()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,  VERY NICE --------------------------')
t1  = time.time()


import heapq

primes = sieve(1000000)

def sqube_gen():
    """Generate all squbes in sorted order."""
    # (val, (sq, cu)).
    q = [(3**2 * 2**3, (0, 1)), (2**2 * 3**3, (1, 0))]
    heapq.heapify(q)
    queued = set((q[0], q[1]))
    while True:
        val, cur = heapq.heappop(q)
        yield val
        children = [(cur[0] + 1, cur[1]), (cur[0], cur[1] + 1)]
        for child_nums in children:
            child = (primes[child_nums[0]]**2 * primes[child_nums[1]]**3,  child_nums)
            if child not in queued:
                queued.add(child)
                heapq.heappush(q, child)

def is_proof(n):
    s = list(str(n))
    for i in range(len(s)):
        tmp = s[i]
        for d in '0123456789':
            if s[i] == d:
                continue
            s[i] = d
            if gmpy2.is_prime(int(''.join(s))):
                return False
        s[i] = tmp
    return True

def solution2():
    vals = []
    for sq in sqube_gen():
        if '200' in str(sq) and is_proof(sq):
            vals.append(sq)
            # print('yay', sq, len(vals))
            if len(vals) == 200 :
                return print('\nSolution : \t', sq)

solution2()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,  0.5 sec --------------------------')
t1  = time.time()

import gmpy2

def sieve (n):
    s = [ False if i % 2 == 0 else True for i in range (n) ]
    yield 2
    for i in range (3, n):
        if s[i]:
            for j in range (i*i, n, i):
                s[j] = False
            yield i

def has_200 (p):
    return True if '200' in str (p) else False

def prime_proof (p):
    s = str (p)
    if p % 2 == 0:
        for d in '13579':
            if gmpy2.is_prime (int (s[:-1] + d)):
                return False
    else:
        for i in range (len (s)):
            sub = '0123456789'
            if i == 0:
                sub = sub[1:]
            if i == len (s):
                sub = '13579'
            for d in sub:
                if gmpy2.is_prime (int (s[:i] + d + s[i+1:])):
                    return False
    return True

def solution3():
    primes = list (sieve (200000))
    ppsq = set ()
    for i in range (len (primes)):
        for j in range (i+1, len (primes)):
            p, q = primes[i], primes[j]
            a, b = p**2*q**3, p**3*q**2
            if a > 250000000000 and b > 250000000000:
                break
            if has_200 (a):
                if prime_proof (a):
                    ppsq.add (a)
            if has_200 (b):
                if prime_proof (b):
                    ppsq.add (b)
    return print(sorted(ppsq)[199])

solution3()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')      #   Completed in : 557.031631 ms

# print('\n--------------------------SOLUTION 4,    --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

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
