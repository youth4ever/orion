from fractions import Fraction
from itertools import cycle
from math import floor

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
        frac = Fraction(1, cfr[-1])
        print(frac) #,'  <-Start')
        for i in reversed(range(1, len(cfr)-1)) :
            frac = 1 / (frac + cfr[i])
            print(frac)
        print(frac+self.a0 ) #, '  <-- Final Answer')
        return frac+self.a0

print('\n', CONTINUED_FRACTIONS().rationalize(2, 15))

print('\n----------------')

x= CONTINUED_FRACTIONS()
# print(x.continued_fractions(991))
# print(x.continued_fractions(2))
y = x.continued_fractions(2)
C=cycle(y)
for i in range(10): print(next(C), end=' ')