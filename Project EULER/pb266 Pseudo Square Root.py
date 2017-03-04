#!/usr/bin/python                   o(^_^)o
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
Pseudo Square Root      -       Problem 266

The divisors of 12 are: 1,2,3,4,6 and 12.
The largest divisor of 12 that does not exceed the square root of 12 is 3.
We shall call the largest divisor of an integer n that does not exceed the square root of n the pseudo square root (PSR) of n.

It can be seen that PSR(3102)=47.

Let p be the product of the primes below 190.
Find PSR(p) mod 10**16.


'''
import time, math
import operator, functools

def prime_generator(lower, upper):      #THIRD FASTEST
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
    from pyprimes import factorise
    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]

def get_divisors(n):      ### ( ͡° ͜ʖ ͡°)  FASTEST  ( ͡° ͜ʖ ͡°)  ### !! FIRST FASTEST
    from math import sqrt
    factors = set()
    for x in range(1, int(sqrt(n)) + 1):
        if n % x == 0:
            factors.add(x)
            factors.add(n//x)
    return sorted(factors)

P_primes = prime_generator(1,190)
print(len(P_primes) ,P_primes)



# Q : How to find the divisors of a very huge number ?
# Q2 : How to find the midle divisor, closest to the square root ?
# A2 : You try to equilibrate all the factors. For example : in 3102 with factors [2,3,11, 47]
# they are best equilibrated wheh  pair 1 is [2*3*11] = 66   and pair 2 is 47 .  abs(diff) = 66-47 = 19
# No other pairs can have a smaller diff :



print('\n--------------------------TESTS------------------------------')
t1  = time.time()

p = functools.reduce( operator.mul , P_primes )
print('p : \t' ,len(str(p)), p, '\n' )


div = get_divisors(3102)
# for i in div :     print(i, 3102% i)

print(div)
print('get_factors : \t',get_factors(3102 ))


# square = math.floor( p**(1/2) )
# for i in range(square, 100, -1):
#     print(i, p%i )
#     if p%i ==0 :
#         print(i, '              ' ,p%i,'     THIS IS IT !!!' )
#         break
print(get_divisors( 2*3*5*7*11*13*17*19*23*29*31 ))

def build_pairs( ordered_lst ) :
    pair1, pair2 = [], []
    for i in range( len(ordered_lst)//2 ) :
        if len(pair1) %2 == 0 :
            pair1.append( ordered_lst[2*i] )
            pair2.append( ordered_lst[2*i+1] )
        else :
            pair1.append( ordered_lst[2*i+1] )
            pair2.append( ordered_lst[2*i] )
    return pair1, pair2


BP = build_pairs(P_primes)
print('\nbuild_pairs : \t ',  BP )

p1 = functools.reduce( operator.mul , BP[0] )
p2 = functools.reduce( operator.mul , BP[1] )
print(' p1, p2, diff : \t', p1, p2, abs(p1-p2), len(str(p1)), len(str(p2)), len(str(abs(p1-p2))) )
print( 'sqrt(P): \t',len(str(round(math.sqrt(p)))), round(math.sqrt(p)) )
print(p1 < p2,  )

# I must balance the two pairs and I need a good algorithm
# https://www.youtube.com/watch?v=s6FhG--P7z0
# It is called BALANCED PARTITION PROBLEM !
# http://algorithmsandme.in/2014/04/balanced-partition-problem/

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
