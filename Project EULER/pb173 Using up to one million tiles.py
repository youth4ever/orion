#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Fri, 11 Nov 2016, 23:21
#The  Euler Project  https://projecteuler.net
'''
    Using up to one million tiles how many different "hollow" square laminae can be formed?         -       Problem 173
We shall define a square lamina to be a square outline with a square "hole" so that the shape possesses vertical
and horizontal symmetry. For example, using exactly thirty-two square tiles we can form two different square laminae:

With one-hundred tiles, and not necessarily using all of the tiles at one time, it is possible to form forty-one different square laminae.
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
            :i:     -       thickness of the sides,     1 <  i <= n/2-1
    '''
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
for i in range(1, int(sqrt(f)) ):
    for n in range(3,   int((f+4*i*i)/(4*i))+1  ):
        tiles = gen_square_hole(i,n)
        if tiles !=0 :
            # print('Thickness:  ',i, '   ; Side : ',n , ' ;  Tiles: ' ,tiles)
            counter+=1

print(counter)              # Answer    1572729

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')          # Completed in : 3960.226536 ms




print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1, TanasaIoan, Romania  --------------------------')
t1  = time.time()
# I've used a little bit of mathematics on this one: each layer which is X long is composed of
# 4*(X-1) squares, and you just keep adding squares with an increment of 2
# (because the length of the squares can be either odd or even for all the squares) and i used 4*(x-1)=10^6 to find out the limit of the list.

L=[4*(i-1) for i in range(2,10**4*5**2+2)]
result=0
for n in range(0,len(L)):
    S=L[n]
    a=0
    while S<=10**6:
        a+=2
        result+=1
        if a+n>=len(L):
            break
        S+=L[n+a]

print(result)


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
# Consider the thick of hollow square instead.  If the thick is tt, then the # of total tiles of hollow squares of side xx is 4tx+4t24tx+4t2.
# # Solve 4tx+4t2≤10000004tx+4t2≤1000000, and then we have x=1...⌊(250000−t2)/t⌋x=1...⌊(250000−t2)/t⌋.
#  So the answer is sum of every ⌊(250000−t2)/t⌋⌊(250000−t2)/t⌋ over t=1...499t=1...499.

print(sum([int((250000-t**2)/t) for t in range(1, 500)]))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4, brainiac1530, USA  --------------------------')
t1  = time.time()

from math import sqrt

from itertools import accumulate,islice
m,soln,MAX = 4,0,10**6
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
        count += (m - int(ceil((max(m**2 - MAX, 1))**.5)))/2
print (count)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


# print('\n--------------------------SOLUTION 6,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
