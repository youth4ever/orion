#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Fri, 11 Nov 2016, 23:21
#The  Euler Project  https://projecteuler.net
'''
    Using up to one million tiles how many different "hollow" square laminae can be formed?         -       Problem 173

We shall define a square lamina to be a square outline with a square "hole" so that the shape possesses vertical
and horizontal symmetry. For example, using exactly thirty-two square tiles we can form two different square laminae:

With one-hundred tiles, and not necessarily using all of the tiles at one time,
it is possible to form forty-one different square laminae.

with 100 tiles => 41 configurations

Using up to one million tiles how many different square laminae can be formed?
'''
import time
from math import sqrt

print('--------------------------TESTS------------------------------')


def gen_square_hole(i, n):
    ''':Description:
    :param:
            :n:     -       side of the square         2i+1     <   n <   infinity
            :i:     -       thickness of the sides,     1 <  i <= n/2-1    '''
    if n%2 ==0:
        if  i <= (n/2)-1 :
            return 4*i*(n-i)
        else : return 0
    if n%2 == 1:
        if  i < n/2 :
            return 4*i*(n-i)
        else : return 0

print('\n--------------------------- JUST TESTS ----------------------')

print('Generate square hole function test :  ', gen_square_hole(4, 7))
print('Generate square hole function test :  ', gen_square_hole(2, 5))



print('\n================  My FIRST SOLUTION,   ===============\n')

t1  = time.time()

f =1e6
counter=0
for i in range(1, int(sqrt(f)), 1 ):
    for n in range(3,   int((f+4*i*i)/(4*i))+1  ):
        tiles = gen_square_hole(i, n)
        if tiles !=0 :
            # print('Thickness:  ',i, '   ; Side : ',n , ' ;  Tiles: ' ,tiles)
            counter+=1

print(counter)              # Answer    1572729

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')          # Completed in : 3960.226536 ms




print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,   --------------------------')
t1  = time.time()

# =====Sun, 22 Jan 2017, 21:45, zinger_13, Canada

nmax = 10**6
smax = int(nmax//4) # corresponds to edge width + inner square side length
emax = int(smax**0.5) # corresponds to edge width

ans = 0
for e in range(1, emax): # for e = emax we have a hole of size 0 (i.e. no hole)
    ans += smax//e-e

print(ans)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2, aolea, Spain  --------------------------')
t1  = time.time()
# Easy problem, just count required tiles depending on the size of the hole and the possible rows.

tiles = 10**6
hole_max = int((tiles-4)/4)
hole_size = 1
count = 0

while hole_size <= hole_max:
    tiles_new_row = hole_size*4 + 4
    tiles_left = tiles
    while tiles_left >= tiles_new_row:
        count = count + 1
        tiles_left = tiles_left - tiles_new_row
        tiles_new_row = tiles_new_row + 8
    hole_size = hole_size + 1
print(count)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3, ChopinPlover, Taiwan  --------------------------')
t1  = time.time()
# Consider the thick of hollow square instead.  If the thick is tt,
# then the # of total tiles of hollow squares of side xx is 4tx+4t24tx+4t2.
# # Solve 4tx+4t2≤10000004tx+4t2≤1000000, and then we have x=1...⌊(250000−t2)/t⌋x=1...⌊(250000−t2)/t⌋.
#  So the answer is sum of every ⌊(250000−t2)/t⌋⌊(250000−t2)/t⌋ over t=1...499t=1...499.

print(sum([int((250000-t**2)/t) for t in range(1, 500)]))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4, brainiac1530, USA  --------------------------')
t1  = time.time()

from math import sqrt

from itertools import accumulate, islice
m, soln, MAX = 4, 0, 10**6
for n in islice(accumulate(range(1,2000,2)),1,None,2):
    soln = soln + MAX // m - n // m
    m += 4
print(soln)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5, Esco, USA  --------------------------')
t1  = time.time()

from math import ceil
MAX = 1000000
count = 0
for m in range(3, int(MAX/4) + 2):
        count += (m - int(ceil((max(m**2 - MAX, 1))**.5)))//2
print (count)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6,   --------------------------')
t1  = time.time()

# ===== Mon, 21 Nov 2016, 00:27, mbh038, England
# 260 ms in Python

import math

def p173(n):
    amin=3
    amax=(n+4)//4
    total=0
    for a in range(amin,amax+1):
        bsqmin=a**2-n
        b= 2 - a%2
        if bsqmin>1:
            b = max(b,math.ceil((bsqmin)**.5))
        total += (a-b)//2
    print( total )

p173(10**6)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')




