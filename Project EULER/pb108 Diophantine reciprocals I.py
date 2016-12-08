#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
            Diophantine reciprocals I           -          Problem 108

In the following equation x, y, and n are positive integers.

                                             1 / x  +  1 / y  =  1 / n

For n = 4 there are exactly three distinct solutions:

                                            1 / 5 + 1 / 20 = 1 / 4

                                            1 / 6 + 1 / 12 = 1 / 4

                                            1 / 8 + 1 / 8 = 1 / 4

What is the least value of n for which the number of distinct solutions exceeds one-thousand?

NOTE: This problem is an easier version of Problem 110; it is strongly advised that you solve this one first.
'''

import time
import math
from  fractions import Fraction
import gmpy2
from itertools import combinations, combinations_with_replacement
import functools, operator, gmpy2
from pyprimes import factorise

print('\n--------------------------TESTS------------------------------')

print('Check the proximity of a number to another:\t',math.isclose(4, 4.0000000001, rel_tol=10**(-14) ))
print('Check the proximity of a number to another:\t',math.isclose(4, 4.0000000001))

print(5/Fraction(6) + 3/Fraction(12))
print('\n----------------------------')




class GET_DIVISORS(object):
    '''Made by Bogdan Trif @ 2016-11-15, based on itertools.combinations module
    and with a little help on list(functools.reduce(operator.mul, i) for i in comb)

    :param nr:  int
    :return: a list with the factors ( method factorise) or divisors (method divisors)
    :Usage:  >>> GET_DIVISORS().divisors(90)    # to obtain the divisors
                 >>>  GET_DIVISORS().factorise(90)   # to obtain the factors                      '''

#     def __init__(self, nr):   # We don't want to initialize the class with a number
#     self.nr = nr

    def factorise(self, nr):
        ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''

        return [val for sublist in [[i[0]]*i[1] for i in factorise(nr)] for val in sublist]

    def divisors(self, nr):
        ''':Description: Use the itertools, functools, operator, gmpy2 modules.
        In the case of multiple calls take the module imports outside the class and load only once => improved speed. '''

        if gmpy2.is_prime(nr) == True or nr == 1 :
            return [1]    # Must be adjusted to [1] if you change on list
        else :
            all_factors =  self.factorise(nr)
            # set_factors=list(set(all_factors))
            comb= set()
            # print('all_factors:\t',all_factors)
            for i in range(1, len(all_factors)):
                c = set(combinations(all_factors, i) )
                comb.update(c)
                comb_prod = list(functools.reduce(operator.mul, i) for i in comb)
                comb_prod.sort()
        return  len(comb_prod)+2   # sum([1]+ comb_prod)   !!! Remember to change on  return [1]  for is_prime case !


def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // math.gcd(a, b)


def primitive_Diophantine(n):
    cnt = 0
    for i in range(n+1, 2*n+1):
        j = i
        while  (i*j)/(i+j) <= n :
            # print(i)
            if (i*j)/(i+j) == n:
                print('n=',n, '\t\t i=', i,'   j=' , j ,'\t' ,(i*j)/(i+j) )
                cnt+=1
            # if cnt > 20 :
            j+=1
    print('------------------------------\n')
    return  cnt


def compute_Diophantine_ways(n):
    cnt = 0
    for i in range(n+1, 2*n+1):
        j = lcm(i, n)
        # print(i)
        if (i*j)/(i+j) == n:
            print('n=',n, '\t\t i=', i,'   j=' , j ,'\t' ,(i*j)/(i+j))
            cnt+=1
        # if cnt > 20 :
    print('------------------------------\n')
    return  cnt

def get_divisors(all_factors) :
    ''':Description: Takes as argument a list of all factors of a number and returns its divisors '''
    comb= set()
    for i in range(1, len(all_factors)):
        c = set(combinations(all_factors, i) )
        comb.update(c)
        comb_prod = set(functools.reduce(operator.mul, i) for i in comb)
        # print(comb_prod)
    return len( [1]+sorted(list(comb_prod))+ [functools.reduce(operator.mul, all_factors)] )

print('\n-----------primitive_Diophantine & compute_Diophantine_ways CORRECTNESS  TESTS ----------------------\n')

print('\nTest for the Function primitive_Diophantine :\t ' ,primitive_Diophantine(210) )
print('Test for the Function compute_Diophantine_ways :\t ' ,compute_Diophantine_ways(210) )



