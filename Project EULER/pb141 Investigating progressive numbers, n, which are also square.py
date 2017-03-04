#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
Investigating progressive numbers, n, which are also square         -       Problem 141

A positive integer, n, is divided by d and the quotient and remainder are q and r respectively.

In addition d, q, and r are consecutive positive integer terms in a geometric sequence, but not necessarily in that order.

For example, 58 divided by 6 has quotient 9 and remainder 4.
It can also be seen that 4, 6, 9 are consecutive terms in a geometric sequence (common ratio 3/2).
We will call such numbers, n, progressive.

Some progressive numbers, such as 9 and 10404 = 102**2, happen to also be perfect squares.
The sum of all progressive perfect squares below one hundred thousand is 124657.

Find the sum of all progressive perfect squares below one trillion (10**12).

'''
import time, gmpy2
from math import sqrt, ceil, floor, gcd
from pyprimes import factorise
from itertools import combinations, permutations
import functools, operator
from decimal import *
getcontext().prec = 50


def pair_Factors(n):        # VERY EFFICIENT !!!! SUPER INTELLIGENT ALGORITHM
    todo, combis = [(n, 2, [])], []
    while todo:
        n, i, combi = todo.pop()
        while i * i <= n:
            if n % i == 0:
                combis += combi + [i, n//i],
                # todo += (n//i, i, combi+[i]),       # If needed only PAIRS (a,b) comment this line !!!
            i += 1
    return combis

def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''

    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]

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

def naive_gen(lim=100):
    P = [2,3,5,7]
    N = []

    for i in P:
        o=i
        while i < 100 :
            N.append(i)
            i*=o
    # print(N)

    for i in P :
        for j in N :
            if j%i != 0 :
                if i*j < 100 and i*j not in N :
                    N.append(i*j)
    N.sort()
    return N

print('\n--------------------------TESTS------------------------------')

# SUMS as checks
#                 10^5: 124657
#                 10^6: 700738
#                 10^8: 171436696

t1  = time.time()

def brute_force(lim = 10**2) :
    R = set([r**2 for r in range(1, int(lim**(1/2)) )  ] + [r**3 for r in range(2, int(lim**(1/3)) )  ])
    S=0

    for i in range(100, lim) :
        if i%10**5 ==0 : print(i)
        if gmpy2.is_prime(i) == False :
            if len(list(factorise(i))) >= 3:
                n = i*i
                for q in range( i-1 , i//6 , -1 ) :
                    r = n%q
                    if r in R :
                        k = q/r
                        d = (n-r)/q
                        # print(n ,q, d, q/d, d/r )
                        if d/q == q/r  :
                            d=int(d)
                            S += n
                            print( str(i)+'.      q=',q, '     d=',d, '     r=' ,r , '  ; gcd(d, q)=',gcd(d, q) , '  ; gcd(r,q)=',gcd(r,q) ,' ;   gcd(i,r)=' ,gcd(i ,r),'  ;   gcd(n-r,q)=' ,gcd(n-r,q)  ,'      n=', n, '     r=', get_factors(r), ' ;  q=' ,get_factors(q),' ;  i=',get_factors(i),'   ;     k=', k )
                            break

    return print('\nBrute Force result : \t', S+9)

# brute_force(lim = 10**4)              #   Completed in : 759.848461 s

# Brute Force result for 10**5 === 10**10 : 	 21434391491



# @ 2017-02-25, 20:00 . This is tooooo SLOW !!!!
# A cannot relate on the ratio k, because I have irrational k like 4.44444444444444444444444
# Brute force attempt is really taking tooooo much
# Also other approach was not successful
#
# I NEEEEEED an insight !  Otherwise this problem is NOT SOLVABLE !!!!
# Imagine that until 10**4 I need 80 seconds . So probably for 10**6 I would need at least 10 hours !!!




t2  = time.time()
print('\nCompleted in :', round((t2-t1), 6), 's\n')

print('\n============  My First solution ==============\n')
t1  = time.time()

        #     n = q*d + r ,               n / d = q +r
        #     58                ÷                9             =           6             and              4
        # Dividend                         Divisor                  Quotient                  Remainder


def square_progressive_numbers( up ) :
    up_lim = up*2/3
    R = set([r**2 for r in range(1, int( up**(1/2)) )  if r**2 <= up_lim ] + \
                [r**3 for r in range(2, int(up**(1/3)) ) if r**3 <= up_lim  ] + [r**5 for r in range(2, int(up**(1/5)) ) if r**5 <= up_lim  ]  )
    R = sorted(list(R))
    N = naive_gen(100)
    print(R,'\n\n')
    S = set()
    for r in R :
        # for j in N :
        for j in range(1, 100+1) :
            if j <= 10 : o = 12
            if 10 < j <= 30 : o = 2.5
            if j > 30 : o = 1.5
            for i in range( j+1, int(o*j)+1 ):
                k = i/j
                d =  r*k
                # if i==23 and j == 18 and r == 5832  :
                #     print('k: ', k, '    r:', r ,'     d : ', d, round(d) , '     error:',abs(d - round(d) )  )
                if abs(d - round(d ) ) < 1e-9 :
                    q = d*k
                    n = q*d+r
                    # if i==23 and j == 18 and r == 5832  :
                    #     print('k: ', k, '    r:', r ,'     d : ', d, round(d) , '     error:',abs(d - round(d) ) ,' q: ' , q, '  n:',n , '   error n:', abs(n - round(n) ) )
                    if abs(n - round(n) ) < 1e-6 :
                        n = round(n)
                        m = int(pow(n, 1/2))

                        if gmpy2.is_square(n) :
                            if n not in S : # and n < up**2 :
                                S.add(n)
                                d, q = int(d), int(q)
                                print( str(m)+'.      r=',r, '     d=',d, '     q=' ,q , '  ; n=', n,'   ;     k=', k )

    print('\nElements : \t',S)

    return print('\nAnswer : \t', sum(S) )

# square_progressive_numbers( up = 10**6)

# Elements : 	 {97344, 6230016, 37344321, 36869184, 10404, 16900, 7322436, 70963776, 1361388609, 9, 9729849600, 547674002500, 1380568336, 576081, 12006225, 13855173264, 8534988225, 123383587600, 16394241600, 256160025}
# TRIED :
# Answer : 	 175067393955
# # Answer : 	 722741396455
# 3634933831057
# 2764653810513
# 1245952747000
# 1036675204136
# 1035044659736
# 1036675204136


t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')


print('\n--------------------------TESTS------------------------------')



print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

def yet_another_brute_force(up) :
    up_lim = up*2/3
    R = set([r**2 for r in range(1, int( up**(1/2)) )  if r**2 <= up_lim ] +
                [r**3 for r in range(2, int(up**(1/3)) ) if r**3 <= up_lim  ] +[ r**5 for r in range(2, int(up**(1/5)) ) if r**5 <= up_lim] )
    R = sorted(list(R))

    print(len(R),'\n' ,R[:100] ,'\n\n')
    S = set()
    for m in range(3 , up) :
    # for m in range(98640 , 98641) :
    # for m in range(200000 , up) :
        r_ind = binary_search(m//100, R  )
        if m < 100 : r_ind = 0
        # print(m, r_ind, R[r_ind])
        for r in R[r_ind:] :
        # for r in R :
            if r >= m : break
            n = m*m
            # k = ( gmpy2.mpq((n-r),(r*r)) ** (1/3) )
            k = pow (  ((n-r) /(r*r))  , 1/3  )
            if k >1 :
                d = r*k
                # if  r == 50625 and m== 98640  :
                #     print('k: ', k, '    r:', r ,'     d : ', d, round(d) , '     error d:',abs(d - round(d) ) ,' q: ' , d*k, '  n:',n , '   error n:', abs(n - round(n) ) )
                # if abs(d - round(d ) ) < 1e-10 :
                if abs(d - round(d ) ) < 1e-8 :
                    q = d*k
                    m2 = pow( (k**3*r**2+r) , 1/2 )
                    # if  r == 50625 and m== 98640  :
                    #     print('k: ', k, '    r:', r ,'     d : ', d, round(d) , '     error d:',abs(d - round(d) ) ,' q: ' , d*k, '  n:',n , '   error n:', abs(n - round(n) ) )
                    if abs(m - m2 ) < 1e-10 :
                    # if abs(n - round(n) ) < 1e-5 :
                        if gmpy2.is_square(round(n)) :
                            if m not in S : # and n < up**2 :
                                S.add(m)
                                d, q = round(d), round(q)
                                print( 'm='+str(m)+'.      r=',r, '     d=',d, '     q=' ,q , '  ; n=', round(n),'   ;     k=', k ,'     r=',get_factors(r), '    d=',get_factors(d) , '  ;   error m:', abs(m - m2 ) )

    print('\nElements : \t', S )

    return print('\nAnswer : \t', sum([i**2 for i in S]) )


# yet_another_brute_force(10**6)


def fifth_attempt_cubes(up) :
    up_lim = up*2/3
    R = set([r**2 for r in range(1, int( up**(1/2)) )  if r**2 <= up_lim ] +
                [r**3 for r in range(2, int(up**(1/3)) ) if r**3 <= up_lim  ] +[ r**5 for r in range(2, int(up**(1/5)) ) if r**5 <= up_lim] )
    R = sorted(list(R))

    print(len(R),'\n' ,R[:100] ,'\n\n')
    S = set()
    for m in range(3 , up) :
    # for m in range(98640 , 98641) :
    # for m in range(200000 , up) :
        r_ind = binary_search(m//100, R  )
        if m < 100 : r_ind = 0
        # print(m, r_ind, R[r_ind])
        for r in R[r_ind:] :
        # for r in R :
            if r >= m : break
            n = m*m
            # k = ( gmpy2.mpq((n-r),(r*r)) ** (1/3) )
            k_3 =  (n-r) /(r*r)
            if k_3 >1 :
                d_6 = (n**3 - 3*r**5*k_3**2 - 3*r**4*k_3 -r**3 ) / (k_3)
                if (n-r)**3 == k_3**3*r**6 :
                    d = pow(d_6, 1/6)
                    if abs( d- round(d) ) < 1e-2 :
                        d_r = round(d)
                        k = k_3**(1/3)
                        q = round(k*d)
                        if n == d*q+r :
                            print( 'm='+str(m)+'.      r=',r, '     d=',d, '     q=' ,q , '  ; n=', round(n),'   ;     k=', k)# ,'     r=',get_factors(r), '    d=',get_factors(d) )
                            if m not in S : # and n < up**2 :
                                S.add(m)
    print('\nElements : \t', S )

    return print('\nAnswer : \t', sum([i**2 for i in S]) )


fifth_attempt_cubes(10**4)







t2  = time.time()
print('\nCompleted in :', round((t2-t1)/60, 6), 'min\n\n')


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
