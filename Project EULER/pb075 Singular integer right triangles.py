#!/usr/bin/python
# Solved by Bogdan Trif @       Completed on Fri, 28 Oct 2016, 23:04
#The  Euler Project  https://projecteuler.net
'''
                    Singular integer right triangles        -       Problem 75
It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle
in exactly one way, but there are many more examples.

                                                            12 cm: (3,4,5)
                                                            24 cm: (6,8,10)
                                                            30 cm: (5,12,13)
                                                            36 cm: (9,12,15)
                                                            40 cm: (8,15,17)
                                                            48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle,
and other lengths allow more than one solution to be found; for example, using 120 cm it is possible to form
exactly three different integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one integer sided right angle triangle be formed?
'''

import time
from math import gcd

print('\n --------------------------- MY SOLUTION  :) :) ----------------------')


t1  = time.time()

def Pythagorean_triplets(limit=1000):
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
        m, n = m+1, (1 if m & 1 else 2)     # make sure m and n have opposite parity
        p = 2*m*(m + n)
        #print(p, m , n)
    #return solutions.index(max(solutions)), max(solutions)
    #return limit-solutions.count(0)
    return solutions.count(1)


print(Pythagorean_triplets(1500001))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,4), 'ms')      # Completed in : 654.0375 ms


print('\n================= OTHER SOLUTIONS FROM THE EULER FORUM ==================')
print('\n------------------------------ SOLUTION 1 ,  GOOD,  michael15,  -------------------------------------------')

t1  = time.time()

import math

def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t

    return a

N = 1500000

counts = [0]*(N+1)

for m in range(2, int(math.floor(math.sqrt(N/2)))):
    for n in range(1, m):
        if (m - n) % 2 == 1 and gcd(m, n) == 1:
            a = m**2 - n**2
            b = 2*m*n
            c = m**2 + n**2

            k = 1
            while k*(a+b+c) <= N:
                counts[k*(a+b+c)] += 1

                k += 1

print (sum(count == 1 for count in counts))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,4), 'ms')      # Completed in : 654.0375 ms

print('\n------------------------------ SOLUTION 2 ,   -------------------------------------------')

t1  = time.time()
#
# This problem is fantastic! It's very similar to Problem 39.
# I solved for this algorithm:
# Let the side-length a,b,c .
# You can generate a primitive Pythagorean triples for this formula.
#
# If (m−n) mod 2=1   and gcd(m,n)=1
# a = m**2−n**2
# b = 2mn
# c=m**2+n**2
#
# So, the side length is 2m(m+n).
#
# Let x_i the number of "side-length ii primitive Pythagorean triples".
#
# The number of "side-length ii Pythagorean triples" is:
#
#                 s_i=∑(k|i  ; x_k)
#
# You can solve x_1,x_2,…,x_n for O(nlogn)O(nlog n).
# You can solve s_1,s_2,…,s_n for O(nlogn)O(nlog n).
#
# So, the overall time complexity is O(nlog n)

from math import gcd
m,n,maxL=2,1,1500000
good,bad=set(),set()
while 2*m**2+2*m<maxL+1:
    while n<m:
        if gcd(n,m)==1 and (m-n)%2==1:
            L=2*m**2+2*m*n
            k=1
            while k*L<maxL+1:
                if k*L in good:bad|={k*L}
                else:good|={k*L}
                k+=1
        n+=1
    m+=1
    n=1
print(len(good-bad))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,4), 'ms')      #

print('\n------------------------------ SOLUTION 3 ,   -------------------------------------------')
# I wanted to try something different and use matrices for this one, this is what I came up with (About 13 seconds):
t1  = time.time()

import numpy as np

A = [[-1, 2, 2],
     [-2, 1, 2],
     [-2, 2, 3]]

B = [[1, 2, 2],
     [2, 1, 2],
     [2, 2, 3]]

C = [[1, -2, 2],
     [2, -1, 2],
     [2, -2, 3]]

