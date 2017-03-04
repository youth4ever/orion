#!/usr/bin/python
# Solved by Bogdan Trif @       Completed on Tue, 21 Feb 2017, 20:08
#The  Euler Project  https://projecteuler.net
'''
Prime triplets      -       Problem 196

Build a triangle from all positive integers in the following way:

 1
 2  3
 4  5  6
 7  8  9 10
11 12 13 14 15
16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31 32 33 34 35 36
37 38 39 40 41 42 43 44 45
46 47 48 49 50 51 52 53 54 55
56 57 58 59 60 61 62 63 64 65 66
. . .

Each positive integer has up to eight neighbours in the triangle.

A set of three primes is called a prime triplet if one of the three primes has the other two as neighbours in the triangle.

For example, in the second row, the prime numbers 2 and 3 are elements of some prime triplet.

If row 8 is considered, it contains two primes which are elements of some prime triplet, i.e. 29 and 31.
If row 9 is considered, it contains only one prime which is an element of some prime triplet: 37.

Define S(n) as the sum of the primes in row n which are elements of any prime triplet.
Then S(8)=60 and S(9)=37.

You are given that S(10000)=950007619.

Find  S(5678027) + S(7208785).


'''
import time, gmpy2
import sys
from math import ceil, sqrt

sys.path.append('d:/Google Drive/Computing & PROGRAMMING/Python/WORK/simple scripts/primes_work_tool')
a =  'd:/Google Drive/Computing & PROGRAMMING/Python/WORK/simple scripts/primes_work_tool'
sys.path.insert(0, a)
# import a
print(sys.path)


def get_row_of_number(n) :
    return ceil(-1/2 + ( pow(1+4*2*n, 1/2 ))/2)

def get_row_first_last_elem(row):
    first_elem = (row-1)*row//2 +1
    last_elem = first_elem + row-1

    return first_elem, last_elem

def get_personal_neighbours( nr ):
    row = get_row_of_number(nr)
    down, up = get_row_first_last_elem(row)
    p = nr
    D = {}
    if p == down:
        P = (a, b, c, d, e) = (p-row+1, p-row+2, p+1, p+row, p+row+1)
        D[row-1] ,  D[row] ,  D[row+1] ,   = [p-row+1, p-row+2], [p+1], [p+row, p+row+1]
    if p == up-1:
        P = (a, b, c, d, e, f, g) = (p-row, p-row+1, p-1, p+1, p+row-1, p+row, p+row+1)
        D[row-1] ,  D[row] ,  D[row+1] ,   = [p-row+1, p-row+2], [p-1, p+1], [p+row-1, p+row, p+row+1]
    if p == up:
        P = (a, b, c, d, e) = (p-row, p-1,  p+row-1, p+row, p+row+1 )
        D[row-1] ,  D[row] ,  D[row+1] ,   = [p-row+1], [p-1], [p+row-1, p+row, p+row+1 ]
    elif p>down and p < up-1 :
        P = ( a, b, c, d, e, f, g, h ) = ( p-row, p-row+1,  p-row+2, p-1, p+1, p+row-1, p+row, p+row+1 )
        D[row-1] ,  D[row] ,  D[row+1] ,   = [ p-row, p-row+1,  p-row+2], [p-1, p+1], [p+row-1, p+row, p+row+1]

    print(str(p)+'.      ', P ,'        ', D )
    return P


print('\nget_personal_neighbours : \t', get_personal_neighbours( 29 ))
print('\nget_personal_neighbours : \t', get_personal_neighbours( 38 ))


print('\nget_row_first_last_elem : \t', get_row_first_last_elem(row = 8) )

print('\n--------------------------TESTS------------------------------')
t1  = time.time()


l = [22, 13, 45, 50, 98, 69, 43, 44, 1]
[x+1 if x >= 45 else x+5 for x in l]

T = []

pos = 1
for i in range(1, 20 ) :
    V = [j for  j in range(pos, pos + i) ]
    print( V )
    # V = [j  if gmpy2.is_prime(j) else 0 for  j in range(pos, pos+i) ]
    T .append([j  if gmpy2.is_prime(j) else 0 for  j in range(pos, pos+i) ])
    pos = V[-1]+1
