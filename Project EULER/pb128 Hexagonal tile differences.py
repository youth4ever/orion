#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Thu, 8 Dec 2016, 00:48
#The  Euler Project  https://projecteuler.net
'''
                Hexagonal tile differences      -   Problem 128

A hexagonal tile with number 1 is surrounded by a ring of six hexagonal tiles, starting at "12 o'clock" and
numbering the tiles 2 to 7 in an anti-clockwise direction.

New rings are added in the same fashion, with the next rings being numbered 8 to 19, 20 to 37, 38 to 61, and so on.
The diagram below shows the first three rings.

By finding the difference between tile n and each of its six neighbours we shall define PD(n) to be the number of those differences which are prime.

For example, working clockwise around tile 8 the differences are 12, 29, 11, 6, 1, and 13. So PD(8) = 3.

In the same way, the differences around tile 17 are 1, 17, 16, 1, 11, and 10, hence PD(17) = 2.

It can be shown that the maximum value of PD(n) is 3.

If all of the tiles for which PD(n) = 3 are listed in ascending order to form a sequence, the 10th tile would be 271.

Find the 2000th tile in this sequence.

'''
import time
import gmpy2
from math import floor
from itertools import count

def bin_search_left(n, List):        # VERY FAST ALGORITHM
    ''':Description: Search for an element in the list and returns the index of it. If it not finds it returns
        the index of the element closest to its left, the smaller number.
    :param: **n**- integer, the number to find
                **List** - lst type, the list to search for
    :returns:   int, the index of the element
    '''
    left = 0
    right = len(List) -1

    while left <= right:
        midpoint = (left+right)//2
        # print(left, right, midpoint)
        if List[midpoint] == n:
            return midpoint
        elif List[midpoint] > n: right = midpoint-1
        else: left = midpoint+1
    if n > List[midpoint]: return midpoint
    else: return (midpoint-1)



def get_neighbors(i):
    r = bin_search_left(i, RMS)

    if (FAG[r].index(i))%(r) == 0 :       # CORNER CASE , every row has 6 corners

        id = FAG[r].index(i) / TN[r]
        id2 = floor(TN[r-1]*id)
        id3 = floor(TN[r+1]*id)
        # print('\n----CORNER CASE----', id, id2, id3)
        n = i+1
        if FAG[r].index(i) == 0:
            sv = i+TN[r]-1
        else :
            sv = i-1
        nv = FAG[r-1][id2]
        se = FAG[r+1][id3]
        if FAG[r].index(i) == 0:
            s = FAG[r+1][-1]
        else :
            s = se-1
        ne = se+1
        return [n,  nv , sv ,s , se, ne]       #print(n, nv, sv, s, se, ne)

    if (FAG[r].index(i))%(r) != 0 :         # GENERAL CASE

        id = FAG[r].index(i) / TN[r]
        id2 = floor(TN[r-1]*id)
        id3 = floor(TN[r+1]*id)
        # print('\n---GENERAL CASE---', id, id2, id3)
        sv = FAG[r-1][id2 ]
        # print(FAG[r].index(i), TN[r] , r , FAG[r-1][0])
        if FAG[r].index(i) == TN[r]-1 :
            n = FAG[r][0]
            nv = FAG[r-1][0]
        else :
            n = i + 1
            nv = sv+1
        s = i-1
        se = FAG[r+1][ id3]
        ne = se+1
    return [n,  nv , sv ,s , se, ne]

print('Generate the 2000-th TILE Number of cells :\t', 6*(2000-1) )
print('\n--------------------------TESTS------------------------------')

# 1790270    for counter =100
rows = 200         #    for counter =100 rows =  780
print('Last number of the row', rows, 'is :', 1+sum([ 6*i for i in range(rows)]) )

RMS = [1,2]         # Row_Map_Start
for i in range(1, rows-1):
    RMS.append(RMS[-1]+i*6)

print('Row_Map_Start, RMS :\t',len(RMS), RMS[0:30] ,'\n')

print('BINARY SEARCH TEST: ',bin_search_left(30, RMS))



TN=[1]
for i in range(1, rows+1):
    TN.append(6*i)
print('TILE NUMBER in a Row, TN : ',TN,'\n')



print('---------------------------')
t1  = time.time()

FAG = []
p, cnt = 1, 0
for i in range(0, rows):
    P = [k for k in range(p, p+TN[i])]
    p = P[-1]+1
    # print(p, H[i], P)
    for j in P :
        if gmpy2.is_prime(j):
            cnt+=1
    FAG.append(P)

print(' =============  Constructing the SEQUENCE :  ============ ')

