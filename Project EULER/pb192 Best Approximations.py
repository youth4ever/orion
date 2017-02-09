#!/usr/bin/python                   ( ͡° ͜ʖ ͡°)
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
                    Best Approximations         -       Problem 192

Let x be a real number.
A best approximation to x for the denominator bound d is a rational number r/s in reduced form,
with s ≤ d, such that any rational number which is closer to x than r/s has a denominator larger than d:

                        |p/q-x| < |r/s-x| ⇒ q > d

For example, the best approximation to √13 for the denominator bound 20 is 18/5
and the best approximation to √13 for the denominator bound 30 is 101/28.

Find the sum of all denominators of the best approximations to √n for the denominator bound 10**12,
where n is not a perfect square and 1 < n ≤ 100000.

'''
import time
from fractions import Fraction
from itertools import cycle
from math import floor
from gmpy2 import mpq


class CONTINUED_FRACTIONS(object):
    '''Made by Bogdan Trif @ 2016-11-18. It needs the factions.Fraction, itertools.cycle and math.floor
        '''
    def continued_fractions(self ,number):        # FASTEST ALGORITHM to compute coefficients
        ''':Description: THE FASTEST ALGORITHM
            After if find the proper period of the continued fractions it returns the result.
        :param number:  is the number for which the square root continued fraction coefficients will be computed
        :return: list containing the periodic continued fractions terms    '''
        # from math import floor
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
        # from fractions import Fraction
        # from itertools import cycle
        C = cycle(self.continued_fractions (number))
        cfr = [ next(C) for i in range(nth) ]
        # print(cfr)
        # frac = mpq(1, cfr[-1])
        frac = mpq(1, cfr[-1])
        # print(frac) #,'  <-Start')
        for i in reversed(range(1, len(cfr)-1)) :
            frac = 1 / (frac + cfr[i])
            # print(frac)
        # print(frac+self.a0 ) #, '  <-- Final Answer')
        return frac+self.a0















print('\n--------------------------TESTS------------------------------')
t1  = time.time()


for i in range(1, 20) :
    v = CONTINUED_FRACTIONS().rationalize(3, i)
    print('\n', v , '      ',eval(str(v)) ,'           ',   3**(1/2)     )


@2017-01-21 , 01:10 - Must Use Rampson - Newton to approximate the radicals


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()







# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 3,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 4,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
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