print('\n-------------------')

for i in range(len(T)):
    print(T[i])



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n================  My FIRST SOLUTION,  45 sec ===============\n')
t1  = time.time()


def get_prime_neighbours( nr ):
    row = get_row_of_number(nr)
    down, up = get_row_first_last_elem(row)
    p = nr

    if p == down:
        P =  (p-row+1, p-row+2, p+1, p+row, p+row+1)
    if p == up-1:
        P = (p-row, p-row+1, p-1, p+1, p+row-1, p+row, p+row+1)
    if p == up:
        P =  (p-row, p-1,  p+row-1, p+row, p+row+1 )
    elif p>down and p < up-1 :
        P =  ( p-row, p-row+1,  p-row+2, p-1, p+1, p+row-1, p+row, p+row+1 )
    primes = [i for i in P if gmpy2.is_prime(i) ]
    # print(str(p)+'.      ', P ,'        ' )
    return primes

print('\nget_prime_neighbours : \t', get_prime_neighbours( 17 ),'\n\n')


def Row_Prime_triplets( row ):
    S=0
    down, up = get_row_first_last_elem(row)
    for p in range(down, up+1):
        D = {}
        if gmpy2.is_prime(p) :
            if p == down:       # first element
                P = (p-row+1, p-row+2, p+1, p+row, p+row+1)

            if p == up-1:       #penultimul element
                P = (p-row, p-row+1, p-1, p+1, p+row-1, p+row, p+row+1)

            if p == up:     # last element
                P = (p-row, p-1,  p+row-1, p+row, p+row+1 )

            elif p>down and p < up-1 :
                P  = ( p-row, p-row+1,  p-row+2, p-1, p+1, p+row-1, p+row, p+row+1 )

            primes = [i for i in P if gmpy2.is_prime(i) ]
            # print(str(p)+'.           ', primes )

            if len(primes) >= 2 :
                S+=p
            elif len(primes) == 1 :
                gN = get_prime_neighbours(primes[0])
                if len(gN) >1 :
                    # print('gN : \t',gN)
                    S+=p
    return S


print('\nRow_Prime_triplets Check : \t', Row_Prime_triplets( 10000 ),'\n' )


# s1 = Row_Prime_triplets(5678027)
# s2 = Row_Prime_triplets(7208785)
# print('\npartial results :     s1=',s1, '      s2=', s2 )
# print('\n\nAnswer : \t', s1+s2 )    #           Answer : 	   322303240771079935


t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')            #   Completed in : 44572.549343 ms


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,   --------------------------')
t1  = time.time()

# ==== Thu, 16 Apr 2015, 05:38, tlesaul2, USA
# Toughest part was bookkeeping during identification of triplets.  I used gmpy.is_prime
# which felt a little cheap, but I got over it.
# Posting because I got to use a for/else-loop which I think more people should be aware of.
# Not entirely necessary, I could have just let the function finish and return None by default,
# but it allowed for a more case-specific comment.
# Also, parens around if statements are used to allow line continuation and comments for individual conditions.

from gmpy2 import is_prime

def base(n):
    """one less than first number in row n"""
    return ((n-1)*n)//2

def getrow(n):
    """iterator for row n"""
    return range(base(n)+1,base(n+1)+1)

# lookup for offsets.
# keys are 1 away from center.
# values are sets 2 away from center and adjacent to their keys
adjacentPositions = {
    (-1,-1):{(0,-2),(-1,-2),(-2,-2),(-2,-1),(-2,0)},
    (-1,0):{(-2,-1),(-2,0),(-2,1)},
    (-1,1):{(-2,0),(-2,1),(-2,2),(-1,2),(0,2)},
    (0,1):{(-1,2),(0,2),(1,2)},
    (1,1):{(0,2),(1,2),(2,2),(2,1),(2,0)},
    (1,0):{(2,1),(2,0),(2,-1)},
    (1,-1):{(2,0),(2,-1),(2,-2),(1,-2),(0,-2)},
    (0,-1):{(1,-2),(0,-2),(-1,-2)}}


