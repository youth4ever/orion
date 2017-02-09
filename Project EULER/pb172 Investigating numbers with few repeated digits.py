#!/usr/bin/python                   ( ͡° ͜ʖ ͡°)
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
Investigating numbers with few repeated digits      -       Problem 172

How many 18-digit numbers n (without leading zeros) are there
such that no digit occurs more than three (3) times in n?

'''
import time, gmpy2



def comb_L( k ) :
    S = 0
    for i in range(2, k+1):
        c = gmpy2.comb(k, i)
        # print(c, S)
        S+=c * 2**(k - i)
    return S

def comb_A(n) :
    k  = n-2
    return k * 3**(k-1) - (k-1)*3**(k-2)

print('\ncomb_L : \t', comb_L(7))
# print('\ncomb_A : \t', comb_A(7))



@ 2017-01-31, 00:40         -       Problema de combinatorica
It is not enough to search only for a digit L , you must be sure that not a single digit
repeats more than 3 times ! you can not cross results from every digit


18 digit :
123456789012345678
Remark in a 30 digit : 123456789012345678901234567890    every digit repeats 3 times
=> You cannot have a 31 digit number which has not at least 1 repeated digit




print('\n--------------------------TESTS------------------------------')
# t1  = time.time()






# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


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
