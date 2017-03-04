#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
Modular inverses        -   Problem 451

Consider the number 15.
There are eight positive numbers less than 15 which are coprime to 15: 1, 2, 4, 7, 8, 11, 13, 14.
The modular inverses of these numbers modulo 15 are: 1, 8, 4, 13, 2, 11, 7, 14
because
1*1 mod 15=1
2*8=16 mod 15=1
4*4=16 mod 15=1
7*13=91 mod 15=1
11*11=121 mod 15=1
14*14=196 mod 15=1

Let I(n) be the largest positive number m smaller than n-1 such that the modular inverse of m modulo n equals m itself.
So I(15)=11.
Also I(100)=51 and I(7)=1.

Find ∑I(n) for 3 ≤ n ≤ 2*10**7

'''
import time
from math import gcd

def egcd(a, b):
    '''     Extended Euclidian Algorithm    '''
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    '''Modular multiplicative inverse function   '''
    g, x, y = egcd(a, m)
    if g != 1:
        # raise Exception('modular inverse does not exist')
        return -1
    else:
        return x % m




print('\n--------------------------TESTS------------------------------')
t1  = time.time()

S=0
for n in range(3, 1001) :
    for i in range(n-2 , 0, -1 ) :
        if gcd(n,i) == 1 :
            m_inv =  modinv(i, n)
            # print(str(i)+'.    ' ,  m_inv )
            if m_inv == i :
                print(str(n)+'.         LMI : ', m_inv ,' corresponding to : ', i)
                break


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

### 2017-02-21, 22:00
# IDEA : We need to find a square which (mod n) == 1. Example
#             27**2 (mod 52) ==1
#             51**2 (mod 100) ==1
#             503**2 (mod 753) ==1
#               1*1 (mod 751) == 1 ==> 751 does not have a != 1 modulo inverse
# There are numbers which have more mods : Like :
#                 281**2 ---> has (mod 470) and (mod 329) == 1
# 912.         LMI :  799  corresponding to :  799
# 950.         LMI :  799  corresponding to :  799

Must build some kind of SIEVE

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
