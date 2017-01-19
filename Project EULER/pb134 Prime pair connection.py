#!/usr/bin/python
# Solved by Bogdan Trif @       Completed on Wed, 11 Jan 2017, 21:35
#The  Euler Project  https://projecteuler.net
'''
            Prime pair connection       -       Problem 134

Consider the consecutive primes p1 = 19 and p2 = 23.
It can be verified that 1219 is the smallest number such that the
last digits are formed by p1 whilst also being divisible by p2.

In fact, with the exception of p1 = 3 and p2 = 5, for every pair of consecutive primes,
p2 > p1, there exist values of n for which the last digits are formed by p1 and n is divisible by p2.

Let S be the smallest of these values of n.
Find ∑ S for every pair of consecutive primes with 5 ≤ p1 ≤ 1.000.000   (10**6) .


'''
import time, gmpy2, sys
import numpy as np
from itertools import count
from pyprimes import factorise

def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]


def prime_generator(down, up):         # HIghly Efficient !!!!         THE FASTEST, The BEST , The ONE
    """  Sieve of Eratosthenes              !!!!!!!!! THE FASTEST SIEVE. It won the battle with sieve
    Create a candidate list within which non-primes will be marked as None.
    """
    cand = [i for i in range(3, up + 1, 2)]
    end = int(up ** 0.5) // 2

    # Loop over candidates (cand), marking out each multiple.
    for i in range(end):
        if cand[i]:
            cand[cand[i] + i::cand[i]] = [None] * ( (up // cand[i]) - (up // (2 * cand[i])) - 1 )

    # Filter out non-primes and return the list.
    return  [i for i in cand if i and i > down]


def primesieve(n):          ### o(^_^)o  FASTEST  o(^_^)o  ###  Highly Efficient !!!
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]

print('\n--------------------------TESTS------------------------------')

t1  = time.time()

def get_sufix(p1, p2):
    ''' Gets the sufix (prefix) of a prime pair consecutive numbers
    :param p1:  first prime
    :param p2:  second prime
    :return:  prefix number    '''
    n1 = int(str(1)+str(p1))
    n2 = n1 - p1
    inc = n2%p2
    start = inc - (p2%p1)
    # if start
    if start < 0 : start = start + p2
    if start + inc == p2 : return 2
    # print(p1, p2,  n1, n2, '   inc:', inc ,  '   first start:' , start  )

    if (p2 - start) % inc == 0 :
        diff = ((p2-start)//inc )+1
        return diff

    diff = (p2 - start) // inc  +1
    # if start >= p2%inc : diff = (p2 - start) // inc
    # elif start < p2%inc : diff = ((p2 -start ) // inc)+1

    end = (start+diff*inc)%p2
    R = diff+1
    # print(n1, n2, '   inc:', inc ,  '   first start:' , start ,'  end :', end , '   diff:',diff,  '    Accum : ',  R)

    if (end+inc)%p2 == 0 :
        return R+1

    while end !=0 :
        start = end
        if start >= p2%inc : diff = p2 // inc
        elif start < p2%inc : diff = (p2 // inc)+1
        # diff = (p2 - start) // inc + 1
        end = (start+ diff*inc )%p2
        R+=diff
        # print(start, end , diff, R)

    return R

print('\n get_sufix Test Function : \t', get_sufix(491 , 499) )

# p1, p2 :  5 , 7     n= 35  ,        ,           j= 3
# p1, p2 :  17 , 19     n= 817  ,        ,           j= 8
# p1, p2 :  89 , 97     n= 3589  ,       j= 35
# p1, p2 :  491 , 499     n= 4491  ,       j= 4        A= 123257
# p1, p2 :  991 , 997     n= 2991  ,       j= 2        A= 999


print('\n------------------------------------\n')

def brute_force(limit) :
    primes = primesieve(limit+10)
    print( len(primes) ,primes[-5::],'\n')
    S=0
    S1, S2 = 0,0
    for i in range(2, len(primes)-1) :
        p1, p2 = primes[i], primes[i+1]
        # print( p1, p2  )
        A =  get_sufix( p1, p2)
        S1+=A
        j=2
        while True :
            n = int(str(j)+str(p1))
            if n % p2 == 0 :
                S +=n

                print('p1, p2 : ' ,p1, ',',p2, '    n=',n,' ,       j=', j ,'       A=' , A)
                S2+=j
                break
            j+=1

    return print('\nAnswer : \t', S, S1,S2)

brute_force(10**2)

t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')


# ==== GENERAL IDEA :
# Use Chinese Remainder Theorem
# http://math.stackexchange.com/questions/626502/chinese-remainder-theorem-clarification
#                       EULER THEOREM
"""    Find smallest n such that n is divisible by p2 and n = a_p1 where _ is concatenation

    Suppose p1 is 2 digits...
    100*a + p1 = 0   | mod p2
    100*a = p2-p1    | mod p2
    (100 % p2) * a = p2-p1     | mod p2
    a = (p2-p1) * (100 %p2)**(-1)     | mod p2

    replace (by Euler's theorem):
    k**(-1) = k**(p2-2)     | mod p2
    """
# ==== Tue, 12 Feb 2013, 22:26, neizod, Thailand
# Diophantine Equation and Extended Euclidean, I really like this one. ;)
# For the example of (p1, p2) = (19, 23), the equation is:
#
#     23 x == 19 (mod 100)
# In other words:
#     23 x + 100 y == 19
# Ignore y and find smallest positive x, multiply it by 23, and that's the answer of this case.




# Wed, 17 Jul 2013, 17:16, Hidde, Netherlands
# This was a great problem!
#
# I noticed that the solution was of the form p1+10**d∗x
# where :d is the number of digits of p2,
#         and x the solution of
# 10**d * x  ≡ (p2−p1) (mod p2 )
# The solution to such a problem is
# (p2−p1)∗((10**d) (mod p2) **(p2−2) (mod p2)

# ==== Fri, 18 Sep 2009, 08:04, redfield, China
# Solve modular linear equation
# (x*10^k+p1)%p2==0 -> (x*10^k)%p2 = p2-p1


# ==== Sun, 17 Dec 2006, 07:46, ke9tv, USA
# Hmm.  I observed that
# S == 10**k * q + p1 == 0 (mod p2)
#
# where 10**k is the smallest power of ten greater than p1.
#
# This simplifies to 10**k * q == (p2-p1) mod p2.
#
# or q == (p2-p1) (10**k)' mod p2,
#
# where 10**k' is the multiplicative inverse of 10**k, mod p2.
#
# Solving for the inverse using extended Euclid yields
# the following short program (I omit my usual procedure
# for testing primality).  It runs in about 15 seconds.

# ===== Sat, 16 Dec 2006, 16:08, gianchub, England
# Very nice problem. I applied the Chinese reminder theorem.
# N is the number we are looking for, p1 and p2 are the consecutive primes and m1, m2 the relative prime moduluses such that:
#
# N = p1 mod m1
# N = 0 mod p2
#
# m1 is easily found with 10^ceiling(log10(p1)) and since the CRT states that:
#
# N = a1 * M1 * y1 + a2 * M2 * y2 (mod M)
#
# where M = m1 * m2, Mi = M/mi, yi = mod_inv(Mi, mi), a1 = p1 and a2=0.
#
# We achieve that:
#
# N = (p1 * m2 * mod_inv(m2, m1)) mod M
# The second addend is 0 since a2 = 0

Folding it up in C# code it takes 60 msecs to do the job, prime calculation included.

print('\n================  My FIRST SOLUTION,  SUPER VERY SLOW,  3hours ===============\n')
t1  = time.time()


def first_solution(limit) :
    h=1
    primes = primesieve(limit+10)
    print( len(primes) ,primes[-5::],'\n')
    S=0
    for i in range(2, len(primes)-1) :
        p1, p2 = primes[i], primes[i+1]
        A =  get_sufix( p1, p2)
        n = int(str(A)+str(p1))
        S +=n
        print( p1, p2 , A )
        if i*100 // len(primes)  > h-1 :        # Progress Bar #
            h += 1
            # sys.stdout.write("\r%d%%-" %h )
            sys.stdout.write('\r' + str(h)+' % ['+'#'*h+str(' ')*(220-22*h//10) +']' )   # Font Segoe UI Semibold
            # sys.stdout.write('\r' + str(h)+' % ['+'#'*h+str(' ')*(100-h) +']' )         #  Calibri, Adjust the numbers, for the font of your configuration
            # sys.stdout.flush()
    return print('\nAnswer : \t', S )

# first_solution(10**6)              # Answer : 	 18613426663617118



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n=========  My SECOND SOLUTION,     ===============\n')
t1  = time.time()

def get_smallest_connection(p1, p2):
    """
    Find smallest n such that n is divisible by p2 and n = a_p1 where _ is concatenation

    Suppose p1 is 2 digits...
    100*a + p1 = 0   | mod p2
    100*a = p2-p1    | mod p2
    (100 % p2) * a = p2-p1     | mod p2
    a = (p2-p1) * (100 %p2)**(-1)     | mod p2

    replace (by Euler's theorem):
    k**(-1) = k**(p2-2)     | mod p2
    """
    p1, p2 = int(p1), int(p2)
    pow10 = 10**len(str(p1))
    a = ((p2-p1) * pow(pow10 % p2, p2-2, p2)) % p2

    # print(pow10, p2-p1, pow10%p2, pow(pow10 % p2, p2-2, p2), a)
    ans = a*pow10+p1
    return ans

limit = 10**6
primes = primesieve(limit+10)

S=0
for i in range(2, len(primes)-1) :
        p1, p2 = primes[i], primes[i+1]
        n =  get_smallest_connection( p1, p2)
        S +=n
        # print( p1, p2 , n )

print('\nAnswer : \t', S )


# first_solution(10**6)              # Answer : 	 18613426663617118





#
#
# def first_solution(limit) :
#     h=1
#     primes = primesieve(limit+10)
#     print( len(primes) ,primes[-5::],'\n')
#     S=0
#     for i in range(2, len(primes)-1) :
#         p1, p2 = primes[i], primes[i+1]
#         A =  get_sufix( p1, p2)
#         n = int(str(A)+str(p1))
#         S +=n
#         print( p1, p2 , A )
#         if i*100 // len(primes)  > h-1 :        # Progress Bar #
#             h += 1
#             # sys.stdout.write("\r%d%%-" %h )
#             sys.stdout.write('\r' + str(h)+' % ['+'#'*h+str(' ')*(220-22*h//10) +']' )   # Font Segoe UI Semibold
#             # sys.stdout.write('\r' + str(h)+' % ['+'#'*h+str(' ')*(100-h) +']' )         #  Calibri, Adjust the numbers, for the font of your configuration
#             # sys.stdout.flush()
#     return print('\nAnswer : \t', S )
#




t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,   --------------------------')
t1  = time.time()

# ==== Thu, 22 May 2014, 23:33, Paul Crowley, England

def primesUpTo(n):
    yield 2 # assume n >= 2
    sieve = [True]*(n+1)
    for i in range(3,n+1,2):
        if sieve[i]:
            yield i
            for j in range(i*i,n+1,i*2):
                sieve[j] = False

def extendedEuclid(a, b):
    if b == 0:
        return a, 1, 0
    k, q = a // b, a % b # a = kb + q
    g, xp, yp = extendedEuclid(b, a % b)
    # g = xp * b + yp * q
    #   = xp * b + yp * (a - kb)
    #   = (xp - k*yp) * b * yp * a
    return g, yp, xp - k * yp

def answers():
    primes = list(primesUpTo(1000010))
    for p1, p2 in zip(primes[2:-1], primes[3:]):
        m = 10**len(str(p1))
        g, x, y = extendedEuclid(m, p2)
        r = (p1*p2*y) % (p2 * m)
        #print p1, p2, r
        yield r

print (sum(answers()))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2, Fermat s little theorem --- SUPER FAST  --------------------------')
t1  = time.time()


# ===== Mon, 15 Sep 2014, 15:42, That Guy, Israel
# Efficient solution written in python. Takes about 0.67 seconds.
#
# The math behind the code:
# lets say we have to prime numbers - p1 and p2 and a third number - a.
# (p1 is the small prime, p2 is the large prime and a is 10^(digits of p1))
#
# In this problem we would like to find the minimal n for which:
# a∗n = −p1(mod p_2)
#
# From now on:
# b = p_1
# c = p_2
#
# So:
# a ∗ n ≡ −b(mod c)
#
# Now we add c to the right side:
# a∗n≡(c−b)(mod c)
#
# We can simplify the problem by saying that-
# n = n_2∗(c−b)
#
# So:
# a∗n_2 ≡ 1(mod c)
#
# According to Fermat's little theorem:
# (for a prime number c)
# a**(c−1) ≡ 1 (mod c)
#
# So if :
# n_2 = a**(c−2)
# we have found a solution.
#
# Therefore:
# n=(a**(c−2)∗(c−b))%c
#
# In the code I used the function 'pow' so the code is pretty fast.



# Checks if n is a prime number
def prime_check(n):
    if(n < 3):
        return n==2

    for i in range(3, int(n**0.5)+1, 2):
        if(n % i == 0):
            return 0

    return 1

# prime1 < prime2
# s ends with [prime1]
# s % prime2 = 0
def get_s_2(prime1, prime2):
    digits = len(str(prime1))

    a = pow(10, digits, prime2)
    b = prime1
    c = prime2

    ret_s = pow(a, c-2, c) * (c - b) % c

    return int(str(ret_s) + str(prime1))

# Generates all primes under n
def prime_gen(n):
    good = [1] * n
    for i in range(3, int(n**0.5) + 1, 2):
        if(good[i]):
            good[2*i::i] = [0] * ((n-1)// i -1)

    return [2] + [i for i in range(3, n, 2) if good[i]]

# Generate all primes under 1000000
primes = prime_gen(1000000)

i = 1000000

# Find the first prime over 1000000 and add it
while(not prime_check(i)):
    i+= 1

primes += [i]

fin_sum = 0

# For every prime number, add the minimal number that fits the problem
for i in range(2, len(primes) - 1):
    fin_sum += get_s_2(primes[i], primes[i+1])

print (fin_sum)



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,  SUPER ELEGANT, EULER THEOREM --------------------------')
t1  = time.time()

# ===== Fri, 7 Nov 2014, 06:46 , grovert, USA
# Short solution in Python... Runs in less than 0.2 seconds (0.14 seconds after prime number generation)... Runs in 0.07 seconds with pypy.


#134
def getn(p1, p2):
    """
    Find smallest n such that n is divisible by p2 and n = a_p1 where _ is concatenation

    Suppose p1 is 2 digits...
    100*a + p1 = 0   | mod p2
    100*a = p2-p1    | mod p2
    (100 % p2) * a = p2-p1     | mod p2
    a = (p2-p1) * (100 %p2)**(-1)     | mod p2

    replace (by Euler's theorem):
    k**(-1) = k**(p2-2)     | mod p2
    """
    pow10 = 10**len(str(p1))
    a = ((p2-p1) * pow( pow10 % p2, p2-2, p2 ))%p2
    ans = a*pow10+p1
    return ans

def p134():
    ps = prime_gen(10**6+10)
    print (sum(getn(ps[i], ps[i+1]) for i in range(2, len(ps)-1)))

p134()


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,   --------------------------')
t1  = time.time()

# ==== Mon, 12 Dec 2016, 14:14, mbh038, England
# About 700 ms in Python. A blessed relief to be here after 10 days of failing to solve everything I have attempted!
#
# I realised, eventually, that for each prime pair this could be cast as a problem in solving
# the linear Diophantine equation ax+by=c where bb is the larger of the two primes, c is the smaller and −a is 10**n
# , where n is the number of digits in c. Thus, for the prime pair 19 and 23, for example, {a,b,c} are {−100,23,19}.
#
# Given a solution x1,y1 to a prime pair, a possible value for S is S=−ax1+c,
# but to find the minimum value of S we need to find the minimum positive value of x1.
#
# I used a Euclid-esque recursive function to find a solution x1,y1 to each of the Diophantine equations,
# then invoked the fact that, given any solution x1,y1, all x=x1−nb/gcd(a,b) and y=y1+na/gcd(a,b)
# are also solutions, for integer values of n. Given that b is prime and a is a power of 10,
# gcd(a,b)=1, so  our  solutions for x are x=x1−nb.
# The minimum positive value of x is thus x1 (mod b).


import math
import numpy as np
import sympy as sp


def p134(limit):


    ps=primesieve(limit)[2:]
    ps=np.append(ps,sp.nextprime(limit))   #the pesky extra prime at the end!

    S=0
    for i in range(len(ps)-1) :
        a=-10**(int(math.log10(ps[i]))+1)
        b=ps[i+1]
        c=ps[i]
        x1,y1=primeLD(a,b,c)
        x=x1%b   #b is prime, and a is a multiple of 100, so gcd(a,b)=1
        S+=-a*x+c
    print(S)

def primeLD(a,b,c):
    """finds a solution to diophantine equation ax+by=c"""
    q,r=a//b,a%b
    if r==0:
        return 0,c//b
    u,v=primeLD(b,r,c)
    return v,u-q*v

def primesieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]

p134(10**6)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5,   --------------------------')
t1  = time.time()

===== Sat, 15 Aug 2009, 01:02, PyRangers, Bulgaria

def extendedGCD(a, b):
    if not a % b:
        return (0, 1)
    else:
        (x, y) = extendedGCD(b, a % b)
        return (y, x - y*(a // b))

primes = primes

total = 0
for i in range(2, len(primes)-1):
    a = primes[i]
    b = primes[i+1]

    pt = 10 ** len(str(a))
    x = b - a
    r, s = extendedGCD(pt, b)
    solution = (r*x) % b
    answer = solution * pt + a
    total += answer

print (total)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6,   --------------------------')
t1  = time.time()



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

