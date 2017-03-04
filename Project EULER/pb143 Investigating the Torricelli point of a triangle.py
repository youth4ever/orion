#!/usr/bin/python                   o(^_^)o
# Solved by Bogdan Trif @       Completed on Sun, 19 Feb 2017, 23:48
#The  Euler Project  https://projecteuler.net
'''
Investigating the Torricelli point of a triangle        -           Problem 143

Let ABC be a triangle with all interior angles being less than 120 degrees.
Let X be any point inside the triangle and let XA = p, XC = q, and XB = r.

Fermat challenged Torricelli to find the position of X such that p + q + r was minimised.

Torricelli was able to prove that if equilateral triangles AOB, BNC and AMC are constructed on each side of triangle ABC,
the circumscribed circles of AOB, BNC, and AMC will intersect at a single point, T, inside the triangle.
Moreover he proved that T, called the Torricelli/Fermat point, minimises p + q + r.
Even more remarkable, it can be shown that when the sum is minimised,
AN = BM = CO = p + q + r and that AN, BM and CO also intersect at T.


If the sum is minimised and a, b, c, p, q and r are all positive integers we shall call triangle ABC a Torricelli triangle.
For example, a = 399, b = 455, c = 511 is an example of a Torricelli triangle, with p + q + r = 784.

Find the sum of all distinct values of p + q + r ≤ 120.000 for Torricelli triangles.

'''
import time
from gmpy2 import is_square, sqrt
from math import gcd, ceil, sqrt

######### GENERAL IDEA ###############
# 1.   We use https://en.wikipedia.org/w/index.php?title=Circumscribed_circle#Cyclic_quadrilaterals
#                   HAS THE PROPERY THAT 2 oppsoed angles of the patrulater sum up to 180 degrees
# 2.  Thus we find out that all the angles : ATC, ATB, BTC are 120 degrees
# 3.  We use the LAW OF COSINES and we find that c**2 = p**2 + r**2 - 2*p*r * cos(120) = p**2+r**2-p*r


# https://en.wikipedia.org/w/index.php?title=Circumscribed_circle#Cyclic_quadrilaterals
# https://en.wikipedia.org/wiki/Fermat_point
# http://www.cut-the-knot.org/Generalization/fermat_point.shtml
# http://mste.illinois.edu/courses/ci336sp04/folders/ckoeppen/5dayunit/lesson1.html
# https://www.youtube.com/watch?v=zPrzlbv6pTg

# http://www.geocities.ws/fredlb37/node9.html


def compute_triangle_angles( sides ):   # o(^_^)o #  Made by Bogdan Trif @ 2017-02-19, 12:20
    ''':Description: given a triangle with sides a,b,c the function computes all its angles.
        It uses the LAW OF SINES , where A,B,C are the angles opposed to corresponding sides a,b,c
        sin(A)/a =sin(B)/b =sin(C)/c
        and the LAW OF COSINES c**2 = a**2 + b**2 - 2*a*b * cos(C)
    :returns: A,B,C, the three corresponding angles    '''
    a, b, c = sides
    from math import sqrt, cos, sin, pi, acos, asin
    C = acos((a**2+b**2-c**2)/(2*a*b) )*180/pi
    A = asin(( a*sin(C*pi/180) )/c )*180/pi
    B = asin(( b*sin(C*pi/180) )/c )*180/pi
    return A, B, C

def triangle_primitive_triplets_120_gen(  ) :      # o(^_^)o #  Made by Bogdan Trif @ 2017-02-19, 13:10
    ##### 120 degree TRIANGLES GENERATOR
    # http://www.geocities.ws/fredlb37/node9.html
    ''':Description: GENERATOR for Triangle primitive triplets of 120 degrees
    :param up_lim: integer, the limit to which the sum of sides a,b,c is up to
    :return: the sides of the 120 degree triangle , p ,q, r   '''
    # cnt=0
    m, n = 1, 1
    while True :   # If needed we can set a limit based on m**2-n**2
        for n in range(1, m) :      ### range(1,m) as we need only p > 0 !!!!!!!!
            if gcd(m,n)==1 and (m-n)%3 !=0  :         #!!!! if we omit the %3 condition we will get duplicates !!!
                p = (m**2-n**2)
                q = (2*m*n+n**2)
                r = (m**2+n**2+m*n)
                if p > 0 :
                    # cnt+=1
                    # print(str(cnt)+'.         '  , p, q, r ,'       sum =',  p+q+r ,'            m,n =',m, n)#, compute_triangle_angles( [ p, q, r ] )  )
                    yield p,q, r
        m+=1


