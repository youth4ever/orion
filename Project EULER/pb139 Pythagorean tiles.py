#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Sat, 21 Jan 2017, 21:34
#The  Euler Project  https://projecteuler.net
'''
                Pythagorean tiles       -       Problem 139

Let (a, b, c) represent the three sides of a right angle triangle with integral length sides.
It is possible to place four such triangles together to form a square with length c.

For example, (3, 4, 5) triangles can be placed together to form a 5 by 5 square with a 1 by 1 hole in the middle
and it can be seen that the 5 by 5 square can be tiled with twenty-five (25) 1 by 1 squares.


However, if (5, 12, 13) triangles were used then the hole would measure 7 by 7
and these could not be used to tile the 13 by 13 square.

Given that the perimeter of the right triangle is less than one-hundred million (10**8),
how many Pythagorean triangles would allow such a tiling to take place?

'''
import time, sys
from math import gcd, sqrt


def Pythagorean_Triples_gen(plim):          ### ( ͡° ͜ʖ ͡°)  ### Last Modif  by Bogdan Trif @ 2017-01-21, 20:45
    ''':Description: Generator for Pythagorean Triplets with their multiples until an up_limit, plim
        which is the Perimeter of the triangle.
        :Formulas used: :
    a^2 + b^2 = c^2     ;
        a = m^2 - n^2       ;
    b = 2mn     ;
        c = m^2 + n^2        ;
            k [ a + b + c = p = 2 * m * ( m + n ) ]     ;

    :Usage: >>> next(pythagorean_triple(30))
    Pythagorean triplets with this property that the greatest common divisor of
    any two of the numbers is 1 are called primitive Pythagorean triplets.
        :param: **plim** --> int,  limit of the perimeter of the triangle
    '''
    m = 1
    while 2*m**2 < plim:
        for n in range( 1 + m%2, m, 2):
            if gcd(m, n)==1:
                p = 2 * m * (m+n)
                a, b, c = m**2-n**2  ,    2*m*n ,     m**2+n**2
                for k in range(1, plim//p + 1):
                    yield (k*a, k*b, k*c)
        m+=1

itr=0
PT = Pythagorean_Triples_gen(100)
for i in PT:
    itr+=1
    print(str(itr)+'.      ',i)



print('\n--------------------------My INITIAL SOLUTION,  Slow,  4 min------------------------------')
t1  = time.time()

def first_solution(perim_lim):
    h = 0
    PT = Pythagorean_Triples_gen(perim_lim)
    cnt = 0
    for T in PT:
        d = abs( T[0]-T[1] )
        if  T[2]% d ==0 :
            cnt+=1
            # print(str(cnt)+'.          diff:\t', d,'        a,b,c = \t', T,'     ',sum(T))

        if ( cnt* 99) //(10057761)  > h-1 :        # Progress Bar #
            h += 1
            sys.stdout.write('\r' + str(h)+' % ['+'#'*h+str(' ')*(220-22*h//10) +']' )   # Font Segoe UI Semibold
        #     # sys.stdout.write('\r' + str(h)+' % ['+'#'*h+str(' ')*(100-h) +']' )         #  Calibri, Adjust the numbers, for the font of your configuration
        #     # sys.stdout.flush()

    return print('\nAnswer : \t', cnt)

# first_solution(10**8)                           #     Answer : 	 10057761


t2  = time.time()
print('\nCompleted in :', round((t2-t1), 4), 's\n\n')          # Completed in : 219.574 s


print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()







# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


# =========== GENERAL IDEAS : ===============
# Fri, 12 Aug 2011, 17:32, learnmath, India
# If a primitive triplet (a,b,c) with a<b<c is a solution, then all multiples of the triplet below 50M are solutions.
# So, for every primitive triplet, we have n/p solutions where n=50M and p=a+b+c.
# Next, the area of the smaller square is c*c-2*a*b=(b-a)**2 as c*c=a*a+b*b.
# This must divide c*c (larger square area) for the square to be tiled. Therefore, c*c % (b-a)*(b-a)==0

# === EUCLID FORMULA works instantly

print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')

print('\n--------------------------SOLUTION 00, INSTANT  EUCLID FORMULA  --------------------------')
t1  = time.time()


# ====Wed, 31 Dec 2008, 03:31, Jepso, Finland
# I used Euclid's formula for generating the triplets: a = 2mn, b = m2 - n2, c = m2 + n2.
# In order for a right-angle triangle to allow tiling, c % (b - a) == 0 must hold.
# If this holds for the primitive triangle, it's true for all (k*a, k*b, k*c).
#
# Then I noticed a pattern between such (m, n) pairs for which this holds.
# If we start from (m0, n0) = (2, 1), we can get all (m, n) pairs that generate correct triangles
# with the following recursive formula: (mi, ni) = (2mi-1 + ni-1, mi-1).
#
# The code below runs in 0.020 seconds.


p_max = 100 * 10**6
cnt = 0

m, n = 2, 1
while True:
    a = 2 * m * n
    b = m*m - n*n
    c = m*m + n*n
    p = a + b + c
    if p >= p_max:
        break
    cnt += p_max // p
    print (m, n, cnt)
    m, n = 2*m + n, m
print (cnt)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n--------------------------SOLUTION 0, VERY FAST, PATTERN Found  --------------------------')
t1  = time.time()

# =====Fri, 18 Jan 2013, 19:12, Steven White, USA

# Similar to other posts, I found the pattern of generating primitive triples where the next m = 2m+n.
# Just add floor(10^8 / c) for each of the 10 values of m to get the number of distinct triples.
# This runs very fast since there are only 10 iterations

Limit=10**8
Total=0
m=2
n=1
while(m**2-n**2)+(2*m*n)+(m**2+n**2) < Limit:
    Total += Limit//((m**2-n**2)+(2*m*n)+(m**2+n**2))
    n,m = m,2*m+n

print(Total)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 1, 200 ms, VERY FAST  --------------------------')
t1  = time.time()

# ===== Thu, 1 Dec 2016, 14:49, Khalid, Saudi Arabia
#
# I used my code for problem 75 with some optimizations, and I checked that for a triplet (a, b, c)
# b - a should divide c.
# If a triplet should succeed, I would calculate its children triplets (using the generating matrices)
# and its multiples (MAX / length), otherwise, I'd just keep going. The code runs in 0.1 seconds.

import numpy as np
from collections import deque

A = [[-1, 2, 2],
     [-2, 1, 2],
     [-2, 2, 3]]

B = [[1, 2, 2],
     [2, 1, 2],
     [2, 2, 3]]

C = [[1, -2, 2],
     [2, -1, 2],
     [2, -2, 3]]

MAX = 100000000
total = 0
q = deque([(np.array([3, 4, 5]), 12)])

def calc_children(t, lt):
    global total
    if t[2] % (t[0] - t[1]) == 0:
        total += MAX // lt
    else:
        return
    children = [np.dot(A, t), np.dot(B, t), np.dot(C, t)]
    for c in children:
        lc = c[0] + c[1] + c[2]
        if lc > MAX:
            continue
        q.append((c, lc))

while True:
    try:
        c = q.pop()
        calc_children(c[0], c[1])
    except IndexError:
        break

print(total)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,  1 ms, PELL Equation using PQa algorithm of John D. Robertson  --------------------------')
t1  = time.time()

# ==== Sat, 17 Dec 2016, 18:47, mbh038, England
# All done in <100 μs. Another generalised Pell equation.
# This time, the requirement that b−ab−a divides cc, where a<b<c are the three sides of a candidate
# right-angled triangle leads us to the Diophantine equation x**2−2y**2=−1, where x=a+b and y=c.
# I solved this using the same PQa algorithm I have used for the last two problems,
# from Robertson, but this time with P0=0 and Q0=1 and now coded as a generator.
# Each valid pair of x and y gives us a valid fundamental triangle,
# and for each of the ten of these that exist there are as many similar multiples as the perimeter limit allows.


def mbh038(limit):
    t=time.clock()
    vals=PQa2(2,0,1)
    next(vals)
    triangles=0
    perimeter=0
    while 1:
        next(vals)
        a, A, n, k = next(vals)
        perimeter=n+k
        if perimeter<limit:
            triangles+=limit//perimeter
            continue
        break
    print(triangles)
    print(time.clock()-t)


def PQa2(D,P0,Q0):
    '''
        #generator version
        #this implements the PQa algorithm of John D. Robertson
        #http://www.jpr2718.org/pell.pdf
    '''
    A2,A1=0,1
    B2,B1=1,0
    G2,G1=-P0,Q0

    P1=P0
    Q1=Q0

    a0=int((P1+D**0.5)/Q1)
    A0=a0*A1+A2
    B0=a0*B1+B2
    G0=a0*G1+G2

    yield a0,A0,B0,G0

    while 1:

        A1,A2=A0,A1
        B1,B2=B0,B1
        G1,G2=G0,G1
        a1=a0

        P1=P0
        Q1=Q0

        P0=a1*Q1-P1
        Q0=(D-P0**2)/Q1
        a0=int((P0+D**0.5)/Q0)
        A0=a0*A1+A2
        B0=a0*B1+B2
        G0=a0*G1+G2

        yield a0,A0,B0,G0

mbh038(10**8)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3, PELL Equation  --------------------------')
t1  = time.time()

# ====Mon, 19 Dec 2016, 22:57, night.train, USA
# Python - 0.15 ms
#
# Proved that solutions can only be multiples of Pythagorean triples where abs(a-b) = 1.
#
# From there, used Pell solution recurrence to find all the primitive solutions and
# counted how many scaled triangles fit within the perimeter limit.
# Did this for both positive and negative Pell's equation, as both are relevant.

def Pell_recurrence (init_x, init_y, max_perimeter):
    soln_count = 0

    perimeter = calc_triangle_perimeter (init_x, init_y)

    # every linear multiple of this triangle is a solution
    soln_count += max_perimeter // perimeter

    past_x, past_y = init_x, init_y

    # Pell solution recurrence for positive/negative Pell equation, d = 2
    while perimeter < max_perimeter:
        x = 3 * past_x + 4 * past_y
        y = 2 * past_x + 3 * past_y
        perimeter = calc_triangle_perimeter (x, y)
        soln_count += max_perimeter // perimeter

        past_x, past_y = x,y

    return soln_count

# Given Pell solutions, translate this into n,m (Pythagorean triple
# generators) to yield the sides of the triangle
def calc_triangle_perimeter (x, y):

    m,n = y, x + y

    a = n**2 - m ** 2
    b = 2 * m * n
    c = n ** 2 + m ** 2
    return (a + b + c)

def main():
    max_perimeter = 100 * (10 ** 6)
    total_solns = 0

    init_x, init_y = 3, 2 # initial solution to Pell's equation, d = 2
    total_solns += Pell_recurrence (init_x, init_y, max_perimeter)

    init_x, init_y = 1, 1 # initial solution to negative Pell's equation, d = 2
    total_solns += Pell_recurrence (init_x, init_y, max_perimeter)

    print (total_solns)


main()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,  Euclid Formula --------------------------')
t1  = time.time()

# ==== Mon, 10 Nov 2014, 08:25, grovert, USA
# Found recurrence in (a,b) using Euclid's formula: (x,y,z) = (a*a-b*b, 2*a*b, b*b+b*b)

a, b = 2,1
N = 0
while True:
    perim = 2*a*a + 2*a*b
    if perim >= 100000000: break
    N = N +  100000000 // perim
    a,b = 2*a+b, a
print (N)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5,   --------------------------')
t1  = time.time()

from math import *
import time
t0=time.time()

def pell(x,y):
   x,y=3*x+4*y,3*y+2*x
   return x,y

maxi = 10**8

x = 7
y = 5

somme = 0

while x+y<maxi:
   somme += maxi//(x+y)
   x,y=pell(x,y)

prob139=int(somme)

print(prob139)
print(time.time()-t0)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6,  20 sec --------------------------')
t1  = time.time()

# ==== Thu, 2 Sep 2010, 20:29, jsudhir, India
# Generated all primitive pythagorean triplets (a,b,c).
# Checked for c%(a-b)==0 and added n1/p1 for all p1=a+b+c till n1=10^8
# Straightforward code. Runs in 15s in Python

def p139(n1=10**8) :
	ilm=int((n1/2)**0.5)
	cn=0
	for i1 in range(1,ilm+1) :
		isq = i1*i1
		for j1 in range(1,i1) :
			jsq = j1*j1
			a1, b1, c1 = isq-jsq, 2*i1*j1, isq+jsq
			p1 = a1+b1+c1
			if p1 >= n1 : break
			if a1<b1 : a1, b1=b1, a1
			if not c1%(a1-b1) and gcd(a1,b1)==1 :
				cn+=n1/p1
	return cn

# p139(n1=10**8)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 7,  INSTANT --------------------------')
t1  = time.time()

# ==== Wed, 26 Jan 2011, 22:34, WillemW, Netherlands
# I do not believe my eyes.
# Of the 73 programs and program ideas posted in this thread 51 are incorrect and 20 are correct (2 I couldn't make out).
# While most programs check for the perimeter to be less than the limit (10^8) in the calculation of the number of "derived" triangles,
# limit divided by perimeter is used, which should have been: (limit - 1) divided by perimeter!
# If one takes 120 as limit, the difference will show up.
#
# Looking at all these programs I am most impressed by hyperdex solution, in spite of his (then) limited knowledge of python.
# The corrected version could be:


def euler_139(limit):
	# progam based on source by hyperdex
 	x, y, sum = 7, 5, 0
 	while x + y < limit:
 		sum += (limit - 1) // (x + y)
 		x, y = 3 * x + 4 * y, 3 * y + 2 * x
 	return sum


print (euler_139( 10**8 ))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 8, INSTANT  EUCLID FORMULA  --------------------------')
t1  = time.time()


# ====Wed, 31 Dec 2008, 03:31, Jepso, Finland
# I used Euclid's formula for generating the triplets: a = 2mn, b = m2 - n2, c = m2 + n2.
# In order for a right-angle triangle to allow tiling, c % (b - a) == 0 must hold.
# If this holds for the primitive triangle, it's true for all (k*a, k*b, k*c).
#
# Then I noticed a pattern between such (m, n) pairs for which this holds.
# If we start from (m0, n0) = (2, 1), we can get all (m, n) pairs that generate correct triangles
# with the following recursive formula: (mi, ni) = (2mi-1 + ni-1, mi-1).
#
# The code below runs in 0.020 seconds.


p_max = 100 * 10**6
cnt = 0

m, n = 2, 1
while True:
    a = 2 * m * n
    b = m*m - n*n
    c = m*m + n*n
    p = a + b + c
    if p >= p_max:
        break
    cnt += p_max // p
    print (m, n, cnt)
    m, n = 2*m + n, m
print (cnt)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 9, 29 sec  --------------------------')
t1  = time.time()

# ==== Fri, 28 Nov 2014, 06:47, raulbc777, Paraguay
# The idea is to generate all the primitive pythagorean triplets first with:
# a=m**2−n**2
# b=2*m*n
# c=m**2+n**2
# with the special condition that (b−a)(b−a) divides c
# The difference b−a>=0
# So, n>=m(sqrt(2)−1)
# This condition will shorten the range of values of n for a faster search.
# Making brute force search with m<10000m<10000 is enough and we obtain the following primitive triplets
# with a perimeter bellow than 100.000.000:
# Each primitive generates a number of triangles, ni
# ni=100.000.000/(ap+bp+cp)ni=100.000.000/(ap+bp+cp)
#
# ap,bp,cp, the sides for the primitives.
# Obtaining each nini for each primitive and adding them up, we obtain the result.
# The code I used gives the result in less than 20 secs.

def slow_solution():
    from math import gcd

    pMax = pow(10, 8)
    countTriang = []
    def isPythSq(m, n):
        global pMax
        global countTriang
        a = m**2 - n**2
        b = 2*m*n
        c = m**2 + n**2
        if c %(a - b) == 0:
            primitCount = int(pMax/float(a + b + c))
            countTriang.append(primitCount)
            print( (a, b, c), sum((a, b, c)))
            if countTriang[-1] == 1:
                print ("Number of Triangles ", sum(countTriang))
                return 0

        else:
            return 1
    print ("Primitive Triplets and Perimeter")

    limit = 10000
    flag = False
    for m in range(2, limit + 1):
        for n in range(int(m*(2**0.5 - 1)), m):
            if gcd(m, n) == 1 and (m - n) % 2 != 0:
                if isPythSq(m, n) == 0:
                    flag = True

                    break

        if flag == True:
            break

# slow_solution()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

