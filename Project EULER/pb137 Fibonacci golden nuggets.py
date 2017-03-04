#!/usr/bin/python
# Solved by Bogdan Trif @       Completed on Wed, 1 Mar 2017, 14:17
#The  Euler Project  https://projecteuler.net
'''
Fibonacci golden nuggets        -           Problem 137

Consider the infinite polynomial series A_F(x) = x*F_1 + x**2*F_2 + x**3 *F_3 + ...,
where F_k is the k-th term in the Fibonacci sequence: 1, 1, 2, 3, 5, 8, ... ;
that is, F_k = F_(k−1) + F_(k−2),   F_1 = 1 and F_2 = 1.

For this problem we shall be interested in values of x for which A_F(x) is a positive integer.

Surprisingly A_F(1/2)	 = 	(1/2)*1 + (1/2)**2*1 + (1/2)**3*2 + (1/2)**4*3 + (1/2)**5*5 + ...
 	 = 	1/2 + 1/4 + 2/8 + 3/16 + 5/32 + ...
 	 = 	2

The corresponding values of x for the first five natural numbers are shown below.

                                                    x	                AF(x)
                                                √2−1	             1
                                                1/2	                 2
                                                (√13−2)/3	         3
                                                (√89−5)/8	         4
                                                (√34−3)/5	         5

We shall call A_F(x) a golden nugget if x is rational, because they become increasingly rarer;
for example, the 10th golden nugget is 74049690.

Find the 15th golden nugget.

'''
import time
from math import sqrt
from gmpy2 import mpq, fib
from decimal import *
getcontext().prec = 100

def Fibonacci_Binet(n_th) :
    ''':Description:    Returns the Fibonacci corresponding to the number  and uses the Binet Formula.
        http://mathworld.wolfram.com/BinetsFibonacciNumberFormula.html
        :param n_th: F_nth Fibonacci in sequence
        :return: str, first 9 digits of the Fibonacci number
    '''

    phi = Decimal((1+5**(1/2))/2)
    phi_ = Decimal((1- 5**(1/2))/2)
    # phi = (1+5**(1/2))/2
    # phi_ = (1-5**(1/2))/2
    # a = ( ( phi**n_th-phi_**n_th ) / ( phi - phi_) )%(10**9)
    a = str(((phi**n_th)-(phi_)**n_th)/( phi - (phi_)))[0:10].replace( '.' , '')
    # b =   ( (( 1 + np.sqrt(5))/2)**n_th - ((1 - np.sqrt(5))/2)**n_th  ) /np.sqrt(5)
    return str(a)

def Fibo_gen():
    #   Fibonacci GENERATOR , while loop
    a1, a2 = 0, 1
    while True:
        a = a1 + a2
        yield a
        a1, a2 = a2, a

def Fibonacci_kth( k ):
    return (1/5**(1/2) )*( ((1+ 5**(1/2)) /2 )**k - ((1- 5**(1/2))/2 )**k )


print('Fibonacci_kth : ',Fibonacci_kth (541))

print('Test for the Fibonacci_Binet : ', Fibonacci_Binet(50))
print('gmpy2.fib : \t\t\t\t\t\t\t' ,fib(50) )

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
    while (asc and c <= n) or (not asc and a > 0):
        k = int((n + b)/d)
        a, b, c, d = c, d, k*c - a, k*d - b
        F.append( mpq(a,b) )
        i+=1
    F.pop(-1)
    return F

print(farey_frac(8))



A_F = lambda x : x/(1-x-x**2)

print('A_F :\t', A_F(1/2))



print('\n--------------------------TESTS------------------------------')
t1  = time.time()

# epsilon = 1e-9
# FG = Fibo_gen()
# f1=1
# for i in range(1, 500):
#     f2 = next(FG)
#     f3 = f1**2+f2**2
#     x = (pow(f3, 1/2) - f1 )/f2
#     A = A_F(x)
#     if (A-round(A)) < epsilon :
#         print(str(i)+'.    ', f1, f2,'    ' ,f3,'       ' , round(A) )
#     f1 = f2


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n==========  My FIRST SOLUTION, SUPER FAST, 1 ms  ===============\n')
t1  = time.time()