print('\ncompute_triangle_angles :\t', compute_triangle_angles( [ 19, 261, 271] ) ,'\n'  )

# 1.      p,q,r =  325 264 195           sum= 784           a,b,c= 399.0 511.0 455.0
# 2.      p,q,r =  440 325 264           sum= 1029           a,b,c= 511.0 665.0 616.0
# 3.      p,q,r =  650 528 390           sum= 1568           a,b,c= 798.0 1022.0 910.0
# 4.      p,q,r =  880 650 528           sum= 2058           a,b,c= 1022.0 1330.0 1232.0

print('\n-----------------------BRUTE FORCE --------------------\n')

def brute_force(lim) :

    Z=set()
    cnt=0
    for p in range(195, 50000):
        q = r= p
        for q in range(p+1, int(1.5*p)) :
            for r in range(q+1, int(1.5*q) ) :
                if p+q+r > lim  : break
                sq_c = p*p + r*r + p*r
                sq_b = p*p + q*q + p*q
                sq_a = q*q + r*r + q*r
                if is_square(sq_c) and is_square(sq_b) and is_square(sq_a) :
                    cnt+=1
                    print(str(cnt)+'.      p,q,r = ',p, q, r , '          sum=', p+q+r, '          a,b,c=', sqrt(sq_a), sqrt(sq_b), sqrt(sq_c) )
                    if p+q+r not in Z :
                        Z.add(p+q+r)
    return print('\nAnswer : \t', sum(Z))

# brute_force(lim=10**3)

# print('\n--------------------------TESTS------------------------------')
# t1  = time.time()
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1),6), 's\n\n')          #   Completed in : 3408.195019 ms

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()


def Torricelli_p_q_r( up_lim = 1.2*10**5 ) :
    Y = {}
    TPT = triangle_primitive_triplets_120_gen(  )
    p, q = 0, 0
    cnt=0
    while p <= up_lim :
        I = next(TPT)
        cnt+=1
        p, q, c = I
        pair = tuple(sorted([p, q]))
        # print(str(cnt)+'.     ', pair  )
        #   We put in a DICT all the sorted pairs with the key being the first value
        if pair[0] not in Y : Y[ pair[0] ] = [pair]
        elif pair[0] in Y :   Y[ pair[0] ].append(pair)
        # Multiply each element of the tuple with k to obtain multiple of the original primitive triplets
        k=2
        while (p+q)*k <= up_lim :
            cnt+=1
            pair_m = tuple(list(map(k .__mul__, ( pair ) )   ))
            # print(str(cnt)+'.     ', '     mult=',k,'      ', pair_m )
            if pair_m[0] not in Y : Y[ pair_m[0] ] = [pair_m]
            elif pair_m[0] in Y :  Y[ pair_m[0] ].append(pair_m)
            k+=1
    print('\n Y dictionary length:\t',len(Y), '\n' ,'\n\n')

    Uni = set()
    scnt, S = 0, 0
    for I in Y.keys() :
        for j in range(len(Y[I])) :
    # Establish the first pair, Example :  (195, 264) & set  p,q = 1-st, 2-nd value of this pair
            p, q = Y[I][j]
    # Look for the pair which has the first value the second value of the first pair, E.g. :  (264,325)
    # and set the second value as the 3-rd value : r = 325
            if q in Y :
                for k in range(len(Y[q])) :
                    r = Y[q][k][1]
                    # print('^^^^^^^^^^  r =  ' ,r , (q,r) ,'    p=' ,p,'          Y[p] =   ',Y[p] )
    # Now look into the first key for the last pair (p, r) =   (195, 325). If True, we found a p,q,r
                    if ( p, r) in Y[p] :
                        if p+q+r <= up_lim :
                            if p+q+r not in Uni :
                                Uni.add(p+q+r)
                                S+=p+q+r
                                scnt+=1
                                print(str(scnt)+'.         p, q, r = ' , p, q, r  )

    return print('\nSum of all distinct p, q, r values : \t', sum(Uni), '     ',S)

Torricelli_p_q_r( up_lim = 1.2*10**3 )              #    30758397


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,   --------------------------')
t1  = time.time()

# ==== Tue, 14 Apr 2015, 02:52, jh724186, Scotland
# Runs in a couple of seconds in python. Like many others, I spent a lot more time trying to solve via geometry than i care to recall.

# generate a set of unique integer triangles as tuple (the longest side is not needed)
mySet = set()
for n in range(1,200):
    for m in range(n+1,400):
        a = (2*m*n)+(n**2)
        b = (m**2)-(n**2)
        i=1                         # handle multiples
        while (i*(a+b))<120000:
            tup=(i*a,i*b)
            mySet.add(tup)
            i +=1

