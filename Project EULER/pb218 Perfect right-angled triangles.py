#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @     Completed on Fri, 10 Mar 2017, 22:56
#The  Euler Project  https://projecteuler.net
'''
            Perfect right-angled triangles          -       Problem 218

Consider the right angled triangle with sides a=7, b=24 and c=25.
The area of this triangle is 84, which is divisible by the perfect numbers 6 and 28.
Moreover it is a primitive right angled triangle as gcd(a,b)=1 and gcd(b,c)=1.
Also c is a perfect square.

We will call a right angled triangle perfect if :
-it is a primitive right angled triangle
-its hypotenuse is a perfect square

We will call a right angled triangle super-perfect if :
-it is a perfect right angled triangle and
-its area is a multiple of the perfect numbers 6 and 28.

How many perfect right-angled triangles with c≤1016 exist that are not super-perfect?

'''
import time, zzz, gmpy2
from math import gcd
from itertools import count

def Pythagorean_primitive_triplets_gen():    # by Bogdan Trif @ 2017-01-21, 16:30     ### ( ͡° ͜ʖ ͡°)  FASTEST  ( ͡° ͜ʖ ͡°)  ###
    ''':Usage:      >>> pyt = Pythagorean_primitive_triplets_gen()
                        # >>> next(pyt)
                        # >>> for i in Pythagorean_primitive_triplets_gen(): print(i)
    :param i:   i
    :param j:   j
    :return:    a,b,c - primitive pythagorean triplet
    '''
    m = 1
    while True :
        for n in range(1, m):           ### range(1,m) as we need only a > 0 !!!!!!!!
            a = m**2-n**2
            b = 2*m*n
            c = m**2 + n**2
            if gcd(a,b) ==1 :           #   Assure that we generate ONLY primitive Pythagorean triplets
                # print(' m, n = \t',m, n,'            a,b,c =\t',sorted((a,b,c)))
                yield a,b,c
        m+=1


print('\n--------------------------TESTS------------------------------')
t1  = time.time()

