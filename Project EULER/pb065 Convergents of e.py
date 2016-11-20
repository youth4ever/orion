#!/usr/bin/python3
# Solved by Bogdan Trif @   Completed on Fri, 4 Nov 2016, 20:29
#The  Euler Project  https://projecteuler.net
'''
                        Convergents of e        -       Problem 65
The square root of 2 can be written as an infinite continued fraction.

The infinite continued fraction can be written, √2 = [1;(2)], (2) indicates that 2 repeats ad infinitum.
In a similar way, √23 = [4;(1,3,1,8)].

It turns out that the sequence of partial values of continued fractions for square roots provide the best rational approximations.
Let us consider the convergents for √2.
...         ...      ...         ...

Hence the sequence of the first ten convergents for √2 are:

1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...

What is most surprising is that the important mathematical constant,
e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

The first ten terms in the sequence of convergents for e are:
2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...

The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.
'''

from decimal import *
from fractions import Fraction
from math import sqrt, e, pi
getcontext().prec =103
import time

class CFraction(list):
    """
    A continued fraction, represented as a list of integer terms.
    """
    def __init__(self, value, maxterms=15, cutoff=1e-10):
        if isinstance(value, (int, float, Decimal)):
            value = Decimal(value)
            remainder = int(value)
            self.append(remainder)
            # print(value,'         ' ,remainder)

            while len(self) < maxterms:
                value -= remainder
                # print(value,'  <-    -= remainder ')
                if value > cutoff:
                    value = Decimal(1) / value
                    remainder = int(value)
                    self.append(remainder)
                    print(value,'     ' ,remainder )
                else:
                    break
        elif isinstance(value, (list, tuple)):
            self.extend(value)
            print(value,'   < from tuple isinstance')
        else:
            raise ValueError("CFraction requires number or list")

    def fraction(self, terms=None):
        "Convert to a Fraction."
        if terms is None or terms >= len(self):
            terms = len(self) - 1
            # print(terms,'   <- initial')
        frac = Fraction(1, self[terms])
        print('\n',frac, '    ', self,  self[terms] ,' <- initial ', terms, reversed(self[1:terms]) )
        for t in reversed(self[1:terms]):
            frac = 1 / (frac + t)
            print(frac, '  ',t ,'   ' ,frac + t )
        frac += self[0]
        return frac

    def __float__(self):
        return float(self.fraction())

    def __str__(self):
        return "[%s]" % ", ".join([str(x) for x in self])


print('\n-------------------------TESTS ----------------------')
cf = CFraction(e , maxterms=10)
print(cf)
print('\n',cf.fraction(),'   Final Answer')


print(Decimal(e),'\n' ,getcontext())

print('---------------------')
def compute_quare_root(n, decimals=4) :
    n = n*10**(decimals*2)
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

print(compute_quare_root(2,101))

# if __name__ == "__main__":
#     from math import e, pi, sqrt

    # numbers = { "phi": (1 + sqrt(5)) / 2, "pi": pi, "e": e,    }
    # #
    # # print ("Continued fractions of well-known numbers")
    # # for name, value in numbers.items():
    # #     print ("   %-8s  %r" % (name, CFraction(value)))
    #
    # value = e
    # cf = CFraction(value,maxterms = 100)
    # print(cf.fraction())
    # print(sum(list(int(x) for x in str(cf.fraction()).split("/")[0]) ))         # The answer of the problem : 206
    #
    # for name, value in numbers.items():
    #     print ("Approximations to", name)
    #     cf = CFraction(value)
    #     for t in range(len(cf)):
    #         print (cf.fraction(t), end='  ')
    #
    # print('\n--------------------------')
    # print ("Some irrational square roots")
    # for n in 2, 3, 5, 6, 7, 8:
    #     print ("   ", "sqrt(%d)  %r" % (n, CFraction(sqrt(n))))
    #
    # print('\n---------------------------')
    # print ("Decimals from 0.1 to 0.9")
    # for n in range(1, 10):
    #     cf = CFraction(n / 10.0)
    #     print ("   ", float(cf), cf)

print('\n================  My SOLUTION with Functions based on the Studied Class, just ok  ===============\n')
t1  = time.time()

def cont_frac(val, maxterms=15, lim=  1e-10 ):
    ''' :Description: Generates Continued fraction terms for a number
        :param:     val - the value to evaluate, integers, sqrt(val)...
                        maxterms - the number of terms to evaluate
                        lim - precision, this may be removed         '''
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

def rationalize(x, maxterms=15, lim=1e-50) :
    cfr = cont_frac(x, maxterms, lim)
    frac = Fraction(1, cfr[-1])
    print(frac,'  <-Start')
    for i in reversed(range(1, len(cfr)-1)) :
        frac = 1 / (frac + cfr[i])
        print(frac)
    print(frac+cf[0], '  <-- Final Answer')
    return frac+cfr[0]


E=Decimal(e)
# print(E, len(str(E)))
cfr = [2, 1, 2, 1, 1, 4, 1, 1, 6, 1]     # 10 terms gives the correct answer : 1457/536
print(cont_frac( E , 50 )  )


e_frac = [2]
for i in range(1,34):
    #e_frac = e_frac + [1, 2*i, 1]
    e_frac.extend([1, 2*i, 1])
print(e_frac)

