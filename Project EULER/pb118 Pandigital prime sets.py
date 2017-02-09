#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Mon, 6 Feb 2017, 16:39
#The  Euler Project  https://projecteuler.net
'''
                Pandigital prime sets       -       Problem 118

Using all of the digits 1 through 9 and concatenating them freely to form decimal integers, different sets can be formed.

Interestingly with the set {2, 5, 47, 89, 631 }, all of the elements belonging to it are prime.

How many distinct sets containing each of the digits one through nine exactly once contain only prime elements?

'''
import time
import gmpy2, functools, operator
from itertools import  combinations, permutations


# Rules :
# 4,6,8 must be within a number AND not at the end
# 2 free or within a number AND NOT at the end

def prime_generator(lower, upper):      ### o(^_^)o  FASTEST  o(^_^)o  ###  HIghly Efficient !!!
    """  Sieve of Eratosthenes              !!!!!!!!! THE FASTEST SIEVE. It won the battle with sieve
    Create a candidate list within which non-primes will be marked as None.         """
    cand = [i for i in range(3, upper + 1, 2)]
    end = int(upper ** 0.5) // 2

    # Loop over candidates (cand), marking out each multiple.
    for i in range(end):
        if cand[i]:
            cand[cand[i] + i::cand[i]] = [None] * ( (upper // cand[i]) - (upper // (2 * cand[i])) - 1 )

    # Filter out non-primes and return the list.
    return [ i for i in cand if i and i > lower ]

def partitions(n):
    '''     Taken from http://code.activestate.com/recipes/218332-generator-for-integer-partitions/
            Created by David Eppstein on Wed, 27 Aug 2003
    :What it is:    A generator of number partition
    :Usage:     Example:    >>>             for i in partitions(5):    print(i)
    :param n:   the number you want the partitions
    :return:    set of lists with all the possible combinations                              '''
    # base case of recursion: zero is the sum of the empty list
    if n == 0:
        yield []
        return

    # modify partitions of n-1 to form partitions of n
    for p in partitions(n-1):
        yield [1] + p
        if p and (len(p) < 2 or p[1] > p[0]):
            yield [p[0] + 1] + p[1:]

def primesieve(n):          ### o(^_^)o  FASTEST  o(^_^)o  ###  Highly Efficient !!!
    import numpy as np
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]

print('\n--------------------------TESTS------------------------------')

t1  = time.time()

# primes_8 = [i for i in sieve(10**7, 10**8) if  len(set(list(str(i)))) == 8 and list(str(i)).count('0') ==0  ]
# print(len(primes_8) ,  primes_8)

# 23082 primes [12345769, 12346589, 12346597, 12348659, 12354689, 12354967,            Completed in : 58071.321487 ms

def get_eights() :
    primes_8 = [i for i in prime_generator( 10**7, 10**8 ) if  len(set(list(str(i)))) == 8 and list(str(i)).count('0') ==0  ]
    print(len(primes_8) ,  primes_8)

    Eights = 0
    P = set('2357')
    for s in primes_8 :
        A= set(str(s))
        if len(P - A) >= 1  :
            Eights +=1
            print( s , P-A )

    return print('\nThere are Eighths: \t', Eights )

# print('\nThere are Eights: \t', get_eights() )           #   There are Eigths: 	 11483

Eigths =  11483

print('\n--------------- SEVENS--------------')

def get_sevens():
    primes_7 = [i for i in prime_generator( 10**6, 10**7 ) if  len(set(list(str(i)))) == 7 and list(str(i)).count('0') ==0  ]
    print(len(primes_7) ,  primes_7)

    Sevens = 0
    P = set(list(int(i) for i in str(123456789)))        #set('12357')
    # # primes_7 = [ 9854231 ,9854261 , 9854371 , 9854623, 9854627 ]

    cnt = 0
    for s in primes_7 :                 #    (7,2), (7,1,1)
        A= set(list(int(i) for i in str(s)))
        B = list(P-A)
        if B[0]%2 == 1 or B[1]%2 == 1  :
            if gmpy2.is_prime( B[0]) and gmpy2.is_prime( B[1]) :
                cnt +=1
                Sevens +=1         # Both are primes :
                print(str(cnt)+'.    ', s ,A, P-A)
            d2_1, d2_2 = int(str(B[0])+str(B[1])) , int(str(B[1])+str(B[0]))            # forming two digits nrs : 23, 32
            if gmpy2.is_prime(d2_1) :                # if  23 is prime
                cnt+=1
                Sevens +=1
                print(str(cnt)+'.    ', s ,A, d2_1)
            if gmpy2.is_prime(d2_2) :                   # if  32 is prime
                cnt+=1
                Sevens +=1
                print(str(cnt)+'.    ', s ,A, d2_2)
    return Sevens

# get_sevens()

# print('\nThere are Sevens: \t', get_sevens() )     #   There are Sevens: 10896            Completed in : 3595.205545 ms
Sevens = 10896



print('\n------------ SET INTERSECTION of a list of numbers -------------------------')

# We have a list of numbers and we have a test number.
# We want to make the intersection of the test number with every number from the list
# and return only the numbers which have no common digits with the test number
# lst = {257, 641, 643, 769, 389, 263, 647, 137, 521, 139, 523, 269, 397, 271, 653, 659, 149}
# print('The initial list to of elements :\t',lst)
# test_nr = 324
# set_nr = set([int(i) for i in str(test_nr)])
# print('Test number :\t', test_nr, set_nr)
# INTERSECTION = [ s for s in lst if len(set_nr& set([int(i) for i in str(s)]) )==0 ]
# print(' Intersection of the test_nr with every element of the list yields :\n', INTERSECTION )

def generate_digits_combinations(n, length ) :
    PART = []
    for i in partitions(n):
        if 1 < len(i) <= length :
            Prt = tuple(i[::-1])
            if Prt < (7,) :
                # print(Prt)
                PART.append(Prt)

    return PART

PART = generate_digits_combinations(9, 6)
print('\nPartitions :\n', PART ,'\n')

def separated_primes_unique_digits( up_lim = 10**6) :
    primes = primesieve(up_lim)
    D ={}                   # We separate length of primes in a dictionary
    for p in primes :
        l = len(str(p))
        if l not in D :
            D[l]=set([])
            if len(str(p)) == len(set (str(p)) ) :
                if str(p).count('0') == 0 :
                    D[l].add(p)
        else :
            if len(str(p)) == len(set (str(p)) ) :
                if str(p).count('0') == 0 :
                    D[l].add(p)
    return D

# D = separated_primes_unique_digits( 10**6 )
# for k, v in D.items():
#     print(k ,'    ', len(D[k]) ,'    ', list(D[k])[:50] )



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n=============  My FIRST SOLUTION,  2 min, Primitive  ===============\n')
t1  = time.time()


def initial_solution() :
    REST = 0
    for T in PART :
        cnt   = 0
        W = []
        lsT = list(set(T))
        # print(T,  lsT , len(lsT) )
        for a in range(len(lsT )) :
            L = list(combinations( D[ lsT[a] ] , T.count( lsT[a] ) ))
            W.append( L )
            # print(W)
            # print (  lsT[a], T.count(lsT[a]) , '    ',len(L), L[:100]  )

        # 1  number     (3,3,3)
        if len(lsT) == 1 :
            for i in range(len(W[0])) :
                w = sorted(W[0][i])
                v= ''.join( str(i) for i in w)
                if len(set(str(v))) == 9 :
                    cnt+=1
                    # print( w ,  ''.join( str(i) for i in w) , len(set(str(v)))  )

         # 2  numbes        ( 3, 2, 2, 2 )
        if len(lsT) == 2 :
            for i in range(len(W[0])) :
                for j in range(len(W[1])) :
                    # print( W[0][i]+W[1][j] )
                    w = sorted( W[0][i]+W[1][j] )
                    v= ''.join( str(i) for i in w)
                    if len(set(str(v))) == 9 :
                        cnt+=1
                        # print(str(cnt)+'.   ', w ,  v ,  len(set(str(v)))  )

        # 3  numbes        (4, 2, 1, 1, 1)
        if len(lsT) == 3 :
            for i in range(len(W[0])) :
                for j in range(len(W[1])) :
                    for k in range(len(W[2])) :
                        # print( W[0][i]+W[1][j] + W[2][k] )
                        w = sorted( W[0][i]+W[1][j] + W[2][k] )
                        v= ''.join( str(i) for i in w)
                        if len(set(str(v))) == 9 :
                            cnt+=1
                            # print(str(cnt)+'.     ', w ,  v ,  len(set(str(v)))  )
        REST +=cnt
        print(T,'       ' ,cnt, '\n')

    print('REST Answer : ', REST,'\n')

    return print('\n Pandigital Prime Sets : \t',  REST + Sevens + Eigths )

# initial_solution()          # Answer  :  	 44680


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')      #   Completed in : 100.946 s


# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1, 2sec  !!!! MUST LEARN FROM IT  --------------------------')
t1  = time.time()

# === Sun, 14 Aug 2016, 22:35, j123, Canada
# Concise and pretty fast, using Python's itertools module, takes under 2s in interpreted Python3 on my ancient laptop.
# The only reduction I use is automatically marking composite all numbers other than 3 whose digit sum is a multiple of 3.
# In 20 seconds, gives the the number for all digits 0-9: 248769 if we don't allow 0-leading numbers, 351889 if we do.

#updated, slightly cleaner
#This version uses about 50MB RAM.  Instead could use the is_prime I posted in the thread for problem 387;
# takes no memory, runs about 2-3 times longer.

from itertools import count, combinations, permutations

def odd_prime(N):
    from itertools import count
    '''Boolean of odd primes up to and including N; bytearray of size N+1>>1'''
    a, b = 0, N - 1 >> 1
    B = bytearray([0]) + bytearray([1]) * b
    for c in count(1, 2):
        a += c - 1 << 1  #a = c * c // 2
        if a > b: return B
        if B[c >> 1]: B[a::c] = bytearray((b - a) // c + 1)

#There are two ways to accomodate 0: allow or prevent leading 0's.  Uncomment
#the relevant line for the desired behaviour.

def do(D=range(1,10)):
    B = odd_prime(int(''.join(map(str, reversed(sorted(D)[not sum(D)%3:])))))
    def isprime(x, B=B):
        #if x[0] == '0': return 0 #prevent leading 0's (if D=range(10), say)
        n = int(''.join(x))
        return n & 1 and B[n >> 1] or n is 2

    def f(s, D= { frozenset() : 1} ) :
        if s in D: return D[s]
        end = len(s) - (sum(map(int, s)) % 3 == 0 and s != {'3'})
        ##if we accept leading 0's, use version below
        #end = len(s) - (sum(map(int, s)) % 3 == 0 and s - {'0'} != {'3'})
        d = next( iter(s) )
        sd = s - {d}  #frozenset equivalent of pop()
        ans = sum(f(sd - set(t)) * sum(map(isprime, permutations((d,) + t)))
                  for k in range(end) for t in combinations(sd, k))
        D[s] = ans
        return ans

    return f(frozenset(map(str, D)))

print(do())

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2, 40 sec  --------------------------')
t1  = time.time()

# === Sat, 7 May 2016, 04:59, xanxerus, Sweden
# 6-7 seconds in pypy.
# Did some recursive stuff. The prime test is efficient trial division, memoized for a 1 second boost.
#
# I start with a set of all digits. For every permutation of every combination of digits of every length from 1
# to the number of digits left, if that permutation of digits is prime and greater than the previous
# call's prime permutation of digits, recurse. Hopefully the code is less confusing than my words.


from itertools import permutations, combinations

def memoize(fun):
	cache = dict()
	def hjalp(n):
		if n in cache:
			return cache[n]
		else:
			pot = fun(n)
			cache[n] = pot
			return pot
	return hjalp

@memoize
def isprime(n):
	if n < 4:
		return n > 1
	if (n&1)==0 or (n%3)==0:
		return False
	for x in range(5, int(n**.5)+1, 6):
		if n%x==0 or n%(x+2)==0:
			return False
	return True

def f(unused=set(range(1, 10)), m=0):
	ret = 0
	for j in range(1, len(unused)+1):
		for e in combinations(unused, j):
			for p in permutations(e):
				pot = int(''.join(map(str, p)))
				if pot > m and isprime(pot):
					if j == len(unused):
						ret += 1
					else:
						ret += f(unused - set(p), pot)
	return ret

# print (f())

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,   16 sec --------------------------')
t1  = time.time()


# ====Wed, 24 Dec 2014, 05:19, CBurkhart. USA
#
# I did it as a recursive function (with memoization) on the digits not already used.
# The answer is simply the function called on [1,2,3,4,5,6,7,8,9].
#
# In order to avoid over counting by different orders on the set, we force the recursive function
# to use the first number in the input (which will be the smallest left) when it makes the next prime.
# We loop over all subsets of the rest of the list, and then all permutations of the subset plus forced number.
# If the number formed by that permutation is prime then we add on the recursive call with the new set of leftover numbers.
#
# To check for primes I created a sieve for all primes less than √10**10.
# Since the largest number we need to check is 987654321,
# we will have all the primes up to the square root of the number being tested.
# Simple trial division is used for the actual test.
# There is no memoization on the prime test since no number will be checked twice.
# Total run time: 9.653351068496704.

from math import floor, sqrt
from itertools import combinations, permutations


target = floor(sqrt(10**10))

primality = [ True for i in range(target+1)]
primality[0] = False
primality[1] = False

for i in range(floor(sqrt(target))+1):
    if primality[i]:
        j = i**2
        while j <= target:
            primality[j] = False
            j += i

primes = [p for p in range(target+1) if primality[p]]
del primality[:]

def isPrime(n):
    if (n == 1):
        return False
    upperlimit = floor(sqrt(n))

    for p in primes:
        if p > upperlimit:
            break
        if (0 == (n % p)):
            return False

    return True

primesetsdict = {tuple() : 1}

pows = [10**ix for ix in range(0,10)]

def listtoint(thelist):
    total = 0
    for i, digit in enumerate(thelist):
        total += digit*pows[i]
    return total

def primesets(numsleft):
    if tuple(numsleft) in primesetsdict:
        return primesetsdict[tuple(numsleft)]
    answer = 0
    forcednum = numsleft[0]
    possibleextras = len(numsleft)-1

    for numextras in range(0, possibleextras+1):
        for e in combinations(numsleft[1:], numextras):
            extras = list(e)
            newnumsleft = [ix for ix in numsleft[1:] if ix not in extras]
            for p in permutations(extras + [forcednum]):
                perm = list(p)
                if isPrime(listtoint(perm)):
                    answer += primesets(newnumsleft)

    primesetsdict[tuple(numsleft)] = answer
    return answer

# print("Answer: ", primesets([1,2,3,4,5,6,7,8,9]))



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4, VERY GOOD, 9 sec  --------------------------')
t1  = time.time()

# ===at, 8 Aug 2015, 21:20, lnconclusive, USA
# I broke the problem into 3 pieces:
# 1: representing the elements of the powerset of {1,2,3,4,5,6,7,8,9} as numbers 0-511, find all possible combinations
# of them that would contain every digit exactly once.  I'm pretty happy with the efficiency of this piece.
#
# 2: For each element of the powerset, find how many primes can be formed by arranging its elements.
# Probably could have done this part more efficiently.
#
# 3: Loop over the combinations found in (1), multiply the number of primes possible for each of the subsets it contains,
# and add all the results together.
def solution_4():
    from itertools import permutations

    def getsets2(p):
        D = {}
        def sub(n):
            if n in D: return D[n]
            S = []
            for i in range(n+1,p-n):
                if i&n==0:
                    if i+n+1==p:
                        S += [[i]]
                    else:
                        S+=[x+[i] for x in sub(n+i)]
            D[n] = S
            return S
        sub(0)
        return D[0]

    def is_prime(n):
        """Deterministic Miller-Rabin Test"""
        if n<10: return n in [2,3,5,7]
        if n%2==0: return False
        d = n-1; s=0; i=0
        while not d&1: s+=1; d=d>>1;
        for a in [2,3,5,7]:
            if pow(a,d,n)!=1 and all(pow(a,d<<r,n)!=(n-1) for r in range(s)):
                return False
        return True

    def get_multiplicities(p=512):
        alldigits = range(1,10)
        def get_mult(i):
            c = '{0:>9b}'.format(i)
            digits = [x for x,y in zip(alldigits,c) if y=='1']
            if sum(digits)%3==0 and digits!=[3]: return 0 # all arrangements will be divisible by 3
            sdigits = [str(x) for x in digits]
            return sum(is_prime(int(''.join(x))) for x in permutations(sdigits))
        return [get_mult(i) for i in range(p)]

    X = getsets2(512)
    C = get_multiplicities(512)

    total = 0
    for x in X:
        c = 1
        for term in x:
            c *= C[term]
            if c==0: break
        total += c

    return print (total)

# solution_4()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5,  45 sec --------------------------')
t1  = time.time()

# ==== Tue, 25 Oct 2016, 11:27, mbh038, England
# Pretty slow at 26 s in Python 3. Most of that time is spent generating the set of primes from 2 to 987654321.
# I use my own prime sieve to do this, and some neat recursive code by Stefan Pochmann to find all the partitions of 1...9.
#
# Given the partitions e.g.[[1],[2,3],[4,6,7],[8,9]] I then compile a dictionary in which the keys are the sub-partitions e.g.
# {4,6,7} as sets and the values are the number of prime permutations that can be formed from all the digits in this sub-partition.
# For each partition we can then find the number of pan digital prime sets that can be formed from it,
# mostly by looking up values already calculated for partitions that were inspected earlier. Still, 26s...:(

import itertools as it
import numpy as np

def p118():
    count=0
    prime_sets=0
    digits=set([x for x in range(1,10)])
    primes=set(mysieve(987654321))

    pdic={}
    for n, p in enumerate( partitions(digits), 1):
        pprime=1
        flag = True
        for x in p:
            if x != [2] and all([ i%2==0 for i in x ]):
                flag=False
                count+=1
                break
        if flag:
            ps = [set(x) for x in p]
            for pset in ps:
                pset = tuple(pset)
                try:
                    pprime *= pdic[pset]
                except KeyError:
                    pdic[pset]=0
                    for perm in it.permutations(pset):
                        if int(''.join([str(x) for x in perm])) in primes:
                            pdic[pset]+=1
                    pprime *= pdic[pset]
            prime_sets += pprime
    print(prime_sets)


#code by Stefan Pochmann, Stack Exchange, May 8 2015
def partitions(A):
    if not A:
        yield []
    else:
        a, *R = A
        for partition in partitions(R):
            yield partition + [[a]]
            for i, subset in enumerate(partition):
                yield partition[:i] + [subset + [a]] + partition[i+1:]

def mysieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]

# p118()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6,  RECURSION, 9 sec,  VERY ELEGANT  --------------------------')
t1  = time.time()

# ====Mon, 15 Apr 2013, 22:47, joente, Netherlands
# not really fast... 13.6 sec on my computer.

from itertools import permutations
from gmpy2 import is_prime

def problem118():
    def checkNumber(s, pn = 1):
        total, l, m = 0, 1, len(s)
        while l <= m:
            if l*2 > m: l = m
            i = int(s[:l])
            if i > pn and is_prime(i):
                if l == m:
                    total += 1
                else:
                    total += checkNumber(s[l:], i)
            l += 1
        return total

    t = 0
    for i in permutations("123456789", 9):
        t += checkNumber("".join(i))
    return t

print (problem118())




t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

