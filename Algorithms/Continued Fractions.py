import time
from decimal import *
from fractions import Fraction
from itertools import cycle
getcontext().prec = 500
from math import floor, sqrt

print('------------------- CONTINUED FRACTION --------------------------- ')


def continued_fractions(number):        # FASTEST ALGORITHM to compute coefficients
    ''':Description: THE FASTEST ALGORITHM to date.
        After if find the proper period of the continued fractions it returns the result.

        :param number:  is the number for which the square root continued fraction coefficients will be computed
        :return: list containing the periodic continued fractions terms with the leading integer
        :Example:  >>>continued_fractions(71)  returns
                       [ 8, (2, 2, 1, 7, 1, 2, 2, 16)]'''
    from math import floor
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




def cont_fraction(num):
    '''     Algorithm to compute partial fractions of square roots
        :Description:
            Algorithm taken from:  https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Algorithm.
            Very Fast & Efficient Algorithm to compute the partial fractions of square roots.
    :param:     num: is the number for which sqrt(num) will be considered and for which partial fractions will
                        be computed
    :returns:   the number of unique sequence terms and the list with the unique sequence terms    '''
    sqr = [x*x for x in range( int(num**0.5)+1)]
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
    return i, digits[:-1]

####### MY FUNCTIONS & ALGORITHMS

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


 # I must do a proper class here containing both coefficients and rationals with best algorithms
def rationalize(x, maxterms=40, lim=1e-50) :
    cfr = cont_frac(x, maxterms, lim)
    frac = Fraction(1, cfr[-1])
    print(frac,'  <-Start')
    for i in reversed(range(1, len(cfr)-1)) :
        frac = 1 / (frac + cfr[i])
        print(frac)
    print(frac+cfr[0], '  <-- Final Answer')
    return frac+cfr[0]


def guess_seq_len(seq):         # by Bogdan Trif @ 2016-11-06, 15:00
    '''    :SCOPE: Functions which returns a repeating sequence within a list of integers.
        If  it not finds a sequence it will return just the first element of the sequence
        Observation : It may not work properly if the sub sequence ends with double, triple ... of the same digit.
        In this case it needs adjustments
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



print(rationalize( Decimal(2).sqrt() , 8))



def main():
    print('\n========== ALGORITHM TESTS =============\n')
    t1  = time.time()
    # Number to test :
    sqrt_of_nr = 94125               # 99127449

    print(cont_fraction(sqrt_of_nr))

    t2  = time.time()
    print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

    print('\n-------  MY ALGORITHM, 10x SLOWER  --------\n')

    t1  = time.time()

    seq = cont_frac( Decimal(sqrt_of_nr).sqrt() , 218, 1e-30 )[1:]
    guess = guess_seq_len(seq)
    print(len(guess), guess)

    t2  = time.time()
    print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

#######################
    print('\n--------  THIRD  ALGORITHM, THE FASTEST -----------\n')
    t1  = time.time()

    s = continued_fractions(94125)
    print(s)

    t2  = time.time()
    print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


if __name__ == "__main__":    main()              # Uncomment to execute









##########################################################

# print('\n ------------------------SLOW ALGORITHMS ----------------------')
#
# # Calculating e using Continued Fraction
# # http://en.wikipedia.org/wiki/Continued_fraction
# import math
# from decimal import *
# getcontext().prec = 102
# n = 1000 # number of iterations
# x = 0.0
# for i in range(n, 0, -1):
#     if i % 3 == 1:
#         j = int(i / 3) * 2
#     else:
#         j = 1
#     x = 1.0 / (x + j)
#
# print ('Calculated e : ',x + 1,'            Computer defined e :' ,math.e)
#
# print('\n-----------------------------------------------------------')
#
#
#
# # Calculating PI using Continued Fraction
# # http://en.wikipedia.org/wiki/Continued_fraction
# import math
# n = 10000000 # number of iterations
# x = 0.0
# for i in range(n, 0, -1):
#     x = 1.0 / (x + 1.0 / i)
# print ('Calculated pi : ', x * 2.0 + 2.0,  '             Computer Calculated pi :' ,math.pi)
#
# print('\n-----------------------------------------------------------')
#
# # Calculating nth-root using Newton Iteration
# # http://en.wikipedia.org/wiki/Newton_iteration
# import math
# n = 2.0; a = 3.0 # calculate sqrt(3)
# eps = 1e-9 # max error allowed
# x = a
# while True:
#     xnew = x - (x ** n - a) / (n * x ** (n - 1.0))
#     if abs(x - xnew) <= eps: break
#     x = xnew
# print ('Calculated root : ',x , '        Computer Root Calculated :',a ** (1.0 / n))
#
# print('\n-----------------------------------------------------------')
#
# # Calculating PI using Mandelbrot Fractal (Point)
# # http://en.wikipedia.org/wiki/Approximations_of_%CF%80
# import math
# k = 7 # number of decimal digits wanted
# eps = 1.0 / 10 ** k
# z = complex(-0.75, eps) ; c = z
# n = 0
# while True:
#     n += 1
#     z = z * z + c
#     if abs(z) >= 2.0: break
# print ('Calculated pi  :', n * eps, '          Computer Calculated pi :', math.pi)
#
# print('\n-----------------------------------------------------------')
#
# import math
# def e(accuracy):            # Not ok yet, must re - furbish it
#     return sum(Decimal(1.0/math.factorial(i)) for i in range(accuracy))
#
# print(Decimal(e(30)))
# print(Decimal(math.e))




