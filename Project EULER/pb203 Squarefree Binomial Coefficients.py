#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
            Squarefree Binomial Coefficients            -           Problem 203

The binomial coefficients C{n,k} can be arranged in triangular form, Pascal's triangle, like this:

                                                1
                                            1     1
                                         1     2     1
                                      1     3     3     1
                                   1     4     6     4     1
                                1     5    10   10    5     1
                            1     6    15    20    15    6    1
                         1     7   21    35    35    21   7     1

                                           .........

It can be seen that the first eight rows of Pascal's triangle contain twelve distinct numbers: 1, 2, 3, 4, 5, 6, 7, 10, 15, 20, 21 and 35.

A positive integer n is called squarefree if no square of a prime divides n.
Of the twelve distinct numbers in the first eight rows of Pascal's triangle, all except 4 and 20 are squarefree.
The sum of the distinct squarefree numbers in the first eight rows is 105.

Find the sum of the distinct squarefree numbers in the first 51 rows of Pascal's triangle.


'''
import time, math
from pyprimes import factorise

def prime_generator(lower, upper):      ### o(^_^)o  FASTEST  o(^_^)o  ###  HIghly Efficient !!!
    """  Sieve of Eratosthenes              !!!!!!!!! THE FASTEST SIEVE. It won the battle with sieve
    Create a candidate list within which non-primes will be marked as None.         """
    cand = [i for i in range(3, upper + 1, 2)]
    end = int(upper ** 0.5) // 2

    # Loop over candidates (cand), marking out each multiple.
    for i in range(end):
        if cand[i]:
            cand[cand[i] + i::cand[i]] = [None] * ( (upper // cand[i]) - (upper // (2 * cand[i])) - 1 )

    # Filter out non-primes and return the list.
    return [2] + [ i for i in cand if i and i > lower ]


def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''

    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]


print('\n--------------------------TESTS------------------------------')

def generate_Pascal_Triangle(row_nr) :
    '''**©** Made by Bogdan Trif @ 2016-12-20, 21:20.

        :Description: Generates the Pascal Triangle , Binomial Coefficients
        :param row_nr: int, the row number, int
        :return: nested list, matrix in the form of Pascal's Triangle       '''
    blueprint = [1]*(row_nr+1)
    Pascal= [blueprint]
    for i in range(row_nr) :
        tmp=[]
        for j in range(0, row_nr-i) :
            tmp.append(sum(Pascal[-1][0:j+1]) )
        # print(tmp)
        Pascal.append(tmp)
    return Pascal




P = prime_generator(2, 10**2)

def square_free_nr(n):
    for i in P :
        if (n / i**2) % 1 == 0 :
            return False
    return True

print('\nTest for the function square_free_nr :  ', square_free_nr(16))
print('Test for the function square_free_nr :  ', square_free_nr(6) ,'\n')

# print('\n-------------- AUTOMATED TESTS -----------------')
# for i in range(1,300) :
#     print(i, square_free_nr(i), '   ', get_factors(i))

print('\n================  My FIRST SOLUTION, VERY FAST  ===============\n')
t1  = time.time()

print('\n-----------Pascal s Triangle --------------' )

S = 0
Pasc = generate_Pascal_Triangle(50)
# print(Pasc,'\n')

L = set([val for sublist in Pasc for val in sublist])
# print(L, sum(L),'\n')

for n in L:
    if square_free_nr(n) :
        S+= n
        # print(n, end=' ,  ' )

print('\n\nSum = ', S)          # Sum =  34029210557338













t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()

# ==== Tue, 8 Nov 2016, 19:34, mbh038, England
# About 4 ms in Python.
# I use recursion to find the Combinations{n, k}, but could have used factorials directly at about the same speed.

def mbh038(rows):
    t=time.clock()
    sfs=set()
    for n in range(rows):
        for k in range(n+1):
            c=nCk(n,k)
            if squareFree(c):
                sfs.add(c)
    print(sum(sfs),time.clock()-t)

def nCk(n,k,memo={}):
    """returns n Choose k"""
    if n<k:
        return 0
    if n==0 or k==0 or k==n:
        return 1
    try:
        return memo[(n,k)]
    except KeyError:
        result=nCk(n-1,k-1,memo)+nCk(n-1,k)
        memo[(n,k)]=result
    return result

def squareFree(n):
    """returns True if n is square-free, False if not"""
    i = 2
    factors = set()
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            if i in factors:
                return False
            factors.add(i)
    if n > 1:
        if n in factors:
            return False
    return True

# mbh038(51)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

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
