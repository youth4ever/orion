#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
Divisor Square Sum      -       Problem 211

For a positive integer n, let σ2(n) be the sum of the squares of its divisors. For example,

σ2(10) = 1 + 4 + 25 + 100 = 130.

Find the sum of all n, 0 < n < 64,000,000 such that σ2(n) is a perfect square.


'''
import time, gmpy2
from math import sqrt
from pyprimes import factorise
import functools, operator

def sieve(n):       # SECOND FASTEST        o(^_^)o
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def get_divisors(n):      ### ( ͡° ͜ʖ ͡°)  FASTEST  ( ͡° ͜ʖ ͡°)  ### !! FIRST FASTEST
    factors = set()
    for x in range(1, int(sqrt(n)) + 1):
        if n % x == 0:
            factors.add(x)
            factors.add(n//x)
    return sorted(factors)

def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''

    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]

print('\n--------------------------TESTS, 3 hours------------------------------')
t1  = time.time()

def divisor_square_sum_sigma_2(n):
    '''     Π  = ((p_1**(a_1+1)*2)-1) / (p_1 -1)*...*((p_k**(a_k+1)*2)-1) / (p_k -1)
    where p_1, p_2,...p_k are the prime factors of the number , together with their
    coefficients exponentials a_1, a_2,...,a_k
    :param n: int, number
    :return: int, sigma2 representing the Sum of the squares of its divisors !              '''

    D = list(factorise (n ))
    P = [( i[0]**((i[1]+1)*2)-1 ) //(i[0]**2-1) for i in D ]
    # print(D)
    return functools.reduce(operator.mul, P)

print( list( factorise(64000)))
print( divisor_square_sum_sigma_2(64000) ,'' )                  #       1422213156
print( divisor_square_sum_sigma_2(64*10**6) ,'\n\n' )

def slow_brute_force(lim):
    S=0
    for i in range( 2, lim ) :
        if gmpy2.is_prime(i) == False :
            D = get_divisors(i)
            dsq = sum([j*j for j in D ])
            if gmpy2.is_square(dsq) :
                S+=dsq
                print(str(i)+'.       ', dsq ,'          ', get_factors(i)  ,  '         ', D, sum(D) )

    return print('\nTotal sum :\t', S,'\n\n')

# slow_brute_force(40000)


def brute_force_sigma_2(lim):
    S=0
    for i in range( lim , 2, -1 ) :
        if gmpy2.is_prime(i) == False :
            dsq = divisor_square_sum_sigma_2(i)
            if gmpy2.is_square(dsq) :
                S+=i
                print(str(i)+'.       ', dsq ,'          ', get_factors(i)  )

    return print('\nTotal sum :\t', S+1)

# brute_force_sigma_2(lim = 64*10**6)                 #   ANSWER : Total sum :	 1922364685

t2  = time.time()
print('\nCompleted in :', round((t2-t1), 6), 's\n\n')



# 2017-02-06 --> found on the Internet that you must transform into an Geom Series,
# http://math.stackexchange.com/questions/166501/delta-2n-the-sum-of-the-squares-of-the-positive-divisors-of-n
# Still miss an insight
# http://stackoverflow.com/questions/335955/project-euler-211-efficiency-issue


#                                   Answer : 5688888803185771



t2  = time.time()
print('\nCompleted in :', round((t2-t1), 6), 's\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

lim = 64*10**3
primes=sieve( lim//20 )
for p in primes:
    e = 1
    while p**e < lim :
        p1 = p**e

        e+=1

# for i in range(1, 64*10**6):
#     a=i
# print('finished')













t2  = time.time()
print('\nCompleted in :', round((t2-t1)/60, 6), 'min\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,  12 min --------------------------')
t1  = time.time()

def pe211():
	sq=[0 for i in range(64000001)]
	for i in range(2,64000001):
		for j in range(i,64000001,i):
			sq[j] += i*i
	res=0
	for i in range(1,64000001):
		if ((1+sq[i])**.5)%1==0:res+=i
	print(res)

# pe211()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)/60, 6), 'min\n\n')

print('\n--------------------------SOLUTION 2, 12 min  --------------------------')
t1  = time.time()

# ====Wed, 12 Mar 2014, 21:51, Nicolas Patrois, France

def Nicolas_Patrois():
    from math import sqrt

    def estcar(x):
      return (int(sqrt(x)))**2==x

    nb=64*10**6-1
    som2div=[0]+[1]*nb

    for i in range(2,nb+1):
      ii=i*i
      for j in range(i,nb+1,i):
        som2div[j]+=ii

    print("crible ok")

    somme=0

    for i in range(1,nb+1):
      if estcar(som2div[i]):
        somme+=i

    return print(somme)

# Nicolas_Patrois()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)/60, 6), 'min\n\n')

print('\n--------------------------SOLUTION 3,   --------------------------')
t1  = time.time()




t2  = time.time()
print('\nCompleted in :', round((t2-t1)/60, 6), 'min\n\n')

print('\n--------------------------SOLUTION 4, 6 min  --------------------------')
t1  = time.time()

# === Thu, 20 Sep 2012, 09:55, ephemeral, USA
# My solution uses a sieve.
# Runs in ~7.8 seconds in Python with PyPy :)

def sieve():
    from math import sqrt

    sqs = [False] * 256
    for i in range(256):
        sqs[(i * i) & 255] = True

    def is_square(n):
        if not sqs[n & 255]: return False
        x = sqrt(n)
        return x == int(x)

    def divisor_square_sum_sieve(n):
        sieve, limit = [0] * (n + 1), int(sqrt(n)) + 1
        for i in range(1, limit):
            sieve[i * i] += i * i; temp = i + 1
            for j in range(i * i + i, n + 1, i):
                sieve[j] += i * i + temp * temp
                temp += 1
        return sieve

    def euler_211():
        limit, s1 = 64000000, 0
        s = divisor_square_sum_sieve(limit)
        for i in range(1, len(s)):
            if is_square(s[i]): s1 += i
        return print(s1)

    euler_211()

# sieve()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)/60, 6), 'min\n\n')

print('\n--------------------------SOLUTION 5,  13 min --------------------------')
t1  = time.time()

# ==== Mon, 12 Jan 2015, 11:48 , jvbelle, South Africa
# Brute force sieve. A few minutes. Would be sub-minute in compiled or parallellized.
# 64-bit makes it a bit faster. Perhaps could optimize it a bit further by pre-computing
# the (j//i) squares.
# Still haven't figured out a shorter way. Perhaps I should read up on the sigma-function ;)
# However the code is nice, clear and very short (6 lines :).
# Except I spent an hour looking for a tiny bug (used index i instead of i2 in sieve[i2] += i2)
# which remarkably only differed from the correct result by 9587 (<0.001%)
#### 13 min

def brute_force_sieve() :           # SIEVE
    sieve = [1+i**2 for i in range(64000000)]     #high = 64000000
    for i in range(2,int(64000000**0.5)):         #assume sieve to a perfect square
        i2 = i**2
        sieve[i2] += i2
        for j in range(i2+i,64000000,i): sieve[j] += i2 + (j//i)**2 #decreasing loop prob. quicker on 32-bit platform

    print('sum =',sum((i for i,j in enumerate(sieve) if int(j**0.5)**2==j))+1) #1, 1**2 double-counted for n=1

# brute_force_sieve()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


# print('\n--------------------------SOLUTION 6,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
