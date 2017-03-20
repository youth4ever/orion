#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
Investigating progressive numbers, n, which are also square         -       Problem 141

A positive integer, n, is divided by d and the quotient and remainder are q and r respectively.

In addition d, q, and r are consecutive positive integer terms in a geometric sequence, but not necessarily in that order.

For example, 58 divided by 6 has quotient 9 and remainder 4.
It can also be seen that 4, 6, 9 are consecutive terms in a geometric sequence (common ratio 3/2).
We will call such numbers, n, progressive.

Some progressive numbers, such as 9 and 10404 = 102**2, happen to also be perfect squares.
The sum of all progressive perfect squares below one hundred thousand is 124657.

Find the sum of all progressive perfect squares below one trillion (10**12).

'''
import time, gmpy2
from math import sqrt, ceil, floor, gcd
from pyprimes import factorise
from itertools import combinations, permutations
import functools, operator
from decimal import *
getcontext().prec = 50

import numpy
def prime_sieve_numpy(n):                       ### o(^_^)o  FASTEST  o(^_^)o  ###  Highly Efficient !!!
    """ Input n>=6, Returns a array of primes, 2 <= p < n
    http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188 """
    sieve = numpy.ones(n//3 + (n%6==2), dtype=numpy.bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]

def pair_Factors(n):        # VERY EFFICIENT !!!! SUPER INTELLIGENT ALGORITHM
    todo, combis = [(n, 2, [])], []
    while todo:
        n, i, combi = todo.pop()
        while i * i <= n:
            if n % i == 0:
                combis += combi + [i, n//i],
                # todo += (n//i, i, combi+[i]),       # If needed only PAIRS (a,b) comment this line !!!
            i += 1
    return combis

def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''

    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]

def binary_search(n, List):        # VERY FAST ALGORITHM
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

def naive_gen(lim=100):
    P = [2,3,5,7]
    N = []

    for i in P:
        o=i
        while i < 100 :
            N.append(i)
            i*=o
    # print(N)

    for i in P :
        for j in N :
            if j%i != 0 :
                if i*j < 100 and i*j not in N :
                    N.append(i*j)
    N.sort()
    return N


def inverse_farey( n, max_ratio ):      ####  o(^_^)o  FASTEST  ( ͡° ͜ʖ ͡°)  ### !!! Best Farey Sequence
    ''':Description: Generates INCREASING FAREY SEQUENCE
        taken from http://pythonfiddle.com/farey-series-generator/
        Modified by Bogdan Trif @2017-02-28, 14:00     '''
    F , asc = [], True
    if asc:
        a, b, c, d = 0, 1, 1, n
    else:
        a, b, c, d = 1, 1, n-1, n
    i=1
#     print ("%d/%d" % (a,b),)
    while (asc and c <= n) or (not asc and a > 0):
        k = int((n + b)/d)
        a, b, c, d = c, d, k*c - a, k*d - b
#         print ("%d/%d" % (a,b),end=' ')
        if b/a <= max_ratio :
            F.append((b,a))
        i+=1
    return F

print(inverse_farey(18, 5 ) )

print('\n--------------------------TESTS------------------------------')

# SUMS as checks
#                 10^5: 124657
#                 10^6: 700738
#                 10^8: 171436696

t1  = time.time()


# @ 2017-02-25, 20:00 . This is tooooo SLOW !!!!
# A cannot relate on the ratio k, because I have irrational k like 4.44444444444444444444444
# Brute force attempt is really taking tooooo much
# Also other approach was not successful
#
# I NEEEEEED an insight !  Otherwise this problem is NOT SOLVABLE !!!!
# Imagine that until 10**4 I need 80 seconds . So probably for 10**6 I would need at least 10 hours !!!


t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')


print('\n--------------------------TESTS------------------------------')



print('\n================  SECOND BRUTE FORCE   ===============\n')
t1  = time.time()

def yet_another_brute_force(up) :
    up_lim = up*2/3
    R = set([r**2 for r in range(1, int( up**(1/2)) )  if r**2 <= up_lim ] +
                [r**3 for r in range(2, int(up**(1/3)) ) if r**3 <= up_lim  ] +[ r**5 for r in range(2, int(up**(1/5)) ) if r**5 <= up_lim] )
    R = sorted(list(R))

    print(len(R),'\n' ,R[:100] ,'\n\n')
    S = set()
    for m in range(3 , up) :
    # for m in range(98640 , 98641) :
    # for m in range(200000 , up) :
        r_ind = binary_search(m//100, R  )
        if m < 100 : r_ind = 0
        # print(m, r_ind, R[r_ind])
        for r in R[r_ind:] :
        # for r in R :
            if r >= m : break
            n = m*m
            # k = ( gmpy2.mpq((n-r),(r*r)) ** (1/3) )
            k = pow (  ((n-r) /(r*r))  , 1/3  )
            if k >1 :
                d = r*k
                # if  r == 50625 and m== 98640  :
                #     print('k: ', k, '    r:', r ,'     d : ', d, round(d) , '     error d:',abs(d - round(d) ) ,' q: ' , d*k, '  n:',n , '   error n:', abs(n - round(n) ) )
                # if abs(d - round(d ) ) < 1e-10 :
                if abs(d - round(d ) ) < 1e-8 :
                    q = d*k
                    m2 = pow( (k**3*r**2+r) , 1/2 )
                    # if  r == 50625 and m== 98640  :
                    #     print('k: ', k, '    r:', r ,'     d : ', d, round(d) , '     error d:',abs(d - round(d) ) ,' q: ' , d*k, '  n:',n , '   error n:', abs(n - round(n) ) )
                    if abs(m - m2 ) < 1e-10 :
                    # if abs(n - round(n) ) < 1e-5 :
                        if gmpy2.is_square(round(n)) :
                            if m not in S : # and n < up**2 :
                                S.add(m)
                                d, q = round(d), round(q)
                                print( 'm='+str(m)+'.      r=',r, '     d=',d, '     q=' ,q , '  ; n=', round(n),'   ;     k=', k ,'     r=',get_factors(r), '    d=',get_factors(d) , '  ;   error m:', abs(m - m2 ) )

    print('\nElements : \t', S )

    return print('\nAnswer : \t', sum([i**2 for i in S]) )


# yet_another_brute_force(10**6)


def brute_force (up_bound) :
    S = 0

    for d in range( 2, up_bound ) :
        for r in range(d-1, 0, -1 ) :
            if d/r >12 : break
            n = d**3 /r + r
            if  (n**(1/2)) % 1 != 0 : continue
            if  (n**(1/2)) % 1 == 0 and n < up_bound**2 :
                q , k  = d**2//r , d/r
                S += n
                print('   r =  ',r , '     d=',d , '       q=',q , '     n=',n,'     ratio =', k ,'       r = ', get_factors(r))

    return print('\nAnswer : \t', S)

# brute_force( 10**6  )


t2  = time.time()
print('\nCompleted in :', round((t2-t1)/60, 6), 'min\n\n')


print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()


def progressive_numbers(up) :
    up_lim = up*3//5
    # up_lim = up
    R = set([r**2 for r in range(2, int( up_lim**(1/2) ) )  if r**2 <= up_lim ]  )

    tmp=[]
    for n in range(2, 10**3) :
        for r in sorted(list(R)) :
            if  n* r <  up_lim :
                tmp.append(n*r)
    R |= set(tmp)
    R = sorted(list(R))
    print(len(R),  max(R) ,R[:50], R[-50::]  , '\n')

    S, cnt = 9, 1

    for d in range( 2, 7*up//8) :

    # for d in range( up*8//10,  up ) :
        if d% 10**4 == 0 : print(d)
        if gmpy2.is_prime(d) : continue
        if d <= 10**4 : f = d//12
        if  d > 10**4 : f = d//4
        if  d > 5*10**5 : f = d//1.6
        ind_r = binary_search(f, R)

        for r in R[ind_r:] :
        # for r in R :
            if r > d  : break
            if gcd (d , r) == 1 : continue
            n = d**3 /r + r
            if  (n**(1/2)) % 1 == 0 and n < up**2 :
                q , k  = d**2/r , d/r
                if q % 1 == 0 :
                    S += n
                    cnt+=1
                    print(str(cnt)+'.     r =  ',r , '     d=',d , '       q=',q , '     n=',n,'     ratio =', k ,'       r = ', get_factors(r),'     ' , S)

    return print('\nAnswer : \t', S )


# progressive_numbers( 10**6  )
# progressive_numbers( int((10**5)**(1/2) )+1  )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)/60, 6), 'min\n\n')


print('\n================  My SECOND SOLUTION,   ===============\n')
t1  = time.time()

def second_solution( lim ):
    S = 0
    cnt =  0

    for a in range(2, lim + 1 ):
        for b in range(1, a) :
            if gcd(a,b) == 1 :
                c= 1
                while 1 :
                    n = a**3*b*c**2 + b**2*c
                    if n > 10**12 : break
                    if gmpy2.is_square(n) :
                        r , d, q, k = c*b**2, a*b*c, a**2*c,  a/b
                        cnt+=1
                        S+=n
                        print(str(cnt)+'.     r =  ',r , '     d=',d , '       q=',q , '     n=',n,'     ratio =', k ,'       r = ', get_factors(r),'     ' , S , '        a,b,c = ',a,b,c)

                    c+=1
        if a%10**3 == 0 : print(a)

    return print('\nAnswer : \t', S)

# second_solution(10**4)              #       Answer : 	 878454337159

t2  = time.time()
print('\nCompleted in :', round((t2-t1)/60, 6), 'min\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,   --------------------------')
t1  = time.time()



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()

# === Tue, 14 Jul 2015, 05:32, bukebuer, China
# Reached n=k3t(c3+t)=m2n=k3t(c3+t)=m2 as most people.
# Then using brute search, while having some generator techniques to accelerate the code.

import math
from itertools import takewhile, count

def f(k, t, c):
    return k*k*k * t * (c*c*c + t)

def ep141():
    N = 1000000000000
    s = set([])
    for k in takewhile(lambda k: f(k, 1, k+1) < N, count(1)):
        for t in takewhile(lambda t: f(k, t, t*k+1) < N, count(1)):
            for c in takewhile(lambda c: f(k, t, c) < N, count(t*k+1)):
                n = f(k, t, c)
                if n in s:
                    continue
                sn = int(math.sqrt(n))
                if sn*sn == n:
                    print (k*k*k*t*t, k*c*c, n)
                    s.add(n)
    return sum(s)

ep141()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,   --------------------------')
t1  = time.time()



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
