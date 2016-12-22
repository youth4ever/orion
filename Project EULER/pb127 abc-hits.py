#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
abc-hits        -       Problem 127

The radical of n, rad(n), is the product of distinct prime factors of n. For example, 504 = 23 × 32 × 7, so rad(504) = 2 × 3 × 7 = 42.

We shall define the triplet of positive integers (a, b, c) to be an abc-hit if:

1.      GCD(a, b) = GCD(a, c) = GCD(b, c) = 1
2.      a < b
3.      a + b = c
4.      rad(abc) < c
For example, (5, 27, 32) is an abc-hit, because:

1.      GCD(5, 27) = GCD(5, 32) = GCD(27, 32) = 1
2.      5 < 27
3.      5 + 27 = 32
4.      rad(4320) = 30 < 32

It turns out that abc-hits are quite rare and there are only thirty-one abc-hits for c < 1000, with ∑c = 12523.

Find ∑c for c < 120000.

'''
import time, gmpy2
from math import gcd, log
from pyprimes import factorise
import sympy, numtheory


print(' Test the power', gmpy2.is_prime(491 ) )


def get_factors(n):
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]

def prime_generator(n):         # HIghly Efficient !!!!         THE FASTEST, The BEST , The ONE
    """  Sieve of Eratosthenes              !!!!!!!!! THE FASTEST SIEVE. It won the battle with sieve
    Create a candidate list within which non-primes will be marked as None.
    """
    cand = [i for i in range(3, n + 1, 2)]
    end = int(n ** 0.5) // 2

    # Loop over candidates (cand), marking out each multiple.
    for i in range(end):
        if cand[i]:
            cand[cand[i] + i::cand[i]] = [None] * ( (n // cand[i]) - (n // (2 * cand[i])) - 1 )

    # Filter out non-primes and return the list.
    return [2] + [i for i in cand if i]


# def  abc-hit()

print('\n--------------------------TESTS------------------------------')
P = prime_generator(120000)
print(len(P), P[-100::],'\n')
print('Factorise Test :  ', list(factorise(32)) )

print('There are exactly C{11414,3}: ' , gmpy2.comb(11414, 3),'   unique combinations' )
print('There are exactly C{11414,2}: ' , gmpy2.comb(11414, 2),'   unique combinations' )



# cnt=0
# for n in range(2, 1000) :
#     if gmpy2.is_prime(n) == False:
#         f = list(factorise(n))
#         # print( f  )
#         if len(f) == 3 :
#             a, b, c = pow(f[0][0], f[0][1] ) , pow(f[1][0], f[1][1] ) , pow(f[2][0], f[2][1] )
#             # cnt+=1
#             # print(str(cnt)+'.  ', a,  b, c ,'    ' , f, '    ' ,n)
#             if gcd(a,b) == gcd(a,c) == gcd(b,c) == 1 :
#                 # cnt+=1
#                 # print(str(cnt)+'.  ', a,  b, c ,'    ' , f, '    ' ,n)
#                 if a< b and a+b == c :
#                     cnt+=1
#                     print(str(cnt)+'.  ', a,  b, c ,'    ' , f, '    ' ,n)
# print()


prm = prime_generator(350)
def find_base_pwr(n, prm):
    ''':Description: Returns a tuple in the form (base, power). Depends on pre-generated primes up to sqrt(n)
            :param: **n**  - int, searching for number
            :param: **prm**  - the list of primes generated before
            :return: tuple(base, power)    '''
    # prm = [2,3,5,7,11]
    for i in prm :
        if  0 <= abs( log(n , i) - round(log(n , i)) ) %1 <= 1e-9 :
            return i, round(log(n , i))
    return n

print('Test for the function find_base_pwr :\t',find_base_pwr(815730721, prm) )
print('Test for the function find_base_pwr :\t',find_base_pwr(17**4, prm) ,'\n')


def rad_abc( a, b, c ):
    ''':Description: Scope: a,b,c - must be primes or primes raised to some power. Otherwise do not apply
           Deppends on the function  find_base_pwr  which finds the logarithm of a power number (non-composite) '''
    if gmpy2.is_prime(a) == True : x = a
    else :  x = find_base_pwr(a, prm)[0]
    if gmpy2.is_prime(b) == True : y = b
    else :  y = find_base_pwr(b, prm)[0]
    if gmpy2.is_prime(c) == True : z = c
    else :  z = find_base_pwr(c, prm)[0]
    return x* y* z

print('Test for the rad_abc Function : \t ',rad_abc( 89**2, 3**7, 11**3  ) )
print('Test for the rad_abc Function : \t ',rad_abc( 2, 241, 243  ) )
print('Test for the rad_abc Function : \t ',rad_abc( 5, 32, 27  ) )

# OBSERVATIONS :
# 1. c must be a prime power, So we must first generate all the numbers up_to range which are powers
# 2. 2 --> 2**16,   3 --> 3**10, 5 ---> 5**7 , 7--> 7**6
# 3 . There are exactly :  247769701764    unique combinations, We need to REDUCE IT !!!
# 4. Actually we make only 2 COMBINATIONS !, which reduces the number to :  65.133.991 combinations !, more aceptable
# So we go now with a & b with a < b
# 5. We further reduce to 30.000.000 combinations by applying a+b < ap_range

print('\n------------ Construction of the Initial List------------\n')
up_range = int(1.0*10**3)
AB = prime_generator(up_range)
print(len(AB) , AB)
C = set()
for i in AB :
    c = i
    while c* i < up_range :
        c *= i
        C.add( c  )

# C.sort()
print(len(C), C)
# C_set= set(C)
# print(len(C_set), C_set)

print('---------------------------\n')
t1  = time.time()
cnt , S = 0, 0
for a in range(len(AB)):
    for b in range(a+1 ,len(AB)):
        # cnt+=1
        # print(str(cnt)+'.      a=' , AB[a],' ;  b=' ,AB[b]   )
        c = AB[a]+AB[b]
        if c >= up_range  : break
        # # if gcd( C[a], C[b]) == 1 :
        if c in C :
                if gcd (AB[a], c ) == 1 and gcd (AB[b], c ) == 1 :
                    # if rad_abc(AB[a], AB[b], c) < c :
                        cnt+=1
        #                 S += c
        #                 print(str(cnt)+'.      a=' , AB[a],' ;  b=' ,AB[b],'  ;        c= ' ,c ,   '      '   ,'   ;    rad: ' ,rad_abc(AB[a], AB[b], c))
                        print(str(cnt)+'.      a=' , AB[a],' ;  b=' ,AB[b],'  ;        c= ' ,c ,   '      '  )


print('\n\nAnswer :\t', S)
# with if gcd( C[a], C[b]) == 1 :
# 22643.     54163 65536 119699
# 22644.     54277 65536 119813
# without :
# 22643.     54163 65536 119699
# 22644.     54277 65536 119813


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


# print('\n-------------- Search Testing -----------')
#
# t1  = time.time()
#
# print('Test Search list', 745 in C)
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# t1  = time.time()
#
# print('Test Search set', 745 in C_set)
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')




print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()
















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