def brute_force_testing() :
    PT = Pythagorean_primitive_triplets_gen()
    cnt=0
    for i in count(1) :
        a, b, c = next(PT)
        if gmpy2.is_square(c) :
            Area = a*b //2
            if Area %84 != 0  :
                if c <= 10**16 :
                    cnt+=1
                    print(str(cnt)+'.     ', a,b, c , '        Area :', Area , Area%84 )
        if i% 10** 6 == 0 : print(str(i)+'.     ', a,b, c ,'     ' ,len(str(c)), '        Area :', a*b//2 , (a*b//2)/6 , (a*b//2)/28, (a*b//2)/84   )

# brute_force_testing()

# Answer : 0

t2  = time.time()
print('\nCompleted in :', round((t2-t1)/60, 6), 'min\n\n')


# SOME OTHER REMARKS :
# ==== Sat, 22 Nov 2008, 06:13, balakrishnan_v, India
# It turns out that the number of perfect triangles with hypotenuse<=N is approximately sqrt(N)/(2*Pi)



print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()







# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,   --------------------------')
t1  = time.time()


# ====Sat, 22 Nov 2008, 12:28, karlo, Romania
#
# I got that Area=2*m*n*(m**2-n**2)*|m**4+n**4-6*m**2*n**2|, where (m,n)=1 and m>n.
# One can see right away that 4|Area and 3|Area.
# It was a big surprise to notice that 7|Area (the explanation for this is easy: if 7|m or 7|n we're done;
# else, since every square is 1,2, or 4 mod 7 we have the cases (m**2,n**2, m**4,n**4)=(1,2,1,4),
# (m**2,n**2, m**4,n**4)=(1,4,1,2), (m**2,n**2, m**4,n**4)=(2,4,4,2).
# Each one gives an Area divisible by 7.
#
# Well, I still thought I was doing something wrong and coded it, but got the same answer.
# It seems 0 was indeed the answer:))
# Btw, are there 23873247 such triangles?
#
# EDIT: I was wrong about the number of triangles.
# I forgot about the condition (m-n)%2=1. Now I get 15915492:D
#
# Here's my code to count them:
import gmpy2
import time

def answer218():
    t=time.time()
    count=0
    for m in range(2,10**4):
        for n in range(m%2+1,m,2):
            if m**2+n**2<=10**8 and gmpy2.gcd(m,n)==1:
                count+=1
    return print(count, time.time() -t)
answer218()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()

# ==== Thu, 15 Aug 2013, 06:06, Oren, USA
# A primitive triplet is: a = m^2-n^2, b=2mn, c=m^2+n^2 with gcd(m,n)=1.
#
# * Perfect triplet: c=m^2+n^2=r^2, so (m,n,r) is also a -primitive- triplet (since gcd(m,n)=1).
# Thus n=N^2-M^2, m=2MN and the area is a*b/2 = 2*M*N*(M^2-N^2)*((2*M*N)^2 - (M^2-N^2)^2).
#
# * Perfect, non super-perfect triplet: 2*M*N*(M^2-N^2)*((2*M*N)^2 - (M^2-N^2)^2) mod 84 != 0
# or M*N*(M^2-N^2)*((2*M*N)^2 - (M^2-N^2)^2) mod 42 != 0.
# Here it suffices to consider M and N to be remainders of the original M,N modulo 42.
# Therefore we only need to check 42 x 42 possibilities to verify that all of them are divisible by 42,
# and therefore no such triplet exists.
#
# The hard way and the easy way in code:

from math import gcd
import itertools

def num_perfect(L):
    '''Enumerate primitive triples whose hypotenuse is a perfect square r^2 (i.e., r is the hypotenuse
    the primitive triplet (m,n,r), where m,n parametrize the original triples. Look for those that
    don''t yield an area divisible by 84.'''
    s, L2 = 0, L ** 0.5
    for N in (N for N in range(1, int((L2 // 2) ** 0.5) + 1) if N % 4 != 0):
        N2 = N * N
        for M in (M for M in range(N + 1, int(L2 - N2) + 1, 2) if M % 4 != 0 and gcd(M, N) == 1):
            m, n = M * M - N2, 2 * M * N
            if ((m * m - n * n) * m * n % 84 != 0): s += 1
    return s

if __name__ == "__main__":
    # The easy way: if no combination of remainders s = m mod 42, t = n mod 42 yields an area/2 that's
    # not divisible by 42, no non-super-perfect triplet can exist. Note: the area is always even.
    p = 42
    if not [(s, t) for (s, t) in itertools.product(range(p), range(p)) if (s * t * (t * t - s * s) * ((2 * t * s) ** 2 - (t * t - s * s) ** 2)) % p]:
        print (0)
    # The hard way
    #print (num_perfect(10 ** 16))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')




print('\n--------------------------SOLUTION 3,   --------------------------')
t1  = time.time()

# ====Sat, 15 Mar 2014, 22:48, l.paranoid, France
# I used the Pythagorean triple twice. It takes 45s.

def problem218():
    S = 0
    N = int(1E12)
    nLim = int((N-1)**0.5)
    nLim2 = int((nLim-1) ** 0.5)
    for n in range(2, nLim2+1):
        mStart = 1 if (n%2 == 0) else 2
        mLim = min(n-1,int((nLim-n*n)**0.5))
        n2 = n*n
        for m in range(mStart,mLim+1,2):
            a = n2 - m*m
            b = 2*m*n
            if b < a:
                a,b = b,a
            if gcd(a,b) == 1:
                A = a*b*(b-a)*(a+b)
                if A % 6 != 0 or A % 28 != 0:
                    S+=1
    return print(S)

problem218()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 4,   --------------------------')
t1  = time.time()

# ==== Fri, 6 Feb 2015, 14:59, Nicolas Patrois, France
# Output=0. What the?
# OK, let’s dig it.
#
# Let u and v be integers.
# u²-v² 2uv u²+v² are the sides of the triangle.
# u²+v² is also a square so there exist a and b such that u=a²-b² v=2ab
# u²-v²=(a²-b²)²-4a²b²=a^4+b^4-8a²b²
# 2uv=4ab(a²-b²)
# Area=(u²-v²)*uv/2=(a²-b²-2ab)(a²-b²+2ab)4ab(a-b)(a+b)/2 multiple of 3, 4 and 7


def isqrt(n):
  x=n
  y=(x+1)/2
  while y<x:
    x=y
    y=(x+n/x)/2
  return x

def vecprod(M,V):
  nlM=len(M)
  return [sum([l[j]*V[j] for j in range(nlM)]) for l in M]

pmax=10**8
A=[[1,-2,2],[2,-1,2],[2,-2,3]]
B=[[1,2,2],[2,1,2],[2,2,3]]
C=[[-1,2,2],[-2,1,2],[-2,2,3]]
listmat=(A,B,C)

liste=[[3,4,5]]
compte=0

while liste:
  list2=[]
  for t in liste:
    for m in listmat:
      t2=sorted(vecprod(m,t))
      p=sum(t2)
      if p<pmax:
        list2.append(t2)
        if (t2[0]*t2[1])%42!=0 and isqrt(t2[2])**2==t2[2]:
          compte+=1
  liste=list(list2)

print(compte)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

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
#
# print('\n--------------------------SOLUTION 7,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 8,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 9,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 10,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 11,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 12,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

