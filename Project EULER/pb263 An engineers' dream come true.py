#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @     Completed on Thu, 16 Mar 2017, 13:43
#The  Euler Project  https://projecteuler.net
'''
                        An engineers' dream come true           -               Problem 263

Consider the number 6. The divisors of 6 are: 1,2,3 and 6.
Every number from 1 up to and including 6 can be written as a sum of distinct divisors of 6:
1=1, 2=2, 3=1+2, 4=1+3, 5=2+3, 6=6.
A number n is called a practical number if every number from 1 up to and including n can be expressed as a sum of distinct divisors of n.

A pair of consecutive prime numbers with a difference of six is called a sexy pair (since "sex" is the Latin word for "six").
The first sexy pair is (23, 29).

We may occasionally find a triple-pair, which means three consecutive sexy prime pairs, such that the second member of each pair is the first member of the next pair.

We shall call a number n such that :

(n-9, n-3), (n-3,n+3), (n+3, n+9) form a triple-pair, and
the numbers n-8, n-4, n, n+4 and n+8 are all practical,
an engineers’ paradise.

Find the sum of the first four engineers’ paradises.

'''
import time, zzz

def numpy_prime_sieve(n):          ### o(^_^)o  FASTEST  o(^_^)o  ###  Highly Efficient !!!
    import numpy as np
    """return array of primes 2<=p<=n"""
    sieve=np.ones( n+1, dtype=bool )
    for i in range( 2, int((n+1)**0.5+1) ) :
        if sieve[i] :
            sieve[2*i :: i] = False
    return np.nonzero(sieve)[0][2:]

