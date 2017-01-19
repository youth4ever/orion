#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Thu, 22 Dec 2016, 15:02
#The  Euler Project  https://projecteuler.net
'''
            Special isosceles triangles         -           Problem 138

Consider the isosceles triangle with base length, b = 16, and legs, L = 17.

By using the Pythagorean theorem it can be seen that the height of the triangle, h = √(172 − 82) = 15,
which is one less than the base length.

With b = 272 and L = 305, we get h = 273, which is one more than the base length,
and this is the second smallest isosceles triangle with the property that h = b ± 1.

Find ∑ L for the twelve smallest isosceles triangles for which h = b ± 1 and b, L are positive integers.

'''
import time
import math
from itertools import count

def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    from pyprimes import factorise
    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]

def Pythagorean_triplets_for_isoscel( i ):    # by Bogdan Trif
    ''':Usage:      >>> pyt = gen_Pythagorean_triplets(5,5)
                        # >>> next(pyt)
                        # >>> for i in gen_Pythagorean_triplets(8,8): print(i)
    :param i:   i
    :param j:   j
    :return:    a,b,c - pythagorean triplet
    '''
    for m in range(1, i+1):
        for n in range(m//5+1 , m//4+1):
        # for n in range(i//8 , i//4+1):

            a = m**2-n**2
            b = 2*m*n
            c = m**2 + n**2
            if a > 0:
                print(m,n,'    ',sorted((a,b,c)), end='  ')
                yield a,b,c


print('\n--------------------------TESTS------------------------------')

print('angle has : \t', math.acos(15/17)*180/math.pi, '  degrees ')
print('angle has : \t',math.acos(273/305)*180/math.pi,  '  degrees ')

print('\n---------------- Theory Test --------------')

cnt , SL = 0, 0

print(' Integer Test : ', pow ( ( (534252352/2)**2 + 534252353 **2  ), 1/2  ) , '\n' )

# for b in count(16, 16):
#     L1 = pow( ( pow(b+1, 2) + pow( b/2 , 2)), 1/2)
#     L2 = pow( ( pow(b-1, 2) + pow( b/2 , 2)), 1/2)
#
#     if abs(L1-round(L1)) < 1e-12   :
#         cnt+=1
#         SL += L1
#         print( str(cnt)+'.    b= ',b, get_factors(b) , ' ;     h=' ,b+1 , get_factors(b+1) , ' ;   L1=', '  ',L1, get_factors(L1)  ,'    case1')
#
#     if abs(L2-round(L2)) < 1e-12   :
#         SL += L2
#         cnt+=1
#         print( str(cnt)+'.    b= ',b, get_factors(b) , ' ;     h=' , b-1, get_factors(b-1) , ' ;   L2=',L2,'  ' ,get_factors(L2)  ,'    case2')
#     if cnt == 2 : break
#
# print('\nAnswer:',SL)



print('\n================  My FIRST ATTEMPT SOLUTION,   ===============\n')
t1  = time.time()

up_lim = 7*10**3
PT = Pythagorean_triplets_for_isoscel( up_lim )


# M=[1]
# for p in PT:
#     cnt+=1
#     print(str(cnt)+'.   ', p)
    # b, h, L = p[1], p[0], p[2]
    # if b*2 == h-1 or b*2 == h+1 :
    #     cnt+=1
    #     S += L
    #     M.append(L)
    #     print(str(cnt)+'.    ', p ,';      h=' ,h,'    ', get_factors(h) ,'    b=',2*b, '     ',get_factors(2*b),'     L=', L , '  ', get_factors(L), '   ', M[-1]/M[-2] )
    # if cnt ==6 : break
# print('\nAnswer :', S)



def special_Isosceles_Tiangles(how_many) :
    cnt, S = 0, 0
    m, n = 4, 1
    while True :
        for m in count(m, 1):
            h = m**2-n**2
            b = 2*m*n
            L = m**2 + n**2
            if b*2 == h+1 or b*2==h-1 :
                cnt+=1
                print('(m,n)=' ,m,n,'        (h, b, L)= ', (h, b ,L) )
                S+=L
                break
        n = m
        m = int(4.236*n)
        if cnt == how_many :
            return print('\nAnswer :', S)

special_Isosceles_Tiangles(12)





t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1, Pythagorean Triplets  --------------------------')
t1  = time.time()

# =====  Mon, 18 Aug 2014, 15:28, Larry, USA
# I missed the Fibonacci connection entirely. I'll call my an intelligent brute force.
# First realization was that the triangle could be looked as as two right triangles that had to be primitive Pythagorean triplets.
# I prefer formulation for generating the Pythagorean triplet give at http://www.math.rutgers.edu/~erowland/pythagoreantriples.html
#
# The first stop was to solve for r in terms of s on the assumption that the two sides of the triangle has a ration of 1:2 on length.
# This is close to the h = b +-1 in the problem. Not exact, but close.
# With this I simply had to iterate over s and look at a limited range around either 1.61*s or 0.30*s.
# The exact relationship is in the code below.
#
# Next realization was that the solutions were spread in a multiplicative sequence.
# That is s[i+1] is approximately 4.236 * s[i]. So, find a solution - jumb s by a factor a 4.236 and start searching again.
# From observation I notice that only one of the two equations ( r = 0.309*s) was providing triangles.
# So the code for the other was commented out.
#
# Run time for the search on my eight year old PC was about 1.8 seconds.

# http://www.math.rutgers.edu/~erowland/pythagoreantriples.html
import math

def p_triplet(r,s):
    a = s * (2 * r + s)
    b = 2 * r * (r + s)
    c = a + b - 2 * r * s
    triplet = [c,min(a,b),max(a,b)]
    return tuple(triplet)

count = 0
s = 2
trag = []
limit1 =(1 + math.sqrt(5))/2
limit2 =(math.sqrt(5) - 1)/4
while count < 12:
    #loop 1 on r --- r = 1.6180 * s
    limit = int(s * limit1)

    #loop 2 on r --- r = 0.3090 * s
    limit = int(s * limit2)
    low_r = limit - 50
    high_r = limit + 50
    for r in range(low_r,high_r):
        triangle = p_triplet(r,s)
        if abs(triangle[2] - 2 * triangle[1]) == 1:
            count += 1
            trag.append(triangle)
            print (count, r, s, triangle, 'Bottom')
            if count > 2:
                s  = int(s * 4.236) - 50
                break
    s += 1
trag.sort()
sum_hyp = 0
for i in range(12):
    sum_hyp += trag[i][0]

print (sum_hyp)



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2, Fibonacci  --------------------------')
t1  = time.time()

# ==== Sat, 3 Oct 2015, 19:33, supinf
# using a bit of math using fibonacci numbers, i came up with this python 3-liner:

a=lambda x:x+[x[-1]+x[-2]]
f=lambda n:a(f(n-1)) if n>1 else [0,1]
pe138=lambda k:sum(f(6*k+3)[9::6])/2
print (pe138(12))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3, Fibonacci  --------------------------')
t1  = time.time()

# ==== Wed, 9 Oct 2013, 00:59, BostonBear, USA
# I tried my best to brute force this thing, figuring if I program it in Java and I can loop my way through it with speed,
# alas, once I realized I needed to use Java's BigInteger class, I tossed that out the window.
# OEIS to the rescue again.  http://oeis.org/A007805
#
# I programmed it in Python and Java for kicks, since that equation made the code very simple.
# I realized that I could go the primitive triangles route, Pell, blah blah, but was feeling lazy.
# I saw that equation though and I thought, wow, that's clever, who knew that this class of triangles would be related to Fibonacci numbers.
# I find it rather mind blowing.
#
# Oddly, I coded it in Java and Python and Python was as fast or faster than Java, which is the first time I've seen this.
# I assumed Java would do it in .001 ms or something.


def a(n):
  if n == 0:
    return 1
  elif n == 1:
    return 17
  else:
    return 18*a(n-1)-a(n-2)
##############################
tot = 0

for i in range(1,13):
  L = a(i)
  tot += L
  print (L)


print ("\nTotal is :\t", tot)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,   --------------------------')
t1  = time.time()

# ====Fri, 24 Jan 2014, 14:47, India, kartikeyag
# Here is my extremely short and fast python code. It takes 0.013 s to run.
# I basically noticed a property connecting L.
# Li+1= Li*18 - li-1 where L0= 1
#
# I noticed the above by observing the terms that were part of the sequence of L.

def euler138(lim):
        prev,current,count,sum1=1,1,0,0
        while (count <lim):
                temp= current
                current=current*18 -prev
                prev=temp
                sum1 += current
                count +=1
                print (current)
        return sum1

print ('\n',euler138(12))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5, Using Fibonacci  --------------------------')
t1  = time.time()


# =====  Thu, 7 Mar 2013, 02:31, drome, Argentina
# Hi, I found first 4 values using brute force and the concepts of Euclid's formula.
# Well, I noticed that the integers m and n were Fibonacci's numbers,
# I used the sequence A000045 to confirm my guess and then I did the following code in Python:



# Los primeros numeros de Fibonacci
n = 3
m = 5
suma = 0

for c in range(1, 13):
   b = m**2 - n**2
   h = m*n
   L = (m**2 + n**2)/2

   print(c, ") b=", b, " h=", h, " L=", L, "  ====> n=", n, "m=", m)
   suma += L
   # Buscar el siguiente nro de fibonacci
   fn = n  + m
   n  = m  + fn
   m  = fn + n

print("Suma = ", suma)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6, Fibonacci  --------------------------')
t1  = time.time()

# ===== Fri, 5 Apr 2013, 00:52, drodrigues, France
# Like others, I used Fibonacci sequence with half '6*n+3 elements'.

def fibonacci(n):
    a,b=0,1
    for i in range (n-1):
        a,b=b,a+b
    return b

prob138=0
for n in range(1,13):
    prob138+=int(fibonacci(6*n+3)/2)

print(prob138)



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 7, Fibonacci  --------------------------')
t1  = time.time()

# ===== Tue, 23 Jan 2007, 18:02, carl, Wales
# I've got 'flu. I'm happy to say that I actually got it right, despite this slight obstacle (!)
# Python, pretty much instantaneous (timeit says around 0.0035 milliseconds!):
# I must admit, though, I did pretty much stumble across the patterns. The one I used for the solution was, when values of n and m (as in the famous formula for Pythagorean triplets) for which n^2 + m^2 == L^2 are tabulated, and certain pairs only are selected, they are written out following this pattern:
# n    -  m
# ---------
# 4    -  1      n is 4 here...
# 17   -  4      m is 4 here... n is 17 here
# 72   -  17                    m is 17 here... etc.
# 305  -  72
# 1292 -  305
# 5473 -  1292
#
# So for each iteration in my algo., m becomes n.
# The other fact, which took my script from exponential(?) to linear time was that in each of these cases,
# n=4*m + old_m (my starting values for n and m were 1 and 0 respectively).
# Yay! Maybe I'll actually check why now I've solved it.

n,m,s=1,0,0
for c in range(1,13):
    m,n=n,4*n+m
    s+=n**2+m**2
print (s)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