print('The first rows of the complete Sequence. FAG :\n',FAG[0:11])
# print('Verification Last number of the Sequence :\t',FAG[rows-1][-1])


SEQ = []
for i in range(1, 20):
    # if i%2 == 1 :
        SEQ.append(FAG[i][0])
    # if i%2 ==0 :
        SEQ.append(FAG[i][-1])

print('\nConstr. Sequence :',SEQ)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('Hex (or centered hexagonal) numbers: 3*n*(n+1)+1 (crystal ball sequence for hexagonal lattice) : ')
for i in range( 100) :
    x = 3*i*(i+1)+1
    print(x, end= ', ')

print('\n\n' , '#--'*30,'\n')




print('\n ----------- Building the Main Algorithm ----------------------')

# i=19
# print('Row number is: ', r)
# x = TN[r]/6
# print('x - Numbers on the side : ',x)
# # 2 CASES
# print('Modulo TEST : ', ( i-RMS[r-1])/(r-1) )
# print( 'gen case : ', i , FAG[r].index(i)  ,  RMS[r], (r),  (FAG[r].index(i))%(r)  ,TN[r] )


# I left HERE !!!!!!!!!!!!!!!!! must define the general case, 2016-12-05, 23:15
# r=2
# i=8
# print('\nIndex test : ',[ FAG[r].index(i) ], FAG[r])
#
# id = FAG[r].index(i) / TN[r-1]
# id2 = TN[r-2]*id
# id3 = TN[r]*id
#
# print( id, '   id2: ', id2, floor(id2), '       id3: ',  id3,  floor(id3)   )

print('\n---------------- My INITIAL SOLUTION -------------')

print('get_neighbors Function Test : ',get_neighbors(28) )

t1  = time.time()


def RMS() :
    ''':Generator: used for generating RMS's, Row Map Start sequence.
    :return:yield  *[ last_row_start_nr, current_row_start_nr, next_row_start_nr ]*       '''
    HL = gen_hex_lattice()
    n=2
    RMS = [1, 2, 8]
    k = (RMS[-1]-RMS[-2])//6
    while True :
        if  RMS[-1] <= n < RMS[-1]+(k+1)*2  :
            k+=1
            RMS.append(k*6+RMS[-1])
            RMS.pop(0)
        yield RMS
        n+=next(HL)

def TN():
    ''':Generator of the length of rows
    :return:yield the *[last_row_length, current_row_length, next_row_length]*    '''
    HL = gen_hex_lattice()
    n = 2
    k = 7
    TN = [1, 6, 12]
    while True :
        if n > k:
            k += TN[-1]
            TN.append(TN[-1]+6)
            TN.pop(0)
        yield TN
        n+=next(HL)

def FAG():
    ''':Generator for the rows of the hexagon
    :return:  *[last_row, current_row, next row ]*
    '''
    HL = gen_hex_lattice()
    FAG = [[1], [2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19] ]
    n = 2
    while True :
        if n > FAG[1][-1] :
            p = FAG[-1][-1]
            l = len(FAG[-1])+6
            FAG.append([ i+p+1 for i in range(l) ])
            FAG.pop(0)
        yield FAG
        n+=next(HL)



def manual_pb128() :
    counter=1
    PD=[1]
    for n in count(2) :
        Nb = get_neighbors(n)      # Neighbours
        # id = get_neighbors(n)[1]
        # print(n,'\t',  Nb    , end='   ' )
        cnt=0
        for i in Nb :
            p = abs(n - i )
            if gmpy2.is_prime(p) :
                cnt+=1
        if cnt ==3 :
            PD.append(n)
            counter+=1
            print('Nr: \t', n ,'\t\tCounter  : ', counter)
        if counter == 100 : break
    return print('\n\nAnswer:  ',n , counter, PD[-20::])

# manual_pb128()              # Completed in : 372.944331 s   to 100 !!!!!!!!!!!! Very SLOW, must find a pattern

t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')


print('\n================  My FIRST SOLUTION,  GOOD, 1 sec ===============\n')
t1  = time.time()

def gen_hex_lattice():
    ''':Generator: for Hex (or centered hexagonal) numbers: 3*n*(n+1)+1 (crystal ball sequence for hexagonal lattice) :
    :return:  int  1, 7, 19, 37, 61, 91, 127, 169, 217, 271, 331, 397, 469....
    :Usage: >>> HL = gen_hex_lattice()
                # >>> for i in range(2,11):  print(str(i)+'==.   ', next(HL))    '''
    n = 2
    while True :
        yield 3*n*(n+1)+1
        n+=1



