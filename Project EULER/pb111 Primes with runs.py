#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Tue, 17 Jan 2017, 15:00
#The  Euler Project  https://projecteuler.net
'''
                Primes with runs        -           Problem 111
Considering 4-digit primes containing repeated digits it is clear that they cannot all be the same:
1111 is divisible by 11, 2222 is divisible by 22, and so on.
But there are nine 4-digit primes containing three ones:

           1117, 1151, 1171, 1181, 1511, 1811, 2111, 4111, 8111

We shall say that M(n, d) represents the maximum number of repeated digits for an n-digit prime
where d is the repeated digit, N(n, d) represents the number of such primes, and S(n, d) represents the sum of these primes.

So M(4, 1) = 3 is the maximum number of repeated digits for a 4-digit prime where one is the repeated digit,
there are N(4, 1) = 9 such primes, and the sum of these primes is S(4, 1) = 22275. It turns out that for d =0,
it is only possible to have M(4, 0) = 2 repeated digits, but there are N(4, 0) = 13 such cases.

In the same way we obtain the following results for 4-digit primes.

                                        +----------------------------------------+
                                        | Digit, d | M(4, d) | N(4, d) | S(4, d) |
                                        |----------+---------+---------+---------|
                                        | 0        | 2       | 13      | 67061   |
                                        |----------+---------+---------+---------|
                                        | 1        | 3       | 9       | 22275   |
                                        |----------+---------+---------+---------|
                                        | 2        | 3       | 1       | 2221    |
                                        |----------+---------+---------+---------|
                                        | 3        | 3       | 12      | 46214   |
                                        |----------+---------+---------+---------|
                                        | 4        | 3       | 2       | 8888    |
                                        |----------+---------+---------+---------|
                                        | 5        | 3       | 1       | 5557    |
                                        |----------+---------+---------+---------|
                                        | 6        | 3       | 1       | 6661    |
                                        |----------+---------+---------+---------|
                                        | 7        | 3       | 9       | 57863   |
                                        |----------+---------+---------+---------|
                                        | 8        | 3       | 1       | 8887    |
                                        |----------+---------+---------+---------|
                                        | 9        | 3       | 7       | 48073   |
                                        +----------------------------------------+

For d = 0 to 9, the sum of all S(4, d) is 273700.

Find the sum of all S(10, d).

'''
import time, gmpy2


def primesieve(n):          ### o(^_^)o  FASTEST  o(^_^)o  ###  Highly Efficient !!!
    import numpy as np
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]         # Here we modify it to return only 10-digits primes above 10**9, 50847534 primes to 10**9

print('Çombinations : ',gmpy2.comb(9,8), gmpy2.comb(9,7)  )

