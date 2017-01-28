#!/usr/bin/python
# Solved by Bogdan Trif @       Completed on Tue, 24 Jan 2017, 20:32
#The  Euler Project  https://projecteuler.net
'''
Investigating the behaviour of a recursively defined sequence       -       Problem 197

Given is the function f(x) = ⌊2**(30.403243784-x**2)⌋ × 10**-9 ( ⌊ ⌋ is the floor-function),
the sequence un is defined by u_0 = -1 and u_(n+1_ = f(u_n).

Find u_n + u_(n+1) for n = 10**12.

Give your answer with 9 digits after the decimal point.

'''
import time
from math import floor







print('\n--------------------------TESTS------------------------------')
t1  = time.time()



def f(x) :
    return floor(2**(30.403243784 - x**2)) * 10**(-9)

def recursive_gen(limit ) :
    u = -1
    for i in range(1, limit +1) :
        # print(u, f(u))
        u = f(u )
        yield u, f(u)

limit = 10**3
G = recursive_gen(limit)

for i in range(1, limit+1) :
    k = next(G)
    # print(i , k )
    if k[0] == 0.681175878 : break

print('\nAnswer : \t', sum(k))          #       Answer : 	 1.710637717




t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()







# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 0,   --------------------------')
# t1  = time.time()
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 1,   --------------------------')
t1  = time.time()

# ==== Wed, 23 Dec 2015, 23:09, prune, Romania
# I coded this the way I'd give it to my students: lots of intermediate results and room to slip in
# debugging statements.  Python code runs just over half a millisecond.

import time
start = time.time()

c = 30.403243784

u = -1
last_u = 0
n = 0
scale = 1e-9
last_sum = 0
while n <= 10**12:
    n += 1

    # Evaluate function
    expon = c - u*u
    whole = int(2**expon)
    u = whole * scale

    # Check for repetition of f(u(n)) + f(u(n+1)
    this_sum = last_u + u
    if this_sum == last_sum:
        break
    last_sum = this_sum
    last_u = u

lag = time.time() - start
print ("Solution:", last_sum)
print (lag, "sec.")

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,   --------------------------')
t1  = time.time()

# ==== Sun, 9 Nov 2014, 06:12, KING-OLE, Denmark
# Took less than a second in Python.
# I discovered (like I see many others before me has) that the results iterates with n=10^p when p >= 3.
# So, the fastest code I could come up with has n=1000.

import math
u=-1

def f(x):
  return math.floor(2**(30.403243784-(x**2)))*(10**-9)

for n in range(1,1001):
  u=f(u)

u2=f(u)

print(u+u2)

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
