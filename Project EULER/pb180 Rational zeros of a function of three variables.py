#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @     Completed on Tue, 28 Feb 2017, 23:51
#The  Euler Project  https://projecteuler.net
'''
Rational zeros of a function of three variables     -       Problem 180
For any integer n, consider the three functions

f1,n(x,y,z) = x**n+1 + y**n+1 − z**n+1
f2,n(x,y,z) = (x*y + y*z + z*x)*(x**n-1 + y**n-1 − z**n-1)
f3,n(x,y,z) = x*y*z*(x**n-2 + y**n-2 − z**n-2)

and their combination

fn(x,y,z) = f1,n(x,y,z) + f2,n(x,y,z) − f3,n(x,y,z)

We call (x,y,z) a golden triple of order k if x, y, and z are all rational numbers of the form a / b with
0 < a < b ≤ k and there is (at least) one integer n, so that fn(x,y,z) = 0.

Let s(x,y,z) = x + y + z.

Let t = u / v be the sum of all distinct s(x,y,z) for all golden triples (x,y,z) of order 35.

All the s(x,y,z) and t must be in reduced form.

Find u + v.

'''

import time
from gmpy2 import mpq
import gmpy2


f1 = lambda n, x, y, z :   x**(n+1) + y**(n+1) - z**(n+1)
f2 = lambda n, x, y, z :   (x*y + y*z + z*x ) * ( x**(n-1) + y**(n-1) - z**(n-1) )
f3 = lambda n, x, y, z :  ( x * y * z ) * ( x**(n-2) + y**(n-2) - z**(n-2) )
f = lambda n, x, y, z :     f1(n, x, y, z ) + f2(n, x, y, z ) - f3(n, x, y, z )
s = lambda x, y, z : x + y + z

######## The equivalent Function of f
f_equiv = lambda n, x, y, z :     ( x + y + z ) * ( x**(n) + y**(n) - z**(n) )

print( f1(21, 8/13, 5/12, 12/29))
print( f1(21, mpq( 8,13), mpq(5,12), mpq(12,29) ))
print( f2(21, 8/13, 5/12, 12/29))
print( f3(21, 8/13, 5/12, 12/29))

print( '\nTwo equivalent functions : \t',                       f(2, mpq(2/13), mpq(5/12), mpq(12/29)))
print( '2-nd of the two equivalent functions : \t',f_equiv(2, mpq(2/13), mpq(5/12), mpq(12/29) ) )

print( '\nTwo equivalent functions : \t',                       f(1, mpq(2/5), mpq(5/6), mpq(1/2)))
print( '2-nd of the two equivalent functions : \t',f_equiv(1, mpq(2/5), mpq(5/6), mpq(1/2) ) )



def farey( n, asc=True ):      ####  o(^_^)o  FASTEST  ( ͡° ͜ʖ ͡°)  ### !!! Best Farey Sequence
    ''':Description: Generates INCREASING FAREY SEQUENCE
        taken from http://pythonfiddle.com/farey-series-generator/
        Modified by Bogdan Trif @2017-02-28, 14:00     '''
    F=[]
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
        F.append((a,b))
        i+=1
    return F

print('\nthe Farey Sequence : ',farey(8))

print('\n----------------------------------')

def farey_frac( n, asc=True ):      ####  o(^_^)o  FASTEST  ( ͡° ͜ʖ ͡°)  ### !!! Best Farey Sequence
    ''':Description: Generates INCREASING FAREY SEQUENCE
        taken from http://pythonfiddle.com/farey-series-generator/
        Modified by Bogdan Trif @2017-02-28, 14:00     '''
    from gmpy2 import mpq
    F=[]
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
        F.append( mpq(a,b) )
        i+=1
    F.pop(-1)
    return F



print('\n---------------------- The First TEST, 45 min------------------------------')
t1  = time.time()

def first_brute_force(lim):
    F = farey_frac(lim)
    print(len(F), F[:100])

    S = set()

    cnt=0
    for n in [-2, -1, 1, 2 ] :
        print(n)
        for x in F :
            for y in F :
                for z in F :
                    g1 = f1(n, x , y , z )
                    g2 = f2(n, x , y , z )
                    g3 = f3(n, x , y , z )
                    g = g1 + g2 - g3

                    if g == 0  :
                        cnt+=1
                        ss = s(x,y,z)
                        if ss not in S :
                            S.add(ss)

                        print (str(cnt)+'.       n=', n,'    g1=',g1 ,'   g2=',g2, '   g3= ', g3, '         g=' ,g ,'        x , y, z = ' , x,y,z, '     s=' , ss )

    SUM = sum(S)
    print('\nLength of  distinct  s(x,y,z) :\t ', len(S) )
    u, v =  SUM.numerator, SUM.denominator

    return print('\nAnswer : \t', u+v ,'           t=' , SUM  )

# first_brute_force(lim = 15)

