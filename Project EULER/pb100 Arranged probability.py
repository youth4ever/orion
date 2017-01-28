#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Fri, 18 Nov 2016, 13:12
#The  Euler Project  https://projecteuler.net
'''
                                                       Arranged probability     -       Problem 100
If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs,
and two discs were taken at random, it can be seen that the probability of taking two blue discs,
P(BB) = (15/21)×(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random,
is a box containing eighty-five blue discs and thirty-five red discs.
P(BB) = (85/120)×(84/119) = 1/2.

By finding the first arrangement to contain over 10**12 = 1,000,000,000,000 discs in total,
determine the number of blue discs that the box would contain.
'''
import time
from math import gcd, sqrt, floor
from fractions import Fraction
from itertools import cycle


class CONTINUED_FRACTIONS(object):
    ''' Made by Bogdan Trif @ 2016-11-18.

    :NOTE: CUSTOMIZED Here for Problem 100 - Arranged Probabilities

            It needs the factions.Fraction, itertools.cycle and math.floor        '''
    # from math import floor
    # from fractions import Fraction
    # from itertools import cycle
    def continued_fractions(self ,number):        # FASTEST ALGORITHM to compute coefficients
        ''':Description: THE FASTEST ALGORITHM
            After if find the proper period of the continued fractions it returns the result.
        :param number:  is the number for which the square root continued fraction coefficients will be computed
        :return: list containing the periodic continued fractions terms    '''
        result = []
        fraction = ()
        m = 0
        d = 1
        self.a0 = number ** 0.5     # self.a0 - guaranties that I can access a0 to the second method (function)
        if self.a0.is_integer():
            return [self.a0, None]
        self.a0 = floor(self.a0)
        a = self.a0
        # result.append(a)
        while True:
            m = d * a - m
            d = (number - m ** 2) / d
            a = floor((self.a0 + m) / d)
            fraction += (a,)
            if a == 2 * self.a0 :
                break
        # result.append(fraction)
        return fraction

    def rationalize(self, number, nth) :
        ''' :Description:   Adapted for the class CONTINUED_FRACTIONS. It cycles the periodic coefficients with number of terms specified
        :param:     :number:  int,  number for which square root rationals will be computed
                        :nth:     int, the number of terms to be computed: n-th representation
        :Example:   *>>>CONTINUED_FRACTIONS().rationalize(2, 8)*    will yield :

            *1/2,   2/5,   5/12,   12/29,   29/70,   70/169,   169/408,   577/408*
        '''
        COEFF=[]
        C = cycle(self.continued_fractions (number))
        cfr = [ next(C) for i in range(nth) ]
        # print(cfr)
        frac = Fraction(1, cfr[-1])
        n,d = int(str(frac).split('/')[0]), int(str(frac).split('/')[1])
        COEFF.append((n,d))
        # print(frac , end='  ') #,'  <-Start')
        for i in reversed(range(1, len(cfr)-1)) :
            frac = 1 / (frac + cfr[i])
            # print(frac, end= '  ')
            n,d = int(str(frac).split('/')[0]), int(str(frac).split('/')[1])
            COEFF.append((n,d))
        #print(frac+self.a0 ) #, '  <-- Final Answer')
        return COEFF        # frac+self.a0

def calc_probability_blue(b, r):
    return (b/(b+r) * (b-1)/(b+r-1))

print('\n--------------------------TESTS------------------------------')



print(calc_probability_blue(85,35),'\n')

# epsilon=1e-12
# for r in range(6, 10000):
#     for b in range(int(r*2.4), int(r*2.5)+1 ):
#         p = calc_probability_blue(b,r)
#         if abs(p-(1/2)) <  epsilon :
#             g = gcd(b,r)
#             print(p, '    r=',r ,'   b=' ,b, b+r, ' ', b-1, b+r-1, '    gcd=',g , (b+r)/g,  (b/g)*(b+r)/g )

