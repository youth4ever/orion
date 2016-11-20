#!/usr/bin/python
# Solved by Bogdan Trif @   Mon, 10 Oct 2016, 22:47
#The  Euler Project  https://projecteuler.net
'''
Quadratic primes        -      Problem 27
Euler discovered the remarkable quadratic formula:
n**2+n+41
It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤390≤n≤39.
However, when n = 40, 40**2 + 40 + 41 = 40(40+1)+41,
and certainly when n = 41 , 41**2 + 41 + 41  is clearly divisible by 41.

The incredible formula n**2−79*n+1601 was discovered, which produces 80 primes
for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.
Considering quadratics of the form:
n**2+a*n+b,  where |a| < 1000 and |b| ≤ 1000
where |n| is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a and b, for the quadratic expression that produces
the maximum number of primes for consecutive values of n, starting with n=0.
'''
import time

def is_prime(n):
    # Function which checks if a number is prime
    for i in range(2, int(pow(n,1.0/2))+1):
        if n%i==0:
            return 0
    return 1

def sieve_of_eratosthenes(limit):
    primes = []
    table = [True] * limit
    table[0] = table[1] = False
    for i, is_prime in enumerate(table):
        if is_prime:
            for n in range(i * i, limit, i):
                table[n] = False
    for j in range(limit):
        if table[j] is True:
            primes.append(j)
    return primes


primes = sieve_of_eratosthenes(1000)
print(primes)

'''

cum,A,B = 0,0,0
for a in range(-1000,1000):                 # Actually both must be primes
    #for b in range(-950,980):                   # b MUST BE PRIME
    for b in primes:                   # b MUST BE PRIME
        seq = 0
        for n in range(0,100):
            x = n**2 + a*n + b
            if (x > 0 and is_prime(x) == 1 and (n-1)**2+a*(n-1)+b >0 and is_prime((n-1)**2 + a*(n-1) + b) ==1 ):
                seq += 1
                #print(seq, a, b, n, x)
                if cum < seq :
                    cum = seq
                    A, B = a, b
            else: seq = 0
    print('Consecutives : ',cum,'  ;   a =',A, ',  b =', B, '  ;  Prod :',A*B)          # Answer : -59231 ;  Consecutives :  72   ;   a = -61 ,  b = 971



In the first, I did not notice that b has to be prime and a has to be odd.
After I noticed the particularities of a and b, i just changed the limit of b values (from [-1000,1000] to prime numbers),
and the second code gives me the result:
a must be odd, b must be prime and odd (if n = 0, n^2+a*n+b = 0^2+a*0+b = b)
'''
print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1 , NICE PIECE OF CODE & FAST  by Sahexa, --------------------------')

t1  = time.time()

def sieve_of_eratosthenes(limit):
    primes = []
    table = [True] * limit
    table[0] = table[1] = False
    for i, is_prime in enumerate(table):
        if is_prime:
            for n in range(i * i, limit, i):
                table[n] = False
    for j in range(limit):
        if table[j] is True:
            primes.append(j)
    return primes

primes = sieve_of_eratosthenes(1000)

def isprime(n):
    return n in primes

def quadratic():
    max_n = 0
    for a in range(-999, 1000):
        for b in primes:
            n = 0
            while isprime(n ** 2 + n * a + b):
                n += 1
                if n > max_n:
                    max_n, product = n, a * b
    return product, (0, max_n)

print(quadratic())

t2  = time.time()
print('\nCompleted in :', round((t2-t1),4), 's\n\n')

print('\n--------------------------SOLUTION 2 , dugar_ab, --------------------------')

t1  = time.time()

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*int((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]


def binSearch(a,x):
    first = 0;
    last = len(x)-1
    mid = int((first+last)/2)
    while(first<=last):
        if(x[mid]>a):
            last = mid-1
        elif(x[mid]<a):
            first = mid+1
        else: return mid

        mid = int((first+last)/2)
    return -1

x = primes(1000100)
barray = x[0:168]

maximum=0
product = 1

for a in range(-999,1001,2):
    count = 0
    for b in barray:
        i=1
        while(binSearch((i*i + i*a + b),x)>=0):
            #print(str(i*i + i*a + b) + " a: " + str(a) + " b: " + str(b))
            i+=1
        if(i>maximum):
            maximum = i
            #print("count: " + str(i) + " a: " + str(a) + " b: " + str(b))
            product = a*b
        count+=1

print (product)

t2  = time.time()
print('\nCompleted in :', round((t2-t1),4), 's\n\n')

print('\n--------------------------SOLUTION 3 - Incredible Fast , FJ_Sevilla, Spain --------------------------')
t1  = time.time()

from math import sqrt

def Eratosthenes_sieve(lim):
    sieve = [True] * lim
    sieve[0:2]=[False]*2
    sieve[2]=True
    sieve[4::2]=[False]*len(sieve[4::2])
    for num in range(3,int(sqrt(lim))+1,2):
        if sieve[num]:
            sieve[num*num::2*num]=[False]*int((lim-num*num-1)/(2*num)+1)
    return sieve

def f():
    sieve=Eratosthenes_sieve(10**5)
    primes=[n for n in range(3,1001,2) if sieve[n]]
    ma,mb=1,41 # n² + n + 41 (a=1, b=41, n max = 39)
    maxN=40

    for b in primes:
        for a in range(-999,1001,2):
            s=maxN*maxN+a*maxN+b
            if s < 3: continue
            elif sieve[s]:
                for n in range(1,maxN):
                    if not sieve[n*n+a*n+b]:break
                else:
                    ma,mb=a,b
                    maxN+=1

    print('Sol:', ma*mb,'a=',ma, 'b=',mb,'n=', maxN)

f()

t2  = time.time()
print('\nCompleted in :', round((t2-t1),4), 's\n\n')