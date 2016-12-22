#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Tue, 22 Nov 2016, 20:49
#The  Euler Project  https://projecteuler.net
'''
                                    Square remainders   -   Problem 120

Let r be the remainder when (a−1)**n + (a+1)**n is divided by a**2.

For example, if a = 7 and n = 3, then r = 42: 6**3 + 8**3 = 728 ≡ 42 mod 49.
And as n varies, so too will r, but for a = 7 it turns out that rmax = 42.

For 3 ≤ a ≤ 1000, find ∑ r_max.
'''
import time

print('\n--------------------------TESTS------------------------------')

print(728%49)

f = lambda a, n : ( (a-1)**n + (a+1)**n )%(a*a)

print(f(7,7))


for a in range(3,20):
    for n in range(1,5*a):
        print('a=',a,'   n=',n,'     r=',f(a,n))





print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

R=0
for a in range(3,1001):
    if a%2 ==1 :
        r = a*(a-1)
    elif a%2 == 0 :
        r = a*(a-2)
    R+=r

print('\nAnswer : ', R)                    # Answer :  333082500


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')          # Completed in : 0.999928 ms


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1, mbh038, England  --------------------------')
t1  = time.time()
# About 0.2 ms in Python. I just calculated rmax for aa up to 100 or so and saw the pattern:
# for even a, rmax=a(a−2),
# for odd a, rmax=(a−1)a so that,
# for all a, rmax=(a+a mod 2−2)a.
# From there on it is a one liner.


def p120(amin=3,amax=1000):

    print(sum([a*(a+a%2-2) for a in range(amin,amax+1)]))

def maxr(alist):
    for a in alist:
        rmax=-1
        nmax=-1
        for n in range(1,1000):
            ran=r(a,n)
            if ran>rmax:
                rmax=ran
                nmax=n
        print(a,nmax,max)

p120()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,  aolea Spain --------------------------')
t1  = time.time()
# All the terms in the binomial expansion are divisible by a**2 except the last one,
# this one is the one that gives us the remainder, when n is even is always 2 and when n is odd
# is always 2*n*a so the issue is to find the biggest 2*n smaller than a.
# So 2n = a-1 when a is odd because obviously 2n must be even
# 2n = a -2 when a is even
# Less than 1 ms in python

sum = 0
for a in range(3,1001):
    if a % 2 == 0:
        sum = sum + a*(a-2)
    else:
        sum = sum + a*(a-1)
print(sum)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3, Khalid, Saudi Arabia  --------------------------')
t1  = time.time()
# I didn't reach the level of simplification that some people arrived at, but I got that only the last two terms matter,
# and that it will come out to i*a where i is in 6, 10, 14, 18, 22 ...
# So I just went with that, and it worked.

def r_max(num):
    max = 0
    square = num**2
    debug = False
    for n in range(1, num+1):
        result = (2 + n * 4) * num % square
        if result > max:
            max = result
    return max

start = 3
end = 1000
total = 0
for n in range(start, end+1):
    total += r_max(n)

print (total)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

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