print('\n\nCONTINUED_FRACTIONS().rationalize(2, 8)  Test CLASS : \n', CONTINUED_FRACTIONS().rationalize(2, 8))


            # 0.5     r= 6    b= 15 21   14 20     gcd= 3 7.0 35.0
            # 0.5     r= 35    b= 85 120   84 119     gcd= 5 24.0 408.0
            # 0.5     r= 204    b= 493 697   492 696     gcd= 17 41.0 1189.0
            # 0.5    r= 1189    b= 2871 4060   2870 4059     gcd= 29 140.0 13860.0
            # 0.5     r= 6930    b= 16731 23661   16730 23660     gcd= 99 239.0 40391.0
#
# Raspuns : partial fractions :
# example
# r : 35-6=29 , b : 85-15=70 => 29/70
# r : 204-35=169 , b : 493-85=408 => 169/408
# r : 1189-204=985 , b : 2871-493=2378 => 985/2378
#
# OLAAAAAAAAAAAAAAAAAAAAAAAA ! PARTIAL FRACTIONS !!!!!!!!!!!!

print('\n-------------------------- END TESTS------------------------------')

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

def blue_da_ba_di_discs_eiffel65(limit) :
    COEFFs = CONTINUED_FRACTIONS().rationalize(2, 35)
    COEFFs = COEFFs[4::2]
    print('\n',COEFFs,'\n')
    r , b = 6, 15       # r -red,  b - blue
    d = r+b             # d - total discs
    i=0
    P =  lambda b,r : (b /(b+r) * (b-1)/(b+r-1))
    p = P(b,r)
    print( str(i+1)+'.   r=', r ,'   b=' ,b ,   d, '  ', b-1, d-1, '      prob=', p  )
    while d < 1e12 :
        r += COEFFs[i][0]
        b += COEFFs[i][1]
        d = r+b
        p = P(b,r)
        print( str(i+2)+'.   r=', r ,'   b=' ,b ,   d, '  ', b-1, d-1, '      prob=', p, '  ' ,len(str(d))  )
        i+=1
    return print('\n\nBLUE DISCS within limit ', limit,' are : ', b )

blue_da_ba_di_discs_eiffel65(1e12)



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,  kfukuda2   --------------------------')
t1  = time.time()

import numpy as np
b = 15
r = 6
prev_r = 1
sum = 0
while sum < 10**12:
    temp = 6*r - prev_r
    prev_r = r
    r = temp
    b = int(np.max(np.roots([-1, 2*r+1, -r+r**2])))
    sum = r+b
print (b)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,  JMoc1978, USA --------------------------')
t1  = time.time()
# So, not as sophisticated as the Diophantine equation, but my reasoning got me in the door to learn more.
# This has been one of my favorite problems thus far.
# I started with the assumption that the ratio of blue discs (b) to the total (n) was b ≈ n/√2
#
# Next, the number of blue discs progressed such that the next value for blue discs was
# b_(n+1) ⪅ [ b_n / ( b_(n−1) / b_n ) ]
# This always underestimated b and n, therefore, one could loop up to the next values that fit the criteria.

from time import clock
import math

def Prob(TotalDiscs):

    Total = 3     #The denominator
    Ratio = 1     #The probability that is being tested
    LastBlue = 1  #The number of blue discs that last met the criteria

    while Total:

        Blue = (math.ceil(Total/math.sqrt(2)))
        Ratio = (Blue*(Blue-1))/(Total*(Total-1))

        if Ratio == 0.5:

            Total = math.ceil((Blue/(LastBlue/Blue))*math.sqrt(2))
            LastBlue = Blue

            if Blue*math.sqrt(2) > TotalDiscs:
                break

        else:

            Total += 1

    return LastBlue

print(Prob(10**12))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3, WalkerTesla, USA  --------------------------')
t1  = time.time()
# Pell Equations really kill this question. Through repeated use of the Quadratic Formula, we find that if t = total and b = blue,
# and if [a,c] is a solution to a^2-2c^2 = -1, then t = (a+1)/2 and b = (c+1)/2.
# From here we can recursively generate the solutions to this Pell Equation to quickly solve the problem.
# Here is a Python script which does this:

import math
pell_pair = [41,29]
def the_recurse():
    a = pell_pair[0]
    b = pell_pair[1]
    pell_pair[0] = 3*a+4*b
    pell_pair[1] = 2*a+3*b

while pell_pair[0]<2*10**12-1:
    the_recurse()

