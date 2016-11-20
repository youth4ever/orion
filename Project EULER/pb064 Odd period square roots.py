#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Sun, 6 Nov 2016, 16:33
#The  Euler Project  https://projecteuler.net
'''
                            Odd period square roots     -       Problem 64
All square roots are periodic when written as continued fractions and can be written in the form:

It can be seen that the sequence is repeating. For conciseness,
we use the notation √23 = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats indefinitely.

The first ten continued fraction representations of (irrational) square roots are:

                                                √2=[1;(2)], period=1
                                                √3=[1;(1,2)], period=2
                                                √5=[2;(4)], period=1
                                                √6=[2;(2,4)], period=2
                                                √7=[2;(1,1,1,4)], period=4
                                                √8=[2;(1,4)], period=2
                                                √10=[3;(6)], period=1
                                                √11=[3;(3,6)], period=2
                                                √12= [3;(2,6)], period=2
                                                √13=[3;(1,1,1,1,6)], period=5

Exactly four continued fractions, for N ≤ 13, have an odd period.

How many continued fractions for N ≤ 10000 have an odd period?
'''

from math import sqrt
from decimal import *
from fractions import Fraction
getcontext().prec = 500     # Initially I used 1000 to be sure
import time


def compute_quare_root(n, decimals=4) :
    n = n*10**(decimals*2)
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

print('TEST :          ',compute_quare_root(2,101))

print('\n================  My FIRST SOLUTION, SLOW  ===============\n')
t1  = time.time()
# My solution computes radicals with hundreds of decimals and calculates the continued fractions
# This increases much the time of the computations as the largest sequence period is 217 for sqrt(9949)
# I need to improve my algorithm for calculating partial fractions

def cont_frac(val, maxterms=15, lim=  1e-10 ):
    if isinstance(val, (int, float, Decimal)):
        frac=[]
        val = Decimal(val)
        r = int(val)
        frac.append(r)
        # print(frac)
        while len(frac) < maxterms :
            # print(val,'   ' ,r)
            val -=  r
            if val > lim :
                val = Decimal(1)/val
                r = int(val)
                frac.append(r)
            else: break
    return frac

print()

def rationalize(x, maxterms=40, lim=1e-50) :
    cfr = cont_frac(x, maxterms, lim)
    frac = Fraction(1, cfr[-1])
    # print(frac,'  <-Start')
    for i in reversed(range(1, len(cfr)-1)) :
        frac = 1 / (frac + cfr[i])
        # print(frac)
    # print(frac+cf[0], '  <-- Final Answer')
    return frac+cfr[0]

# print(cont_frac(sqrt(3)) )


def guess_seq_len(seq):         # by Bogdan Trif @ 2016-11-06, 15:00
    '''    :SCOPE: Functions which returns a repeating sequence within a list of integers.
        If  it not finds a sequence it will return just the first element of the sequence
        Observation : It may not work properly if the sub sequence ends with double, triple ... of the same digit.
        In this case it needs adjustments. However, in the case of lists of partial fractions where the function was used,
        this never happens.
    :param:
        :seq:     List of integers
        :return:     The unique  sequence of numbers from the list        '''
    def inside_loop(seq):
        guess = len(seq)//2
        for guess in range(guess, 1, -1 ):
            guess-=1
            s1, s2 = seq[0:guess], seq[guess: 2*guess ]
            # print(len(s1), s1, end='     ')
            # print(len(s2) , s2)
            if s1 == s2 : break
        if s1 != s2 :  return seq
        else: return s1

    s = inside_loop(seq)
    if len(list(set(s))) == 1 :
        return [s[0]]
    else:                   #return  s
        l1 = len (list(set(s)))
        lst=[]
        for i in range(len(s)):
            lst.append(s[i])
            if l1 == len(list(set(lst))) :
                break
        return lst

def square_roots_cont_frac_odd_terms(lim):                  # 128 Largest period :     217 --> for range 9000-10001
    largest_period = 0
    counter=0
    for i in range(2, lim+1):
        if len(str (Decimal(i).sqrt()) ) > 4  :
            seq = cont_frac( Decimal(i).sqrt() , 450, 1e-250 )[1:]    # 500 , with getcontext().prec=500
            guess = guess_seq_len(seq)
            print(i ,len (guess),  guess ,'     ########       '  , seq )
            if len(guess) > largest_period :
                largest_period = len(guess)
                # print(i, largest_period, guess ,'   ###########    ' , seq)
            if len(guess) % 2 == 1 :
                    counter+=1
                    # print(i ,seq,'        ' ,guess, len(guess))
    return counter, 'Largest period :', largest_period        # Answer : 1322

