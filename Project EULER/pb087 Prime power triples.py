#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Sat, 29 Oct 2016, 21:17
#The  Euler Project  https://projecteuler.net
'''
                                Prime power triples     -       Problem 87
The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28.
In fact, there are exactly four numbers below fifty that can be expressed in such a way:

                                                28 = 2**2 + 2**3 + 2**4
                                                33 = 3**2 + 2**3 + 2**4
                                                49 = 5**2 + 2**3 + 2**4
                                                47 = 2**2 + 3**3 + 2**4

How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?
'''
from itertools import combinations, permutations
import time


def sieve(lower, upper_bound):         # THE FASTEST  SIEVE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # SIEVE OF ERATOSTHENES
    n = upper_bound + 1
    check = [True] * n
    check[0] = check[1] = False
    for i in range(2, int(upper_bound**0.5) + 1):
        if check[i]:
            for j in range(i**2, upper_bound + 1, i):
                check[j] = False
    primes = [i for i, flag in enumerate(check) if flag and i > lower ]
    return primes

def is_prime(n):
    # Function which checks if a number is prime
    for i in range(2, int(pow(n,1.0/2))+1):
        if n%i == 0 :
            return 0
    return 1

primes = sieve(1,7100)
#print(primes)


#  1. You need primes until 7072 to  2-nd power
#  1. You need primes until 369 to  3-nd power
#  1. You need primes until 85 to  4-nd power


print('\n-------------------------- MY SOLUTION , Fast enough --------------------------')

t1  = time.time()


Numbers = {}
NR = []
iter=0
i, j, k = 0, 0, 0
while primes[i]**4 < 5*10**7 :
    a = primes[i]**4
    #print(a)
    while (a + primes[j]**3 < 5*10**7 ) :
        b = primes[j]**3
        #print(a, b, a+b  )
        while (a + b + primes[k]**2 < 5*10**7) :
            c = primes[k]**2
            #print(primes[i], primes[j], primes[k] ,'     ',a+b+c  )
            Numbers[(a+b+c)] = 1
            # NR.append(a+b+c)
            # iter+=1
            # if iter % 10**5 == 0 : print(iter)
            k+=1
        j+=1
        k=0
    j = 0
    i += 1

print('Note that with dictionary in this case is faster ')
# print('\nResult: ',len(set(NR)),'\n')          # Answer :  1097343        # List variant
print('\nResult: ',len(Numbers),'\n')          # Answer :  1097343          # Dictionary variant
#print(sorted(set(Numbers))[0:3000])


t2  = time.time()
print('\n' ,' Completed in  :', round((t2-t1),6), 's\n')        #Completed in  : 3.368193 s


print('\n-----------Test  Triple Loop-------------------')
i, j, k = 0,0,0
count=0
while i < 3 :
    while j < 3 :
        while k < 3 :
            count+=1
            print(str(count)+'. ', i, j, k,  end='   ')
            k+=1
        j+=1
        k=0
    j  = 0
    i+=1
print('\n',count,' iterations')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1 , mbh038, England  --------------------------')
t1  = time.time()


import numpy as np
import itertools as it
import time

def mysieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]

def ppt(n):

    p2=[pa**2 for pa in mysieve(int(n**(1/2)))]
    p3=[pb**3 for pb in mysieve(int(n**(1/3)))]
    p4=[pc**4 for pc in mysieve(int(n**(1/4)))]

#    ppts=set(pa+pb+pc for pa,pb,pc in it.product(p2,p3,p4) if pa+pb+pc<n) # also works
#    ppts={pa+pb+pc for pa in p2 for pb in p3 if pa+pb<n for pc in p4 if pa+pb+pc<n} #also works
    p234=(set([x for x in np.add.outer(np.add.outer(p2,p3).ravel(),p4).ravel() if x<n])) #fastest
    print (len(p234))

ppt(5*10**7)

t2  = time.time()
print('\n' ,' Completed in  :', round((t2-t1),6), 's\n')


print('\n--------------------------SOLUTION 2 ,  Avi Levy, USA --------------------------')
t1  = time.time()

from math import floor, sqrt

pows = [[] for i in range(5)] # only populate pows[2 thru 4]
N = 5*10**7
M = floor(sqrt(N))
s = [0] * N
for i in range(2,M):
  for j in range(i+i,M,i):
    s[j] = 1
for i in range(2,M):
  if not s[i]:
    for j in range(2,5):
      t = pow(i,j)
      if t < N:
        pows[j].append(t)

s = 0
d = set()
for i in pows[2]:
  for j in pows[3]:
    for k in pows[4]:
      t = i + j + k
      if t < N and t not in d:
        s += 1
        d |= {t}
print(s)


t2  = time.time()
print('\n' ,' Completed in  :', round((t2-t1),6), 's\n')


print('\n--------------------------SOLUTION 3 , mfm24,    --------------------------')
t1  = time.time()

from itertools import takewhile

def primes_below(n):
    # use a sieve to find primes
    r = bytearray(n)
    r[0] = r[1] = 1
    for x in range(2, int(n**0.5)):
        if r[x] != 0:
            continue
        for s in range(2*x, n, x):
            r[s] = 1
    return [i for i, x in enumerate(r) if x==0]

def values_below(vals, n):
    return takewhile(lambda x: x<n, vals)

def count_ways(N):
    primes = primes_below(int(N**(1/2)))
    r = {a**2+b**3+c**4
                for c in values_below(primes, N**(1/4))
                for b in values_below(primes, (N - c**4)**(1/3))
                for a in values_below(primes, (N - c**4 - b**3)**(1/2)) }
    return len(r)
count_ways(50000000)



t2  = time.time()
print('\n' ,' Completed in  :', round((t2-t1),6), 's\n')

print('\n--------------------------SOLUTION 4 , merkez3110 , Turkey  --------------------------')
t1  = time.time()

def main(max_sum):
    sum_root = int(max_sum ** (1 / 2))
    list_powers = []
    list_prime_sieve = [i for i in range(sum_root)]
    list_prime_sieve[1] = 0

    for i in list_prime_sieve:
        if i != 0:
            k = 2 * i

            while k < len(list_prime_sieve):
                list_prime_sieve[k] = 0
                k += i

    for prime in list_prime_sieve:
        if prime != 0:
            list_powers.append((prime ** 2, prime ** 3, prime ** 4))

    solution_set = set()

    for i in list_powers:
        t1 = i[0]
        for j in list_powers:
            t2 = t1 + j[1]
            if t2 < max_sum:
                for k in list_powers:
                    t3 = t2 + k[2]
                    if t3 < max_sum:
                        solution_set.add(t3)
                    else:
                        break
            else:
                break

    print(len(solution_set))
    return

if __name__ == '__main__':
    main(50000000)



t2  = time.time()
print('\n' ,' Completed in  :', round((t2-t1),6), 's\n')

print('\n--------------------------SOLUTION 5 ,  kenkamau, Kenya  --------------------------')
t1  = time.time()

#straightforward, if you know you that duplicates may arise..hence the set

import math
upper = 50000000
def primes(limit):
    a = [True] * limit
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):
                a[n] = False

listPrimes = list(primes(int(math.sqrt(upper))))

s = set()
for a in listPrimes:
    for b in listPrimes:
        for c in listPrimes:
            result = a ** 2 + b ** 3 + c ** 4
            if result < upper:
                s.add(result)
            else: break
print(len(s))


t2  = time.time()
print('\n' ,' Completed in  :', round((t2-t1),6), 's\n')