print ( (pell_pair[1]+1)/2 )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4, Alex-82w4, USA  --------------------------')
t1  = time.time()
# The solution based on a Pell equation.
# P(BB)=x(x−1) / y(y−1)=1/2(1)

import math

def MainProc1() :
    a = 3 + 2 * math.sqrt(2)
    b = 3 - 2 * math.sqrt(2)

    for i in range (2, 20, 1) :
        k_s = math.ceil(math.ceil((math.pow(a, i) + math.pow(b, i)))/2)
        z = math.ceil(math.sqrt(math.ceil((math.pow(k_s, 2) - 1))/8))
        x = z + math.ceil((k_s + 1)/2)
        y = x + z

        if y > math.pow(10, 12) :
            print ("i       y           x               z")
            print (i, y, x, z)
            break

#i       y                x               z
#16 1070379110497 756872327473 313506783024
MainProc1()



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5, Sandamnit, USA  --------------------------')
t1  = time.time()

# Can derive Pell's equation pretty easily from the information given.
# The "smallest" solution is (3,1) where 3^2 - 8*1^2 = 1, corresponding to the solution b=3 and r=1.
# Repeatedly composing this solution using Brahmagupta's identity, we obtain all "larger" solutions (n,r),
# putting b = (1+2r+n)/2.

x,y = 3,1
while True:
   x,y = 3*x+8*y, 3*y+x
   b = (1+2*y+x)//2
   if b+y > 1000000000000: break
print(b)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6, DFHD, England  --------------------------')
t1  = time.time()

# Nice problem to complete the first 100!
# I thought Pell must be involved but I couldn't figure out how.
# Also realised sqrt(2) as a fraction was relevant but I couldn't find a way to use it.
#
# So I tried brute force, but soon realised that was getting nowhere fast, even after much work improving the brute force technique.
# So another day later, after staring at the low solutions that I'd already found by brute force,
# I finally saw patterns in the number of red and blue discs for each solution:

# r[i] = 6*r[i-1] - r[i-2]
# b[i] = 6*b[i-1] - b[i-2] - 2
#
# Then it was easy to code a solution, as long as I put in correct starting conditions


r = [0, 1]
b = [1, 3]

d = r[-1] + b[-1]

while d < 10**12:
    r.append(6 * r[-1] - r[-2])
    b.append(6 * b[-1] - b[-2] - 2)
    d = r[-1] + b[-1]
    print(r[-1], b[-1], d)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 7, aolea, Spain  --------------------------')
t1  = time.time()
#
# From b*(b-1)/t*(t-1) --> 2*b^2-2*b-t^2+t=0
#
# Using:
# 8*b = x +4
# 8*t = y + 4
#
# We have:
#
# 2*x^2 - y^2 = 16
#
# Using:
# x = 4*u + 4*v
# y 4*u + 8*v
#
# We have:
#
# u^2 - 2*v^2 = 1
#
# Equation with least solution of (3,2) and a recurrence of:
#
# xk+1 = x1*xk + 2*y1*yk
# yk+1 = x1*yk + y1*xk


t = 0
x1 = 3
y1 = 2
n = 2

x = x1
y = y1

while t < 10**12:
    xm = x
    x = x1 * x + n * y1 * y
    y = x1 * y + y1 * xm
    b = (x + y + 1) / 2
    t = (x + 2 * y + 1) / 2
    print(x,y,b,t)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 8, eltong, Albania --------------------------')
t1  = time.time()

# Instant answer, coded in Python. Oh well...

from math import ceil, sqrt

def gen_b(n):
    """number of blue discs"""
    return int(ceil((2 * (3 - 2 * sqrt(2))**n + sqrt(2) * (3 - 2 * sqrt(2))**n + 2 * (3 + 2 * sqrt(2))**n - sqrt(2) * (3 + 2 * sqrt(2))**n + 4) / 8))

def gen_s(n):
    """total number of discs"""
    return int(ceil((-(3 - 2 * sqrt(2))**n - sqrt(2) * (3 - 2 * sqrt(2))**n - (3 + 2 * sqrt(2))**n + sqrt(2) * (3 + 2 * sqrt(2))**n + 2) / 4))

i = 5

while True:
    if gen_s(i) > 10**12:
        print(gen_b(i))
        break
    i += 1

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

