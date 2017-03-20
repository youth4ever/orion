#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Sat, 17 Dec 2016, 00:00
#The  Euler Project  https://projecteuler.net
'''
                        Pandigital Fibonacci ends   -       Problem 104

The Fibonacci sequence is defined by the recurrence relation:

F_n = F_n−1 + F_n−2, where F_1 = 1 and F_2 = 1.

It turns out that F_541, which contains 113 digits, is the first Fibonacci number for which the
last nine digits are 1-9 pandigital (contain all the digits 1 to 9, but not necessarily in order).

And F_2749, which contains 575 digits, is the first Fibonacci number for which the first nine digits are 1-9 pandigital.

Given that F_k is the first Fibonacci number for which the FIRST nine digits AND
the LAST nine digits are 1-9 pandigital, find k.


'''
import time
import gmpy2
import numpy as np
from itertools import count
import eulerlib
from decimal import *
getcontext().prec = 100



def Fibonacci(n):
    iter = 0 		# Number of terms
    #	ORIGINAL Fibonacci with iteration, while loop
    a, b = 0, 1
    while iter < n:
        iter +=1
        a  , b = b, a + b
    return a




def prime_generator(n):      ### o(^_^)o  FASTEST  o(^_^)o  ###  HIghly Efficient !!!
    """  Sieve of Eratosthenes              !!!!!!!!! THE FASTEST SIEVE. It won the battle with sieve
    Create a candidate list within which non-primes will be marked as None.
    """
    cand = [i for i in range(3, n + 1, 2)]
    end = int(n ** 0.5) // 2

    # Loop over candidates (cand), marking out each multiple.
    for i in range(end):
        if cand[i]:
            cand[cand[i] + i::cand[i]] = [None] * ( (n // cand[i]) - (n // (2 * cand[i])) - 1 )

    # Filter out non-primes and return the list.
    return [2] + [i for i in cand if i]

def Fibo_gen():
    #   Fibonacci GENERATOR , while loop
    a1, a2 = 0, 1
    while True:
        a = a1 + a2
        yield a
        a1, a2 = int(str(a2)[-10::]), int(str(a)[-10::])

def Fibonacci_Binet(n_th) :
    ''':Description:    Returns the Fibonacci corresponding to the number  and uses the Binet Formula.
        http://mathworld.wolfram.com/BinetsFibonacciNumberFormula.html
        :param n_th: F_nth Fibonacci in sequence
        :return: str, first 9 digits of the Fibonacci number
    '''
    phi = Decimal((5**(1/2)+1)/2)
    phi_ = Decimal((1- 5**(1/2))/2)
    # phi = (1+5**(1/2))/2
    # phi_ = (1-5**(1/2))/2
    # a = ( ( phi**n_th-phi_**n_th ) / ( phi - phi_) )%(10**9)
    a = str(((phi**n_th)-(phi_)**n_th)/( phi - (phi_)))[0:10].replace( '.' , '')
    # b =   ( (( 1 + np.sqrt(5))/2)**n_th - ((1 - np.sqrt(5))/2)**n_th  ) /np.sqrt(5)
    return str(a)


print('\n--------------------------TESTS------------------------------')

print('Test for the Fibonacci_Binet : ', Fibonacci_Binet(541))
print('gmpy2.fib : \t\t\t\t\t\t\t' ,gmpy2.fib(541) )

print('Test for the Fibonacci_Binet : ', Fibonacci_Binet(1271659))
print('gmpy2.fib : \t\t\t\t\t\t\t' ,gmpy2.fib(1271659) )


print('---------------MORE TESTS---------\n')
t1  = time.time()

# y = Fibo_gen(1)
# for i in range(2, 30):    print(str(i)+'. ' ,y.__next__() , end=' ;   ' )

print('\ngmpy2.fib2 : \t' ,gmpy2.fib2(541) )

print('\ngmpy2.fib : \t' ,gmpy2.fib(2749) )
print('\n eulerlib.is_pandigital  : \t' , eulerlib.is_pandigital ( 1234567890 ,  1 , 9) )


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n================  My FIRST SOLUTION, SLOW 30 sec  ===============\n')
t1  = time.time()

# !!! IMPORTANT OBSERVATIONS : FIRST Fib number to have the LAST 9 digits pandigital is a prime
# FIRST Fib number to have the FIRST 9 digits pandigital is a prime

def my_first_solution():
    pan = '123456789'
    z = Fibo_gen()
    for p in count(2 ) :
        y = z.__next__()
        x = Fibonacci_Binet(p)
        # w = gmpy2.fib(p)
        # print(str(p)+'.    ', x, y  , str(w)[:9] , str(w)[-9::])
        f9 = ''.join(sorted(str(x)[:9]))
        l9 = ''.join(sorted(str(y)[-9::]))
        if   ( f9 == pan or l9  == pan ) :
            print(str(p)+'.       first9: ord:\t', f9 ,  '\texact: ', str(x)[:9],  '       last9 : ord\t', l9,  '\texact: ', str(y)[-9::],'        ' )
        if   f9 == pan and l9  == pan :
            return print('\nAnswer :   F',  p )


# my_first_solution()            #       Answer :   F 329468

t2  = time.time()
print('\nCompleted in :', round((t2-t1), 6), 's\n\n')      #  Completed in : 33,40791  s

# 541.    516212329      839725641
# 919.    513046096      965324781
# 2749.    143726895      002250249
# 7727.    314782956      397498593
# 20411.    198262300      241573689
# 28837.    168692931      283594617
# 32717.    125643798      869963797
# 34883.    583942167      566962697

###   2016-12-16, 16:25       investigating primes until
# 1271659.       first9: ord:	 112344568 	exact:  461453182        last9 : ord	 123456789 	exact:  356827941




print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,   --------------------------')
t1  = time.time()

# ===== Tue, 20 Sep 2016, 23:22, Aguy
# Less than a second. I used two sequences. One is keep doing mod 1e9 when needed,
# the other is keeping the integer part 9 digit long by dividing by 10 when appropriate.

a, b = 1, 1
c, d = 1, 1
k = 1
while True:
    k += 1
    a, b = b, a + b
    c, d = d, c + d
    if c > 1e9:
        c /= 10
        d /= 10
    if a > 1e9:
        a %= 1e9
        b %= 1e9
    if len(set(str(int(a)))) == 9 and '0' not in set(str(int(a))):
        if len(set(str(int(c)))) == 9 and '0' not in set(str(int(c))):
            break
print(k)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()

# ==== Sat, 3 Sep 2016, 17:19, fioi, France


from math import log10, floor, sqrt

def is_pandigital(n):
        seen = [False] * 10
        while n > 0:
                seen[n % 10] = True
                n //= 10
        return not False in seen[1:]

phi = (1 + sqrt(5)) / 2
logphi = log10(1 + sqrt(5)) - log10(2)
logsqrt5 = log10(5) / 2

def match(last_digits, n):
        if not is_pandigital(last_digits):
                return False
        logun = n * logphi - logsqrt5
        nb_digits = int(round(logun)) + 1
        val = int(floor(10 ** (logun - (nb_digits - 9))))
        return is_pandigital(val)

MOD = 10 ** 9
a, b = 1, 1
i = 2
while not match(b, i):
        a, b = b, (a + b) % MOD
        i += 1
print(a, b, i)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3, FASTEST   --------------------------')
t1  = time.time()

# =======  Mon, 10 Oct 2016, 09:39, mbh038, England
# About 115 ms in Python. I get the first digits from 10**a
# where a is the decimal part of n log_10 (1+√5) /2  −log_10 √5, and the final 9 digits by calculating Fibonacci numbers
# mod 10**9.
# This avoids the need to calculate huge numbers.

import numpy as np

def mbh038():
    digits=set('123456789')
    n=0
    last,b=0,1
    logphi = np.log10((1+np.sqrt(5))/2)
    logroot5=0.5*np.log10(5)
    while 1:
        n+=1
        last, b=(last+b)%1000000000, last
        if last%9 !=0:
            continue
        if set(str(last))==digits:
            c=10**(( n * logphi - logroot5)%1 )
            first=str(c)[0]+str(c)[2:11]
            if set(first)==digits:
                break
    print(n)

mbh038()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 4,   --------------------------')
t1  = time.time()
# =====Thu, 3 Nov 2016, 20:37, Khalid, Saudi Arabia
# That was a fun one, I used mod to check for the lower bounds, and then if it's pan digital,
# I estimated the full number using the golden ratio. Runs in half a second.

from math import sqrt, log10

def fib_generator(mod):
    prev1 = 1
    prev2 = 2
    while True:
        swap = prev2
        prev2 = (prev1 + prev2) % mod
        prev1 = swap
        yield prev1


fib_gen = fib_generator(10**9)

Phi = (sqrt(5) + 1) / 2
def fib_estimate(digits, i):
    lg = i * log10(Phi) - log10(5) / 2
    lg -= int(lg)
    lg = 10**lg * 10**(digits-1)
    return int(lg)

pandigtal = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
i = 2 # 1 and 2
while True:
    i += 1
    n = next(fib_gen)
    if sorted(str(n)) == pandigtal:
        f_est = fib_estimate(9, i)
        if sorted(str(f_est)) == pandigtal:
            print( i, f_est)
            break


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5, Also Binet Formula  --------------------------')
t1  = time.time()

# ====    Wed, 16 Dec 2015, 15:22, whitealley, Ukraine

# Fibonacci numbers generator
# return only 9-last numbers
def fib():
    yield 1
    a = b = 1
    while True:
        a, b = b, (a+b) % 10**9
        yield a


# if n is 1-9 pandigital return true
# False - otherwise
def pandig(n):
    if n < 123456789:
        return False
    d = [0]*9
    while n>0:
        c = n % 10
        if not c:
            return False
        if d[c-1]:
            return False
        d[c-1] = c
        n //= 10
    return True


# Main program

f = fib()
k = 0
for i in f:
    k += 1
    if pandig(i):
        j = (k * 0.20898764024997873 - 0.3494850021680094)
        j = int(10**(j-int(j)+8))
        if pandig(j):
            print ('k=', k)
            break

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6,   --------------------------')
t1  = time.time()

# ====Sun, 17 Jan 2016, 00:38, michael15, USA
# We can use modular arithmetic to quickly filter out invalid values of k.
# This doesn't use the formula to get the first 9 digits. Runs in ~4-5 seconds.

def is_pandigital(n):
    return ''.join(sorted(str(n))) == "123456789"

def is_end_pandigital(n):
    return is_pandigital(n % 10**9)

def is_beg_pandigital(n):
    return is_pandigital(int(str(n)[:9]))

def mod_fib():
    yield 1
    yield 1
    a = b = 1
    while True:
        a, b = b % 10**9, (a + b) % 10**9
        yield b

def end_pandigital():
    k = 1
    for n in mod_fib():
        if is_end_pandigital(n):
            yield k
        k += 1

candidates = end_pandigital()
cur = next(candidates)

a = b = 1
k = 3
while True:
    a, b = b, a + b
    if k == cur:
        v = is_beg_pandigital(b)
        print (cur, v)
        cur = next(candidates)

        if v:
            break

    k += 1

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