# The CALL For the First Solution :
print('\n Answer: ',square_roots_cont_frac_odd_terms(10000))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')      # Completed in : 219739.568233 ms


print('\n================  My SECOND SOLUTION, FAST  ===============\n')
# the second solution is faster because the Algorithm used to generate partial fractions terms searches
# the sequence as it goes. In my first algorithm I compute for all numbers 500 digits (unnecessarilly ) and only
# after I use a search guess_seq_len sequence algorithm. This is really a much slower way

num=10000
sqr = [x*x for x in range( int(num**0.5)+1)]
def cont_fraction(num):
    '''     Algorithm to compute partial fractions of square roots
        :Description:
            Algorithm taken from:  https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Algorithm.
            Very Fast & Efficient Algorithm to compute the partial fractions of square roots.
    :param:     num: is the number for which sqrt(num) will be considered and for which partial fractions will
                        be computed
    :returns:   the number of unique sequence terms and the list with the unique sequence terms    '''

    i, m, d = 0, 0, 1
    a_0 = int(num**0.5)
    a = a_0
    m = d*a - m
    # print(a, m, d, '<-- init')
    d = (num - sqr[m])/d
    a = (a_0 + m) // d
    first = [m, d, a]
    # print(first, 'init')
    digits = [int(a)]
    while i == 0 or first != [m, d, a]:
        i += 1
        m = d*a - m
        d = (num - sqr[int(m)])/d
        a = (a_0 + m) // d
        digits.append(int(a))
        # print(m,d,a)
        return i    # , digits[:-1]             #  do not modify digits[:-1] --> IT IS CORRECT


def pb064(num):
    iter = 0
    for i in range(2, num+1):
        if i not in sqr :
            x = cont_fraction(i)
            if x%2 == 1 :
                iter += 1
    return iter




def main():        #********  the MAIN LOOP ********#
##############  SECOND SOLUTION call() ####################
    t1  = time.time()

    print(pb064(num))

    t2  = time.time()
    print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')      #Completed in : 1144.065619 ms

if __name__ == "__main__": main()                   # Uncomment to execute



print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1, VERY VERY FAST, mbh038, England  --------------------------')
t1  = time.time()

import time
import math
def p64(n):
    """returns number of  integers <=n that have odd-period continued fractions"""
    t=time.clock()
    c=0
    for i in range (1,n+1):
        if  i%4==0 or int(math.sqrt(i))==math.sqrt(i):
            continue
        if len(sqcf(i)[1])%2==1:
            c+=1
    print (c,time.clock()-t)

def sqcf(S):
    """
    S is a natural number. Must not be a perfect square

    returns (a0,[r0,..,rn]) where a0 is the stem and [r0,...,rn] is the
    repeating part of the square root continued fraction of S
    """
    a=[int(math.sqrt(S))]
    d0,d=1,1
    m=0
    while 1:
        m=d*a[-1]-m
        d=int((S-m**2)/d)
        a.append(int((a[0]+m)/d))
        if d==d0:
            return (a[0],a[1:])
            break
p64(10000)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')          # Completed in : 628.035784 ms


# IDEA:
# The only thing I miss in most postings in this thread is constructing the radicands instead of taking
# all the numbers below 10^4 and calculating their square roots. Pseudocode:
#
# for m = 1 .. 99
#    for r = 1 .. 2 * m
#       S = m * m + r
#       calculate the continued fraction expansion of S (Wikipedia algorithm)
#
# Here m is the largest square below S. No calculation of square roots at all.
# Skipping numbers which are guaranteed to produce even periods should be easy, I didn't yet try that.


print('\n--------------------------SOLUTION 2, Similar to mine but faster , jerryxjr1220 --------------------------')
t1  = time.time()
# "Did anyone try the 'stupid' brute force to solve it?"
# "I did..."
# Use Decimal by high accuracy > 250 digital...
# It still works...and seems fast then expected...
# 1322
# Use: 7.469 sec.


import decimal as dc

dc.getcontext().prec = 250
def root(n):
    blist = []
    n0 = dc.Decimal(i).sqrt()
    a0 = int(n0)
    b0 = n0 - a0
    n1 = 1/b0
    a1 = int(n1)
    b1 = n1 - a1
    while str(b1)[:11] not in blist:
        blist.append(str(b1)[:11])
        n1 = 1/b1
        a1 = int(n1)
        b1 = n1 - a1
    return len(blist)