print('\n------------------------ TESTS ----------------------')
# 2016-06-12, 16:30, I will retry later
# For some reason the answer is not    --->    Answer: 	 1024 349188840 [2, 2, 2, 3, 3, 3, 5, 7, 11, 13, 17, 19]


# test_factors = (2, 3, 5, 7, 2, 3, 2, 3, 11, 13, 17, 19)
test_factors = [2]*5+[3]*3+[5]*2+[7]+[11]+[13]+[17]
n = functools.reduce(operator.mul, test_factors)
print('Number to Test:\t',n)
print('\nTest for functools.reduce  :\t ', functools.reduce(operator.mul, test_factors), '\n')

# print('\nFunction compute_Diophantine_ways :\t',compute_Diophantine_ways( n ))

print('\nTest for the Function get_divisors :\t ' ,get_divisors(test_factors) )

print('Class Method for GET_DIVISORS().divisors :\t', GET_DIVISORS().divisors(n))

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()



primes = [2]*6+[3]*4+[5]*4+[7]*3 +[11]+[13]#+[17]
# primes=[2, 3]*3 +[5, 7] + [11, 13, 17, 19 ]
# primes=[2, 3, 5, 7, 11, 13 ]*3
# C = list(combinations_with_replacement( primes, 12) )

C = list(combinations( primes, 15) )
print('Combinations possible :\t',len(C),'\n' ,C[0:100])

def solution_comb_pb108():
    n_min, len_min, c  = 10**10, 2000, 0
    for i in range(len(C)):
        l = get_divisors(C[i])
        if l > 1000  :
            n = functools.reduce(operator.mul, C[i])
            print('Number:\t',n, len(str(n)) , '\t\t Length: ' , l,'\t\tFactors:\t', C[i])
            if  n_min > n : #and len_min > l :
                len_min = l
                n_min = n
                c = C[i]
        if i%2.5e3 == 0 : print(i)
    return print('\nAnswer: \t', len_min , n_min, c)

# solution_comb_pb108()

################## SOLUTION 2 ##################
from itertools import count
def solution_iter_pb108():
    n_min, len_min, c  = 10**10, 2000, 0
    for n in count(18378360, 510510) :
        l = GET_DIVISORS().divisors(n)
        print('Number:\t',n, len(str(n)) , '\t\t Length: ' , l,)
        if l > 1000  :
            len_min = l
            n_min = n
            return print('\nAnswer: \t', len_min , n_min , GET_DIVISORS().factorise(n))



# solution_iter_pb108()




print('\n--------------------------------------')



# Answer: 	   n= 831600 	   240
# Answer: 	   n= 5821200 	   360      2*2*2*2*3*3*3*5*5*7*7*11
# Answer: 	   n= 4233600 	   288      2*2*2*2*2*2*2*3*3*3*5*5*7*7
# Answer: 	   n= 510510 	   128       2*3*5*7*11*13*17               # Completed in : 11716.670275 ms
# Answer: 	   n= 510510 	   128       2*3*5*7*11*13*17               # Completed in : 1305.074692 ms
# Answer: 	   n= 3063060 	   288          2*2*3*3*5*7*11*13*17
# Answer: 	   n= 9699690 	   256          2*3*5*7*11*13*17*19
# Answer: 	   n= 19399380 	   384         2*2*3*5*7*11*13*17*19
# Answer: 	   n= 58198140 	   576          2*2*3*3*5*7*11*13*17*19
# Answer: 	   n= 116396280 	768        2*2*2*3*3*5*7*11*13*17*19

# Answer: 	 1024 459459000 (2, 3, 5, 7, 2, 3, 5, 2, 3, 5, 11, 13, 17)
# Answer: 	 1024 349188840 (2, 3, 5, 7, 2, 3, 2, 3, 11, 13, 17, 19)
# Answer: 	 1152 367567200 (2, 2, 2, 2, 2, 3, 3, 3, 5, 5, 7, 11, 13, 17)
# Answer: 	 1008 302702400 (2, 2, 2, 2, 2, 2, 3, 3, 3, 5, 5, 7, 7, 11, 13)
# Answer: 	 1008 245044800 (2, 2, 2, 2, 2, 2, 3, 3, 5, 5, 7, 11, 13, 17)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


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