def rationalize_e(fr_terms) :
    frac = Fraction(1, fr_terms[-1])
    print(frac,'  <-Start')
    for i in reversed(range(1, len(fr_terms)-1)) :
        frac = 1 / (frac + fr_terms[i])
        print(frac)
    # print(frac+cf[0], '  <-- Final Answer')
    return frac+fr_terms[0]

Answer = rationalize_e(e_frac)
print( Answer )
print('Answer: ' ,sum(list(int(x) for x in str(Answer).split("/")[0]) ))         # The answer of the problem : 272

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')




print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1, VERY Interesting ,YoniK, Israel  --------------------------')
t1  = time.time()


from fractions import Fraction
from functools import reduce
from itertools import chain, count, islice

def digit_sum(n):
    return sum(map(int, str(n)))

def convergent(terms, n):
    return reduce(lambda acc, x: x + Fraction(1, acc), reversed(list(islice(terms, n))), 1)

def e_convergent(n):
    return convergent(chain([2], chain.from_iterable([1, 2 * k, 1] for k in count(1))), n)

print(digit_sum(e_convergent(99).numerator))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2, daOnlyBG, USA  --------------------------')
t1  = time.time()

e_dna = [2]
numer = [2,3]

for i in range(1,34): e_dna += [1,2*i,1]

for i in range(2,100,1): numer.append(e_dna[i]*numer[i-1]+numer[i-2])

sum_of_digits = sum([int(i) for i in list(str(numer[-1]))])
print(sum_of_digits)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3, VERY INTERESTING, Magdiragdag ,   --------------------------')
t1  = time.time()

# After a while of solving this type of problem, I started gathering a library of reusable functions.
# Here is one that generates the convergents of a continued fraction, written in Python using generators.
# See, for instance, the Wikipedia page on continued fractions for the method.
# https://en.wikipedia.org/wiki/Continued_fraction

from itertools import count, islice

def continued_fraction_convergents(cf):
    num_prev, num, den_prev, den = 0, 1, 1, 0
    for x in cf:
        num_prev, num = num, x * num + num_prev
        den_prev, den = den, x * den + den_prev
        yield (num, den)

# Then you need the continued fraction of ee as well, also as a generator in Python.
def e():
    yield 2
    for n in count(2, 2):
        yield from (1, n, 1)

# And finally it is just a matter of getting the numerator of the 100th convergent.
cf = continued_fraction_convergents(e())
n, d = next(islice(cf, 99, 100))
print(sum(int(x) for x in str(n)))

print(islice)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4, Used Build Coefficients, kenkamau, Kenya --------------------------')
# Somehow he found a way to compute directly the numerator coefficients of e from the serie
t1  = time.time()
# In python, simple and intuitive
myList = []
myList.append(1)
myList.append(2)

multiple = 0
for i in range(2, 101):
    if i % 3 == 0:
        multiple = multiple + 2
        myList.append(multiple * myList[i - 1] + myList[i - 2])
        # print(myList)
    else:
        myList.append(myList[i - 1] + myList[i - 2])
        # print(myList,'  <--- else')
print(myList)
s = str(myList[100])

suma = 0
for i in s:     suma += int(i)
print(suma)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5,  SUPER COOL, snamellit, Belgium --------------------------')
t1  = time.time()

from itertools import islice, count
from functools import reduce
from fractions import Fraction
import operator

def cont_fraction(initial, a_generator, n):
    """
    calculate the continued fraction for n levels (n>0)

    l consist of a tuple with a number followed by a generator of repeating
    a's for the continued fraction

    example:

    >>> from itertools import cycle
    >>> cont_fraction(1,cycle((2)),1)
    1
    >>> cont_fraction(1,cycle((2)),2)
    3/2
    >>> cont_fraction(1,cycle((2)),3)
    7/5
    >>> cont_fraction(1,cycle((2)),4)
    17/12
    >>> cont_fraction(1,cycle((2)),5)
    41/29

    of course we can also specify non repeating generators
    """

    a = [initial] + list(islice(a_generator, n - 1))
    a.reverse()

    return reduce(lambda x, y: Fraction(y) + Fraction(1, x), a)

def e_terms():
    c = count(2, 2)
    for x in c:
        yield 1
        yield x
        yield 1

def sum_digits_numerator_approx_e():
    approx_e = cont_fraction(2, e_terms(), 100)
    return reduce(operator.add, map(int, str(approx_e.numerator)))

sum_digits_numerator_approx_e()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 6,  chris_bandit, USA --------------------------')
t1  = time.time()
# I wrote a recursive solution taking advantage of the fraction module..
from itertools import cycle
from fractions import Fraction

def k_sieve():
    yield 2
    yield 1
    k = 1
    multipliers = cycle([2,1,1])
    while 1:
        n = next(multipliers)
        if n == 2:
            n = k * n
            k += 1
        yield n

#e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

def cf(k, terms):
    '''if we are n(terms) levels deep, then return 1/k(n+1) + k(n):
       else return k(n) + 1/cf(k(n+1)'''
    # print("called with k,terms=", k,terms)

    if terms == 1:
        return k
    elif terms == 2:
        return k + Fraction(1, next(k_terms))
    else:
        return k + Fraction(1, (cf(next(k_terms), terms - 1)))

term_num = 100
k_terms = k_sieve()
e = cf(Fraction(next(k_terms)), term_num)
print("For", term_num, "terms, e is approximately: ", e)
print("Sum of numerator is", sum(map(int, str(e.numerator)  )))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