def Fibonacci_golden_nuggets(k_th):
    FG = Fibo_gen()

    cnt = 1
    while cnt < k_th+1 :
        num, den = next(FG), next(FG)
        A = A_F(mpq(num,den)  )
        print(str(cnt)+ '.       x= ',num,'/', den , '        A(x) =', A,'    ' ,'       ' )
        cnt+=1
    return print('\nAnswer : \t  '+str(k_th)+'-th golden nugget is : \t', A)

Fibonacci_golden_nuggets(150)            #   Answer : 	  15-th golden nugget is : 	 1120149658760



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*10**6,6), 'μs\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,   --------------------------')
t1  = time.time()

# ==== Thu, 15 Dec 2016, 19:33, mbh038, England
# Less than 100μs in Python.
#
# I managed to deduce that A(x)=x/(1−x−x**2), which is easy to see if you write down the first few terms
# of A, Ax and Ax**2, and hence realised that for x to be rational, i.e. x=p/q where p and q are integers,
# we required that gcd(p,q)=1 and that both p and q be divisors of A.
# At this point I should have spotted that pq=A....but I did not, so I brute forced this just enough to get
# the first four valid pairs of pp and qq: (1,2), (3,5), (8,13), (21,34), which appear very quickly.
# From these, an obvious recursion relation emerges:
# p_n=p_(n−1)+q_(n−1)
# q_n=p_n(n−1)+2q_(n−1)

# Given p_15,q_15, I had to take care in combining them to find A in order to avoid rounding errors.

def p137(n):

    t=time.clock()
    p,q=gn(n)
    x=p/q
    print (x/(1-x-x**2)) #gives rounding errors
    print (p*q/(q**2-p*q-p**2)) #no rounding errors
    print(time.clock()-t)

def gn(n,memo={}):
    """returns p,q where p/q gives us the the nth Golden nugget"""
    if n==1:
        return 1,2
    try:
        return memo[n]
    except KeyError:
        p=gn(n-1,memo)[0]+gn(n-1,memo)[1]
        q=gn(n-1,memo)[0]+2*gn(n-1,memo)[1]
        memo[n]=(p,q)
        return p,q

p137(15)


# Having now read many of the posts here, and coming back here from Problem 138,
# let me just write this down while it is clear in my head: We can rapidly deduce that x/(1−x−x**2)=n,
# where n is a positive integer. Solving this for x with the requirement that x be rational leads us to
# 5n**2+2*n+1=k**2, where k is a positive integer.
# Solving this for n with the requirement that n be an integer leads us to the generalised Pell equation
# m**2−5*k**2=4. We solve this first to find the minimum positive solution (m0,k0)=(1,1),
# and then from this we can find all other solutions (mi,ki) by recursion.
# Integer values of n arise when m_i%5=1.
# My code to do all this takes about 3 ms.
# To solve the Pell equation  I made use of the very helpful document mentioned in a post above:
# Solving the generalized Pell equation x**2−D*y**2=N by John Robertson.
# http://www.jpr2718.org/pell.pdf
# I have implemented what he calls the  PQa algorithm.


