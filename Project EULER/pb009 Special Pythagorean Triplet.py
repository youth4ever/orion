#!/usr/bin/python
# Solved by Bogdan Trif @   Sun, 2 Oct 2016, 22:06
#The  Euler Project  https://projecteuler.net
'''
Special Pythagorean triplet     -       Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
import time
from math import gcd

print('------------------- MY FIRST METHOD :( :(----------------------')
t1  = time.time()

def Pythagorean_triplet():
    for a in range(100,500):
        for b in range(100,500):
            for c in range(100,500):
                S = a +b +c
                if  ( S ==  1000 and a**2 + b**2 == c**2 ):
                    return (a ,b ,c , S, a*b*c )            # 31875000

print(Pythagorean_triplet())
t2  = time.time()
print('\nCompleted in :', (t2-t1)*1000, 'ms')           # Completed in: 4238.242387771606 ms

print('\n----------------- MY SECOND METHOD, More Efficient :) :) ----------------------')

t1  = time.time()

def Pythagorean_triplet_2():
    for a in range(100,500):
        for b in range(100,500):
            c = 1000 - a - b
            if  ( a**2 + b**2 == c**2 ):
                return (a ,b ,c , a+b+c , a*b*c )            # 31875000

print(Pythagorean_triplet_2())

t2  = time.time()
print('\nCompleted in :', (t2-t1)*1000, 'ms')                       #Completed in : 103.00588607788086 ms




print('\n===============  SOLUTIONS FROM THE EULER FORUM ===============')
print('\n--------------SOLUTION 1 , pyandi----------------------')
t1  = time.time()

for i in range(334, 500):
     for j in range(1, i):
         k = 1000 - i - j
         if j ** 2 + k ** 2 == i ** 2:
            print(i*j*k)
            break

t2  = time.time()
print('\nCompleted in :', (t2-t1)*1000, 'ms')