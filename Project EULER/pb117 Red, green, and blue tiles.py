#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Fri, 16 Dec 2016, 11:58
#The  Euler Project  https://projecteuler.net
'''
                            Red, green, and blue tiles      -       Problem 117

Using a combination of black square tiles and oblong tiles chosen from: red tiles measuring two units,
green tiles measuring three units, and blue tiles measuring four units,
it is possible to tile a row measuring five units in length in exactly fifteen different ways.

How many ways can a row measuring fifty units in length be tiled?

NOTE: This is related to Problem 116.

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


def calc_perm(lst) :        ### o(^_^)o    o(^_^)o  ###
    '''     **©** Made by Bogdan Trif @ 2016-12-16, 1150.

        :Description:    Calculates the number of unique permutations of a list.
        :param lst: list
        :return: int, number of permutations                    '''
    from math import factorial
    from functools import reduce
    from operator import mul
    total = len(lst)
    elem_nr=[]
    for i in set(lst): elem_nr.append(lst.count(i))
    numerator = factorial(sum(elem_nr))
    denominator =  reduce(mul, [factorial(i) for i in elem_nr] )
    return numerator // denominator



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

t1  = time.time()

S = 0
rod_len = 20            # CHECK METHOD ONLY, UNACCEPTABLE SOLUTION otherwise, RED-GREEN-BLUE TILES NOW
for L in partitions(rod_len):
    targets = [ i for i in L if 4>=i>=1 ]
    exclude = [ i for i in L if i>4 ]
    if    len(exclude) ==0  :
        print(L,'     ' , calc_perm(L) ,'   ' , targets, exclude, '     ' )# , list(unique_permutations(L))   )
        cnt = calc_perm(L)
        S+=cnt

print('\nAnswer :\t', S)        #


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------TESTS------------------------------')

lst= [1, 1, 1, 1, 1, 2, 2, 2]
print('\nThe Permutation Function calc_perm :\t',calc_perm(lst))

print('\n---------------------')
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

red_rod_ways(10)            # VALIDATED

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

green_rod_ways(10)            # VALIDATED

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

blue_rod_ways(10)            # VALIDATED



print('\n===========  My FIRST SOLUTION, With PARTITIONS, 2 sec  ===============\n')
t1  = time.time()

def solve_with_partitions(rod_length) :
    S = 0
    for L in partitions(rod_length):
        targets = [ i for i in L if 4>=i>=1 ]
        exclude = [ i for i in L if i>4 ]
        if    len(exclude) ==0  :
            # print(L,'     ' , calc_perm(L) ,'   ' , targets, exclude, '     ' )
            cnt = calc_perm(L)
            S+=cnt

    return print('\nAnswer :\t', S)

solve_with_partitions(50)            #   Answer : 100808458960497

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')          # Completed in : 2690.154076 ms


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')


print('\n--------------------------SOLUTION 0,   --------------------------')
t1  = time.time()

# =======   Fri, 17 Jul 2015, 11:34, Haroun, Algeria
# The solution for nn is f(n)=f(n−1)+f(n−2)+f(n−3)+f(n−4).
# This should be enough, the code below runs in < 0.05 ms.

def f(n):
	a, b, c, d = 1, 2, 4, 8 ;
	for i in range(n-4):
		a, b, c, d = b, c,d , a+b+c+d ;
	return d

n=50;
sol=f(n)

print ("the answer is" ,sol)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 0b, RECURSION with lru_cache as Memoization  --------------------------')
t1  = time.time()

# ==== un, 13 Dec 2015, 19:32, RachmanyinooooV, Hungary
# Recursive solution with python.

from functools import lru_cache
red, green, blue = 2, 3, 4

@lru_cache()
def ways(n):
    count = 1
    for color in (red, green, blue):
        for first_block in range(n - color + 1):
            count += ways(n - first_block - color)
    return count

print(ways(50))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n--------------------------SOLUTION 0c, DYNAMIC PROGRAMMING   --------------------------')
t1  = time.time()

# ====== Fri, 27 Sep 2013, 12:26, gl1, France
# My First post!!!  This problem is actually exactly identical to #31!
# "Dynamic programming" solution in python:

N =  [1] + [0] * 50
for n in range(0, 50):
    for k in range(0, min(4, n+1)):
        N[n+1] = N[n+1] + N[n-k]
print (N[50]  )


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n--------------------------SOLUTION 1,   --------------------------')
t1  = time.time()

# ====== Mon, 29 Aug 2016, 17:17, Anthony, England
# Euler 117
# Red, Green and Blue Tiles



def SolveBlock(number):
    if solvedblocks[number] > 0:
        counter = solvedblocks[number]
    else:
        counter = 1
        for blocklength in range(2, min(4, number)+1):
            for i in range(0, number - blocklength + 1):
                counter += SolveBlock(number-blocklength-i)
        solvedblocks[number]=counter
    return counter


mainblocklength = 50
solvedblocks = [0] * (mainblocklength+1)
solvedblocks[0] = 1
solvedblocks[1] = 1

print("There are", SolveBlock(mainblocklength), "ways of filling the block. ")

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()
# # ==== Sat, 12 Nov 2016, 20:18, Khalid, Saudi Arabia
# I followed a similar approach to problems 114 and 115. This program is almost the same as the one for 116.

def count_blocks(row_size, block_sizes):
    finalized_blocks = {}
    pending_blocks = {}
    for block_size in block_sizes:
        pending_blocks[block_size] = []
        for i in range(block_size + 1):
            pending_blocks[block_size].append(0)
        if (block_size == 1):
            finalized_blocks[block_size] = 1
        else:
            finalized_blocks[block_size] = 0
            pending_blocks[block_size][1] = 1
    for i in range(2, row_size + 1):
        completed = 0
        for block_size in block_sizes:
            for j in range(len(pending_blocks[block_size]) - 1, 0, -1):
                pending_blocks[block_size][j] = pending_blocks[block_size][j - 1]
            finalized_blocks[block_size] += pending_blocks[block_size][block_size]
            completed += pending_blocks[block_size][block_size]
            pending_blocks[block_size][block_size] = 0
        for block_size in block_sizes:
            pending_blocks[block_size][0] = completed
    return sum(finalized_blocks.values())

size = 50
print (count_blocks(size, [1, 2, 3, 4]))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,   --------------------------')
t1  = time.time()
# =======   Wed, 23 Nov 2016, 10:34, mbh038, England
# Solved in 10−100μs using recursion with a memo, O(n).
# It's like Fibonacci except that the nthnth term is found by adding the previous 4 terms rather than the previous two,
# and with base cases of F(4,n)=(0,1,2,4,8) for n=(0,1,2,3,4).
#
# More generally, given that F(m,0)=0 for any m,
# F(m,n)=∑{k=0, n−1} 1+F(m,k)   ,  if (n≤m)
#
# F(m,n)=∑{k=1,m }  F(m,n−k),     otherwise
#
# where m is the maximum tile length and n is the row length.



def F(baseCases,m,n,memo={}):
    """m is maximum tile length,n is length of row"""
    #base cases
    if n<=m:
        return baseCases[n]
    try:
        return memo[n]
    except KeyError:
        result=sum([F(baseCases,m,n-k,memo) for k in range(1,m+1)])
        memo[n]=result
        return result

def bases(m):
    """base cases for rows with maximum tile length m"""
    b={0:0}
    for x in range(1, m+1):
        b[x]=1+sum([b[y] for y in range(x)])
    return b


def mbh038(m,n):
    b=bases(m)
    print (n,F(b,m,n))

mbh038(4, 50)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4, List Comprehension  --------------------------')
t1  = time.time()

# =====  Sun, 14 Jun 2015, 15:45, Robert_Reid, Australia
# A one-liner in Python. Takes 30 milliseconds.
# # let the number of blue, green, red, and black tiles be b, g, r, and black


from math import factorial as fact

print(sum([fact(b+g+r+black)//(fact(b) * fact(g) * fact(r) * fact(black))
           for b in range(50//4 + 1) for g in range((50-4*b)//3 + 1)
           for r in range((50-4*b-3*g)//2 + 1) for black in [50-4*b-3*g-2*r]]))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5,   --------------------------')
t1  = time.time()

# =====  Tue, 30 Jun 2015, 00:36, fdemichelis, France
# recursively, but storing previous value, put a tile of size 1,2,3 or 4 count 1 when there is no place to put more.

setsol={}
setsol[0]=1

def combin(n):
    if n in setsol:
        return setsol[n]
    s=0
    for i in range(1,5):
        if n>=i:
            s+=combin(n-i)
    setsol[n]=s
    return s

print(combin(50))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6,   --------------------------')
t1  = time.time()

# ====== Mon, 13 Jul 2015, 08:14, xanxerus, Sweden
# Simple recursive solution with memoization. Runs in 5 ms with Pypy

memo = {}
def e117(row):
	if row <= 0:
		return 0

	if row in memo:
		return memo[row]

	ret = 0

	if row >= 2:
		ret += 1
	if row >= 3:
		ret += 1
	if row >= 4:
		ret += 1

	ret += e117(row-1) + e117(row-2) + e117(row-3) + e117(row-4)

	memo[row] = ret

	return ret

print (1 + e117(50))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')




print('\n--------------------------SOLUTION 7,   --------------------------')
t1  = time.time()

# ======   Wed, 9 Sep 2015, 19:09, oneequalstwo,  USA
# I explicitly used a combinatorial Stars and Bars solution, appending to a total a product of
# (1) how many ways to arrange a collection of some number of red/blue/green bars determined using for loops,
# and (2) how many ways to insert however many black squares in between some number of colored bars. It ran in 7 ms.
# I included the timeit code because I'm lazy

import math


def nCr(n,r):
    f = math.factorial
    return f(n)/f(r)/f(n-r)

def nCabc(n,a,b,c):
    f = math.factorial
    return f(n)/f(a)/f(b)/f(c)

total = 0

for red in range(0,50 // 2 + 1):
    remain1 = 50 - 2*red
    for green in range(0,remain1 // 3 + 1):
        remain2 = remain1 - 3*green
        for blue in range(0,remain2 // 4 + 1):
            black = remain2 - 4*blue
            colorSum = red+green+blue
            colorArrange = nCabc(colorSum,red,green,blue)
            starsAndBars = nCr(colorSum+black,colorSum)
            total += colorArrange * starsAndBars
print (total)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 8,   --------------------------')
t1  = time.time()

# =====Wed, 18 Nov 2015, 20:03, Oliver1978. Germany
# I used a method with "distinct permutations", that way avoiding permutations of like [2, 2]. The rest is with factorials. See for yourselves...

# constants
MAXLENGTH = 50
RED = 2
GREEN = 3
BLUE = 4

# fill list of factorials
F = list()
F.append(1)
for f in range (1, MAXLENGTH+1):
    F.append(F[f-1] * f)

# combine coloured blocks
def Combine(r, g, b, bk):
    # length by blocks
    blocks = r + g + b + bk
    # distinct permutations
    perms = F[blocks] / (F[r] * F[g] * F[b] * F[bk])

    return perms

# get max. number of blocks
mr = MAXLENGTH // RED
mg = MAXLENGTH // GREEN
mb = MAXLENGTH // BLUE

# iterate over blocks and combine them
count = 0
for r in range (0, mr+1):
    for g in range (0, mg+1):
        for b in range (0, mb+1):
            len = r*RED + g*GREEN + b*BLUE
            if (len <= MAXLENGTH) and (len != 0):
                k = MAXLENGTH - len
                count += Combine(r, g, b, k)

# print result; add "all black" solution
print( "--> " + str(count+1))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n--------------------------SOLUTION 9,   --------------------------')
t1  = time.time()
# ======= Sun, 29 Dec 2013, 06:48, userz, USA
# not super elegant but easy to understand:

import math
import collections
import operator, functools

M = 50
Combo = collections.namedtuple('Combo', ['black', 'red', 'green', 'blue'])


# build out all possible block configurations
combos = []
for blue in range(M//4 + 1):
  for red in range(M//2 + 1):
    for green in range(M//3 + 1):
      black = M - 2*red - 3*green - 4*blue
      if black >= 0:
        combos.append(Combo(black, red, green, blue))
combos = sorted(combos)

# check that they're valid
for c in combos:
   assert M == sum(map(lambda t: t[0]*t[1], zip(c, (1,2,3,4))))

#
total = 0
for c in combos:
  total += math.factorial(sum(c)) / functools.reduce(operator.mul, map(math.factorial, c), 1)

print (total)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 10,   --------------------------')
t1  = time.time()
# =======Mon, 5 May 2014, 19:35, SafassThin, France
# edit - I tried to make the calculation sequential, and ended up with this code:
# I confirm the result for l=5000 given in the previous page by romanAround (in 6ms :-) )

def euler_117(l=50):
    count,a,b,c,d = 4,1,2,4,8
    while count<l:
        count,a,b,c,d = count+1,b,c,d,a+b+c+d
    return d

print( euler_117(50))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 11,  DYNAMIC PROGRAMMING --------------------------')
t1  = time.time()
# =======Mon, 5 May 2014, 22:22, Nicolas Patrois, France

maxi=50

rgb=[0, 1, 2, 4, 8]
for i in range(5,maxi+1):
  rgb.append(rgb[-1]+rgb[-2]+rgb[-3]+rgb[-4])

print(rgb[-1])

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