# Answer : 	 285196020571078987            t= 285123818794632187/72201776446800     Length of  distinct  s(x,y,z) :	  3677

t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')

print('\n=========== My FIRST SOLUTION, 12 min ,Simplified the function, Still SLOW  ===============\n')
t1  = time.time()


def second_smarter_brute_force(lim):
    F = farey_frac(lim)
    print('Length : ',len(F),'\n' ,F[:100])

    S = set()

    cnt=0
    for n in [-2, -1, 1, 2 ] :
        print(n)
        for x in range( len(F)) :
            for y in range(0,  len(F)) :
                for z in range(len(F)) :
                    g = f_equiv(n, F[x] , F[y] , F[z] )
                    if g == 0  :
                        cnt+=1
                        ss = s(F[x] ,F[y] ,F[z] )
                        if ss not in S :
                            S.add(ss)

                        # print (str(cnt)+'.       n=', n, '         g=' ,g ,'        x , y, z = ' , F[x],F[y],F[z], '     s=' , ss )

    SUM = sum(S)
    print('\nLength of  distinct  s(x,y,z) :\t ', len(S) )
    u, v =  SUM.numerator, SUM.denominator

    return print('\nAnswer : \t', u+v ,'           t=' , SUM  )

second_smarter_brute_force(lim= 15 )            # # Answer : 	 285196020571078987


t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')


print('\n==== My SECOND SOLUTION, 12 min ,FERMAT LAST THEOREM, not working properly  ===============\n')
t1  = time.time()

### Inspired from the Euler forum I arrived at the expression :
# f(x,y,z) = (x+y+z)(x**n+y**n-z**n)  and when equaling = 0 =>
# f(x,y,z) =  0  <=> (x+y+z)(x**n+y**n) = (x+y+z)(z**n)   =>
# x**n+y**n= z**n         which the FERMAT LAST THEOREM.
#
# Now all we have to do is to test the Farey sequence agains these values :

####  !!!!!! NOT WORKING PROPERLY !!!! Problems with cases with negative powers both on Fraction and mpq:
# it misses those cases as it wronlgy computes :

# n= -2 ; x , y =  mpq(3/8), mpq(1/2)
# z_n = x**(n)+y**(n)
# z = mpq((z_n.numerator)**(1/n) / mpq(z_n.denominator)**(1/n))
# z
# mpq(1125899906842624,3752999689475413)        instead of 10/3

def first_optimized_solution( lim ):
    F = farey_frac(lim)
    print(len(F), F[:100])
    S = set()
    # a, b = set([ i*i for i in F ]) , set([1/(i*i) for i in F ])
    # Z = set(F).union(a)
    # Z = Z.union(b)
    # print(Z)
    cnt=0
    for n in [-2, -1, 1, 2 ] :
    # for n in [ -1] :
        print(n)
        for x in F :
            for y in F :
                z_n = x**n + y**n
                # z = mpq( ( ( x.numerator/x.denominator)**n + ( y.numerator/y.denominator)**n ) ** mpq(1, n)  )
                z = mpq( ( ( x**n +  y**n ) ** mpq(1, n)  ))
                num, den = z.numerator, z.denominator
                # if x.numerator == 2 and x.denominator == 5 :
                #     print(x, y, z,'          ',n)
                # if num == 3 and den == 11  :
                #     print(str(n)+'.      x, y, z = ' ,x, y, z, '   ',z_n)

                if num < den <= lim and z < 1 :
                    cnt+=1
                    ss = mpq(x+y+z)
                    print (str(cnt)+'.       n=', n, '         x=', x ,'    y= ' , y  , '      z= ' , z  ,'       z_n = ' ,z_n , '     s=' , ss )
                    if ss not in S :
                        S.add(ss)


    SUM = sum(S)
    print('\nLength of  distinct  s(x,y,z) :\t ', len(S) )
    u, v =  SUM.numerator, SUM.denominator

    return print('\nAnswer : \t', u+v ,'           t=' , SUM  )

# first_optimized_solution(15)    # NOT YET WORKING

##### VERY VERY STRANGE ! Outside the loop works fine, INside is WRONG :
# 2/5 6/7 z= 562949953421312/2064149829211477           instead of z= 3/11


print('\n--------------')
n= -1    ;    x , y, =  2/5, 6/7   ;
# z = mpq((x**(n)+y**(n))**(mpq(1,n)))
z = mpq(( (x)**n+(y)**n)**(mpq(1,n)))

ss = mpq(x+y+z)

print(x, y, z,ss,'   ',n)


t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')




print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,  25 seconds  --------------------------')
t1  = time.time()

