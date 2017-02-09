#!/usr/bin/python                   ( ͡° ͜ʖ ͡°)
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
                Totient Chains      -       Problem 214

Let φ be Euler's Totient function, i.e. for a natural number n,
φ(n) is the number of k, 1 ≤ k ≤ n, for which gcd(k,n) = 1.

By iterating φ, each positive integer generates a decreasing chain of numbers ending in 1.
E.g. if we start with 5 the sequence 5,4,2,1 is generated.
Here is a listing of all chains with length 4:

5,4,2,1
7,6,2,1
8,4,2,1
9,6,2,1
10,4,2,1
12,4,2,1
14,6,2,1
18,6,2,1
Only two of these chains start with a prime, their sum is 12.

What is the sum of all primes less than 40.000.000 which generate a chain of length 25?


'''
import time, gmpy2
import sympy
from pyprimes import factorise

def sieve(n):       # SECOND FASTEST
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def prime_generator(lower, upper):      #THIRD FASTEST
    """  Sieve of Eratosthenes              !!!!!!!!! THE FASTEST SIEVE. It won the battle with sieve
    Create a candidate list within which non-primes will be marked as None.         """
    cand = [i for i in range(3, upper + 1, 2)]
    end = int(upper ** 0.5) // 2

    # Loop over candidates (cand), marking out each multiple.
    for i in range(end):
        if cand[i]:
            cand[cand[i] + i::cand[i]] = [None] * ( (upper // cand[i]) - (upper // (2 * cand[i])) - 1 )

    # Filter out non-primes and return the list.
    return [2] + [ i for i in cand if i and i > lower ]

def Euler_totient(n):   # o(^_^)o  @2017-01-23, 10:30 by Bogdan Trif
    ''':Works without errors !
        https://en.wikipedia.org/w/index.php?title=Euler%27s_totient_function&action=edit&section=3
    :param n: int
    :return: int, Euler Phi, Euler Totient
    '''
    def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
        ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
        return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]
    F = set(get_factors(n))
    for i in F :
        n*=(1-1/i)
    return round(n)


print('\n--------------------------TESTS------------------------------')
t1  = time.time()

NR = list(range( 31455263372, 31455263372+10) )

for i in NR :
    print( sympy.totient(i), end='  ' )

print(sympy.totient(1))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

R = {1:1}
def totient_chain(n):
    n0 = n
    cnt = 1
    while n != 1 :
        if n  in R :
            R[n0] = R[n]+cnt-1
            # print('print\t ',n0,'     R[n0]: ' ,R[n0] ,'     R[n]=' ,R[n], cnt, R[n]+cnt , R )
            return R[n]+cnt-1
        else :
            # print(n,'  ---')
            n = sympy.totient(n)
            cnt+=1
    R[n0] = cnt

    return cnt



def totient_chain1(n):
    if n==1 : return 1
    cnt = 1
    while n != 1 :
        n = sympy.totient(n)
        cnt+=1
    return cnt

# print('\ntotient_chain : \t ', totient_chain1(18) )

print('\n================  My BRUTE FORCE SOLUTION, VERY SLOW, 1 hour  ===============\n')
t1  = time.time()

primes = prime_generator(9.5*10**6, 4*10**7)           # 40.000.000
print(len(primes), primes[:50] , '\n\n')


def brute_force():
    S, cnt =0, 0
    for p in primes:
        # b = totient_chain1(i)
        a = totient_chain(p)
        if a == 25:
            S+=p
        if a >=25 :
            cnt+=1
            print(str(cnt)+'.       ', p ,'          length: ',  a  )

    return print('\nAnswer : \t', S , '\n\n')       #Answer : 	 1677366278943

print('\n', R)


# for i in primes: print(i)

t2  = time.time()
print('\nCompleted in :', round((t2-t1), 6), 's\n\n')


print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()







t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()

try: #i.e. if using Python2
    range=xrange
except Exception:
    pass

from array import array
from itertools import chain, compress, count

#adapted from the pypy code of Animus
def phi_values(N):
    phi = array('l', [0]) * 2 + array('l', [1]) * (N - 1)
    for p, ph in enumerate(phi):
        if ph != 1: continue
        p_pow, multiple = p, p-1
        while p_pow <= N:
            for i in range(p_pow, N + 1, p_pow):
                phi[i] *= multiple
            multiple = p
            p_pow *= p
    return phi

def primes(N):
    '''Iterator of primes up to and including N'''
    b = N - 1 >> 1
    if b <= 0: return iter(())
    B = bytearray([0]) + bytearray([1]) * b
    for c in count(1, 2):
        if B[c >> 1]:
            a = c * c >> 1
            if a > b: return chain([2], compress(count(1, 2), B))
            B[a::c] = bytearray([0]) * ((b - a) // c + 1)

def do(N=4*10**7, k=25):
    phi = phi_values(N // 2) #It sets phi(0)=phi(1)=0
    x = bytearray([0]) * (N // 2 + 1)
    for i in range(1, N // 2 + 1): x[i] = x[phi[i]] + 1
    return sum(p for p in primes(N)
               if x[phi[p // 2] * (2 if p & 3 == 1 else 1)] == k - 2)

print(do())

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

# print('\n--------------------------SOLUTION 3,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
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