def neighbors(i, R, T, F):          # STILL SLOW, must take only the required numbers, not all row
    r = R[1]
    # print('--- r ---',r)
    # print('Ficatel de Testing for number :', i ,F)
    if (F[1].index(i))%(r) == 0 :       # CORNER CASE , every row has 6 corners

        id = F[1].index(i) / T[1]
        id2 = floor(T[0]*id)
        id3 = floor(T[2]*id)
        # print('\n----CORNER CASE----', id, id2, id3)
        n = i+1
        if F[1].index(i) == 0:
            sv = i+T[1]-1
        else :
            sv = i-1
        nv = F[0][id2]
        se = F[2][id3]
        if F[1].index(i) == 0:
            s = F[2][-1]
        else :
            s = se-1
        ne = se+1
        return [n,  nv , sv ,s , se, ne]       #print(n, nv, sv, s, se, ne)

    if (F[1].index(i))%(r) != 0 :         # GENERAL CASE

        id = F[1].index(i) / T[1]
        id2 = floor(T[0]*id)
        id3 = floor(T[2]*id)
        # print('\n---GENERAL CASE---', id, id2, id3)
        sv = F[0][id2]
        # print(F[r].index(i), T[r] , r , F[r-1][0])
        if F[1].index(i) == T[1]-1 :
            n = F[1][0]
            nv = F[0][0]
        else :
            n = i + 1
            nv = sv+1
        s = i-1
        se = F[2][ id3]
        ne = se+1
    return [n,  nv , sv ,s , se, ne]


def is_PD3(nr, Nb) :
    ''':Usage: is_PD3(271 ,[218, 170, 217, 270, 330, 331])
    :Input : nr - int and Nb - list of six neighbours
    :Returns: boolean : True if there are 3 prime difference otherwise False
    '''
    cnt=0
    for j in Nb :
        p = abs(nr - j )
        if gmpy2.is_prime(p) :
            cnt+=1
    if cnt ==3 :
        return True
    return False


def neighbors_only(nr, row):          # We take only the neighbours which matters, meaning :
                                                    # 1. can't be prime a difference between two evens => even
    if nr % 2 == 0:                           #   2. can't be prime difference between two odds => even
        nv = nr + (row-1)*6 + 1
        se = nr + (row-1)*6 -1
        ne = nv-1 + row*6-1

        return [ nv , se, ne]

    if nr % 2 == 1:
        nv = nr - (row-1)*6 + 1
        sv = nv - (row-2)*6
        ne = nr + row * 6 -1

        return [ nv , sv  , ne  ]

# print('\nTesting the Function neighbors_only :', neighbors_only(38, 5))      # SUCCESS




def solution_pb128() :
    counter=2
    row = 3
    PD=[1, 2]
    N = gen_hex_lattice()
    while True :
        nr2 = next(N)
        nr1 = nr2 - (row-1)*6+1
        Nb1 = neighbors_only(nr1, row)
        Nb2 = neighbors_only(nr2, row)
        # print('Neighbours :', nr1, Nb1,'      ' ,nr2, Nb2 )

        if is_PD3(nr1, Nb1) :
            # PD.append(nr1)
            counter+=1
            # print('Nr: \t', nr1 ,'\t\tCounter  : ', counter)

        if is_PD3(nr2, Nb2) :
            # PD.append(nr2)
            counter+=1
            # print('Nr: \t', nr2 ,'\t\tCounter  : ', counter)
        if counter == 2000 :  break

        row+=1

    # return print('\nAnswer:\t ' ,  PD[-1] ,    '\n\nPD list :', PD[-10::], '\nLength (in case +1 longer) :\t', len(PD) )
    return print('\nAnswer:\t ' ,  nr1 )

solution_pb128()        # Answer:	  14516824220


t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,   --------------------------')
t1  = time.time()
# ==========  Fri, 13 Jun 2014, 15:55, superbit, Israel
# started with a program that generates pd3 matches the trivial way, and then searched for a path on the hexagonal tiles.
# finding that only the first and last tiles are needed to be considered helped a little :)

# python code runs in ~2 seconds, when using primes sieve until 1000000.


import timeit

LAST, CURR, NEXT, HIGH = 0, 1, 2, 3

def sieve_primes(N):
    global primes

    primes = [True]*N
    primes[0] = primes[1] = False
    for i in range(2, N):
        if primes[i]:
            j = i*2
            while j < N:
                primes[j] = False
                j += i

def is_pd3(base_value, level_values, neighbours):
    prime_differences = 0

    for neighbour in neighbours:
        if primes[abs(base_value - (level_values[neighbour[0]] + neighbour[1]))]:
            prime_differences += 1

    return (3 == prime_differences)