def prime_sieve(n):       # SECOND FASTEST        o(^_^)o
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[ i*i :: 2*i ] = [False] * ( (n-i*i-1) // (2*i) +1 )
    return [2] + [i for i in range(3, n , 2) if sieve[i] ]

def get_divisors(n):      ### ( ͡° ͜ʖ ͡°)  FASTEST  ( ͡° ͜ʖ ͡°)  ### !! FIRST FASTEST
    from math import sqrt
    factors = set()
    for x in range(1, int(sqrt(n)) + 1):
        if n % x == 0:
            factors.add(x)
            factors.add(n//x)
    return sorted(factors)

import numpy
def primesfrom3to(n):
    """ Returns a array of primes, 3 <= p < n
    http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188 """
    sieve = numpy.ones(n//2, dtype=numpy.bool)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = False
    return 2*numpy.nonzero(sieve)[0][1::]+1

def binary_search(n, List):        # VERY FAST ALGORITHM
    ''':Description: Search for an element in the list and returns the index of it. If it not finds it returns
        the index of the element closest to its left, the smaller number.
    :param: **n**- integer, the number to find
                **List** - lst type, the list to search for
    :returns:   int, the index of the element
    '''
    left = 0
    right = len(List) -1

    while left <= right:
        midpoint = (left+right)//2
        if List[midpoint] == n: return midpoint
        elif List[midpoint] > n: right = midpoint-1
        else: left = midpoint+1
    if n > List[midpoint]: return midpoint
    else: return (midpoint-1)


def  isSubsetSum(sett , n,  suma ) :        ## ( ͡° ͜ʖ ͡°)  FASTEST  ( ͡° ͜ʖ ͡°)  ### !! FIRST FASTEST
                                                                    ## !!!!!!!! ALGORITHM FAR MORE EFFICIENT !!!!!!
   # // Base Cases
    if (suma == 0) :
        return True
    if (n == 0 and suma != 0 ):
        return False;

   # // If last element is greater than sum, then ignore it
    if (sett[n-1] > suma) :
        return isSubsetSum(sett, n-1, suma)

   # /* else, check if sum can be obtained by any of the following
   #    (a) including the last element
   #    (b) excluding the last element   */
   #  return isSubsetSum(sett, n-1, suma)
    return isSubsetSum(sett, n-1, suma-sett[n-1] )

def divisor_sum_sigma(n):
    '''     Π  = [(p_1**(a_1+1)-1) / (p_1 -1)]*...*[ (p_k**(a_k+1)-1) / (p_k -1) ]
     condensed :   Π  {p_k - prime, a_k - the exp of the prime } =  ((p_k**(a_k+1)-1) / (p_k -1)
    where p_1, p_2,...p_k are the prime factors of the number , together with their
    corresponding coefficients exponentials a_1, a_2,...,a_k
    :param n: int, number
    :return: int, sigma2 representing the Sum of its divisors !              '''
    # https://en.wikipedia.org/w/index.php?title=Divisor_function&action=edit&section=4
    from pyprimes import factorise
    import functools, operator
    D = list(factorise (n ))
    P = [( i[0]**(i[1]+1)-1 ) //(i[0]-1) for i in D ]
    # print(D)
    return functools.reduce(operator.mul, P)

def practical_number_mechanical(n):         # Highly Inneficient, It's BRUTE FORCE, term by term
    L = get_divisors(n)
    D = set(L)
    # print(L)
    for i in range(2, n) :
        if i in D : continue
        ind = binary_search(i, L)
        tmp = L[:ind+1]
        if isSubsetSum(tmp, len(tmp), i) == False :
            return False
        # print(i,'     ', ind,'    ',L[ind], '    ', tmp)
    return True


def practical_number(n):
    ''':Observation: Depends on the square sum of divisors - sigma function
    p_i <= 1 + σ(p_1**a_1 * p_2**a_2 * ... * p_(i-1)**a_(i-1) ) =
        1 + Π {j=1 , i-1} (p_j**(a_j+1)-1) / (p_j -1)]
     condensed :  = 1 + Π {j=1 , i-1} (p_j**(a_j+1)-1) / (p_j -1)]
    where p_1, p_2,...p_i are the prime factors of the number , together with their
    corresponding coefficients exponentials a_1, a_2,...,a_i
    where σ denotes the sum of the divisors of x.
    :For example: , 2 × 32 × 29 × 823 = 429606 is practical, because the inequality above
    holds for each of its prime factors: 3 ≤ σ(2) + 1 = 4, 29 ≤ σ(2 × 32) + 1 = 40,
    and 823 ≤ σ(2 × 32 × 29) + 1 = 1171.
    :param n: int, number
    :return: int, sigma2 representing the Sum of its divisors !              '''
    # https://en.wikipedia.org/w/index.php?title=Practical_number&action=edit&section=1

    from pyprimes import factorise
    import functools, operator
    if n%2 == 1 : return False

    D = list(factorise (n ))
    # print(D)
    for I in range(1,len(D)):
        sg = functools.reduce(operator.mul, [ l[0]**l[1] for l in D[:I] ] )
        sigma = divisor_sum_sigma (sg) +1
        # print(D[I], D[:I],'    compare :', D[I][0]  , sigma )
        if ( D[I][0] <= sigma ) == False :
            return False

    return True




# print('practical_number_mechanical : \t', practical_number_mechanical(35))
# print('practical_number_mechanical : \t', practical_number_mechanical(36))
print('\npractical_number_mechanical : \t', practical_number_mechanical(5382))
print('practical_number : \t', practical_number(5382))

# @2017-03-15, 23:48 - I need to find the properties of PRACTICAL NUMBERS. The algorithm, the function is TOO SLOW
# Need to find shortcut, formula :
# http://planetmath.org/practicalnumber
# http://mathworld.wolfram.com/PracticalNumber.html
# https://oeis.org/A005153
# https://en.wikipedia.org/wiki/Practical_number
# https://en.wikipedia.org/w/index.php?title=Practical_number&action=edit&section=1

print('\n--------------------------TESTS------------------------------')
t1  = time.time()

# test_array, test_nr = [ 1, 2, 3 , 6, 9  ], 21
test_array, test_nr = [1, 2, 3, 6, 9, 13, 18, 23, 26, 39, 46, 69, 78, 117, 138, 207, 234, 299, 414, 598, 897, 1794, 2691], 4593
print('\nsubsetsum : \t', isSubsetSum( test_array , len(test_array) ,test_nr ))
print('subset_sum : \t', isSubsetSum( test_array , len(test_array) ,test_nr ),'\n')

def mechanical_brute_force_check_practical_numbers(rng) :
    for i in range(2, rng ) :
        # if practical_number_mechanical(i) != practical_number(i)  :
        print (str(i)+ '.        mechanical practical nr : ', practical_number_mechanical(i) , practical_number(i),'    <-smart fnct ')

# mechanical_brute_force_check_practical_numbers(10**3)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n================   FIRST BRUTE FORCE SOLUTION, 4 min  ===============\n')
t1  = time.time()


from collections import deque

def brute_force_solution ( up_prime):

    # P = primesfrom3to(10**10)
    P = primesfrom3to( int( up_prime ) )
    print(P[:10],'\n')

    S, scnt, cnt  = 0, 0, 0
    cache = deque([2, 3, 5, 7])
    for p in P :
        cache.append(p)
        # cache.pop(0)
        cache.popleft()
        a, b, c, d = cache
        if a+18 == b+12 == c+6 == d :
            cnt += 1
            n = a+9
            V = [ n-8, n-4, n, n+4, n+8 ]       # practical numbers
            if cnt %10**3 == 0 : print(str(cnt)+'.       ',  cache ,'       ', n)

            counter = 0
            for i in V :
                if practical_number(i) == False : break
                if practical_number(i) == True : counter +=1
            if counter == 5 :
                scnt += 1
                S +=n
                print(str(scnt)+'.       triple pair : ', cache, '      Practical :  ', V,'     n=', n )

        if scnt == 4 : break

    return print('\nAnswer : \t ', S)

brute_force_solution(1.5*10**9)             #   Answer : 	  2039506520


t2  = time.time()
print('\nCompleted in :', round((t2-t1)/60 , 6), 'min\n\n')              # Completed in : 218.929522 s

zzz.Star_Wars()

# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 3,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 4,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
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
#
# print('\n--------------------------SOLUTION 7,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 8,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 9,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 10,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 11,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 12,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

