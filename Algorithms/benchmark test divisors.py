
import functools, time
from math import sqrt


def factor(n):      ## WINNER
  factors = set()
  for x in range(1, int(sqrt(n)) + 1):
    if n % x == 0:
      factors.add(x)
      factors.add(n//x)
  return sorted(factors)

def factors(n):     # SECOND PLACE
    return set(functools.reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))



class GET_DIVISORS(object):     # THIRD, LOW PERFORMANCE
    '''Made by Bogdan Trif @ 2016-11-15, based on itertools.combinations module
    and with a little help on list(functools.reduce(operator.mul, i) for i in comb)

    :param nr:  int
    :return: a list with the factors ( method factorise) or divisors (method divisors)
    :Usage:  >>> GET_DIVISORS().divisors(90)    # to obtain the divisors
                                                                                                              '''
#     def __init__(self, nr):   # We don't want to initialize the class with a number
#     self.nr = nr

    def factorise(self, nr):
        ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
        from pyprimes import factorise
        return [val for sublist in [[i[0]]*i[1] for i in factorise(nr)] for val in sublist]

    def divisors(self, nr):
        ''':Description: Use the itertools, functools, operator, gmpy2 modules.
        In the case of multiple calls take the module imports outside the class and load only once => improved speed. '''
        from itertools import combinations
        import functools, operator, gmpy2
        if gmpy2.is_prime(nr) == True or nr == 1 :
            return [1]    # Must be adjusted to [1] if you change on list
        else :
            all_factors =  self.factorise(nr)
            # set_factors=list(set(all_factors))
            comb= set()
            # print(all_factors)
            for i in range(1, len(all_factors)):
                c = set(combinations(all_factors, i) )
                comb.update(c)
                comb_prod = list(functools.reduce(operator.mul, i) for i in comb)
                comb_prod.sort()
        return  comb_prod[::-1]   # sum([1]+ comb_prod)   !!! Remember to change on  return [1]  for isprime case !




F = [510510,  1992008, 16777216 ]


print('\n------------------1 ---- GET_DIVISORS CLASS  ----------------')
t1  = time.time()


print('Here we test the GET_DIVISORS CLASS :  \n')
for i in F :
    print(i, GET_DIVISORS().divisors(i) )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

#################### #####################

print('\n--------------- 2 ---- factor ------------------')
t1  = time.time()


for i in F :
    print( "%i: factors: %s" % (i, factor(i)) )



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#################### #####################

print('\n--------------- 3 ---- factors------------------')
t1  = time.time()



for i in F:
    print( "%i: factors: %s" % (i, factors(i)) )


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

# #################### #####################

print('\n--------------- 4 ------------------')
t1  = time.time()

import sympy

for i in F :
    print( "%i: factors: %s" % (i, sympy.divisors(i)) )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