def solve(N):
    PD3 = [0, 1]

    sieve_primes(1000000)
    last, current, next, diffs = 1, 2, 8, 12	# start parameters

    while len(PD3) <= N:
        level_values = [last, current, next, next + diffs]

        # first tile in layer
        neighbours = [(HIGH, -1), (NEXT, 1), (LAST, 0), (NEXT, 0), (CURR, 1), (NEXT, -1)]

        if is_pd3(level_values[CURR], level_values, neighbours):
            PD3.append(level_values[CURR])

        # last tile in layer
        neighbours = [(LAST, 0), (CURR, -1), (CURR, 0), (NEXT, -2), (HIGH, -1), (HIGH, -2)]

        if is_pd3(level_values[NEXT] - 1, level_values, neighbours):
            PD3.append(level_values[NEXT] - 1)

        # promote to next layer
        last, current, next = current, next, next + diffs
        diffs = diffs + 6

    return PD3[N]

start = timeit.default_timer()	# start timing

print ('calculating solution...\n')
answer = solve(2000)

print ('Answer	 : {0}'.format(answer))
print ('Run time : %.3f'% (timeit.default_timer() - start) +'s')


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2, VERY SHORT & SIMPLE   --------------------------')
t1  = time.time()
# ==========Sat, 27 Dec 2014, 21:33 , lahvak

import gmpy2

def top(n):
    "top tile in n-th layer"
    return 2 + 3*n*(n-1)

def right(n):
    "last tile on n-th layer"
    return top(n) + 6*n -1

l = [1,2]
for n in range(2,100000):
    if all(gmpy2.is_prime(k) for k in [6*n-1,6*n+1,12*n+5]):
        l.append(top(n))
    if all(gmpy2.is_prime(k) for k in [6*n+5, 6*n-1, 12*n-7]):
        l.append(right(n))

l.sort()
print(l[1999])

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3, VERY SIMPLE,   --------------------------')
t1  = time.time()

# =========== Tue, 10 Feb 2015, 19:57 - ravoorheis, USA
# As noted several times above, 1 has three primes, and then only two sequences can possibly have 3 primes, defined by the recursions:
#
# a[0] = 2,  a[n] = 6*n + a[n-1]
# b[0] = 19, b[n] = 6*(n+2) + b[n-1]
#
# Then for each of these sequences, there are exactly three sequences that can possibly have prime values.
#
# For sequence a[n] the primes will have the form 6n+5, 6n+7, 12n+17
# For sequence b[n] the primes will have the form 6n+11, 6n+17, 12n+17
#
# So it's just a matter of checking that all three are primes for each n. If they are, then add either a[n] or b[n] to the list of solutions.



import numtheory

a,b = {},{}
a[0],b[0] = 2,19
hits = [1,2,19]

n = 1

while len(hits) < 2000:

    a[n] = 6*n + a[n-1]

    if gmpy2.is_prime(6*(n)+5) and gmpy2.is_prime(6*(n)+7) and gmpy2.is_prime(12*(n)+17):
        hits.append(a[n])

    b[n] = 6*(n+2) + b[n-1]

    if gmpy2.is_prime(6*(n)+11) and gmpy2.is_prime(6*(n)+17) and gmpy2.is_prime(12*(n)+17):
        hits.append(b[n])

    n+=1

print (hits[-1])

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')      # Completed in : 459.026337 ms

print('\n--------------------------SOLUTION 4, VERY NICE & ELEGANT --------------------------')
t1  = time.time()
# Thu, 4 Jun 2015, 16:21 ,Roderic, Canada
# I didn't like this problem. This solution runs pretty fast though.

def primes_upto(k):
    is_prime = [True] * int(k+1)
    is_prime[0] = is_prime[1] = False
    for n in (n for n, prime in enumerate(is_prime) if prime):
        yield n
        if n*n > k: continue
        is_prime[n::n] = [False] * int(k/n)

primes = set(primes_upto(10**6))


x, y, z, w = 2, 8, 20, 38
sols = [1, 2]
i = 0
while len(sols) < 2000:
    a, b = y, z-1

    if b-a in primes:

        if ( (z+1)-a in primes ) and ( (w-1)-a in primes ):
            sols.append(a)

        if ( b-x in primes ) and ( (w-2)-b in primes ):
            sols.append(b)

    x, y, z, w, i = y, z, w, w+6*(i+4), i+1

print(sols[1999])

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5,   --------------------------')
t1  = time.time()



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
