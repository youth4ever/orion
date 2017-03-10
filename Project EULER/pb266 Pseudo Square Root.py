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
import  itertools
from functools import reduce
from operator import mul

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

def binary_search(n, List, direction ):        # VERY FAST ALGORITHM
    ''':Description: Search for an element in the list and returns the index of it. If it not finds it returns
        the index of the element closest to its left, the smaller number.
        :OBSERVATION:  direction argument +1 means to the right ; -1 to the left
    :param: **n**- integer, the number to find
                **List** - lst type, the list to search for
    :returns:   int, the index of the element               '''
    if direction == -1 : alpha = 0
    if direction == 1 : alpha = +1

    left = 0
    right = len(List) -1

    while left <= right:
        midpoint = (left+right)//2
        if List[midpoint] == n: return midpoint
        elif List[midpoint] > n: right = midpoint-1
        else: left = midpoint+1
    if n > List[midpoint]: return midpoint + alpha
    else: return (midpoint-1+alpha )

P_primes = prime_generator(1,190)
print(len(P_primes) ,P_primes)



# Q : How to find the divisors of a very huge number ?
# Q2 : How to find the midle divisor, closest to the square root ?
# A2 : You try to equilibrate all the factors. For example : in 3102 with factors [2,3,11, 47]
# they are best equilibrated wheh  pair 1 is [2*3*11] = 66   and pair 2 is 47 .  abs(diff) = 66-47 = 19
# No other pairs can have a smaller diff :

print('\n-------------------------- TESTS  ------------------------------')

# p = reduce( mul , P_primes )
# print('p : \t' ,len(str(p)), p, '\n' )


div = get_divisors(3102)
# for i in div :     print(i, 3102% i)

print(div)
print('get_factors : \t',get_factors(3102 ))


