#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Wed, 21 Sep 2016, 22:21
#The  Euler Project  https://projecteuler.net
'''
Ordered fractions       -       Problem 71
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.
If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:
1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
It can be seen that 2/5 is the fraction immediately to the left of 3/7.
By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size,
find the numerator of the fraction immediately to the left of 3/7.
'''
import time
print('------------------   MY SOLUTION, Corrected in 2016-09-24, 16:00 ---------------------------')
t1  = time.time()

#   using  DYNAMIC RANGING :

max_nr = 0.4
iter=1
for i in range (999900, 1000000):
    for j in range(int(i*3/7), int(i*3/7)+1) :
        iter+=1
        if ( max_nr < j/i < 3/7  ):         # ATTENTION !!!  What an ERROR LOGIC CAUGHT ME HERE
            max_nr, a , b = j/i , j, i                                          # I put max_nr < 3/7 instead of j/i < 3/7
            #print(str(iter)+'.   j , i = ',j ,', ' , i  , '  ;   ',max_nr,'  ;  ', j / i,'  ; 3/7 = ',3/7)            # Correct : 428570   /  999997

print('\nAnd the ANSWER is :     ',a, b, max_nr)
#time.sleep(1)
t2  = time.time()
print('\nCompleted in :', (t2-t1)*1000, 'ms')                       #Completed in : 3.00 ms

print('-------'*20)




print('\n===============  SOLUTIONS FROM THE EULER FORUM ===============')
print('\n--------------SOLUTION 1 ----------Heureka, from Russia------------')
# Incredible solution
# https://en.wikipedia.org/wiki/Stern%E2%80%93Brocot_tree
t1  = time.time()

M = 1000000

n = 2
d = 5

while d + 7 <= M:
    n = n + 3
    d = d + 7

print(n, d)

t2  = time.time()
print('\nCompleted in :', (t2-t1)*1000, 'ms')

print('\n--------------------SOLUTION 2 ---------------------')

t1  = time.time()

from fractions import Fraction

d = 1000000
lower = int ((3/7 * d) - 50) #as close as possible to 3/7
set1 = set()

while d > 0:
    for i in range (lower,d):
        if i/d < 3/7:
            set1.add(Fraction(i,d))
        else: break
    d -= 1

listAns = sorted(list(set1))
print(listAns[-1].numerator)

t2  = time.time()
print('\nCompleted in :', (t2-t1)*1000, 'ms')

print('\n--------------------SOLUTION 3 ---------------------')
t1  = time.time()

from fractions import Fraction

a=max([Fraction(int((3000000-i)/7),1000000)for i in range(1,100)])
print (max([Fraction(x,y) for x in range(a.numerator-3,a.numerator+3) for y in range (a.denominator-3,a.denominator+1) if float(x)/y<float(3)/7]))

t2  = time.time()
print('\nCompleted in :', (t2-t1)*1000, 'ms')

print('\n--------------------SOLUTION 4 - Brute Force, by davidmcdavid from England ---------------------')
t1  = time.time()

#Brute force with floats in Python3:
target = 3/7
nearest = float('inf')
for d in range(1, 1000000+1):
    n = d*3//7
    distance = target-n/d
    if nearest > distance and distance != 0:
        nearest = distance
        answer = n
print(answer)
assert answer==428570

t2  = time.time()
print('\nCompleted in :', (t2-t1)*1000, 'ms')

print('\n--------------------SOLUTION 5 - Brute Force 2---------------------')
t1  = time.time()

#Brute force in Python 3.
# For i in range(1,000,000), calculate the closest number to 3/7 without going over and then compare it to a running total of the closest.

upper = [3, 7]
lower = [1,3]

for i in range(2,10**6):
    num = (upper[0] * i - 1) // upper[1]
    potential = [num, i]
    if potential[0] * lower[1] > potential[1] * lower[0]:
        lower = potential
print(lower)

t2  = time.time()
print('\nCompleted in :', (t2-t1)*1000, 'ms')

