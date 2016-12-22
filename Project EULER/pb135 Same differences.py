#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Tue, 13 Dec 2016, 19:59
#The  Euler Project  https://projecteuler.net
'''
Same differences        -       Problem 135
Given the positive integers, x, y, and z, are consecutive terms of an arithmetic progression,
the least value of the positive integer, n, for which the equation, x**2 − y**2 − z**2 = n, has exactly two solutions is n = 27:

34**2 − 27**2 − 20**2 = 12**2 − 9**2 − 6**2 = 27

It turns out that n = 1155 is the least value which has exactly ten solutions.

How many values of n less than one million have exactly ten distinct solutions?
'''

import time, sys
from  math import sqrt, gcd
import pyprimes
import gmpy2
from pyprimes import factorise

def get_divisors(n):      ### o(^_^)o  FASTEST  o(^_^)o  ### !! FIRST FASTEST
  factors = set()
  for x in range(1, int(sqrt(n)) + 1):
    if n % x == 0:
      factors.add(x)
      factors.add(n//x)
  return sorted(factors)

def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]

def same_diff(n):
    B=[]
    for x in range(n*3//2, n//32, -1) :
        # print(x)
        for p in range(1, n//4+2 ) :
            y , z = x-p, x-2*p
            if y> 0 and z > 0  :
                if  ( pow(x,2) - pow(y,2) - pow(z,2) == n ) :
                    B.append((n, x, y, z , p,  x+y+z, gcd(n, x+y+z) ))
                    break

    return len(B), B

def get_xyz_1(n):
    B=[]
    for p in range(1, n//2) :
        if gmpy2.is_square(4*p**2-n) :
            x1 = int(3*p+ sqrt(4*p**2-n))
            y1 , z1 = x1-p, x1-2*p
            C1 = (n, x1 , y1, z1, p,  x1+y1+z1, gcd(n, x1+y1+z1) )
            if C1 not in B :
                B.append( C1 )

            z2 = int(p - sqrt(4*p**2-n))
            if z2 > 0 :
                y2 , x2 = z2+p, z2+2*p
                C2 = (n, x2 , y2, z2, p,  x2+y2+z2, gcd(n, x2+y2+z2) )
                if C2 not in B :
                    B.append( C2 )

    return len(B), B

# (n, x, y, z , p,  x+y+z, gcd(n, x+y+z) ))
def get_xyz(n) :
    B=[]
    D = get_divisors(n)[1:]
    for y in D :
        y1 = y
        p = (n+y1**2)/(4*y1)
        if p % 1 == 0 and y1 - p > 0 :
            p = int(p)
            x1 , z1 = y1+p, y1-p
            B.append( (n, x1 , y1, z1, p,  x1+y1+z1, y1 )  )
    return len(B), B



print('\n--------------------------TESTS------------------------------')

print(list(pyprimes.primes_below(500)))


print('Test get_divisors :\t ' , get_divisors(1155))

t1  = time.time()

print('\nTest for the function same_diff : \n', same_diff(1155))
print('\nTest for the function same_diff : ', same_diff(27),'\n\n')
t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

##################
t1  = time.time()

print('\nTest for the function get_xyz_1 : \n', get_xyz_1(1155))
print('\nTest for the function get_xyz_1 : \n', get_xyz_1(2304))
print('\nTest for the function get_xyz_1 : \n', get_xyz_1(6400))
print('\nTest for the function get_xyz_1 : \n', get_xyz_1(8100))

print()

print('Test get_divisors :\t ' , get_divisors(1155))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


##################
t1  = time.time()

print('\nTest for the function get_xyz : \n', get_xyz(1155))
print('\nTest for the function get_xyz : \n', get_xyz(2304),'\n')
print('\nTest for the function get_xyz : \n', get_xyz(6400),'\n')
print('\nTest for the function get_xyz : \n', get_xyz(8100),'\n')



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------MY INITIAL VERIFICATION SOLUTION, VERY SLOW------------------------------')

t1  = time.time()

# cnt=0
# for n in range(2, 100):
#     s = same_diff(n)
#     if len(s) > 0 :
#         cnt+=1
#         print(str(cnt)+'.         ',s )
V=[]
def init_soln() :
    cnt=0
    for n in range(10**3, 10**4):
        if gmpy2.is_prime(n) != True :
            f  =get_factors(n)
            s = get_xyz_1(n)
            if s[0] == 10 :
                cnt+=1
                print(str(cnt)+'.         ',f ,'      ', s )
                V.append(n)
# init_soln()


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n==========My FIRST SOLUTION,  SLOW, Need To Improve Later ===============\n')
t1  = time.time()
W=[]
def first_soln_pb135() :
    cnt=0
    for n in range(10**3, 10**6):
        if gmpy2.is_prime(n) != True :
            f = get_factors(n)
            if len(f ) >  3:
                s = get_xyz(n)
                if s[0] == 10 :
                    cnt+=1
                    # print(str(cnt)+'.   ',n, '\t', f ,'      ', s )
                    # W.append(n)
        if n%10**4 == 0 :
            h = n//10**4
            sys.stdout.write("\r%d%%" %h )
            sys.stdout.flush()

    return print('\nAnswer :\t',cnt)

first_soln_pb135()              # Answer :	 4989


print('\n----------------------COMPARE the 2 RESULTS --------------------')
# print('V: ',sorted(V))
# print('W: ',sorted(W))











t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')

print('\n--------------------------SOLUTION 1,  FASTEST --------------------------')
t1  = time.time()
# ====== Tue, 19 Aug 2014, 00:17, SafassThin, France
# I arrived at the formula: y(4d-y) = n, ie y*x = n
# To make the loop run faster, I used the trick that y+x = y+(4d-y) = 4d is a multiple of 4
# Runs in about one second (700ms give or take)
#
# ps - I'm really glad that the site is fully functionnal again :-)
# My thanks to all people who have helped restore it (and obvioulsy, created it and make it run in the first place!)


def euler_135(limit=1000000):
    # y(4d-y) = n
    count = [0]*limit
    for x in range(1,limit//4):
        y = 1+x//3  # y>d, 4d-y>0
        while (x+y)%4: y += 1   # find first instance of y such that (x+y) is multiple of 4
        for n in range(x*y,limit,4*x):
                count[n] += 1
    return sum(1 for i in count if i == 10)
euler_135()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()

# ===== ue, 2 Apr 2013, 16:40, drodrigues, France

from math import *

solutions={}
maxi=10**6
for u in range(1,maxi):
    for v in range(1, int(maxi/u)):
        if (u+v)%4==0 and 3*v>u and (3*v-u)%4==0:
            if u*v in solutions.keys():solutions[int(u*v)]+=1
            else: solutions[int(u*v)]=1

prob135=len([i for i in solutions.keys() if solutions[i]==10])-1

print(prob135)



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3, ORIGINAL  --------------------------')
t1  = time.time()

# ========= Mon, 29 Apr 2013, 11:38, jbum, USA
#
# I solved this one with the help of a visual aid.  I originally wrote a brute force script, that calculated values of
# (z+2d)**2 - (z+d)**2 - z**2
# for steadily increasing d and z, but it was taking a long time.  I needed a way to eliminate values of z and d which were clearly out of contention.
# So I wrote a Processing script which visualizes this equation for increasing values of d, which produced this image of stacked parabola-like shapes.
#
# From the image, I could see that there was a steadily increasing ray on the right side.  I
# could see that when this ray hit a million, we would be finished with our calculations.
# Moreover, I could avoid calculations where the tops of the parabolas exceed the limit.
# I saw that after d=578, I only had to look at the descending right leg of the parabolas.
# So I added code to keep track of this steadily increasing leading edge, and skip the first chunk of z-values after d > 578.
#
# This reduced the calculations to under 5 seconds.

dct = {}
limit = 10**6
d = 1
mx = 0
rightRay = 0
leadingEdge = 1
while rightRay < limit:
  z = leadingEdge if d > 578 else 1
  lastSol = -1
  while True:
    sol =  (z+2*d)**2 - (z+d)**2 - z**2
    if sol - lastSol < 0 and lastSol >= limit and sol < limit:
      leadingEdge = z
    if sol <= 0:
      if lastSol > 0:
        rightRay = max(rightRay,lastSol-1);
      break
    if sol < limit:
      dct[sol] = dct.get(sol,0) + 1
    mx = max(mx,sol)
    lastSol = sol
    z += 1
  d += 1

tot = sum([1 for key,val in dct.items() if val == 10])

print ("tot",tot)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 5,   --------------------------')
t1  = time.time()

# =======  Sun, 26 Jan 2014, 05:22, lylepmills, USA
"""
Problem 135

x, y, z are consecutive terms of an arithmetic progression. how many values
of n < 10**6 satisfy the property that the equation x**2 - y**2 - z**2 = n
has exactly 10 solutions for (x, y, z)?

Proposed solution
Keep track of an array of 1 million elements, which will map n to the number of
combinations of x, y, z such that x**2 - y**2 - z**2 can sum to n.

In order to populate that array, we note the following.

(1) Since x, y, z are in an arithmetic progression, there exists some d such that
x = z + 2d and y = z + d.

(2)

0 < x**2 - y**2 - z**2 < 10**6
0 < (z + 2d)**2 - (z + d)**2 - z**2 < 10**6
0 < z**2 + 4dz + 4d**2 - z**2 - 2dz - d**2 - z**2 < 10**6
0 < 3d**2 + 2dz - z**2 < 10**6
0 < (3d - z)(d + z) < 10**6

(3)
Assuming z > 0 and d > 0, if d <= z/3, then (3d - z)(d + z) <= 0.
Therefore, d > z/3
"""

from array import array

NMAX = 10**6
ZMAX = NMAX
counts = array('I', [0]*NMAX)

for z in range(1, ZMAX + 1):
    d = (z//3) + 1
    n = int((3*d - z)*(d + z))
    while n < NMAX:
        counts[n] += 1
        d += 1
        n = (3*d - z)*(d + z)

print ("TEN COUNT:", counts.count(10))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 6, VERY FAST  --------------------------')
t1  = time.time()

======= Sat, 28 Jan 2012, 21:25, ving, USA
# Same as Narasimhan-S above, but a bit more concise (in Python):

# (x+d)^2 - x^2 - (x-d)^2 = n ==> x(4d-x) = n  ==>
# n = xy, where x+y = 0 (mod 4) and
# x > d ==> x > (x+y)/4 ==> y < 3x

N = 1000000

counts = N*[0]

for x in range(1, N):
    for y in range((-x)%4, 3*x, 4): # step 4
        n = x*y
        if n >= N:
            break
        counts[n] += 1

print(counts.count(10))  # Answer: 4989

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 7,   --------------------------')
t1  = time.time()
# ====== Fri, 1 Mar 2013, 12:24, tom.wheldon, England
# a(4d-a) = n with d < a < 4d generates all and only the solutions to the problem.
# Since this expression is a quadratic with maximum at a=2d I split the 'a' loop
# into two parts so I could break out when n got to a million.


D = {}

def updateD(n):
    if n in D:
        D[n] += 1
    else:
        D[n] = 1

for d in range(1, 250000):
    for a in range(d+1,2*d + 1):
        n = a*(4*d - a)
        if n > 999999:
            break
        updateD(n)
    for a in range(4*d, 2*d, -1):
        n = a*(4*d - a)
        if n > 999999:
            break
        updateD(n)
ans = 0
for n in D:
    if D[n] == 10:
        ans += 1
print(ans)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')







print('\n--------------------------SOLUTION 8, mbh038  --------------------------')
t1  = time.time()
# ====== Tue, 13 Dec 2016, 19:01, mbh038, England
# 60 s :( A complete rethink required for problem 136.
# I note that (x−5a)(x−a)=−n (, where x is the start value and a is the difference between terms.
# Hence (x−5a)(x−5a) and (x−a) must be matched pairs of divisors of -n, and must satisfy 2a<x<5a .

def p135(n,limit):
    t=time.clock()
    found=[]
    for i in range(1,limit):
        if ndivisors(i)>=16:
            found.append(i)
    print (len(found))
    nn=0
    for d in found:
        aset=set()
        ds=sorted(divisors(d))
        for i in range((len(ds)+1)//2):
            delta=(ds[i]+ds[-i-1])/4
            if delta>int(delta):
                continue
            a1=delta+ds[i]
            a2=delta+ds[-i-1]
            if a1>2*delta and a1<5*delta:
                aset.add((a1,delta))
            aset.add((a2,delta))
        if len(aset)==n:
            nn+=1
    print (nn,time.clock()-t)


def ndivisors(n):
    """find number of divisors of n from prime factor exponents"""
    i = 2
    factors = {}
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors[i]=factors.get(i,0)+1
    if n > 1:
        factors[n]=factors.get(n,0)+1
    divisors=1
    for k,v in factors.items():
        divisors*=(v+1)
    return divisors

def divisors(n):
    """returns the divisors of n"""
    #first get the prime factors
    i = 2
    fs = {}
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            fs[i]=fs.get(i,0)+1
    if n > 1:
        fs[n]=fs.get(n,0)+1

    ps=[k for k,v in fs.items()] #prime factors
    es=[v for k,v in fs.items()] #exponents

    divs=[]
    nfactors = len(ps)
    f = [0] * nfactors
    while True:
        p=1
        pfs=[x**y for (x,y) in zip(ps,f)]
        for i in range(len(ps)):
            p*=pfs[i]
        divs.append(p)
#could use this from np, but is several times slower for large numbers
#        yield ft.reduce(lambda x, y: x*y, [factors[x][0]**f[x] for x in range(nfactors)], 1)
        i = 0
        while True:
            f[i] += 1
            if f[i] <= es[i]:
                break
            f[i] = 0
            i += 1
            if i >= nfactors:
                return divs

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