def verify(row,column):
    """determines if prime in row,column is in a prime triplet"""
    adjacentPrime = None    # initialize
    for (rowOffset,columnOffset) in adjacentPositions.keys():
        if (   row+rowOffset < 1                    # row too high
            or column+columnOffset < 1              # column too far left
            or row+rowOffset < column+columnOffset  # column too far right
           ):    # skip all such cases
            continue
        if is_prime(base(row+rowOffset)+column+columnOffset):
            if adjacentPrime:
                # second adjacentPrime
                # prime being "verified" is at the center of a prime triplet
                return True
            else:
                # first adjacentPrime
                # store offsets for lookup of distance two offsets later
                adjacentPrime = (rowOffset,columnOffset)

    if adjacentPrime:
        # One adjacentPrime
        for (rowOffset,columnOffset) in adjacentPositions[adjacentPrime]:
            if (    row+rowOffset < 1                    # row too high
                 or column+columnOffset < 1              # column too far left
                 or row+rowOffset < column+columnOffset  # column too far right
                ):    # skip all such cases
                continue
            if is_prime(base(row+rowOffset)+column+columnOffset):
                # prime found at distance 2
                # first adjacentPrime is the center of a prime triplet
                # containing the prime being "verified"
                return True
        else:
            # No prime at distance 2 is found
            # prime being "verified" is not in a prime triplet
            return False
    else:
        # Surrounded by composites
        # prime being "verified" is not in a prime triplet
        return False

total = 0
for row in [5678027,7208785]:
    for column,val in enumerate(getrow(row),start=1):
        if is_prime(val):           # val must be prime
            if verify(row,column):  # and contained in a prime triplet
                total += val

print(total)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,  Short but SLOW, 9 min --------------------------')
t1  = time.time()

# ===

import gmpy2
def triplets(n, s, x):
    t = [(s+n+1+x,s+2*n+2+x)]
    if x > 0 and x < s-1: t += [(s-n+1+x,s-2*n+2+x), (s-n+1+x,s+n-1+x)]
    if x < s-3: t += [(s-n+1+x,s-2*n+4+x)]
    if x < s-1: t += [(s-n+1+x,s+n+1+x)]
    if x < s-2: t += [(s+n+1+x,s+x+2)]
    if x > 1: t += [(s+n-1+x,s+x-2)]
    if x > 0: t += [(s+n-1+x,s+n+1+x), (s+n-1+x,s+2*n+x)]
    return t

def S(n):
    answer = 0
    start = n*(n-1)//2+1
    for x in range(n):
        if gmpy2.is_prime(start+x):
            for t in triplets(n, start, x):
                if gmpy2.is_prime(t[0]) and gmpy2.is_prime(t[1]):
                    answer += start+x
                    break
        x += 1
    return answer

print (S(5678027) + S(7208785))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,   --------------------------')
t1  = time.time()

# ==== Sat, 17 Jan 2009, 23:33, tolstopuz, Russia
# 62 sec on E8400

import math

def sq(n):
    return n * (n - 1) // 2 + 1

n1 = 5678027
n2 = 7208785

primes = int(math.sqrt(sq(max(n1, n2) + 3)) + 1) * [True]

primes[0:2] = [False,False]

for x in range(2, int(math.sqrt(len(primes)) + 1)):
    if primes[x]:
        for y in range(2 * x, len(primes), x):
            primes[y] = False

def s(n):
    kmin = sq(n - 2)
    kmax = sq(n + 3)
    p = 5 * n * [True]
    for x in range(2, len(primes)):
        if primes[x]:
            y = (kmin + x - 1) // x * x
            while y < kmax:
                p[y-kmin] = False
                y += x
    x = [[False,False] + p[:n-2] + [False,False,False,False],
         [False,False] + p[n-2:2*n-3] + [False,False,False],
         [False,False] + p[2*n-3:3*n-3] + [False,False],
         [False,False] + p[3*n-3:4*n-2] + [False],
         [False,False] + p[4*n-2:5*n]]

    c = 0
    for i in range(n):
        if x[2][i+2] and any(
            x[j+2][k+i+2] and sum(1 if x[j+q+2][k+t+i+2] else 0
                                  for q in range(-1, 2) for t in range(-1, 2)) >= 3
            for j in range(-1, 2) for k in range(-1, 2)):
            c += sq(n) + i
    return c

print(s(n1) + s(n2))

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
