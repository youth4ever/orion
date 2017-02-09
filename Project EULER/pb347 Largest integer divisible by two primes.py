#!/usr/bin/python                   ( ͡° ͜ʖ ͡°)
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
Largest integer divisible by two primes     -       Problem 347

The largest integer ≤ 100 that is only divisible by both the primes 2 and 3 is 96, as 96 = 32*3 = 25*3.

For two distinct primes p and q let M(p, q, N) be the largest positive integer ≤N
only divisible by both p and q and M(p, q, N)=0 if such a positive integer does not exist.

E.g. M(2, 3, 100)=96.
M(3, 5, 100)=75 and not 90 because 90 is divisible by 2 ,3 and 5.
Also M(2, 73, 100)=0 because there does not exist a positive integer ≤ 100 that is divisible by both 2 and 73.

Let S(N) be the sum of all distinct M(p, q, N). S(100)=2262.

Find S(10 000 000).

'''
import time, gmpy2

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



up_lim = 10**7
primes = sieve( int(up_lim**(1/2)) )










print('\n--------------------------TESTS------------------------------')
t1  = time.time()

S=0
for i in range(2,10**2):
    if gmpy2.is_prime(i) == False :
        g = get_factors(i)
        if len(set(g)) == 2 :
            print(str(i)+'.    ',g )
            S+=i

print('\nSoln :\t', S)


# 201702-02, 22:15 - Not difficult but I need a good IDEA !!!
# Example : Unde 10.000
# get_factors(9996), get_factors(9826),
# Justify how to get to 9826 which is the number [2, 17, 17, 17]) that we are looking for !

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()







# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
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
