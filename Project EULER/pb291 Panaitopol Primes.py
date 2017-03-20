#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @     Completed on Sat, 11 Mar 2017, 12:46
#The  Euler Project  https://projecteuler.net
'''
                Panaitopol Primes           -       Problem 291

A prime number p is called a Panaitopol prime if  :

                            p = (x**4 - y**4 ) / (  x**3 + y**3 )

for some positive integers  x and y.

Find how many Panaitopol primes are less than 5×10**15.

'''
import time, zzz, gmpy2
from itertools import count





print('\n--------------------------TESTS------------------------------')
t1  = time.time()

def brute_force(up_lim) :
    cnt = 0
    for x in range(2, up_lim):
        for y in range(1, x ) :
            p = (x**4 - y**4 ) / (  x**3 + y**3 )
            if p %1 ==0 :
                if gmpy2.is_prime(int(p)):
                    cnt+=1
                    print( str(cnt) +'.      ', p, '       x, y = ', x, y )
    return print('\nAnswer : \t', cnt)

# brute_force(5*10**2)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n==========  My FIRST SOLUTION,  8 min, with help from Internet  =============\n')
t1  = time.time()

# https://mathproblems123.wordpress.com/2017/02/04/panaitopol-primes-simple-representation/#comment-10041

def Panaitopol_primes(up_lim) :
    n, cnt = 1, 0
    while 1 :
        p = n**2 + (n+1)**2
        if p >= up_lim : break
        if gmpy2.is_prime(p) :
            cnt +=1
            print(str(cnt)+'.      ',  p, '     ', len(str(p)))

        n+=1

    return print('\nAnswer : \t', cnt)

Panaitopol_primes(5*10**15 )                #       Answer : 	 4037526




t2  = time.time()
print('\nCompleted in :', round((t2-t1)/60 ,6), 'min\n\n')      #   Completed in : 8 min


# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 3,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 4,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
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
#
# print('\n--------------------------SOLUTION 7,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 8,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 9,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 10,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 11,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 12,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

