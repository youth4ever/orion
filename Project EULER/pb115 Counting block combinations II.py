#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Fri, 9 Dec 2016, 09:02
#The  Euler Project  https://projecteuler.net
'''
Counting block combinations II      -       Problem 115

NOTE: This is a more difficult version of Problem 114.

A row measuring n units in length has red blocks with a minimum length of m units placed on it,
such that any two red blocks (which are allowed to be different lengths) are separated by at least one black square.

Let the fill-count function, F(m, n), represent the number of ways that a row can be filled.

For example, F(3, 29) = 673135 and F(3, 30) = 1089155.

That is, for m = 3, it can be seen that n = 30 is the smallest value for which the fill-count function first exceeds one million.

In the same way, for m = 10, it can be verified that F(10, 56) = 880711 and F(10, 57) = 1148904,
so n = 57 is the least value for which the fill-count function first exceeds one million.

For m = 50, find the least value of n for which the fill-count function first exceeds one million.

'''
import time

def partitions(n):
    '''     Taken from http://code.activestate.com/recipes/218332-generator-for-integer-partitions/
            Created by David Eppstein on Wed, 27 Aug 2003
    :What it is:    A generator of number partition
    :Usage:     Example:    for i in partitions(5):    print(i)
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


class GET_ROD_VARIATIONS(object):
    ''':Description: depends on the unique_permutations function.
            *Made by Bogdan Trif @ 2016-12-06, 22:00*
    :param lst: the list to analyze
    :return: int, the final number of available configurations
    '''
    def __init__( self, lst, m ):
        self.lst = lst
        self.m = m
        self.threes = [i for i in self.lst if i >= self.m]
        self.threes_nr = len(self.threes)
        self.ones = self.lst.count(1)
        self.mark = 0
        self.M = []
        self.up_range = len(self.lst)-2*(self.threes_nr-1)+1

    def unique_permutations(self , threes ):       # VERY EFFECTIVE
        ''':Description: Takes a list and makes ONLY Unique Permutations of a list with repeated elements.
            If one tries itertools.permutations on a list with 14 elements ==> BANG, computer freezes
        :Usage: list(unique_permutations([1,1,1,3]))
        :param lst: type list
        :return:    a list of lists containing all the permutations
        '''
        if len(self.threes) == 1:
            yield (self.threes[0],)
        else:
            unique_lst = set(self.threes)
            for first_element in unique_lst:
                remaining_lst = list(self.threes)
                remaining_lst.remove(first_element)
                for sub_permutation in self.unique_permutations(remaining_lst):
                    yield (first_element,) + sub_permutation

    def get_multiplier(self) :
        w = list( unique_permutations( self.threes ))
        # print(N)
        return len(w)

    def count_unique_perm(self, ones, threes_nr ) :
        ''':Description: Recursion Function to count blocks separated by one tile.
        :param ones: int , the number of ones from the list
        :param threes_nr: int, numbers of threes(numbers >= 3 in the list)
        :return: int, the number of possible configurations
        '''
        tmp = []

        if self.threes_nr > 2 :
            self.threes_nr -= 1
            self.count_unique_perm(  self.ones , self.threes_nr )
            self.mark+=1
            for j in range(1, self.up_range):
                tmp.append( sum( self.M[self.mark-1][0:j] ) )
                # print(tmp)
            self.M.append(tmp)
            # print(self.M)

        elif self.threes_nr == 2 :
            for i in range(1, self.up_range):
                tmp.append(i)
            self.M.append(tmp)
            # print(self.M)

        return sum(self.M[self.mark])

    def __str__(self):
        return self.lst

    def get_result(self):
        if self.threes_nr == 1 : return len(self.lst)
        if self.threes_nr -1 == self.ones :  return (1* self.get_multiplier() )
        if self.threes_nr  == self.ones :  return ( (self.ones +1 )* self.get_multiplier())
        if self.threes_nr  == 0 :  return 1
        if self.ones  == 0 :  return 1

        else :
            return self.count_unique_perm(self.ones, self.threes_nr) * self.get_multiplier()


L=[1, 1, 1, 1, 1, 10, 10, 10]
# print('\nCLASS __str__ TESTING  for GET_ROD_VARIATIONS : ',GET_ROD_VARIATIONS(L).__str__() )
print('\n CLASS get_multiplier TESTING  for GET_ROD_VARIATIONS : ',GET_ROD_VARIATIONS(L, 10).get_multiplier() )
T = GET_ROD_VARIATIONS(L,10).threes
O = GET_ROD_VARIATIONS(L,10).unique_permutations( T)
print('\n CLASS unique_permutations TESTING  for GET_ROD_VARIATIONS : ',GET_ROD_VARIATIONS(L,10).unique_permutations(T ) )
print('CLASS TESTING  for GET_ROD_VARIATIONS : ',GET_ROD_VARIATIONS(L,10).threes_nr )
print('CLASS TESTING  for GET_ROD_VARIATIONS : ',GET_ROD_VARIATIONS(L,10).threes )
print('CLASS TESTING  for GET_ROD_VARIATIONS : ',GET_ROD_VARIATIONS(L,10).ones )
# print('\nCLASS count_unique_perm TESTING  for GET_ROD_VARIATIONS : ',GET_ROD_VARIATIONS(L).count_unique_perm(ones, threes) )
print('\nCLASS get_result TESTING  for GET_ROD_VARIATIONS : ',GET_ROD_VARIATIONS(L,10).get_result() )

print('\nunique_permutations  Function : ', list(unique_permutations(L)) )



print('\n--------------------------TESTS------------------------------')
t1  = time.time()

def count_block_combinations(m, rod_length ) :
    cnt = 0
    for K in partitions(rod_length):
        filter = [i for i in K if  1<i<m]
        # print('filter : ',filter, K)
        if len(filter) == 0 :
            ones = K.count(1)
            threes_nr = len([ i for i in K if i>=m ])
            if  threes_nr <= ones +1 :
                a = GET_ROD_VARIATIONS(K, m).get_result()
                # print(K)
                print(a,'\t', K )# ,  '  ; ones, threes :',ones, [ i for i in K if i>=m ] )
                cnt += a
    return print('\nAnswer : ', cnt)

# count_block_combinations(10, 56)

# It's not gonna work this way. I must find a proper function to count the blocks. See the other problem
#
# Must also fix the classmethod count_unique_partitions


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print("\n================  My FIRST SOLUTION, Using mhb038' s Algorithm  ===============\n")
t1  = time.time()


def F(m,n,memo={}):
    t=time.clock()
    blocks={k:[0, 1] for k in range (1, m)}
    blocks[0]=[0, 0]
    blocks[m]=[1, 1]
    try:
        print(m, n, memo[(m, n)],time.clock()-t)
        return
    except KeyError:
        for L in range (m+1, n+1):
            blocks.setdefault(L, []).append(blocks[L-1][0]+blocks[L-m][1]) #red left-edged solutions
            blocks.setdefault(L, []).append(blocks[L-1][0]+blocks[L-1][1]) #black left-edged solutions
        result =sum(blocks[L])
        memo[(m, n)]=result
    print(m, n, sum(blocks[L]), time.clock()-t)

F(50, 168, {})          # Answer : 168










t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')

# !!!!!!!!!    GOOD IDEAS, GENERAL IDEA :
# =====Thu, 16 Oct 2014, 05:40,  HuggyHermit, Scotland
# Just putting this out there, since it surprised me how many complicated programs are being posted.
# As others have pointed out, F obeys a simple recurrence relation:
#
# F(m, n) = F(m, n - (m+1)) + 2*F(m, n - 1) - F(m, n - 2)
#
# As such all you need to do is keep iterating until you hit a million. This runs in the blink of an eye:

# ========== Wed, 11 Mar 2009, 23:16, Orbifold, Canada        IDEA OF THE PROBLEM ###########
# Simple once you know the recursion :
#         F(m,n) = 1 if 0 <= n < m, otherwise
#         F(m,n) = F(m,n-1) + F(m,n-m-1) + F(m,n-m-2) + ... + F(m,1) + F(m,0).
#         Telescoping, this becomes :
#         F(m,n) = 2*F(m,n-1) - F(m,n-2) + F(m,n-m-1)



print('\n--------------------------SOLUTION 0,   --------------------------')
t1  = time.time()
# ========Fri, 27 Feb 2009, 22:16,  Knut.Angstrom, Sweden

m=50
ff=[1]*(m+1)
for n in range (200):
  f = ff[0] - ff[m-1] + 2*ff[m]       # Using the Recursion Relation
  for r in range (m):
    ff[r]=ff[r+1]
  ff[m]=f
  if f > 1000000:
    print (n+m, f)
    break

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 1,  VERY FAST, mhb038, England --------------------------')
t1  = time.time()
# ========    Tue, 22 Nov 2016, 10:20, mbh038 , England
# About 3 ms in Python. I use the function F(m,n)F(m,n) from problem 114, then started with F(50,500)
# and  found the target value of nn by bisection, in 7 iterations.


def F(m,n,memo={}):

    blocks={k:[0,1] for k in range (1,m)}
    blocks[0]=[0,0]
    blocks[m]=[1,1]
    try:
        return memo[(m,n)]
    except KeyError:
        for L in range (m+1,n+1):
            blocks.setdefault(L,[]).append(blocks[L-1][0]+blocks[L-m][1]) #red left-edged solutions
            blocks.setdefault(L,[]).append(blocks[L-1][0]+blocks[L-1][1]) #black left-edged solutions
        result =sum(blocks[L])
        memo[(m,n)]=result
    return result


def p115(m,limit):
    """returns smallest value n, given m, for which F(m,n) exceeds limit"""
    t=time.clock()
    ln=m+1
    hn=10*ln
    count=0
    memo={}
    while 1:
        count+=1
        n=(ln+hn)//2
        ans=F(m,n,memo)
        if ans>limit:
            if F(m,n-1,memo)< limit:
                break
            hn=n
        if ans<limit:
            if F(m,n+1,memo)> limit:
                break
            ln=n
    print(count,'iterations')
    print ('m',m,'n',n,'F',F(m,n),'time',time.clock()-t)

p115(50, 200)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()
# ========= Fri, 17 Jul 2015, 18:31,  Haroun, Algeria
# I used memoization, it takes 6 ms only.



c={}; m=50; L=10**6
def f(n):
	if n<m : return 1;
	if n==m : return 2;
	if n not in c :
		c[n]= sum(f(n-k) for k in range(m+1,n+1))+f(n-1)+1;
	return c[n];
k=1;
while f(k)<L :
	k+=1;
sol=k;

print ("the answer is :" , (sol))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,   --------------------------')
t1  = time.time()
# =======  Wed, 10 Feb 2016, 03:27, xhshen, China
# Solved by generating function and combinatio,  use 8.5 ms,  2.7 GHz Intel Core i5

from operator import mul
from fractions import Fraction
import functools
start = time.time()

def nCk(n,k):
  return int( functools.reduce(mul, (Fraction(n-i, i+1) for i in range(k)), 1) )

# m is minimum units length
# n is path length
# uAm is units amount
# coffient C(2*uAm+k,k)x^((m+1)*uAm+k-1)
def F(m,n):
	 ret = 0
	 for uAm in range(1,n//(m+1)+1):
	 	k = n+1-(m+1)*uAm
	 	ret = ret + nCk(2*uAm+k,k)
	 return ret+1


def method1():
	ret = 0
	n=50
	while ret <=1000000:
		n = n+1
		ret = F(50,n)

	print (n)

method1()
elapsed = time.time() - start
print("Elasped Time: %ss" % elapsed)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,   --------------------------')
t1  = time.time()
# ========== Thu, 19 May 2016, 07:25, nandersen, USA
# Incredibly fast Dynamic Programming in Python.

n = [1]
m = 50
def tile_count(x):
    total = n[x-1]
    for i in range(m,x+1):
        if i is x: total += 1
        else: total += n[x-i-1]
    return total

x = 1
while True:
    tc = tile_count(x)
    if tc > 1000000:
        print(x,tc)
        break
    else:
        n.append(tc)
        x += 1



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5,   --------------------------')
t1  = time.time()

# ======== Sun, 22 May 2016, 07:41, pj6444, USA
# Tweaked my solution to 114.
# solve(n, m) takes n as the length, m as the block length and recursively solves the problem by breaking it into smaller pieces.
# Checked to see when it broke 10**6, printed it out.


def solve(n, m):
    if n < m: return 1
    if n == m: return 2

    res = solve(n - 1, m)
    for redLength in range(m, n + 1):
        newLength = n - redLength - 1
        if newLength < 0:
            res += solve(newLength, m)
        elif memo[newLength] != 0:
            res += memo[newLength]
        else:
            memo[newLength] = solve(newLength, m)
            res += memo[newLength]
    return res

memo = []
n = 51
m = 50

while True:
    memo = [0] * n
    if solve(n, m) > 10**6:
        print (n)
        break
    n += 1



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6,   --------------------------')
t1  = time.time()

# ======== Fri, 21 Oct 2016, 13:50, DFHD , England
# Yup, just re-used my recursive memoised function from 114, and manually did a binary search.
# Glad to see it didn't get bogged down using m=50 and 100<n<200, still only taking milliseconds

def pe_114_Counting_block_combinations_I():
    global fn_cache
    fn_cache = dict()

    def count_block_combinations_recursive(m, n, depth=0):
        # count the ways of adding a single block, and recurse for
        # counting additional blocks.
        global fn_cache
        b_counter = 0
        for b_start in range(n - m + 1):
            for b_len in range(m, n - b_start + 1):
                b_counter += 1
                b_remaining = n - b_start - b_len
                if b_remaining > m:  # strictly greater coz we need the extra space for a gap between blocks
                    if (m, b_remaining) not in fn_cache:
                        fn_cache[(m, b_remaining)] = count_block_combinations_recursive(m, b_remaining - 1, depth+1)
                    b_counter += fn_cache[(m, b_remaining)]
#                 print("start,len,rem,depth", b_start, b_len, b_remaining, depth)
#                 print((m, n), b_counter, fn_cache)
        return b_counter

#     m, n = 3, 50
#     x = count_block_combinations_recursive(m, n) + 1  # +1 for the "empty" combination
#     print((m, n), x)
#     print(fn_cache)

    m, n = 50, 168
    x = count_block_combinations_recursive(m, n) + 1  # +1 for the "empty" combination
    print((m, n), x)

pe_114_Counting_block_combinations_I()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 7,   --------------------------')
t1  = time.time()

# ======== Thu, 10 Nov 2016, 19:33, Khalid, Saudi Arabia
# Used the same solution I used for 114 with minor modification. Still runs very fast (almost 1 ms):

target = 1000000
min_block = 50
rows = {0: 1, 1: 1}

for i in range(2, min_block + 1):
    rows[i] = 0

rows["M"] = 0

row_size = 1
while rows[0] + rows["M"] < target:
    oldM = rows["M"]
    rows["M"] += rows[min_block - 1]
    for i in range(min_block - 1, 0, -1):
        rows[i] = rows[i - 1]
    rows[0] = rows[0] + oldM
    row_size += 1


print (row_size)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')




print('\n--------------------------SOLUTION 9,   --------------------------')
t1  = time.time()
# ========= Thu, 16 Oct 2014, 05:40,  HuggyHermit, Scotland
# Just putting this out there, since it surprised me how many complicated programs are being posted.
# As others have pointed out, F obeys a simple recurrence relation:
#
# F(m, n) = F(m, n - (m+1)) + 2*F(m, n - 1) - F(m, n - 2)
#
# As such all you need to do is keep iterating until you hit a million. This runs in the blink of an eye:


# METHOD I
print('METHOD I')
m, target = 50, 1000000

n, ways = m-1, [1 for _ in range(m + 1)]
while ways[-1] < target:
    n, ways = n+1, ways[1:] + [ways[0] + 2*ways[-1] - ways[-2]]

print (n)

# This version avoids recreating the list at each step, so should be slightly faster, but it's a bit more confusing to read!

# METHOD II
print('METHOD II')
m, target = 50, 1000000

n, p, l, ways = m - 1, m, m + 1, [1 for _ in range(m + 1)]
while ways[p] < target:
    p = (p + 1)%l
    ways[p] += 2*ways[(p - 1)%l] - ways[(p - 2)%l]
    n += 1

print (n)

# It was really interesting to read about the combinatoric solutions, but I'd be surprised if they were
# any faster for n's as small as this, given that the iteration is so fast. :)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n--------------------------SOLUTION 10,   --------------------------')
t1  = time.time()
# ===========  Fri, 28 Nov 2014, 19:56, fioi, France

m = 50
n = 1
while True:
	dp = [0] * (n + 2)
	dp[0] = 1
	for i in range(0, n):
		for k in range(m, n - i + 1):
			dp[i + k + 1] += dp[i]
		dp[i + 1] += dp[i]
	if dp[n] + dp[n + 1] > 10 ** 6:
		print(n)
		break
	n += 1

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 11,   --------------------------')
t1  = time.time()
# ======== Thu, 12 Feb 2015, 10:18, Nicolas Patrois, France

m=50
u=[1]*m
n=m-1

while u[-1]<10**6:
  u.append(u[-1]+sum(u[:len(u)-m])+1)
  n+=1

print(n)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n--------------------------SOLUTION 13,  SLOW, RECURSION without Memoization  --------------------------')
t1  = time.time()

# ======== Wed, 17 Sep 2014, 15:44, NeatMonster, France
# Pretty straightforward:

def F(m, n):
    if n < m:
        return 0
    count = 0
    for t in range(m, n + 1):
        count += 1 + F(m, n - t - 1)
    count += F(m, n - 1)
    return count

n = 50
while True:
    if 1 + F(50, n) >= 10**6:
        print (n)
        break
    n += 1

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
