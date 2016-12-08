#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Thu, 1 Dec 2016, 20:29
#The  Euler Project  https://projecteuler.net
'''
                Prime square remainders     -       Problem 123

Let p_n be the nth prime: 2, 3, 5, 7, 11, ..., and let r be the remainder when :

                ( p_(n−1) )**n + ( p_(n+1) )**n is divided by ( p_n )**2.

For example, when n = 3, p_3 = 5, and 4**3 + 6**3 = 280 ≡ 5 mod 25.

The least value of n for which the remainder first exceeds 10**9 is 7037.

Find the least value of n for which the remainder first exceeds 10**10.

'''
import time
from itertools import count

def prime_generator(n):         # HIghly Efficient !!!!         THE FASTEST, The BEST , The ONE
    """  Sieve of Eratosthenes              !!!!!!!!! THE FASTEST SIEVE. It won the battle with sieve
    Create a candidate list within which non-primes will be marked as None.
    """
    cand = [i for i in range(3, n + 1, 2)]
    end = int(n ** 0.5) // 2

    # Loop over candidates (cand), marking out each multiple.
    for i in range(end):
        if cand[i]:
            cand[cand[i] + i::cand[i]] = [None] * ( (n // cand[i]) - (n // (2 * cand[i])) - 1 )

    # Filter out non-primes and return the list.
    return [2] + [i for i in cand if i]

primes = prime_generator(10**6)
print(len(primes) ,primes[0:100])
print('\n--------------------------TESTS------------------------------')


def prime_square_remainder(p_th) :
    p = primes[p_th-1]
    # print(p)
    return ((p-1)**p_th + (p+1)**p_th ) %(p**2)

print('Test for the function prime_square_remainder :  ', prime_square_remainder(3))



print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

maxv=0
for i in range(int(2.1*10**4)+1, len(primes), 2 ):
    x = prime_square_remainder(i)
    # print(str(i)+'.   ', x)
    if x > 10**9 :  print(str(i)+'.   ', x)
    if x > 10**10 :
        maxv = x
        i_th = i
        print(str(i)+'.   ', maxv, i_th)
        break

print('\nAnswer : ', i_th, maxv)            # Answer :  21035


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')      # Completed in : 523.030043 ms


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1, slower ,WalkerTesla, USA  --------------------------')
t1  = time.time()

# The Binomial Theorem essentially trivializes this question. We notice that when n is even,
# the remainder is 2 no matter what the value of n is.
# We notice that when n is odd, the remainder is 2*n*p_n.
# From here, we have a straightforward finish. Here is my Python Script for this question:

# import math
# def is_prime(x):
#     counter = 2
#     while counter<=math.sqrt(x):
#         if x%counter==0:
#             return False
#         counter+=1
#     return True
#
# def next_prime(x):
#     counter = x+2
#     while is_prime(counter) == False:
#         counter+=2
#     return counter
#
# prime_list = [5, 3]
#
# def prime_square(n):
#     a = prime_list
#     answer = 2*a[0]*a[1]
#     d = n[0]**2
#     answer %= d
#     prime_list[0] = next_prime(next_prime(prime_list[0]))
#     prime_list[1] = prime_list[1] + 2
#
#     return answer
#
# counter = 1
# while prime_square(prime_list) < 10**10:
#     counter+=1
#
# print (prime_list[1] - 2)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,  VERY FAST & EFFICIENT, mbh038, England --------------------------')
t1  = time.time()

# 65 ms in Python. Algebra tells us that the remainder is either 2 for even values of n or 2np_n for odd values,
# so I use a prime generator and look for the first odd power of n for which 2np_n exceeds the limit given.

import itertools as it

def erat2a():
    D = {}
    yield 2
    for q in it.islice(it.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q * q] = 2 * q # use here 2 * q
            yield q
        else:
            x = p + q
            while x in D:
                x += p
            D[x] = p

def p123(limit):
    t=time.clock()
    n=1
    prime=erat2a()
    next(prime)
    while 2*next(prime)*n<=limit:
        n+=2
        next(prime)
    print(n+2,next(prime))

p123(10**10)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3, hornemann55, Denmark --------------------------')
t1  = time.time()

# Using a binary search, could absolutely be optimized. Runs in 4 secs

def sqrrem(n):
    p=primes[n-1]
    return ((p-1)**n + (p+1)**n)%(p*p)

lim = 10**10
i1 = 7307
i2 = len(primes)
i2 = i2 - (i2%2==0)
p1 = sqrrem(i1)
p2 = sqrrem(i2)
i = 9001

while i2-i1 > 2:
    p = sqrrem(i)
    if p >= lim:
        p2,i2,i = p,i,min(i2-2,i2 - int((i2-i1)*(p2-lim)/(p2-p1)))
    else:
        p1,i1,i = p,i,max(i1+2,i1 + int((i2-i1)*(lim-p1)/(p2-p1)))
    i = i - (i%2 == 0)
print(i2)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,  FASTEST, dellasantina, France --------------------------')
t1  = time.time()

print ([(2*n+1,pn) for n,pn in enumerate(primes[::2]) if 2*(2*n+1)*pn >= 10**10][0])

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5, hansaplast, Switzerland  --------------------------')
t1  = time.time()

# Python, using binary search and hv's formula f(p)=2(n+1)p(n) if n is odd.
# The binary search only needs 16 iterations (compared to 7000 iterations when doing a linear search).
# In the end both linear search and binary search are under 0.1s so in the end the binary search was just for educational purposes..

fp=lambda n:2*(n+1)*primes[n] if n%2==1 else 2 # thanks to hv
n1,n2=7037,len(primes)
while n2-n1 > 2:
	middle = n1+(n2-n1)//2
	middle += (middle % 2 == 0)
	n1,n2 = (n1,middle) if fp(middle) > 10**10 else (middle,n2)
print(n2)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6, Exelian, Netherlands  --------------------------')
t1  = time.time()

Using python's built-in modulo power function, executes almost instantly

for n, p in enumerate(primes, start=1):
    if n%2==0:
        continue
    r = pow(p-1,n,p*p)+pow(p+1,n,p*p)
    if r > 10**10:
        print(p,n,r)
        break

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

