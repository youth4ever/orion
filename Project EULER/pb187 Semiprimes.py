#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Sat, 3 Dec 2016, 00:02
#The  Euler Project  https://projecteuler.net
'''
                    Semiprimes      -       Problem 187

A composite is a number containing at least two prime factors.

        For example, 15 = 3 × 5; 9 = 3 × 3; 12 = 2 × 2 × 3.

There are ten composites below thirty containing precisely two, not necessarily distinct, prime factors:
                4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

How many composite integers, n < 10**8, have precisely two, not necessarily distinct, prime factors?

'''
import time


def prime_generator(n):         # HIghly Efficient !!!!         THE FASTEST, The BEST , The ONE
    """  Sieve of Eratosthenes              !!!!!!!!! THE FASTEST SIEVE. It won the battle with sieve
    Create a candidate list within which non-primes will be marked as None.
    """
    cand = [i for i in range(3, n + 1, 2)]
    end = int(n ** 0.5) // 2

    # Loop over candidates (cand), marking out each multiple.
    for i in range(end):
        if cand[i]:
            cand[cand[i] + i::cand[i]] = [None] * ( (n // cand[i]) - (n // (2 * cand[i])) - 1 )

    # Filter out non-primes and return the list.
    return [2] + [i for i in cand if i]

def bin_search(n, List):        # VERY FAST ALGORITHM
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
        if List[midpoint] == n: return midpoint
        elif List[midpoint] > n: right = midpoint-1
        else: left = midpoint+1
    if n > List[midpoint]: return midpoint
    else: return (midpoint-1)


print('\n--------------------------TESTS------------------------------')

primes = prime_generator( 10**3 )
print(len(primes), primes[0:100])

myNumber = 87
print('Closest number of :',myNumber,'is :  ' ,min(primes, key=lambda x: abs(x-myNumber)),'\n')
# print(2*primes[-1])



print('\n================  My FIRST SOLUTION, VERY SLOW, 20 min  ===============\n')
t1  = time.time()
# It is very slow because of  min(primes, key=lambda x: abs(x-up_limit)) which takes > 1s for each iteration, for a >10**6 primes
# it is VERY VERY SLOW. Solution : Use the binary approach ! MUch Much FASTER

up_range = 10**4
primes = prime_generator( up_range//2 )
print('There are ', len(primes),' primes in the range ', up_range,'\n\n')

up_limit = pow(up_range, 1/2)
lim = min(primes, key=lambda x: abs(x-up_limit))
if lim**2 < up_range :  UP = primes.index(lim)+1
else :  UP = primes.index(lim)
# print(lim, UP)

counter = 0
for i in range(UP):
    a = primes[i]
    y = up_range//a
    b = min(primes, key=lambda x: abs(x-y))

    if a*b > up_range :
        b = primes[primes.index(b)-1]
    i_a, i_b = primes.index(a), primes.index(b)
    length = i_b-i_a+1
    counter += length
    print('first nr: ',a, '   last nr: ',b, ' ;   max prod: ' ,a*b ,'       Length:  ', length , '    counter:', counter  )

print('\nAnswer : ', counter)          #  Answer :  17427258





t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')            # Completed in : 6.845392 s

print('\n================  My Second SOLUTION, Improved Using BINARY SEARCH  ===============\n')
t1  = time.time()


up_range = 10**8
primes = prime_generator( up_range//2 )
print('There are ', len(primes),' primes in the range ', up_range,'\n\n')

up_limit = pow(up_range, 1/2)
lim = min(primes, key=lambda x: abs(x-up_limit))
if lim**2 < up_range :  UP = primes.index(lim)+1
else :  UP = primes.index(lim)
# print(lim, UP)

counter = 0
for i in range(UP):
    a = primes[i]
    y = up_range//a
    i_b = bin_search(y, primes)
    # b = primes[i_b]
    # if a*b > up_range :
    #     b = primes[primes.index(b)-1]
    i_a  = primes.index(a)
    length = i_b - i_a + 1
    counter += length
    # print('first nr: ',a, '   last nr: ',b, ' ;   max prod: ' ,a*b ,'       Length:  ', length , '    counter:', counter  )
    # print('first index: ',i_a, '   last index: ',i_b, ' ;          Length:  ', length , '    counter:', counter  )

print('\nAnswer : ', counter)               #  Answer :  17427258



t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')            # Completed in : 8.379479 s



print('\n--------------------------MORE TESTS  --------------------------')
t1  = time.time()


y = 5555555
# b = min(primes, key=lambda x: abs(x-y))
b = primes.index(min(primes, key=lambda x: abs(x-y)))
print(b)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

t1  = time.time()

# takeClosest = lambda num,collection:min(collection,key=lambda x:abs(x-num))
# takeClosest(y ,primes)

# print( min(enumerate(primes), key=lambda x: abs(x[1]-y)) )

# from heapq import nsmallest
# print(nsmallest(3, primes, key=lambda x: abs(x-y) ))

# print(  [n for d, n in sorted((abs(x-y), x) for x in primes)[:3]]  )

print(bin_search(y, primes))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1, Binary Search Algorithm  ,FJ_Sevilla, Spain, FAST --------------------------')
t1  = time.time()

from math import sqrt

def Eratosthenes_sieve(lim):
    sieve = [True] * lim
    for num in range(3,int(sqrt(lim))+1,2):
        if sieve[num]:
            sieve[num*num::2*num]=[False]*int((lim-num*num-1)/(2*num)+1)
    return [2] + [n for n in range(3,lim,2) if sieve[n]]

def bin_search(n,List):
    left = 0
    right = len(List) -1

    while left <= right:
        midpoint = (left+right)//2
        if List[midpoint] == n: return midpoint
        elif List[midpoint] > n: right = midpoint-1
        else: left = midpoint+1
    if n > List[midpoint]: return midpoint
    else: return (midpoint-1)

def main():
    lim = 10**8
    primes= Eratosthenes_sieve(lim//2)
    res=0
    for n in range(bin_search(int(sqrt(lim)),primes)+1):
        res += bin_search(int(lim/primes[n]),primes)-n+1
    print(res)

if __name__ == '__main__':
    main()
    # input('Press "Enter" to out...')


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')          # Completed in : 5204.297781 ms

print('\n--------------------------SOLUTION 2, mmaximus, Portugal  --------------------------')
t1  = time.time()

# The idea is: generate all primes under 10**8/2 and store then in a list.
# Then, pick the largest prime, and start pairing up with 2, 3, 5, etc.. until you go above 10**8/2 or you meet yourself on the list.
# Count +1 every time you do this. Then, add 1 at the end because we leave 4 out.
#
# Runs in 34 seconds on a i3 dual core @2.4 GHz laptop, windows 8
# (lol it took me longer to find out my system specs than to solve the problem)


def primes_sieve2(limit):
    a = [True] * limit
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i * i, limit, i):
                a[n] = False
print('sieving')
working_primes = list(primes_sieve2(50000001))
print('done sieving')

count = 0
i = -1
p = working_primes[i]
while p > 2:
    k = 0
    while (p * working_primes[k] < 10**8) and p >= working_primes[k]:
        count += 1
        k += 1
    i -= 1
    p = working_primes[i]

print(count + 1) # include 4 at the end

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3, Hoxie Ackerman, USA  --------------------------')
t1  = time.time()
# It made sense to start with the primes and generate/count the two-factor composite numbers.
# How do we generate these composite numbers?
#
# Well, for the first prime (2), we can use it in a product with 2, 3, ..., all the way up to the largest prime less than or equal to 10**8 // 2.
#
# For the second prime, we can use it in a product with 3, ..., all the way up to the largest prime le 10**8 // 3.
#
# (Because of the Prime Factorization Theorem, these products are all guaranteed to be unique, so we don't need to worry about double-counting.)
#
# So then the question becomes, "How many primes are there between my current prime and an upper cutoff value?"
# Since the primes are sorted, we can use a binary search variation to very quickly find the upper cutoff value,
# and then use the array indices to figure out how many elements we're talking about.

from bisect import bisect_right

def find_le(a, x):
    """
    Find rightmost value less than or equal to x, and its index
    https://docs.python.org/3.5/library/bisect.html#searching-sorted-lists
    """
    i = bisect_right(a, x)
    if i:
        return i-1, a[i-1]
    raise ValueError("{}".format(x))

def ans(upper):
    primes = primes
    num_winners = 0
    for i, prime in enumerate(primes):
        max_possible_factor = upper // prime
        if prime > max_possible_factor:
            break
        j, max_prime_factor = find_le(primes, max_possible_factor)
        num_winning_primes = j - i + 1
        num_winners += num_winning_primes
    return num_winners

assert ans(30) == 10
UPPER = 10**8
print(ans(UPPER))

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