base = np.array([3, 4, 5])

MAX = 1500000
ll = {}
def triplet_length(t):
    lc = t[0] + t[1] + t[2]
    if lc > MAX:
        return True # Target Exceeded
    if lc in ll:
        ll[lc] = False
    else:
        ll[lc] = True
    return False # Continue Calculating

def calc_multiples(t):
    i = 2
    while True:
        m = np.dot(t, i)
        target_exceeded = triplet_length(m)
        if target_exceeded:
            break
        i += 1

def calc_children(t):
    children = [np.dot(A, t), np.dot(B, t), np.dot(C, t)]
    next = []
    for c in children:
        target_exceeded = triplet_length(c)
        if target_exceeded:
            continue
        calc_multiples(c)
        next.append(c)
    if len(next) > 0:
        for c in next:
            calc_children(c)

triplet_length(base)
calc_multiples(base)
calc_children(base)

count = 0
for k in ll:
    if ll[k] == True:
        count += 1

print(count)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,4), 'ms')      # Completed in : 13260.7584 ms

print('\n------------------------------ SOLUTION 4 ,  Ozgur_Ozcelik, Turkey -------------------------------------------')
# Afer the massive Problem-540, this was a very quick implementation.
# Recursively calculate primitive pythagorians, add multiples of each of them to include all non-primitives, eliminate multiple occurances.
# runs in 2 secs

t1  = time.time()

# Project Euler, Problem 075 Singular integer right triangles
#ans=161667

Nmax, Set = 1500000, []

def Primitives(m, n, s):# pr.pythagorians
    if 2*m*(m+n) <= Nmax:
        s += 1
        Set.append(2*m*(m+n))
        mx,nx,s = Primitives(m+2*n,n,s) #1
        mx,nx,s = Primitives(2*m-n,m,s) #2
        mx,nx,s = Primitives(2*m+n,m,s) #3
    return m,n,s

Primitives(2,1,0)

Set2=Set[:]  # appending all multiples of primitive solutions in the set
for i in Set2:
    for t in range(2,1000000):
        if t*i>Nmax: break
        Set.append(t*i)

Set.sort()
Set2=[Set[0]]
if Set[-1]!=Set[-2]: Set2.append(Set[-1])

for i in range(1,len(Set)-1): #selecting only sigle-occurance elements
    if Set[i]!=Set[i-1] and Set[i]!=Set[i+1]:
        Set2.append(Set[i])

Set2.sort()
print('ans=',len(Set2))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,4), 'ms')      # Completed in : 654.0375 ms

print('\n------------------------------ SOLUTION 5 ,   Frexxia, Norway -------------------------------------------')
# 7 lines of Python code. Takes 0.58s (0.15s using PyPy). I did manage to get it to run slightly faster than this (0.5s), but the code is much longer.
t1  = time.time()

from math import floor, gcd, sqrt
from operator import add

N = 1500000
count = [0]*(N+1)
for n in range(1,612):
    for m in range(n+1, floor((sqrt(n**2+2*N) - n)/2)+1, 2):
        if gcd(m,n) == 1:
            count[2*m*(m+n)::2*m*(m+n)] = map(add,count[2*m*(m+n)::2*m*(m+n)],[1]*(N//(2*m*(m+n))+1))
print(sum(c == 1 for c in count))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,4), 'ms')      # Completed in : 1332.0763 ms

print('\n------------------------------ SOLUTION 6 ,   gardener, France -------------------------------------------')
# 7 lines of Python code. Takes 0.58s (0.15s using PyPy). I did manage to get it to run slightly faster than this (0.5s), but the code is much longer.
t1  = time.time()

T=[0]*1500001
for m in range(2,1225):
    for n in range(m-1,0,-2):
        if gcd(m,n)>1:
            continue
        k=1
        s=2*(m*m+m*n)
        while k*s<=1500000:
            T[k*s]+=1
            k+=1
print(T.count(1))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,4), 'ms')      #