def build_pairs( ordered_lst ) :
    pair1, pair2 = [], []
    for i in range( len(ordered_lst)//2 ) :
        if len(pair1) %2 == 0 :
            pair1.append( ordered_lst[2*i] ) ;
            pair2.append( ordered_lst[2*i+1] )
        else :
            pair1.append( ordered_lst[2*i+1] )
            pair2.append( ordered_lst[2*i] )
    return pair1, pair2


BP = build_pairs(P_primes)
print('\nbuild_pairs : \t ',  BP )

# p1 = reduce( mul , BP[0] )
# p2 = reduce( mul , BP[1] )
# print(' p1, p2, diff : \t', p1, p2, abs(p1-p2), len(str(p1)), len(str(p2)), len(str(abs(p1-p2))) )
# print( 'sqrt(P): \t',len(str(round(math.sqrt(p)))), round(math.sqrt(p)) )
# print(p1 < p2,  )

# I must balance the two pairs and I need a good algorithm
# It is called BALANCED PARTITION PROBLEM !
# http://algorithmsandme.in/2014/04/balanced-partition-problem/


print('\n--------------------------BRUTE FORCE  TESTING ------------------------------')
t1  = time.time()

test_A =  [2,3,5,7,11,13,17,19,23,29, 31,37]
sqr = (reduce(mul, test_A) )**(1/2)

def brute_force_testing( lst, sqr ) :
    A, B = 0, 0
    C = list(itertools.combinations(test_A, len(test_A)//2   ))
    print(len(C))

    mmin = 10**8
    for i in C :
        r = reduce(mul, i)
        if abs(sqr - r) <= mmin :
            mmin = abs(sqr - r)
            print(r , i , sqr-r , '    ', sqr)
            A, B = i, list( set(lst)-set(i) )
    return A, B

A, B = brute_force_testing(test_A, sqr )

print('\n',A, B)
a, b = reduce(mul, A), reduce(mul, B)
print('\nList 1 : \t' , a, len(str(a)), '\nList 2 : \t' ,  b , len(str(b)) ,'\nDIFF = \t' ,abs(a-b), len(str(abs(a-b))) )
print( 'sqrt(test_A): \n',len(str(round(sqr) )), round(sqr) )


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

P_primes = prime_generator(1,190)
print(len(P_primes) ,P_primes)

W = [ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37 ]
sqroot = reduce(mul, W)

# def balanced_pair_lists_products(lst ) :
#     U = lst[ : len(lst)//2 ]
#     V = lst[  len(lst)//2 : ]
#     print('Initial lists : \nList 1 :\t',U, '\nList 2 : \t',V,'\n')
#     REF = 10**48
#     for zz in range(2) :
#         print('\n ++++++++++  Main Iteration : ', zz ,'   +++++++++++')
#         u, v = reduce(mul, U), reduce(mul, V)
#         if u < v :
#             i = 0
#             while u < v :       # CASE  1
#                 t = binary_search( U[i] ,V , 1)
#
#                 if t >= len(V)  :
#                     print('Special : ' ,t, '   ',i ,V[i])
#                     t = binary_search( U[i] ,V , -1 )
#                 # if  U[i] < V[t] :
#                 print( '\nList 1 : ' , i, U[i] ,  '        List 2 : ' ,t, V[t]  , '  <------------ CASE 1','       ' )
#                 print('',U, reduce(mul, U) ,'        ',V  , reduce(mul, V), '        ', REF )
#                 temp_U = U[:] ; temp_U.remove(U[i] ) ; temp_U.append(V[t]) ; temp_U.sort()
#                 temp_V = V[:] ; temp_V.remove(V[t]) ; temp_V.append(U[i]) ; temp_V.sort()
#                 u_temp, v_temp = reduce(mul, temp_U), reduce(mul, temp_V)
#
#                 if (abs( u_temp - v_temp ) <  abs( u - v ) ) :
#                     # if (abs( u_temp - v_temp ) < REF) :
#                     U, V = temp_U[:], temp_V[:]
#                     REF = abs( u_temp - v_temp )
#                     print(U, reduce(mul, U) ,'        ',V  , reduce(mul, V) , '        ', REF)
#                     u, v = reduce(mul, U), reduce(mul, V)
#
#
#                 i+=1
#                 if i >=len(U) : break
#
#
#         if u > v :      #CASE 2
#             i = 0
#             while u > v :
#                 t = binary_search( V[i] ,U , 1 )
#                 if t >= len(V)  :
#                     print('Special : ' ,t, '   ',i ,V[i])
#                     t = binary_search( V[i] ,U , -1 )
#                 print( '\nList 1 : ' , t, U[t] ,  '        List 2 : ' ,i, V[i]  , '  <------------ CASE 2','       ' )
#                 print('',U, reduce(mul, U) ,'        ',V  , reduce(mul, V),  '        ', REF )
#                 temp_U = U[:] ; temp_U.remove(U[t] ) ; temp_U.append(V[i]) ; temp_U.sort()
#                 temp_V = V[:] ; temp_V.remove(V[i]) ; temp_V.append(U[t]) ; temp_V.sort()
#                 u_temp, v_temp = reduce(mul, temp_U), reduce(mul, temp_V)
#
#                 if (abs( u_temp - v_temp ) <  abs( u - v ) ) :
#                     # if (abs( u_temp - v_temp ) < REF) :
#                     U, V = temp_U[:], temp_V[:]
#                     REF = abs( u_temp - v_temp )
#                     print(U, reduce(mul, U) ,'        ',V  , reduce(mul, V) , '        ', REF )
#                     u, v = reduce(mul, U), reduce(mul, V)
#
#                 i+=1
#                 if i >= len(V) : break
#     return U , V

# A, B = balanced_pair_lists_products(W)
# A, B = balanced_pair_lists_products(P_primes)

def rotate(l, n):     return l[-n:] + l[:-n]


def balanced_pair_lists_products(lst , alpha) :
    U = lst[ : len(lst)//2 ]
    V = lst[  len(lst)//2 : ]
    print('Initial lists : \nList 1 :\t',U, '\nList 2 : \t',V,'\n')
    DIFF, A, B = 10**48, [], []
    u, v = reduce(mul, U), reduce(mul, V)
    key=[   -2, -1, 1, 2, 3 ]
    Cyc = itertools.cycle(key)
    for loop in range(18) :
        c = next(Cyc)
        U = rotate(U, -2)

        for lup in range(alpha) :
            # print(U, reduce(mul, U) ,'        ',V  , reduce(mul, V) , '        ', REF )
            a, b = U[0], V[0]
            # if a < b :
            t_U = U[:] ; t_U.remove(a ) ; t_U.insert(0, b)
            t_V = V[:] ; t_V.remove(b ) ; t_V.insert(0, a)
            u_check, v_check = reduce(mul, t_U), reduce(mul, t_V)
            val = abs(u_check - v_check)
            # if  val < abs(u-v)  :
            U, V = t_U[:], t_V[:]
            u, v = reduce(mul, U), reduce(mul, V)

            # if a > b  :
            #     t_U = U[:] ; t_U.remove(a ) ; t_U.insert(0, b)
            #     t_V = V[:] ; t_V.remove(b ) ; t_V.insert(0, a)
            #     u_check, v_check = reduce(mul, t_U), reduce(mul, t_V)
            #     val = abs(u_check - v_check)
            #     # if  val < abs(u-v)  :
            #     U, V = t_U[:], t_V[:]
            #     u, v = reduce(mul, U), reduce(mul, V)

            if abs(u-v) < DIFF :
                DIFF = abs(u-v)
                A, B = U[:], V[:]
            d = next(Cyc)
            V = rotate(V, -1)
            print(U, reduce(mul, U) ,'        ',V  , reduce(mul, V) , '        ', DIFF )

    return sorted(A), sorted(B), DIFF
# !!! MUST CORRECT THE ALGORITHM !!! @ 2017-03-07, I will try next to rotate one of the list
# compare them and then switch elements between the two !
# balanced_pair_lists_products(W)

A, B, DIFF = balanced_pair_lists_products(P_primes, 16 )

# THE RESULT SHOULD BE  :   [2, 5, 11, 23, 29, 37)]           [3, 7, 13, 17, 19, 31]
print('\n Answer : \n',A, '\n' ,B, '\n',DIFF)

a, b = reduce(mul, A), reduce(mul, B)
print('\nList 1 : \t' , a, len(str(a)), '\nList 2 : \t' ,  b , len(str(b)) ,'\nDIFF = \t' ,abs(a-b), len(str(abs(a-b))) )
sqroot = reduce(mul, P_primes)
print( '\nsqrt(P) =  \t',  round(math.sqrt(sqroot)) ,' \t' ,len(str(round(math.sqrt(sqroot))))   )

print('\n', min(a,b)%10**16 )


# List 1 : 	 2309953460948766098421388011980028390 37
# List 2 : 	 2336560620831166130407308048732081811 37
# DIFF = 	 26607159882400031985920036752053421 35

# List 1 : 	 2330509488375062610899384243269677110 37
# List 2 : 	 2315951219992168112312073663812093739 37
# DIFF = 	 14558268382894498587310579457583371 35

# List 1 : 	 2326164726702943582227005954688570290 37
# List 2 : 	 2320276905090738626950161894182903601 37
# DIFF = 	 5887821612204955276844060505666689 34

# List 1 : 	 2325336038471418352764734620640358010 37
# List 2 : 	 2321103790381000776999449235158663229 37
# DIFF = 	 4232248090417575765285385481694781 34


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

# print('\n================  My SECOND SOLUTION,   ===============\n')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)/60, 6), 'min\n\n')



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
