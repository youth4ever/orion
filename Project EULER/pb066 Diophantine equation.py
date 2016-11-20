#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
                                        Diophantine equation        -      Problem 66
Consider quadratic Diophantine equations of the form:

                                            x**2 – Dy**2 = 1

For example, when D=13, the minimal solution in x is 649**2 – 13×180**2 = 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

                                                        3**2 – 2×2**2 = 1
                                                        2**2 – 3×1**2 = 1
                                                        9**2 – 5×4**2 = 1
                                                        5**2 – 6×2**2 = 1
                                                        8**2 – 7×3**2 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.
'''

from decimal import *
getcontext().prec = 50
import time
from fractions import Fraction, Decimal
from itertools import count
from math import sqrt

#for y in range(31,1,-1): print(y)

def sieve(lower, upper_bound):         # THE FASTEST  SIEVE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    ''' SIEVE OF ERATOSTHENES Algorithm  , THE FASTEST  SIEVE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'''
    n = upper_bound + 1
    check = [True] * n
    check[0] = check[1] = False
    for i in range(2, int(upper_bound**0.5) + 1):
        if check[i]:
            for j in range(i**2, upper_bound + 1, i):
                check[j] = False
    primes = [i for i, flag in enumerate(check) if flag and i > lower ]
    return primes

print('\n -------------------- MY FIRST ATTEMPT SOLUTION, BRUTE FORCE ---------------------')
# primes = sieve(2,1001)
# x_max = 0
# for y in count(1, 1) :    #range(1, 100):
#     for D in range(1000, 2, -1) :
#     # for D in primes :
#         #x = sqrt(  D*y*y + 1  )
#         x = Decimal(D*y*y + 1).sqrt()
#         #D = ( x*x - 1 ) / (y*y)
#         #if D > 1000 : break
#         #print('x = ', x ,' ,   y =', y,'  ;     D  = ', D )
#         #if x % 1 == 0 :
#         if x % 1  == 0 : #and x > x_max :
#             print('x = ', x ,' ,   y =', y,'  ;     D  = ', int(D) )
#             x_max = x
#     if y % 100000 == 0:
#         print('Check point:', y)

# for i in count(10): print(i)
#       Tried : 873, 781, 991, 919





num=1e6
sqr = [x*x for x in range( int(num**0.5)+1)]

def cont_fraction(num):         # It may be optimized
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
    while i == 0 or first != [m, d, a]: # Smart here
        i += 1
        m = d*a - m
        d = (num - sqr[int(m)])/d
        a = (a_0 + m) // d
        digits.append(int(a))
        # print(m,d,a)
    return  digits[:-1]    # i, digits[:-1]   do not modify i, digits[:-1] --> IT IS CORRECT


nr=14
a = cont_fraction(nr)
print('Continue Fraction Test :  ',a)

def PELL_EQN_minimal_terms(D):
    ''' :Description:   Uses the cont_fraction function which first constructs a list. Then use:
    *frac = 1 / (frac + a[i])* by going backwards and constructs the fraction.
    :param  nr:  the number you want to rationalize. :
        :NOTE: actually nr is considered as sqrt(n)
    :return:    a rational expression under a form of a fraction     '''
    from math import sqrt
    a = cont_fraction(D)
    # print('a  ==> ', a)
    if len(a) > 1 :
        if len(a) % 2 == 1 :
            a = a*2
            frac = Fraction(1, a[-2])
        else :
            frac = Fraction(1, a[-2])
        for i in reversed(range(len(a)-2)):
            # print(frac,'  <-Start')
            frac = 1 / (frac + a[i])
            # print(frac)
        return frac+int(sqrt(D))
    else:
        frac = Fraction(1, a[0])
        return frac+int(sqrt(D))

print('\n---------------Now some Tests ------------------')
print('\nTest of the continued fraction function :  ', cont_fraction(13) )
print( '\n Test of the PELL_EQN_minimal_Terms function :  ', PELL_EQN_minimal_terms(13) )

print('\n================  My FIRST SOLUTION,   ===============\n')


def main():
    up_range=1e3
    global maxv, d
    maxv, d = 0, 0
    for D in range(1, int(up_range)):
        if D not in sqr :
            if len(str(PELL_EQN_minimal_terms(D)).split('/')) == 2 :
                x = int(str(PELL_EQN_minimal_terms(D)).split('/')[0])
                y = int(str(PELL_EQN_minimal_terms(D)).split('/')[1])
            else:
                x = PELL_EQN_minimal_terms(D)
                y = 1
            res = x*x - D*y*y

            if x > maxv:
                maxv, d = x, D
                # print(str(D)+'.    x=',  x ,'  y=',  y ,'   ' , res , '     ' ,cont_fraction(D), '     ',  PELL_EQN_minimal_terms(D)   )
    return d, maxv



if __name__ == "__main__":
    t1  = time.time()

    print('\nAnswer :  ', main() )          # 661 is the correct answer finally

    t2  = time.time()
    print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1, VERY VEY GOOD, ConnorMcLaud, Belarus  --------------------------')
t1  = time.time()
# This is solution for Pell's equation though continued fraction approximation
from math import floor
from itertools import cycle


def continued_fractions(number):
    result = []
    fraction = ()
    m = 0
    d = 1
    a0 = number ** 0.5
    if a0.is_integer():
        return [a0, None]
    a0 = floor(a0)
    a = a0
    result.append(a)
    while True:
        m = d * a - m
        d = (number - m ** 2) / d
        a = floor((a0 + m) / d)
        fraction += (a,)
        if a == 2 * a0:
            break
    result.append(fraction)
    return result


def approximation(number):
    fractions = continued_fractions(number)
    a0, rest = fractions
    old_h = a0
    old_k = 1
    yield old_h, old_k
    if rest is None:
        return
    h = a0 * rest[0] + 1
    k = rest[0]
    yield h, k
    fracts = cycle(rest)
    next(fracts)
    for a in fracts:
        temp_h = h
        temp_k = k
        h = a * h + old_h
        k = a * k + old_k
        yield h, k
        old_h = temp_h
        old_k = temp_k


def solve_equation(D):
    ''' x^2 - Dy^2 = 1 '''
    for x, y in approximation(D):
        if x ** 2 - D * y ** 2 == 1:
            return x, y


def find(limit=1000):
    for D in range(2, limit + 1):
        if (D ** 0.5).is_integer():
            continue
        try:
            solution = solve_equation(D)
        except:
            continue
        yield (solution, D)


print('minimal solutions of x for which the'
      ' largest value of x is obtained is', max(find())[-1])

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2, styko, France  --------------------------')
t1  = time.time()
# Chakravala method in Python (english, french), 100ms
# Cf https://fr.wikipedia.org/wiki/Méthode_chakravala
from math import sqrt, floor

def norm(a, b, n):
    return a**2 - n*(b**2)

def mult(a1, b1, a2, b2, n):
    return a1*a2 + n*b1*b2, a1*b2 + a2*b1

def mypow(a, b, k, n):
    if k == 1:
        return a, b
    elif k%2 == 0:
        c, d = mypow(a, b, k//2, n)
        return mult(c, d, c, d, n)
    else:
        c, d = mypow(a, b, k-1, n)
        return mult(a, b, c, d, n)

def closestM(n, sqn, m_prec, k):
    t = -m_prec
    k = abs(k)
    while t <= sqn:
        t += k
    if n - (t-k)**2 < t**2 -n:
        return t-k
    else:
        return t

# Most important function
def chakravala(n):
    endNorms = [1, -1, 2, -2, 4, -4]
    sqn = sqrt(n)

    a, b = 1, 0
    k = 1
    # 1st step
    m = closestM(n, sqn, 0, 1)
    a, b = (a*m + n*b)//k, (a + m*b)//k
    k = norm(a, b, n)

    # Intermediate steps
    while k not in endNorms:
        m = closestM(n, sqn, m, k)
        a, b = abs((a*m + n*b)//k), abs((a + m*b)//k)
        k = norm(a, b, n)

    # Last step
    if k == 1:
        return a, b
    elif k == -1:
        return mult(a, b, a, b, n)
    elif k == -2 or k == 2:
        c, d = mult(a, b, a, b, n)
        return c//2, d//2
    elif k == 4:
        if a%2 == 0 and b%2 == 0:
            return a//2, b//2
        elif n%2 == 0:
            c, d = mult(a, b, a, b, n)
            return c//4, d//4
        else:
            c, d = mypow(a, b, 3, n)
            return c//8, d//8
    elif k == -4:
        if a%2 == 0 and b%2 == 0:
            return mult(a//2, b//2, a//2, b//2, n)
        elif n%2 == 0:
            c, d = mult(a, b, a, b, n)
            return c//4, d//4
        else:
            c, d = mypow(a, b, 6, n)
            return c//64, d//64
    else:
        print("Error!", n)
        return -1

# Main code
upperBound = 1000
perfectSquares = [i**2 for i in range(2, int(sqrt(upperBound))+1)]

nmax = 0
xmax = 0
for n in range(2, upperBound+1):
    if n not in perfectSquares:
        c = chakravala(n)
        if c[0] > xmax:
            xmax = c[0]
            nmax = n

print("-->", nmax, xmax)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3, mbh038, England  --------------------------')
t1  = time.time()

def PE_0066(nmax):
    """
    Returns D<nmax that gives the greatest value for x where(x,y) is the
    fundamental solution for the Pell equation x^2-Dy^2=1.
    """
    Dmax=-1
    xmax=-1
    for D in range(nmax):
        try:
            xn=Pellfs(D)[0]
            if xn>xmax:
                xmax=xn
                Dmax=D
        except:
            pass
    print (Dmax)

def Pellfs(n):
    """returns fundamental solution for Pell equation x^2-ny^2 =1 for given n"""
    if sqrt(n) == int(sqrt(n)):
        return None
    anext, repeats = sqcf(n)
    rps = cycle(repeats)
    convergents = [(0,1),(1,0)]
    nom,den = 0,0
    while nom**2-n*den**2!=1:
        nom, den = [anext*convergents[-1][j]+convergents[-2][j] for j in range(2)]
        convergents.append((nom,den))
        anext = next(rps)
    return (nom,den)

def sqcf(S):
    """
    S is a natural number. Must not be a perfect square

    returns (a0,[r0,..,rn]) where a0 is the stem and [r0,...,rn] is the
    repeating part of the square root continued fraction of S
    """
    a=[int(sqrt(S))]#isqrt(S)
    d0,d=1,1
    m=0
    while 1:
        m=d*a[-1]-m
        d=int((S-m**2)/d)
        a.append(int((a[0]+m)/d))
        if d==d0:
            return (a[0],a[1:])
            break
PE_0066(1000)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,  aolea, Spain --------------------------')
t1  = time.time()

import fractions
import gmpy2

gmpy2.get_context().precision = 1000

listX = []
listY = []
listD = []

for D in range(1,1001):
    if gmpy2.sqrt(D) - int(gmpy2.sqrt(D)) != 0:
        listH = [0, 1]
        listK = [1, 0]
        rootD = gmpy2.sqrt(D)
        h = int(rootD)*listH[-1] + listH[-2]
        k = int(rootD)*listK[-1] + listK[-2]
        if h**2 - D*k**2 == 1:
            listX.append(h)
            listY.append(k)
            listD.append(D)
        else:
            listH.append(h)
            listK.append(k)
            flag = False
            rest = fractions.Fraction(str(rootD - int(rootD)))
            while flag == False:
                try:
                    inversedRest = gmpy2.div(1,rest)
                except ZeroDivisionError:
                    print(D,'check precision')
                    break
                h = int(inversedRest) * listH[-1] + listH[-2]
                k = int(inversedRest) * listK[-1] + listK[-2]
                if h ** 2 - D * k ** 2 == 1:
                    flag = True
                    listX.append(h)
                    listY.append(k)
                    listD.append(D)
                else:
                    listH.append(h)
                    listK.append(k)
                rest = fractions.Fraction(str(inversedRest-int(inversedRest)))
print(max(listX), listD[listX.index(max(listX))])

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