# create associative array, key="a side", contents list of matching other sides
myData = {}
for i in mySet:
    for j in range(2):
        if i[j] not in myData: myData[i[j]]=[]
        myData[i[j]].append(i[(j+1)%2])

# go through the original tuple to find a common match
myFinal=set()
for i in mySet:
    a,b = i[0],i[1]
    common = set(myData[a]).intersection(myData[b])
    for c in common:
        if (a+b+c)<=120000: myFinal.add(a+b+c)

print (sum(list(myFinal)))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()

# ==== Fri, 21 Oct 2016, 20:57, squidaction, USA
# I generated all p,q such that p^2+q^2+pq = a^2 like so:
# p = c*u*v, 1 <= u < 200, v > 3*u
# q = c*w*x, w = (u+v)/2, x = w-2*u
# and since (u+v)/2 must be an integer you can step v by 2. Runs in a few seconds in python.

from math import ceil
MAX=120000
S = {}
res = 0
sumz = []

def czech(p,q):
    ret = 0
    if p not in S:
        S[p] = set()
    if q not in S:
        S[q] = set()
    if q in S[p]: return 0
    for r in S[p]:
        if r in S[q] and p+q+r <= MAX and p+q+r not in sumz:
            ret += p+q+r
            sumz.append(p+q+r);

    S[p].add(q)
    S[q].add(p)
    return ret

for u in range(1, int(ceil(sqrt(MAX/3)))):
    v = u*3+2
    while u*v < MAX:
        p = u*v
        w = (u+v)//2
        x = w-2*u
        q = w*x
        if p+q >= MAX: break
        if p > q: p,q = q,p
        a = 1
        while True:
            p1,q1= a*p,a*q
            if p1+q1 >= MAX: break
            res += czech(p1,q1)
            a += 1
        v += 2
print(res)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3, SUPER SPEED  --------------------------')
t1  = time.time()

# ===Sat, 22 Jan 2011, 19:26, Orbifold , Canada

# Define a "Torricelli triple" to be three positive integers r, q, a
# where r^2 + r*q + q^2 = a^2.
# A Torricelli triple is "primitive" if gcd(r,q,a)=1.
# It can be shown by the same techniques as for enumerating Pythagorean
# triples that primitive Torricelli triples are completely and uniquely
# parameterized by (n^2-m^2, 2*m*n+m^2, n^2+m*n+m^2) where n and m are
# positive integers with n>m, gcd(n,m)=1, and n not congruent to m modulo 3.

from collections import defaultdict
from math import gcd

# r is a "partner" of q if r<q<a and (r,q,a) is a Torricelli triple.
PARTNERS = defaultdict(set)

# We want all p,q,r where p+q+r<=120000, p>q>r>0 (let's say) and
# p+q = k(n^2-m^2 + 2mn+m^2) = k(n^2+2mn) for some n>m>0.
# k(n^2+2mn) < 120000 implies n^2+2n < 120000, i.e. n<346

for n in range(2, 346):
  for m in range(1, n):
    if gcd(m, n) > 1: continue
    if (n-m)%3 == 0: continue
    q, r = 2*m*n+m**2, n**2-m**2
    if q < r: q, r = r, q
    for k in range(1, 120000//q + 1):
      PARTNERS[k*q].add(k*r)

results = set()

for p, s in PARTNERS.items():
  for q in s:
    if q not in PARTNERS: continue
    for r in s & PARTNERS[q] :
      results.add(p+q+r)

print (sum(n for n in results if n <= 120000))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,   --------------------------')
t1  = time.time()

# === Sun, 28 Dec 2008, 16:50, tolstopuz, Russia

import math
nmax = 110000

s = {}

for cc in range(1, int(math.sqrt(2 * nmax)) + 1):
    for dd in range(1, cc):
        if math.gcd(cc, dd) == 1:
            p = 4 * cc * dd
            q = abs(3 * cc * cc - dd * dd) - 2 * cc * dd
            if q > 0:
                for i in range(2):
                    if q % 2 == 0:
                        p //= 2
                        q //= 2
                for k in range(1, nmax // max(p, q) + 1):
                    if k * max(p, q) in s:
                        s[k * max(p, q)].add(k * min(p, q))
                    else:
                        s[k * max(p, q)] = {k * min(p, q)}

print(sum({x + y + z for x in s for y in s[x] if y in s
        for z in s[x] & s[y] if x+y+z <= nmax}))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

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