def unique_permutations(lst):       # VERY EFFECTIVE
    ''':Description: Takes a list and makes ONLY Unique Permutations of a list with repeated elements.
        If one tries itertools.permutations on a list with 14 elements ==> BANG, computer freezes
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


###################   END FUNCTIONS ############
R  = { 0 : { 0: 2, 1:4, 2: 4 }, 1: {0:4, 3:5, 4:13,7:343} }
print(R)
print(R[1], ' The maximum index of the second entry is : ',max(R[1]))
print(R[1][7])

# X = { x : { y: 0 for y in range(10)}  for x in range(10)}
# print('\nthe Initial Dictionary :',X, '\n')


print('\n-------------   Just some Tests  -------------')
primes = primesieve(10000)
print(primes)
for p in primes :
    p = str(p)
    if p.count('4') == 3 :
        print(p)

# print('=========== MY Initial Solution ==============')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n================  My FIRST SOLUTION,  VERY FAST ===============\n')
t1  = time.time()

def first_solution():           # @2017-01-17 14:00
    '''The idea is that you investigate a handful of numbers. We can reduce the search space to
    only 9 digits as we know that primes are ending in end_digit = [1,3,7,9]
    At this point we suppose that we will find some primes with 9 repeating digits. But there may be also
    exceptions and so to be sure we go down a digit. If there is a digit who is not represented in the 8
    repetitions primes we can go even lower. But as we will see it is not the case. Therefore we search
    numbers with 8,9 repeating digits.
    To simplify the problem we  take only 8 repeating digits and make permutations with start digit in
    range [0,9] .
    Therefore our number will have the form  : start_digit + 8_repeating digits +end_digit
    But we take permutations only of the first 9 digits = start+8 repeating digits and add the end_digit afterwards.
    We must also take care to filter numbers with 0 in front. And this solves the problem very fast.
    '''
    D = { x : { }  for x in range(10)}
    last_digit = [1,3,7,9]
    for repeat in range(8, 7, -1):
        for d in range(10):
            cnt = 0
            for start in range(0, 10):
                mlst = list( str(start) +repeat*str(d) )
                C = list(unique_permutations( mlst))
                # print(mlst, C)
                for I in C :
                    for end in last_digit:
                        st = list(I)+[str(end)]
                        p = int(''.join([i for i in st ]))
                        # print(st, p)
                        if len(str(p)) ==10 and gmpy2.is_prime(p) :
                            cnt+=1
                            r = str(p).count(str(d))
                            # D[d][r] = p
                            if r not in D[d] : D[d][r] = p
                            else : D[d][r] += p
                            # print(d, '       ',p, '       ', r, '     ',D[d] ,'    ' , cnt)

    print('\n',D,'\n')
    S=0
    for i in range(len(D)) :
        S+= D[i][max(D[i])]
        print(i ,D[i] ,'     ' ,max(D[i]),'     ' , D[i][max(D[i])]  )

    return print('\n\nAnswer, Total Sum of digits : \t', S)          #   Total Sum of digits : 	 612407567715


first_solution()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')            # Completed in : 56.003332 ms

print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,   --------------------------')
t1  = time.time()

# ===== Sun, 18 Dec 2016, 18:27, mbh038, England
# I start from the guess that there will be either 8 or 9 repeated digits.
# I find N and S for all the cases of 9 repeated digits, then, where N=0,
# I find N and S for 8 repeated digits. If all N values are non-zero by this time,
# I know that I need look no further, as turns out to be the case.
# This massively reduces the search space. Before checking for primality,
# I throw out all numbers that cannot be prime and also those with a leading zero.
# About 850 ms and some very scrappy looking code.

import itertools as it

def p111(n):
    N=[0]*n
    S=[0]*n
    for i in range(0,10):
        for d1 in range(10):
            for pos in range(1,n+1):
                a=(pos-1)*str(i)+str(d1)+(n-pos)*str(i)
                if a[-1] in '024568' or a[0]=='0' or ((n-1)*i+d1)%3==0:
                    continue
                aval=int(''.join([x for x in  a]))
                if isprime(aval):
                    N[i]+=1
                    S[i]+=aval

    js=[j for j in range(10) if N[j]==0]
    for j in js:
        for ds in it.product('0123456789',repeat=2):
            for pos in it.combinations(list(range(n)),2):
                a=str(j)*(pos[0])+ds[0]+(pos[1]-pos[0]-1)*str(j)+ds[1]+(n-pos[1]-1)*str(j)
                if a[-1] in '024568' or a[0]=='0' or ((n-2)*j+int(ds[0])+int(ds[1]))%3==0:
                    continue
                aval=int(''.join([x for x in  a]))
                if isprime(aval):
                    N[j]+=1
                    S[j]+=aval
    print(sum(S))


def isprime(n):
    """Returns True if n is prime."""
    if n==2 or n==3:
        return True
    if not n%2 or not n%3:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True

# p111(10)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,  VERY FAST --------------------------')
t1  = time.time()

# ==== Mon, 31 Aug 2015, 12:01, hornemann55,  Denmark
# digits 0,2,8 can repeat a maximum of 8 times, the rest 9 times

import gmpy2
N = [1,2,4,5,7,8]
s = 0
for p in [int(str(i)*d+str(n)+str(i)*(9-d))  for i in [1,3,7,9] for n in N for d in range(0,10) if (n != i) and (n+d) > 0]:
      if gmpy2.is_prime(p) :
         s += p

for p in [i+n for i in [4444444440,5555555550,6666666660] for n in [1,7]]:
   if gmpy2.is_prime(p) :
      s += p

for p in [int(str(i)*k+str(j)+str(i)*(8-k)+str(n)) for i in [2,8] for k in range(0,9) for j in range(0,10) for n in [1,3,7,9] if (n!=i) and j!=i and (j+k)>0 ]:
   if gmpy2.is_prime(p) :
      s += p

for p in [i*1000000000+j for i in range(1,10) for j in [1,3,7,9] if j != i]:
      if gmpy2.is_prime(p) :
         s+=p
print(s)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3, SUPER TARE  --------------------------')
t1  = time.time()

# === Mon, 12 Oct 2015, 04:54, j123, Python, Canada
# The following code (Python 2 or 3) works with any reasonable is_prime.
# With the strong pseudoprime function I posted in the thread for problem 387
# (it's deterministic up to at least 264, with no known false positives),
# it determined S(100, d) in under 7 seconds on my 2010 laptop, and the given problem in under 20ms.
# In sage, whose is_prime() function gives a deterministic answer for any sized number,
# running this same code took longer but gave the same result.

#for simpler-looking code, delete the "if" statements that lead to "continue" -- they just prune composite numbers early.
import itertools
def do(n = 10, combs=itertools.combinations, prod=itertools.product):
    '''Note: m here is the number of digits NOT equal to d'''
    digits = set(range(10))
    range_n = range(n)
    ans = 0
    all_ones = (10**n - 1) // 9
    for d in digits:
        ans_d = 0
        all_d = d * all_ones
        for m in range(n):
            for locs in combs(range_n, m):
                if locs and (locs[0] and not (d % 2 and d % 5) or \
                             locs[-1] != n-1 and not d):
                    continue
                for vs in prod(digits - set((d,)), repeat = m):
                    if locs and (locs[-1] == n-1 and not vs[-1] or
                                 not locs[0] and not (vs[0]%2 and vs[0]%5)):
                        continue
                    test = all_d
                    for loc, val in zip(locs, vs):
                        test += (val - d) * 10**loc
                    if gmpy2.is_prime(test):
                        ans_d += test
            if ans_d:
                break
        ans += ans_d
    return ans

do()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4, VERY NICE  --------------------------')
t1  = time.time()

# ===== Fri, 6 Dec 2013, 22:17,SafassThin, France
# Here is my main code - I start from numbers like '11111111112' and check if they are prime,
# then generate all permutations of this but without repetition
# EDIT: I'm stupid... I didn't bother to filter out all number ending in 0,2,4,5,6,and 8 -
# this speeds up quite nicely the code (I borrowed the coding from kutta's contribution)
#
# For those interested, I garbed this from the net (perms without repepetiion and Isprime by Fermat-Euler test
# - I'm not sure how reliable this isprimeFE test is, though - I tested it up to around 1e9...):
# Answer in 250msecs


# PERMUTATIONS WITHOUT REPETITION
# Luka Rahne @ http://stackoverflow.com/questions/6284396/permutations-with-unique-values/6285203#6285203
# (modified)
def permutations_wor(elements): # permutations without repetitions
    def recurse(listunique,p_list,d):
        if d < 0:
            yield tuple(p_list)
        else:
            for i in [j for j in listunique if j[1] > 0]:
                p_list[d] = i[0]
                i[1] -= 1
                for g in recurse(listunique,p_list,d-1):
                    yield g
                i[1] += 1
    listunique = [[i,elements.count(i)] for i in set(elements)]
    l = len(elements)
    return recurse(listunique,[0]*l,l-1)

# Primality test function based on Fermat/Euler pseudoprime test.
# To be used for large numbers (>1e6)
def isprimeFE(n): # http://www.math.umbc.edu/~campbell/Computers/Python/numbthy.py
    """
    isprimeFE(n) - Test whether n is prime using Fermat and Euler pseudoprime tests.
    """
    n = abs(n)
    if n==1 or n==0: return False
    if (n in [2,3,5,7,11,13,17,19,23,29]): return True
    return isprimeE(n,2) and isprimeE(n,3) and isprimeE(n,5) and isprimeE(n,7)

def isprimeF(n,b):
    """isprimeF(n,b) - Test whether n is prime or a Fermat pseudoprime to base b."""
    return (pow(b,n-1,n) == 1)

def isprimeE(n,b):
    """isprimeE(n,b) - Test whether n is prime or an Euler pseudoprime to base b."""
    if (not isprimeF(n,b)): return False
    r = n-1
    while (r%2 == 0): r //= 2
    c = pow(b,r,n)
    if (c == 1): return True
    while True:
        if (c == 1): return False
        if (c == n-1): return True
        c = pow(c,2,n)

def euler_111(ndigits=10):
    from itertools import combinations_with_replacement
    from functools import reduce

    def toint(lst): return reduce(lambda x, y: x*10+y,lst)

    sum,lower = 0,10**(ndigits-1)
    badends = {2,4,5,6,8,0}
    for d in range(10):
        Mnd,Snd = 0,ndigits-1
        while not Mnd:
            for padding in combinations_with_replacement(range(10), ndigits-Snd): # http://euler.clarinetcat.com/Problems/111
                root = [d]*Snd + list(padding)
                for perm in permutations_wor(root):
                    if not perm[-1] in badends:
                        candidate = toint(perm)
                        if candidate<lower: continue
                        if isprimeFE(candidate):
                            Mnd += 1
                            sum += candidate
            Snd -= 1
    return print(sum)

euler_111()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5,   --------------------------')
t1  = time.time()

# ==== Fri, 17 Jan 2014, 22:08, xwhisky, Czeck Republic
# Longer but readable.
# real	0m2.845s
# user	0m2.843s
# sys	0m0.004s

def xwhisky():
    import math

    def isPrime(n):
            d = 2
            while n > 1 and d < math.sqrt(n) + 1:
                    if n % d == 0:
                            return False
                    d += 1

            return True

    def lton(l):
            s = 10
            n = 0
            for d in l[::-1]:
                    n = n*s + d

            return n

    def numlen(n, l):
            return n >= 10**(l-1)

    def gen(d, k, l, n):
            if n == 0:
                    number = lton(l)
                    if isPrime(number) and numlen(number, 10):
                            return [number]
                    else:
                            return []

            res = []
            if k == 0:
                    res += gen(d, k, l + [d], n - 1)
            else:
                    for i in range(10):
                            if d != i:
                                    res += gen(d, k - 1, l + [i], n - 1)
                            else:
                                    res += gen(d, k, l + [d], n - 1)

            return res

    res = []
    for i in range(10):
            l = gen(i, 0, [], 10)
            k = 0
            while l == []:
                    k += 1
                    l = gen(i, k, [], 10)

            res += l
            print (i, l)

    return print (sum(res))

# xwhisky()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6,   --------------------------')
t1  = time.time()

# ===== Wed, 1 Oct 2014, 17:15, viennamarkov
# Algorithm L + fully deterministic Miller-Rabin = 200ms

N = 10
totalsum = 0

for d in range(0,10):    # digit
    primes = []
    for f in range(N-1,0,-1):    # frequency
        # If we've found a prime then we've found the biggest necessary freq.
        if len(primes) > 0:
            break

        for x in range(0,10**(N-f)):   # the other digits
            # Try every possible combination of digits exactly once.
            if str(x) == ''.join(sorted(str(x))):
                # Generate the digits.
                strn = str(d)*f+str(x).zfill(N-f)

                for n in unique_permutations(sorted(strn)):
                    # No leading zeroes.
                    if n[0] == '0':         continue
                    n = int(''.join(n))
                    if gmpy2.is_prime(n):
                        print(n)
                        primes.append(n)

    print(d, sum(set(primes)))
    totalsum += sum(set(primes))

print(totalsum)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 7,  VERY FAST --------------------------')
t1  = time.time()

# ==== Wed, 14 Jan 2015, 17:25, wakkadojo, USA
# I love problems like this one. My code is short, readable, and fast.
#
# Start with all repeated digits, and replace digits until we find primes.
# Once we know the fewest digits needed for replacement to hit a prime, sum all the primes that are encountered.
#
# 612407567715
#
# real	0m0.303s
# user	0m0.293s
# sys	0m0.007s
#
#
# 30 digits
#
# 106817351478400636669090393976752
#
# real	0m3.122s
# user	0m3.120s
# sys	0m0.000s
#
# 50 digits
#
# 13649829874858129439871718475477647224657734457831788
#
# real	0m10.187s
# user	0m10.180s
# sys	0m0.010s

def most_repeat (d, n, k):
    sample, p = [i for i in range (10) if i != d], []
    for x in itertools.combinations (range (n), n-k): # positions wildcards
        for y in itertools.product (sample, repeat=n-k):
            t = [str (d)]*n
            for i in range (n-k):
                t[x[i]] = str (y[i])
            t = ''.join (t)
            if gmpy2.is_prime (int (t)) and t[0] != '0':
                p += [int (t)]
    return sum (p) if len (p) > 0 else most_repeat (d, n, k-1)

print (sum (most_repeat (d, 10, 10) for d in range (10)))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