count = 0
for i in range(2,10000):
    if i**0.5 != int(i**0.5):
        if root(i) % 2 == 1:
            count += 1
print (count)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')          # Completed in : 7913.452625 ms



print('\n--------------------------SOLUTION 3, cadastro  --------------------------')
t1  = time.time()
# I second this...spent all day trying to outwit Python's floating point messiness...then I said to hell
#  with that and focused on the integers you get in each new fraction...
# Nan-Do said
# I had a hard time overcoming the rounding problems until I found the much more elegant approach of the triplets.

from math import floor

def gen_values(n):
    m = 0
    d = 1
    a0 = a1 = floor(n ** 0.5)
    while 2 * a0 != a1:
        m =  d * a1 - m
        d = (n - (m ** 2)) / d
        a1 = floor((a0 + m) / d)
        yield a1

def is_not_cube(n):
    x = floor(n ** 0.5)
    return (x * x) != n

total = 0
for n in filter(is_not_cube, range(2, 10001)):
    if (sum(1 for _ in gen_values(n)) % 2) == 1:
        total += 1
print (total)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n--------------------------SOLUTION 4,  GREAT , detrin, Slovakia --------------------------')
t1  = time.time()
# Here is my solution, I used the algorithm from Wikipedia.
# https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Algorithm

sqr = [x*x for x in range(317)]

def cont_fraction(num):
    i, m, d = 0, 0, 1
    a_0 = int(num**0.5)
    a = a_0

    m = d*a - m
    d = (num - sqr[m])/d
    a = (a_0 + m) // d
    first = [m, d, a]
    while i == 0 or first != [m, d, a]:
        i += 1
        m = d*a - m
        d = (num - sqr[int(m)])/d
        a = (a_0 + m) // d
    return i%2

print (sum([cont_fraction(x) for x in range(2, 10001) if x not in sqr]))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n--------------------------SOLUTION 5, kenkamau, Kenya   --------------------------')
t1  = time.time()

#in python -> recursive solution
import math

def search(root, num, den):
    root = math.sqrt(i)
    output = int((root + num)/den)
    result.append(output)
    multiple = den * output

    netEx = multiple - num

    overallDenom = i - (netEx ** 2)

    if overallDenom % den == 0:
        den = overallDenom / den

    num = netEx

    if den != 1:
        search(i, num, den)
    else:
        result.append(int(math.sqrt(i)) + num)

count = 0
myList = [x for x in range(1, 10000) if math.pow(int(math.sqrt(x)),2) != x]

for i in myList:
    result = []
    initialQuot = math.sqrt(i)
    num = int(initialQuot)
    den = i - int(initialQuot) ** 2

    search(i, num, den)

    if len(result) % 2 == 1 or (len(result) == 2 and result[0] == result[1]):
        count = count + 1

print (count)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n--------------------------SOLUTION 6, Bart23, Belgium  --------------------------')
t1  = time.time()
# Floats didn't work out due to rounding errors, so here is my own attempt
# to solve the problem using only integers and recurrence relations.

import math
squares=set(i*i for i in range(100))
oddcount=0
for i in range(2,10000):
    if i not in squares:
        a, b=[], []
        a.append(math.floor(math.sqrt(i)))
        b.append([a[0],1,i-a[0]**2])  #(t,s,n)<-->(t+s*sqrt(i))/n
        cycle=False
        while not(cycle):
            a.append(math.floor((b[-1][0]+b[-1][1]*math.sqrt(i))/b[-1][2]))
            t=b[-1][2]*(b[-1][0]-b[-1][2]*a[-1])
            s=-b[-1][2]*b[-1][1]
            n=(b[-1][0]-b[-1][2]*a[-1])**2-b[-1][1]**2*i
            d=math.gcd(math.gcd(t,s),n)
            b.append([t//d,s//d,n//d])
            if b[-1] in b[1:-1]:
                cycle=True
                if (len(b)-1-b.index(b[-1]))%2==1:
                    oddcount+=1
print(oddcount)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')






















# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,   --------------------------')
# t1  = time.time()
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 3,   --------------------------')
# t1  = time.time()
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 4,   --------------------------')
# t1  = time.time()
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 5,   --------------------------')
# t1  = time.time()
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

