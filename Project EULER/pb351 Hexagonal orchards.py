#!/usr/bin/python                   ( ͡° ͜ʖ ͡°)
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
                    Hexagonal orchards      -       Problem 351

A hexagonal orchard of order n is a triangular lattice made up of points within a regular hexagon with side n.
The following is an example of a hexagonal orchard of order 5:


Highlighted in green are the points which are hidden from the center by a point closer to it.
It can be seen that for a hexagonal orchard of order 5, 30 points are hidden from the center.

Let H(n) be the number of points hidden from the center in a hexagonal orchard of order n.

H(5) = 30. H(10) = 138. H(1 000) = 1177848.

Find H(100 000 000).


'''
import time, gmpy2
from math import gcd, sqrt
from sympy import totient


def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    from pyprimes import factorise
    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]


def euler_totient(n):
    """returns Euler totient (phi) of n """
    phi=n
    pfs=set(get_factors(n))
    for pf in pfs:
        phi*=(1-1/pf)
    return int(phi)

print('euler_totient : \t', euler_totient(600))



print('\n--------------------------TESTS------------------------------')
t1  = time.time()


def brute_force_check(n) :
    cnt=0
    for i in range(1, n+1):
        if gmpy2.is_prime(i) == False :
            for j in range(2, i):
                if gcd(i, j) != 1  :
                    cnt+=1
    return  (cnt+n-1) *6

print( 'brute_force_check: \t', brute_force_check(100),'\n\n' )

print('\n================  Not Optimized SOLUTION,   ===============\n')
t1  = time.time()

### To optimize the solution we must build a sieve ( or just go on the run) and
# see how many

T = 0
for i in range(2, 101) :
    hp = brute_force_check(i)
    print('order =', i, '    points : ',hp, '   ', hp//6, '     gcds =', i-totient(i) )
    T+=i-totient(i)

print('\nAnswer : \t', T*6)



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n======My FIRST SOLUTION, Using Totient Sieve to compute gcds != 1 , 6min ===============\n')
t1  = time.time()

###    GCDD's  compute The  n- Φ (n) of a number #########

def prime_sieve(n):       # SECOND FASTEST        o(^_^)o
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[ i*i :: 2*i ] = [False] * ( (n-i*i-1) // (2*i) +1 )
    return [2] + [i for i in range(3, n , 2) if sieve[i] ]


def multiple_gen(modulus):
    """Generates the list of multiples of modulus."""
    count = 1
    while True:
        yield modulus * count
        count += 1

def fast_compute_totients(bound):
    """
    gcds are n - Φ (n) , more precisely all the i  smaller < n numbers for which
     gcd( i , n) != 1 , meaning that they have a common factor > 1
    """

    # Populate the initial list with the leading factor of n.
    results = list(range(0, bound+1))

    # Get the list of primes up to the bound.
    primes = prime_sieve(bound)

    for p in primes:
        for m in multiple_gen(p):
            if m > bound:
                break
            results[m] = (results[m] // p) * (p - 1)

    # Here we inverse the list with the formula n- Φ (n)
    # for i in range(1, len(results) ):
    #     results[i] = i-results[i]
    print(results[:100])
    return sum(results)

def my_first_solution( lim ):
    f = fast_compute_totients(lim)
    return print( '\n Answer : \t ',  ( lim*(lim+1)//2 - f) *6 )


# my_first_solution( lim=10**8 )                         #    Answer : 	  11762187201804552


t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')


######## IDEAS ############
# http://math.stackexchange.com/questions/316376/how-to-calculate-these-totient-summation-sums-efficiently


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,  4 min --------------------------')
t1  = time.time()

# === Mon, 9 May 2016, 04:11, Varcho, USA
# Using the basic starting formula:
# f(n)=6(n(n+1)2−∑ni=1ϕ(n))
#
# The solution could then be calculated (somewhat slowly ~1 min run time)


def Solution(N):
    return 6 * (N * (N + 1)/2 - sum(EulerTotient(N)))

def EulerTotient(n):
    phi = list(range(n+1))
    for i in range(2,n+1):
        if phi[i]==i:
            for x in range(i,n+1,i):
                phi[x]-=phi[x]//i
    return phi[1:]

# print (Solution(10**8))

t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')

print('\n--------------------------SOLUTION 2, , VERY FAST, 7 sec  --------------------------')
t1  = time.time()

# I managed to work out that H(n)=6(n(n−1)/2−Φ(n)),
# then  I used code from problem p512, another totient summation problem. It is the O(n3/4) algorithm
# (I think, not sure, yet), using recursion and a memo. About 3 s.
#
# The analysis below and the original (in C) of the code  I use is from the very helpful post by Andy
# on this Stack Exchange page on totient sums, and from the overview for  problem 73..
# http://math.stackexchange.com/questions/316376/how-to-calculate-these-totient-summation-sums-efficiently
#
# The idea is that if
# F=cardinality{a,b:0<a<b≤n}=n(n−1)2
#
# R=cardinality{a,b:0<a<b≤n,gcd(a,b)=1}
#
# then the totient sum Φ(n)=1+R(n)Φ(n)=1+R(n).
# Moreover,
# (⌊nm⌋)=cardinality{a,b:0<a<b≤n,gcd(a,b)=m}
#
# and so
# F(n)=∑m=1nR(⌊nm⌋)
#
# We want the first term of this summation:
# R(n)=F(n)−∑m=2nR(⌊nm⌋)
#
#
# This is what the code implements, exploiting the fact that ⌊nm⌋⌊nm⌋ remains constant over wide ranges of m.
# It is Eq 3.2.2 from Marcus Stuhr's fascinating overview for this problem.
# If I use the recursive version of Marcus's O(n2/3(n log log n)1/3) totient summatory function ' \
# (Algorithm 7 in the overview) instead of my own, then I find the answer for n=10**8 in about 0.6s,
# and about 0.5s if I use the recursive version (Algorithm 8 in the overview).


def p351(n):
    print( 6*(F(n)-totientSum(n)))


def R(n,memo={}):
    if n==1:
        return 0
    try:
        return memo[n]
    except KeyError:
        fsum = F(n)
        m=2
        while 1:
            x = n//m
            nxt = n//x
            if(nxt >= n):
                result=fsum - (n-m+1)*R(n//m,memo)
                memo[n]=result
                return result
            fsum -= (nxt-m+1) * R(n//m,memo)
            m = nxt+1

def F(n):
    return n*(n-1)//2

def totientSum(n):
    return 1 + R(n)

#from overview for pe351 by Marcus Stuhr
#used by TotientSum7 - recursive version of O((n/(log(log(n))))^(2/3)) algorithm
def v7(n,L,sieve,memo):
    if n<=L:
        return sieve[n]
    else:
        try:
            return memo[n]
        except KeyError:
            res=n*(n+1)//2

            for g in range(2,int(n**0.5)+1):
                res-=v7(n//g,L,sieve,memo)

            for z in range(1,int(n**0.5)+1):
                if n//z!=z:
                    res-=(n//z-n//(z+1))*v7(z,L,sieve,memo)

            memo[n]=res
            return res

#from overview for pe351 by Marcus Stuhr
#recursive version of O((n/(log(log(n))))^(2/3)) algorithm
#if use instead of my totientSum(), gives a x5 speed up for n=10^8
def TotientSum7(n):
    L=int((n/(math.log(math.log(n))))**(2/3))
    sieve =list(range(L+1))
    memo={}
    for p in range(2,L+1):
        if p==sieve[p]:
            k=p
            while k <= L:
                sieve[k]-=sieve[k]//p
                k+=p
        sieve[p]+=sieve[p-1]
    return v7(n,L,sieve,memo)

#Algorithm 8 from the p351 overview
#iterative version of O((n/(log(log(n))))^(2/3)) algorithm
#if use instead of my totientSum(), gives a x6 speed up for n=10^8
def TotientSum8(n):
    L=int((n/(math.log(math.log(n))))**(2/3))
    sieve =list(range(L+1))
    bigV=[0]*(n//L+1)

    for p in range(2,L+1):
        if p==sieve[p]:
            k=p
            while k <= L:
                sieve[k] -= sieve[k]//p
                k+=p
        sieve[p] += sieve[p-1]

    for x in range(n//L,0,-1):
        k=n//x
        res=k*(k+1)//2

        for g in range(2,int(k**0.5)+1):
            if k//g<=L:
                res-=sieve[k//g]
            else:
                res-=bigV[x*g]

        for z in range(1,int(k**0.5)+1):
            if z != k//z:
                res -= (k//z-k//(z + 1))*sieve[z]

        bigV[x]=res

    return bigV[1]


# p351(10**8)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,  SUPER TARE !!, Must study it ! --------------------------')
t1  = time.time()

# ===== Wed, 2 Mar 2016, 21:07, j123, Canada
# I'm so happy I kept working on problem 73 to get a fast solution.
# With small and straightforward changes to 2 lines from that code I could get this one without
# even needing to derive the exact connection to Euler's phi.
# This is the O(n3/4) algorithm, takes about 1.5 seconds in interpreted Python on my ancient machine.

from collections import defaultdict
def do(n = 10**8):
    sqrt_n = int(n**0.5)
    quots = [n//i for i in range(1, sqrt_n + 1)]
    quots.extend(range(sqrt_n - (sqrt_n == quots[-1]), 0, -1))
    quots.reverse() #now increasing!
    rest = [(int(k**0.5), 3*k*(k+1)) for k in quots]
    ans = defaultdict(int)
    for k, (sqrt_k, init) in zip(quots, rest):
        k_quot = [k // i for i in range(1, sqrt_k + 2)]
        if k_quot[-2] == sqrt_k: k_quot[-1] = sqrt_k
        that = enumerate(zip(k_quot, k_quot[1:]), 1)
        ans[k] = init - sum([ans[i] * (x - y) + ans[x] for i, (x, y) in that])
    return print(3*n*(n+1) - ans[n])

do()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4, VERY FAST Using  Farey Sequence --------------------------')
t1  = time.time()

# ===== Sun, 13 May 2012, 02:13, mjf,
# About 8 seconds on a 3.3GHz Celeron, using David W. Wilson's recurrence for the Farey sequence ' \
# from http://oeis.org/A005728

import math

def counted_quotients(n):
    """Generate pairs (distinct value, number of occurences ) for
    (n//k for k in range(2, n+1))

    """
    for k in range(2, int(math.sqrt(n)) + 1):
        yield (n//k, 1)
    for q in range(n//int(math.sqrt(n)) - 1, 0, -1):
        if n//q > n//(q+1):
            yield (q, n//q - n//(q+1))

def farey(n, memo={0:1,1:2}):
    if n in memo:
        return memo[n]
    result = n*(n+3)//2 -  sum(f*farey(q) for q, f in counted_quotients(n))
    memo[n] = result
    return result

def hidden_points(n):
    return (6 * (n-1)             # Hidden points on main diagonals
            + 6 * (n-1)*n//2      # All points not on main diagonals >1 from centre
            - 6 * (farey(n) - 2)) # Visible points not on main diagonals >1 from centre
                                  # =sum m=2..n phi(m)

print (hidden_points(10**8))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5,  7 seconds , VERY INTERESTING --------------------------')
t1  = time.time()

# Let V(n)V(n) be the number of visible points in a hexagon of size nn, except for the center.
# Then there is this interesting recursive formula:
# V(n)=3n(n+1)−∑2≤m<nV(⌊nm⌋).
#
#
# The derivation of this formula is that if you dilate the visible points by a factor of mm,
# they land on hidden points, and for different values of mm, they land on different hidden points.
# As Dr.Korbin says earlier in this thread, you can use the method of Möbius inversion to convert
# this formula to a direct expression for V(n) or H(n).
# That is what I thought of first, but then I realized that this direct form is better because of two accelerations:
# (1) ⌊n/m⌋⌊n/m⌋ repeats when m(m+1)>nm(m+1)>n, so you can compress the sum in this range
# instead of summing each term separately.  (2) You can also cache the evaluations of V(n).
# The final algorithm takes O(n3/4)O(n3/4) execution steps and uses a cache of size O(n1/2),
# while many of the alternatives take linear time or worse.
# My Python implementation of this algorithm takes 8 seconds on a laptop.
#
# Lucy_Hedgehog gives a somewhat similar but different solution using the Mertens function.
# The running time of that algorithm is O((logn)αn2/3), which is better than what I obtained.
# However, my direct algorithm works for any fixed shape of polygon or polytope with integer vertices,
# not just for a hexagon in the plane.
# (Of course, the leading term in the above equation gets more complicated as the polytope gets more complicated.)
#
# Here is my code, for those interested:

cache = {}
def visible(size):
    if size in cache: return cache[size]
    total = 3*size*(size+1)
    n = 2
    while n*(n+1) < size:
        total -= visible(int(size/n))
        n += 1
    for m in range(1,int(size/n)+1):
        total -= (int(size/m)-int(size/(m+1)))*visible(m)
    cache[size] = total
    return total

for n in (5,10,1000,10**8):
    print (n,3*n*(n+1)-visible(n))


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
