#!/usr/bin/python3
# Solved by Bogdan Trif @   Completed on Fri, 7 Oct 2016, 18:49
#The  Euler Project  https://projecteuler.net
'''
Integer right triangles     -       Problem 39
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
{20,48,52}, {24,45,51}, {30,40,50}
For which value of p ≤ 1000, is the number of solutions maximised?
'''
import time
print('------------------------MY SOLUTION , Non-Optimized------------------------------')

t1  = time.time()

P = []
maxc=0
for p in range(12, 1001, 2):
    t=[]
    for c in range(int(p/3), int(p/2+1)):
        for b in range(int(2*c/3), c):
            a = p - c - b
            if a**2 + b**2 == c**2 and a >0 and b > a :
                t.append(p)
                #print(a, b , c , p, t )
                P.append(t[0])
    if len(t) > maxc:
        maxc, maxv = len(t), t[0]
        print(t[0],len(t))

print('\nThe number: ', maxv)
print(len(set(P)), set(P))

#Count the number of occurences in a list
#P = ([[x, P.count(x)] for x in set(P)])


t2  = time.time()
print('\nCompleted in :', round((t2-t1),4), 's')        # Completed in : 11.7962 s


print('\n================= OTHER SOLUTIONS FROM THE EULER FORUM ==================')
print('\n------------------------------ SOLUTION 1 ,  JMoc1978 -------------------------------------------')
t1  = time.time()
import math

def TriangleSums(n):
    Perimeters = []
    for a in range(1, n//2):
        for b in range(a, n//2):
            c = math.sqrt(a**2 + b**2)
            if c == int(c):
                p = a + b + int(c)
                Perimeters.append(p)
    return sorted(Perimeters)

def Counts(n):
    Perimeters = TriangleSums(n)
    Counter = 0
    Number = 0
    for i in Perimeters:
        if i > n:
            break
        if Perimeters.count(i) >= Counter:
            Counter = Perimeters.count(i)
            Number = i
    return Number, Counter

print(Counts(1000))


t2  = time.time()
print('\nCompleted in :', (t2-t1)*1000, 'ms')           #


print('\n------------------------------ SOLUTION 2 , Brian038  -------------------------------------------')
# My python version:
# 1. Pythagorean triples must have two or zero odd numbers, so the sum must be even, no point in checking odd numbers.
# 2. Once I have the first number, the other two can be calculated using:
# [a, b, c] - the three numbers
# p=a+b+c
# x=p−a
# c=(x**2+a**2)/2x
#
# So just make sure c and b are positive integers, and b is larger than a (to avoid repetitions).


t1  = time.time()

topCount = 0
for p in range(12,1001,2):
    count = 0
    for a in range(3,p):
        x = p - a
        y = a**2
        # So, given the a+b+c=p and a^2+b^2=c^2, we can solve to determine that c=(x^2+y)/2x
        c = (x**2+y)/2/x
        b = p - a - c
        if int(c) == c and c > b and b >= a:
            count += 1

    if count>topCount:
        print("New max count",count," for ",p)
        topCount = count

t2  = time.time()
print('\nCompleted in :', (t2-t1)*1000, 'ms')           # Completed in : 272.0155715942383 ms



print('\n------------------------------ SOLUTION 3, THE BEST & THE FASTEST -------------------------------------------')
t1  = time.time()

from math import gcd
def method1(limit=1000):
    """
    Generate primitive Pythagorean triplets using Euclids formula.
    (http://mathforum.org/library/drmath/view/55811.html - Doctor Rob)
    In this formula:
    - note that p = a+b+c = 2*m*(m + n), so no need to calculate (a, b, c) - just p.
    - also, if (a, b, c) is a triplet, then so is (k*a, k*b, k*c) - with perimeter k*p....
    Use a list to count solutions per perimeter.
    This code assumes there is a unique maximum - I don't know if this is true
    for all limits.
    (some code based on ideas of janshigola and ephemeral on euler project forum)
    (see pb 9)
    """
    solutions = [0]*limit
    m, n, p = 2, 1, 12  # initial values
    while p < limit:
        while p < limit and n < m:
            for kp in range(p, limit, p): # count k*p solutions within bounds
                solutions[kp] += 1
            # now find next n, relatively prime to m:
            n += 2
            while gcd(m, n) != 1:
                n += 2
            p = 2*m*(m + n)
        m, n = m+1, (1 if m&1 else 2)     # make sure m and n have opposite parity
        p = 2*m*(m + n)
    return solutions.index(max(solutions))

print(method1(1000))

t2  = time.time()
print('\nCompleted in :', (t2-t1)*1000, 'ms')


t1  = time.time()

maxcount = 0
maxn = 0
for n in range(1000, 0, -1):
	count = 0
	for b in range(1, int(n/2)):
		if (n*(n-2*b)) % (2*(n-b)) != 0:
			continue
		a = (n * (n - 2*b)) // (2 * (n-b))
		c = n - a - b
		if a < 1 or c < 1:
			continue
		count += 1
	if count > maxcount:
		maxcount = count
		maxn = n
print(maxcount, maxn)

t2  = time.time()
print('\nCompleted in :', (t2-t1)*1000, 'ms')       # Completed in : 256.0145854949951 ms



print('\n------------------------------ SOLUTION 4 -------------------------------------------')

t1  = time.time()

def perimeters(max_perimeter):
    max_length = int((max_perimeter / 12) * 5)
    results = []
    for a in range(1, max_length):
        for b in range(1, a):
            c = (a ** 2 + b ** 2) ** 0.5
            if c == int(c):
                p = a + b + int(c)
                results.append(p)
    return sorted(results)

def solve():
    all_perimeters = perimeters(1000)
    maximised = [0, 0]
    for i in all_perimeters:
        if all_perimeters.count(i) > maximised[0]:
            maximised[0] = all_perimeters.count(i)
            maximised[1] = i
    return maximised[1]

print(solve())



t2  = time.time()
print('\nCompleted in :', (t2-t1)*1000, 'ms')           # Completed in : 272.0155715942383 ms