def p137v2(limit,D=5,P0=1,Q0=2):

    a,A,B,G=PQa(D,P0,Q0,1)

    t,u=G[0],B[0] # minimum positive solution
    x,y=[2,t],[0,u]
    n=[]
    while len(n)<limit:
        x.append(t*x[-1]+x[-2])
        y.append(t*y[-1]+y[-2])
        if not (x[-1]-1)%5:
            n.append((x[-1]-1)//5)
    print(x[-1],n[-1] )

#this implements the PQa algorithm described by John D. Robertson
#http://www.jpr2718.org/pell.pdf
def PQa(D,P0,Q0,limit):

    a=[0,0]
    A=[0,1]
    B=[1,0]
    G=[-P0,Q0]

    P=[0,0,P0]
    Q=[0,0,Q0]

    i=0
    while i<=limit+1:
        if i>0:
            P.append(a[-1]*Q[-1]-P[-1])
            Q.append((D-P[-1]**2)/Q[-1])
        a.append(int((P[-1]+D**0.5)/Q[-1]))
        A.append(a[-1]*A[-1]+A[-2])
        B.append(a[-1]*B[-1]+B[-2])
        G.append(a[-1]*G[-1]+G[-2])
        i+=1

    return a[2:],A[2:],B[2:],G[2:]


p137v2(15)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()

# === Mon, 28 Nov 2016, 20:06, Khalid, Saudi Arabia
# Simple once you identify the pattern:

from fractions import Fraction

def g_fib():
    a,b = 1,1
    while True:
        yield a
        b = a+b
        yield b
        a = a+b

fib = g_fib()

def A(x):
    return x / (1 - (x + x * x))

for i in range(1, 16):
    print (i, A(Fraction(next(fib),  next(fib)  )))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,  THE SHORTEST SOLUTION --------------------------')
t1  = time.time()

# ==== Fri, 29 Apr 2016, 06:41, Avi Levy, USA
# By examining the generating function for the Fibonacci numbers, it is not hard to see that
# we're enumerating integers nn for which the equation x/(1−x−x**2) = n has a rational solution x.
# The discriminant of the resulting quadratic equation is therefore a perfect square;
# clearing denominators yields a Pell equation.
# The solutions to this Pell equation satisfy the recurrence a_n=7*a_(n−1)−a_(n−2)+1
# with initial conditions a_1=2, a_2=15. We return the 15th term in this sequence.

a = [2, 15]
for i in range(20):
  a += [7*a[-1]-a[-2]+1]
print(a[14])

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,   --------------------------')
t1  = time.time()

# ====    Thu, 1 Oct 2015, 22:54, anumoshsad, Bangladesh
# Generalized Pell's equation x^2-5y^2=-4 solves it in .111 secs.

def pe137():
	t= time.time()
	x,y=1,1 #minimal solution to x^2-5y^2=-4
	x0,y0=2,0
	c=0
	for k in range(100): #just guessing i would get the solution within 100 iteration
		temp= x
		x= temp + x0
		x0=temp
		temp=y
		y = temp+y0
		y0=temp
		if k%2 ==1 and x%5==1:
			c+=1
		if c==15:
			print((x-1)//5)
			print(time.time()-t, ' secs')
			return


pe137()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5,   --------------------------')
t1  = time.time()

# ==== Tue, 20 May 2014, 23:45, sgruenwald, USA
# That was easy. The code runs for 0.072 milliseconds!!! Here is my Python 2.7 code, including timer:

def fib(n,a=1,b=1):
	while n>1:
		n-=1
		a,b=a+b,a
	return b

def golden_nugget(m):
	return fib(2*m)*fib(2*m+1)

print (golden_nugget(15))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6,   --------------------------')
t1  = time.time()

# === Tue, 19 Aug 2014, 00:55, SafassThin, France
# Clearly I missed the fib(2*m)*fib(2*m+1) solution
# Ah well , here's my code anyway (using Pell's, again...)


def euler_137(target=15):
    # Using: Fn+2 = Fn+1 + Fn -> Fn = Fn+2 - Fn+1
    # --> A = ΣFn×x^n =  Σ(Fn+2-Fn+1)×x^n = ΣFn+2×x^n - ΣFn+1×x^n
    # --> x^2×A = ΣFn+2×x^(n+2) - x×ΣFn+1×x^(n+1)  = A-x-x×A --> A=x/(1-x-x^2)
    # (http://www.ilemaths.net/forum-sujet-432510.html)
    # A=x/(1-x-x^2) --> Ax^2+(1+A)x-A=0
    # Δ=(1+A)^2+4A^2 = 5A^2+2A+1
    # x = -((1+A)±√Δ)/2A --> √Δ must be an integer for the solutions to be radicals
    # Δ = m^2 = 5A^2+2A+1 --> 5m^2 = (5A+1)^2+4
    # Posing: x=5A+1 and y=m, the equation becomes: x^2 - 5y^2 = -4
    # This is Pell's equation - special case decribed in www.jpr2718.org/pell.pdf (page 10)
    # Minimal positive solution is (t,u)=(1,1)
    # Solutions are given every 2 iterations

    count,nugget,x,y = 0,0,1,1
    while count < target:
        x,y = (x+5*y)//2, (y+x)//2
        x,y = (x+5*y)//2, (y+x)//2
        # Check that x = 5A+1:
        if (x-1)%5 == 0:
            nugget = (x-1)//5
            count += 1
    return nugget

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 7,   --------------------------')
t1  = time.time()

# ==== Thu, 9 Jul 2015, 04:35, mmaximus, Portugal
# As most people, I summed the infinite series as powers of a matrix and arrived at x/(1−x−x**2) must be an integer n.
# Taking the discriminant of the quadratic to be a perfect square leads to 5*n**2+2*n+1=y**2.
# A substitution u−1=5*n reduces it to u**2−5*y**2=−4.
# Then, I just noticed that solutions satisfy the recurrence relation u_(n+2)=7*u_(n+1)−u_n,
# and after that the problem is trivial.

u_0 = 1
u_1 = 11

L = 15
for i in range(2,L+1):
    u = u_1
    u_1 = 7*u_1 - u_0
    u_0 = u

print((u_1-1)//5)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 8,   --------------------------')
t1  = time.time()

# ====Thu, 20 Jun 2013, 18:30, Oren, USA
# A(x)=x/(1-x-x^2) is the Fibonacci generating function.
# ==> x = -((a+1)+sqrt((a+1)^2+4*a^2))/2 should be rational
# ==> (a+1)^2+4*a^2 = perfect square = b^2
# ==> 5*a^2 + 2a - (b^2-1) = 0 ==> a = (-1 + sqrt(5*b^2-4))/10
# ==> 5*b^2 - 4 is a perfect square = c^2 ==> c^2 - 5*b^2 = -4
# ==> (c,b) is a solution of Pell's equation with D=5 and -4 RHS
# The recurrence relation for the general solution of this equation is
# c(0)=2, b(0)=2
# c(1), b(1) = fundamental solution = easily found to be (1,1) in this case by Brute force
# c(n+1) = c1*c(n) + c(n-1)
# b(n+1) = c1*b(n) + b(n-1)
# and n odd (n even yields solutions with D=5, +4 RHS)
# Thus b is the Fibonacci sequence - as recognized empirically in previous posts, but this is a more general solution.

from itertools import islice

def golden_nugget():
    n, c0, b0, c1, b1 = 2, 2, 0, 1, 1
    while True:
        b, c = b0 + b1, c0 + c1
        if n % 2 and c % 5 == 1: yield (c - 1) / 5
        n, c0, b0, c1, b1 = n + 1, c1, b1, c, b


print (next(islice(golden_nugget(), 14, 15)))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 9,   --------------------------')
t1  = time.time()

# ==== Sat, 2 Mar 2013, 10:10, tom.wheldon, England
# Derived the generating function (I remembered this being set as an exercise when I was doing my degree).
# Noticed that 1/2 was the ratio of successive terms of the Fibonacci sequence so tried plugging some more ratios
# into the generating function by hand and got a hit with 3/5.
# As an experiment I tried the program below and it produced the right answer - very little insight needed.

from fractions import Fraction

res = []

a = 1
b = 2
while len(res) < 15:
    t = Fraction(a,b)
    s = t/(1 - t - t*t)
    if s.denominator == 1 and s > 0:
        res.append(s)
    a, b = b, a+b

print(res[14])

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 10,   --------------------------')
t1  = time.time()

# ==== Sun, 29 Aug 2010, 17:18, Simon Liang, Vhina
# analysis inside

#Solving Pell's Equation

#The series is the generating function for the fibonacci sequence, which is
#f(x) = x / (1 - x - x^2)

#Solve f(x) = k for x in Maple, we have
#x = (sqrt(1 + 2*k + 5*k^2) - 1 - k) / (2 * k) or
#x = (sqrt(1 + 2*k + 5*k^2) + 1 + k) / (-2 * k)

#Since x needs to be rational, which means
#1 + 2*k + 5*k^2 has to be a perfect square

#1 + 2*k + 5*k^2 = r^2
#multiply both sides by 5
#5 + 10*k + 25*k^2 = 5*r^2
#(5*k + 1)^2 + 4 = 5*r^2
#(5*k + 1)^2 - 5*r^2 = -4

#So let
#A = 5*k + 1
#B = r
#We are essentially solving the Pell's Equation
#A^2 - 5*B^2 = -4
#where A % 5 = 1

#And as you can see, the fundamental solution should be A = 1, B = 1

#this time I will try to use a new method to calculate the equation

#http://en.wikipedia.org/wiki/Pell%27s_equation
#('additional solutions from the fundamental solution')

#http://d.hatena.ne.jp/inamori/20091231/p1

x1 = 1
y1 = 1

xk_1 = x1
yk_1 = y1

count = 0
while count < 15:
    xk = (x1 * xk_1 + 5 * y1 * yk_1) / 2
    yk = (x1 * yk_1 + y1 * xk_1) / 2
    if xk % 5 == 1:
        #print (xk - 1) / 5
        count += 1
    xk_1 = xk
    yk_1 = yk
print ((xk - 1) / 5)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 11,   --------------------------')
t1  = time.time()

# ==== Wed, 8 Sep 2010, 06:56, Eigen20, USA
# Pretty much instantaneous, rare for me so I would like to share.
# Big trick is that once you get to 5x^2 + 2x + 1 = 0 (derivation below code),
# to realize that the ratio of one solution over the last converges.
# It is always too large, but you can still pretty much jump exactly to the next soltion.
# Although I suppose not too surprising given the Fibonnaci nature of the problem.  Peace.

import math

count = 0
goods = [float(1)/4]
ratio = [9.]

while count < 15:
    afx = int(goods[-1]*ratio[-1])+2
    while True:
        afx -= 1
        root = (1+afx)**2+4*(afx**2)
##      #negb = (-1-afx)
##      #twoa = 2*afx
##      #print afx, root,negb,twoa
        if int(math.sqrt(root)) == math.sqrt(root):
            goods.append(afx)
            ratio.append(float(goods[-1])/goods[-2])
            print (goods[-1], ratio[-1])
            count += 1
            break

## x^-1 *Af(x) = F1 + xF2 + x^2 *F3 + ....
## x^-1 *Af(x) - F1 = xF2 + x^2 *F3 + x^3 *F4 + ....
## subtract from line 2 this line 4:
##          Af(x)   = xF1 + x^2 *F2 + x^3 *F3 + x^4 *F4 + ....
## to get line 6 and 7:
## (1/x)*(x^-1 * Af(x) - F1 - Af(x)) =
##           x(F2-F1) + x^2(F3-F2) + x^3(F4-F3) + ... =
##           0 +        x^2 * F1   + x^3 * F2 + x^4 * F3 + ....
## so :
## (x^-1 * Af(x) - F1 - Af(x)) = x * Af(x)

## then, rearranging:
## Af(x) - (F1+Af(x))*x = x^2 * Af(x)
## Af(x) * x^2  +  (F1+Af(x)) * x  - Af(x) = 0

## x = [(-F1-Af(x)) + sqrt((F1+Af(x))^2 + 4* Af(x)^2)] / (2*Af(x))
## entering F1 = 1 and multiplying out, the sqrt part becomes
## 5 * Af(x)^2  +  2 * Af(x)  +  1 = 0

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