# ===Sun, 21 Aug 2016, 11:05, marijan, Croatia
def marijan(K):

    from fractions import Fraction

    s=set()
    ab={Fraction(a,b) for a in range(1,K) for b in range(a+1,K+1)}
    aabb={x*x:x for x in ab}
    for x in ab:
      for y in ab:
        if y<=x:
          z=x+y
          if z in ab:
            s.add(x+y+z)
          zz=x*x+y*y
          if zz in aabb:
            s.add(x+y+aabb[zz])
          z=1/(1/x+1/y)
          if z in ab:
            s.add(x+y+z)
          zz=1/(1/x/x+1/y/y)
          if zz in aabb:
            s.add(x+y+aabb[zz])
    t=sum(s)
    return print (t.numerator+t.denominator)

# marijan(35)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()

# ====Sun, 14 Aug 2011, 15:50, MrDrake, Australia
# Simplified into finding solutions to x^n+y^n=z^n, which is solvable only if n = -2, -1, 1 or 2.
# Naive set solution which takes 31s.


from fractions import Fraction as F

def g(x, y):
    z = x+y
    a, b = int(z.numerator**0.5), int(z.denominator**0.5)
    if a**2 == z.numerator and b**2 == z.denominator:
        return F(a, b)
    else:
        return F(-1)

def f(order):
    s, n = set(), set()

    for a in range(1, order):
        for b in range(a+1, order+1):
            n.add(F(a, b))

    for x in n:
        for y in n:
            z = x+y
            if z in n: s.add(x+y+z)
            z = g(x**2, y**2)
            if z in n: s.add(x+y+z)
            z = (x**-1+y**-1)**-1
            if z in n: s.add(x+y+z)
            z = g(x**-2, y**-2)**-1
            if z in n: s.add(x+y+z)

    t = sum(s)
    return t.denominator + t.numerator

# print (f(35))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,  25 sec --------------------------')
t1  = time.time()

# === Tue, 13 Mar 2012, 18:11, ving, USA
# A contrived problem... Same as everyone else:

from fractions import Fraction
from math import sqrt

def solution_3(K):

    fs = set()

    for d in range(2, K+1):
        for n in range(1, d):
            fs.add(Fraction(n, d))

    sums = set()
    for x in fs:
        for y in fs:
            xPlusY = x + y
            xy = x*y

            # 1. x + y = z or 1/x + 1/y = 1/z
            z = xPlusY
            if z in fs:
                sums.add(xPlusY + z)
            z = xy / z
            if z in fs:
                sums.add(xPlusY + z)

            # 2. x^2 + y^2 = z^2 or 1/x^2 + 1/y^2 = 1/z^2
            z2 = x*x + y*y
            n2, d2 = z2.numerator, z2.denominator
            n, d = round(sqrt(n2)), round(sqrt(d2))
            if n*n == n2 and d*d == d2:
                z = Fraction(n, d)
                if z in fs:
                    sums.add(xPlusY + z)
                z = xy / z
                if z in fs:
                    sums.add(xPlusY + z)

    f = sum(sums)
    return print(f.numerator + f.denominator) # Answer: 285196020571078987

# solution_3(35)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,  20 sec --------------------------')
t1  = time.time()


# ==== Mon, 15 Dec 2014, 12:01, ChopinPlover, Taiwan
# fn(x,y,z)=(x+y+z)(x**n+y**n−z**n) .  By Fermat's Last Theorem, n=−2,−1,1,2n=−2,−1,1,2.
#
# Next we generate all reduced rational numbers of order 35, say S={rk}.
#
# The rest is similar to 3SUM.
# We can pre-calculate Sn={r**n_k} where n=−2,−1,1,2 and build a hash table on Sn.
# Time complexity of getting golden triples is O(|S|**2).

import itertools
import fractions
import sys

class Problem():
    def __init__(self):
        self.n_solutions = [-2, -1, 1, 2]
        self.keys = None
        self.numbers = None

    def __init_keys(self, order):
        self.keys = set()
        for a, b in itertools.combinations(range(1, order + 1), 2):
            self.keys.add(fractions.Fraction(a, b))
        self.keys = sorted(list(self.keys))

    def __init_numbers(self, order):
        self.__init_keys(order)
        self.numbers = {}
        for n in self.n_solutions:
            self.numbers[n] = {}
            for key in self.keys:
                self.numbers[n][key**n] = key

    def solve(self):
        result = self.get(35)
        print("answer =>", result.numerator + result.denominator)
        print("exact rational number =>", result)

    def get(self, order):
        self.__init_numbers(order)
        final_result = set()
        for n in self.n_solutions:
            sub_result = self.__get_golden_triple(n)
            final_result |= sub_result
            print(n, "=>", len(sub_result), len(final_result))
        return sum(final_result)

    def __get_golden_triple(self, n):
        result = set()
        for x, y in itertools.combinations_with_replacement(self.numbers[n], 2):
            z = x + y
            if z in self.numbers[n]:
                result.add(self.numbers[n][x] + self.numbers[n][y] + self.numbers[n][z])
        return result

def main():
    problem = Problem()
    problem.solve()

# main()


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
