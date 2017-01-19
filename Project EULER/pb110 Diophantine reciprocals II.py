#!/usr/bin/python
# Solved by Bogdan Trif    ( ͡° ͜ʖ ͡°)     @
#The  Euler Project  https://projecteuler.net
'''
            Diophantine reciprocals II          -           Problem 110

In the following equation x, y, and n are positive integers.
                    1 / x  +  1 / y  =  1 / n

It can be verified that when n = 1260 there are 113 distinct solutions and this is the least value of n
for which the total number of distinct solutions exceeds one hundred.

What is the least value of n for which the number of distinct solutions exceeds four million (4*10**6)   ?

NOTE: This problem is a much more difficult version of Problem 108 and as it is well beyond the limitations
of a brute force approach it requires a clever implementation.


'''
import time
import functools, operator
import functools, operator
from pyprimes import factorise

def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    from pyprimes import factorise
    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]

def  calculate_divisors(nr):
    '''**©** Made by Bogdan Trif @ 2016-12-08, 16:30.
        :Description: Functions which computes the number of divisors of a number.
                It uses the Numbers of Divisors Theorem :which says : if N=a**x*b**y*c**z => divisors_nr=(x+1)(y+1)(z+1)
            Example: N = 216 = 2**3 * 3**3 => divisors_nr = (3+1)(3+1) = 16
    :param nr: int, nr
    :return: int, divisors_number    '''

    def factors(nr):
        ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
        return [i for i in factorise(nr)]
    N = factors(nr)
    return  functools.reduce( operator.mul , [ (i[1]+1) for i in N ])


def Diophantine_Reciprocals(n):
    ''':Description: Function to get the Reciprocals of the Diophantine Equation **1/x  +  1/y  =  1/n**
    :param n:   n from Diophantine Eqn
    :return: int, the number of reciprocals    '''
    count = 0
    nsquared = n**2
    for i in range(1, n+1):
        if nsquared % i == 0:
            count += 1
    return count


print('\n--------------------------TESTS------------------------------')
t1  = time.time()


# L = [2, 19, 3,  5, 7, 11, 13 , 5 ,2, 17 ]
# n = functools.reduce(operator.mul, L )
n = 510510*2
print('Number to test : ', n)

print('\n Test for get_factors() Function :', get_factors(n))

print(' Diophantine_Reciprocals Function :\t' , Diophantine_Reciprocals(n) )
print(' calculate_divisors Function :\t' , calculate_divisors(n) )


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()



import pyprimes
import sympy

def aolea_sol(n=10**3) :

    listResult = [2]
    divisors = 3
    solutions = 2
    flag = False
    i1 = 2
    while flag == False:
        listResult.append(pyprimes.nth_prime(i1))
        num = 1
        for i in listResult:
            num = num*i
        divisors = len(list(sympy.divisors(num**2)))
        solutions =(divisors-1)/2 + 1
        k1, k2, k3, k4 = 0 ,0, 0, 0
        if solutions > n:
            while   k1+1<= len(listResult) and listResult[-1] > listResult[k1]*listResult[k1+1] and int(round(solutions*25/27))>=n :
                    listResult.pop()
                    listResult.append(pyprimes.nth_prime(k3+1))
                    listResult.append(pyprimes.nth_prime(k3+2))
                    k3 = k3 + 2
                    k1 = k1 + 4
                    num = 1
                    for i in listResult:
                        num = num * i
                    divisors = len(list(sympy.divisors(num ** 2)))
                    solutions = (divisors - 1) / 2 + 1
                    listResult=sorted(listResult)
            while   k2+1<= len(listResult) and listResult[-1] > listResult[k2]*listResult[k2+1] and int(round(solutions*49/75))>= n :
                    listResult.pop()
                    listResult.append(pyprimes.nth_prime(k4+1))
                    listResult.append(pyprimes.nth_prime(k4+2))
                    k4 = k4 + 2
                    k2= k2 + 4
                    num = 1
                    for i in listResult:
                        num = num * i
                    divisors = len(list(sympy.divisors(num ** 2)))
                    solutions = (divisors - 1) / 2 + 1
                    listResult = sorted(listResult)
            print(n, 'Number : ',num, '       Solutions :',solutions, '    Divisors:',divisors,       '             List', listResult)
            flag = True
        i1 = i1 + 1

aolea_sol(n = 4*10**6)

# Answer : 4000000 Number :  9350130049860600
# Solutions : 4018613.0     Divisors: 8037225              List [2, 2, 2, 3, 3, 3, 5, 5, 7, 7, 11, 13, 17, 19, 23, 29, 31, 37]

t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')              Completed in : 115694.617271 ms


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
