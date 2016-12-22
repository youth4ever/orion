#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
                            Red, green or blue tiles        -       Problem 116

A row of five black square tiles is to have a number of its tiles replaced with coloured
oblong tiles chosen from red (length two), green (length three), or blue (length four).

If red tiles are chosen there are exactly seven ways this can be done.

If green tiles are chosen there are three ways.

And if blue tiles are chosen there are two ways.

Assuming that colours cannot be mixed there are 7 + 3 + 2 = 12 ways of replacing the black tiles in a row measuring five units in length.

How many different ways can the black tiles in a row measuring fifty units in length be replaced if
colours cannot be mixed and at least one coloured tile must be used?

NOTE: This is related to Problem 117.

'''
import time


print('\n--------------------------TESTS------------------------------')


def partitions(n):
    '''     Taken from http://code.activestate.com/recipes/218332-generator-for-integer-partitions/
            Created by David Eppstein on Wed, 27 Aug 2003
    :What it is:    A generator of number partition
    :Usage:     Example:    <<<**for i in partitions(5):    print(i)**
    :param n:   the number you want the partitions
    :return:    set of lists with all the possible combinations                                                 '''
    # base case of recursion: zero is the sum of the empty list
    if n == 0:
        yield []
        return

    # modify partitions of n-1 to form partitions of n
    for p in partitions(n-1):
        yield [1] + p
        if p and (len(p) < 2 or p[1] > p[0]):
            yield [p[0] + 1] + p[1:]


def unique_permutations(lst):       # VERY EFFECTIVE
    ''':Description: Takes a list and makes ONLY Unique Permutations of a list with repeated elements.
        If one tries itertools.permutations on a list with 14 elements ==> BANG, computer freezes
    :Usage: list(unique_permutations([1,1,1,3]))
    :param lst: type list
    :return:    a list of lists containing all the permutations
    '''
    if len(lst) == 1:
        yield (lst[0],)
    else:
        unique_lst = set(lst)
        for first_element in unique_lst:
            remaining_lst = list(lst)
            remaining_lst.remove(first_element)
            for sub_permutation in unique_permutations(remaining_lst):
                yield (first_element,) + sub_permutation


print('------------- Check Method ----------')

S = 0
rod_len = 16            # CHECK METHOD ONLY, UNACCEPTABLE SOLUTION otherwise, BLUE TILES NOW
for L in partitions(rod_len):
    targets = [ i for i in L if i>4 ]
    exclude = [ i for i in L if 4>i>1 ]
    if  L.count(1)!=rod_len and  len(exclude) ==0 and len(targets) == 0 :
        print(L,'     ' ,targets, exclude, '    ', list(unique_permutations(L)))
        cnt =len(list(unique_permutations(L)))
        S+=cnt

print('\nAnswer :\t', S)        #



print('\n--------------------------TESTS------------------------------')



R = [list(range(1,16))]
print(R)

for i in range(1, 7):
    g = [ sum(R[i-1][0:j]) for j in range(1, len(R[i-1]) )  ]
    # print(g)
    R.append(g)
    # print(R)

print('--------------')
for i in range(len(R)):
    print(R[i])

print('\nLength 5 :\t', R[0][3] , R[1][1] ,'     ' , R[0][3] + R[1][1]  )
print('Length 7 :\t', R[0][5] , R[1][3], R[2][1],'     ' ,R[0][5] + R[1][3] + R[2][1]  )
print('Length 8 :\t',  R[0][6] , R[1][4], R[2][2], R[3][0] , sum ( [R[0][6] , R[1][4], R[2][2], R[3][0] ]) )
print('Length 9 :\t',  R[0][7] , R[1][5], R[2][3], R[3][1] , sum ( [R[0][7] , R[1][5], R[2][3], R[3][1] ]) ,'\n')

Red = 7   # Red Rod Length
itr = Red//2
S =0
for i in range(0, itr ):
    print( R[i][Red-2*(i+1)] , end ='  ')
    S += R[i][Red-2*(i+1)]

print('\nRed Rod Ways :\t',S)

print('\n-------------------------- INITIAL SOLUTION TESTS------------------------------')

def red_rod_ways(L):
    R = [list(range(1, L))]
    max_blocks = L//2
    for i in range(1, max_blocks +1 ):
        g = [ sum(R[i-1][0:j]) for j in range(1, len(R[i-1]) )  ]
        # print(g)
        R.append(g)
        # print(R)
    S =0
    for k in range(0, max_blocks ):
        # print( R[k][L-2*(k+1)] , end ='  ')
        S += R[k][L-2*(k+1)]
    return print('\n\nRed Rod Ways :\t',S)

red_rod_ways(11)            # VALIDATED

def green_rod_ways(L):
    R = [list(range(1, L))]
    max_blocks = L//3
    for i in range(1, max_blocks +1 ):
        g = [ sum(R[i-1][0:j]) for j in range(1, len(R[i-1]) )  ]
        # print(g)
        R.append(g)
        # print(R)
    S =0
    for k in range(0, max_blocks ):
        # print( R[k][L-2*(k+1)] , end ='  ')
        S += R[k][L-3*(k+1)]
    return print('\n\nGreen Rod Ways :\t',S)

green_rod_ways(11)            # VALIDATED

print('\n----------- BLUE TILES ------------- ')

def blue_rod_ways(L):
    R = [list(range(1, L))]
    max_blocks = L//4
    for i in range(1, max_blocks +1 ):
        g = [ sum(R[i-1][0:j]) for j in range(1, len(R[i-1]) )  ]
        # print(g)
        R.append(g)
        # print(R)
    S =0
    for k in range(0, max_blocks ):
        # print( R[k][L-2*(k+1)] , end ='  ')
        S += R[k][L-4*(k+1)]
    return print('\n\nBlue Rod Ways :\t',S)

blue_rod_ways(11)            # VALIDATED



print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

def red_green_blue_rod_ways(L):
    M = [list(range(1, L))]

    for i in range(1, L//2 +1 ):
        g = [ sum(M[i-1][0:j]) for j in range(1, len(M[i-1]) )  ]
        # print(g)
        M.append(g)
        # print(M)
    S =0
    for w in [2, 3, 4] :        # red, green, blue
        max_blocks = L//w
        for k in range(0, max_blocks ):
            # print( M[k][L-2*(k+1)] , end ='  ')
            S += M[k][L-w*(k+1)]
        print(S)
    return print('\nRed-Green-Blue Tiles Rod Ways :\t', S)

red_green_blue_rod_ways(50)     # Answer : Red-Green-Blue Tiles Rod Ways :	 20492570929




t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,   --------------------------')
t1  = time.time()

# ====== Fri, 20 May 2016, 23:46, utkarsh_23, India
# Used combinations, Takes about 0.007 seconds

def comb(n,r):
    return fact(n) / (fact(r) * fact(n - r))
def fact(a):
    if a in D:
        return D[a]
    else:
        f = a * fact(a - 1)
    D[a] = f
    return f
global D
D = {0:1}
summ = 0
for i in range(2,5):
    for j in range(1,50 // i + 1):
        summ += comb(50 - i * j + j,j)
print (summ)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()

# ===== Thu, 19 May 2016, 07:07, nandersen, USA
# Straightforward dynamic programming in Python.

r = []
g = []
b = []

def calc_tiles(arr,length,x):
    total = 0
    for tile in [1,length]:
        if x - tile < 0: continue
        if x is tile: total += 1
        else: total += arr[x-tile]
    return total

for x in range(51):
    r.append(calc_tiles(r,2,x))
    g.append(calc_tiles(g,3,x))
    b.append(calc_tiles(b,4,x))

print(r[50] + g[50] + b[50] - 3)
# there is 1 all-black per type

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,   --------------------------')
t1  = time.time()

# ===== Sun, 1 May 2016, 11:56, ugadal
# sort of fibonacci solutions.. 3 times and sum up

def ana(x):
	t=0
	a,b=0,1
	for i in range(x):a,b=b,a+b
	t+=b
	a,b,c=0,0,1
	for i in range(x):a,b,c=b,c,a+c
	t+=c
	a,b,c,d=0,0,0,1
	for i in range(x):a,b,c,d=b,c,d,a+d
	t+=d
	return t
print( ana(5)-3)
print (ana(50)-3)



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,   --------------------------')
t1  = time.time()

# ==== Fri, 17 Jul 2015, 11:05, Haroun, Python , Algeria
# About 0.05 ms on python (really fast. I considered each case and then summed the three values (like in the example)


def f(n):
	a,b=1,2;
	for i in range(n-2):
		a,b=b,a+b;
	return b-1
def g(n):
	a,b,c=1,1,2;
	for i in range(n-3):
		a,b,c=b,c,c+a;
	return c-1
def h(n):
	a,b,c,d=1,1,1,2;
	for i in range(n-4):
		a,b,c,d=b,c,d,d+a;
	return d-1;
n=50;
sol=f(n)+g(n)+h(n)

print (sol)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5,   --------------------------')
t1  = time.time()

# ===== Fri, 25 Dec 2015, 06:06, PDF, USA
# Python, using a permutations principal from Discrete Math

import math

def choose(x, y):
    return (math.factorial(x)/(math.factorial(y)*math.factorial(x-y)))

def main():
    m = 50
    rgb = [2, 3, 4]
    tot = 0
    for c in rgb:
        for x in range(1, (m//c)+1):
            cho = choose(m-(c*x)+x, x)
            tot += cho
    print(tot)

main()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6,   --------------------------')
t1  = time.time()

# ===== Thu, 27 Nov 2014, 17:37, Omoplata, England
# General term formulae for red (2) green (3) and blue (4) tiles:
# Red:         (x−r)! /(x−2r)!r!
# Green:       (x−2r)! / (x−3r)!r!
#
# Blue:           (x−3r)! / (x−4r)!r!
# For x = 50, sum terms of red up to floor(50/2)=25, green up to floor(50/3)=16, and blue up to floor(50/4)=12.
#
# Total = ∑{r=1, 25} (50−r)! / (50−2r)!r! + ∑{r=1, 16} (50−2r)! / (50−3r)!r! + ∑{r=1, 12 } (50−3r)! / (50−4r)!r!

import math

REDTOTAL = 0
for r in range(1,26):
    REDTOTAL += math.factorial(50-r)/(math.factorial(50-(2*r))*math.factorial(r))
GREENTOTAL = 0
for r in range(1,17):
    GREENTOTAL += math.factorial(50-(2*r))/(math.factorial(50-(3*r))*math.factorial(r))
BLUETOTAL = 0
for r in range(1,13):
    BLUETOTAL += math.factorial(50-(3*r))/(math.factorial(50-(4*r))*math.factorial(r))
GRANDTOTAL = REDTOTAL + GREENTOTAL + BLUETOTAL
print(int(GRANDTOTAL))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 7,   --------------------------')
t1  = time.time()

# ==== Sun, 1 Feb 2015, 01:40, raulbc777, Paraguay
# I used a code to generate all possible partitions of the integer 50. I only selected:
# 1. Partitions with 1's and 2's (red size tiles combined with black ones)
# 2. Partitions with 1's and 3's (green size tiles  "       "    "     " )
# 3. Partitions with 1's and 4's (blue size tiles   "       "    "     " )
#
# Example of a single partition = [1,1,1,1,1,1,1,1, ........, 2] (with 49 ones and 1 two)
# The sum of the integers of each list(partition) is 50.
# Each black tile is represented by a one, and each red tile by a two.
# In this case we have a feasable partition with 49 black tiles and one red one.
#
# As the function partitions gives the result in lists, I used the condition:
#
# number of black tiles + number of coloured_tiles = length of partition.
#
# Let be:
#
# count1 = number of black tiles
#
# countColour = number of coloured_tiles
#
# As each partition will generate a set of permutations, we can estimate this number and:
#
# numberPermutations for partition = (count1 + countColour)!/ ((count1)!*(countColour)!)
#
# We sum the number of permutations for each partition for the red case, then for the green one and finally for the blue case.
# The sum of total for the three cases will give the result.
#
# Obs. A special partition is all tiles in red (without any black one)
#
# The following code gives the result in less than 2 secs:


import math, time
def allPermutColour(countTuple):
    countBlack, countColour = countTuple
    sum_ = countBlack + countColour
    return math.factorial(sum_)/(math.factorial(countBlack) * math.factorial(countColour))


def partitions(n):
    if n == 0:
        yield []
        return
    for p in partitions(n-1):
        yield [1] + p
        if p and (len(p) < 2 or p[1] > p[0]):
            yield [p[0] + 1] + p[1:]

start = time.time()

total = 50
sizeRed, sizeGreen, sizeBlue = 2, 3, 4
PermutRed, PermutGreen, PermutBlue = 0, 0, 0
permutRedDict, permutGreenDict, permutBlueDict = {}, {}, {}
for comb in partitions(total):
    setComb = set(comb)
    count1 = comb.count(1)
    if 2 in setComb:
        countRed = comb.count(sizeRed)
        countRedTuple = (count1, countRed)
        if count1 + countRed == len(comb):
            permutRed = allPermutColour(countRedTuple)
            permutRedDict[countRedTuple] = permutRed
    elif 3 in setComb:
        countGreen = comb.count(sizeGreen)
        countGreenTuple = (count1, countGreen)
        if count1 + countGreen == len(comb):
            permutGreen = allPermutColour(countGreenTuple)
            permutGreenDict[countGreenTuple] = permutGreen
    elif 4 in setComb:
        countBlue = comb.count(sizeBlue)
        countBlueTuple = (count1, countBlue)
        if (count1 + countBlue == len(comb)):
            permutBlue = allPermutColour(countBlueTuple)
            permutBlueDict[countBlueTuple] = permutBlue

res1 = sum(permutRedDict.values())
res2 = sum(permutGreenDict.values())
res3 = sum(permutBlueDict.values())
print ("Ordered Partitions with Red Tiles(size =2):   ", res1)
print ("Ordered Partitions with Green Tiles(size=3):    ", res2)
print ("Ordered Partitions with Blue Tiles(size=4):       ", res3)
print ("                                          ----------------")
print ("Total of different ordered partitions:        ", res1 + res2 + res3)
print()
print (time.time() - start, " secs")

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

