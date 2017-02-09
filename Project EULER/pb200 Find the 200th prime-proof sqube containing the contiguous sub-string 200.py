#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
Find the 200th prime-proof sqube containing the contiguous sub-string "200"         -       Problem 200

We shall define a sqube to be a number of the form, p2q3, where p and q are distinct primes.
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

for i in range(len(P) )  :
    for j in range( i+1 , len(P) ) :
        sqube1 = P[i]**2*P[j]**3
        sqube2 = P[i]**3*P[j]**2
        print(P[i], P[j], '      ',sqube2)
        print(P[i], P[j], '      ',sqube1)

print('\n--------------------------------------')


def prime_proof(n) :
    l = len(str(n))
    m = int(str(1)+ str(n)[1:] )
    print(m)
    for i in range(1, 9):
        m += 10**(l-1)
        print(m)
        if gmpy2.is_prime(n) :  return True
    o = str(n)[:-1]
    for j in [1, 3, 7 ,9] :
        m = int( o + str(j) )
        print(m)
        if gmpy2.is_prime(n) :      return True

    for k in range(1, l):
        print('----------------')
        m = n
        for q in range(0, 10) :
            m = (q * 10**(k)) #% (10**k)
            @2017-01-29, Federer won today 18-th Grand Slamp title at Australian Open
            Must finish the function
            print(m)



    return False


prime_proof (1234567)



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
