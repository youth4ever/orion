#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
            Special isosceles triangles         -           Problem 138

Consider the isosceles triangle with base length, b = 16, and legs, L = 17.

By using the Pythagorean theorem it can be seen that the height of the triangle, h = √(172 − 82) = 15,
which is one less than the base length.

With b = 272 and L = 305, we get h = 273, which is one more than the base length,
and this is the second smallest isosceles triangle with the property that h = b ± 1.

Find ∑ L for the twelve smallest isosceles triangles for which h = b ± 1 and b, L are positive integers.

'''
import time
import math
from itertools import count

def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    from pyprimes import factorise
    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]

def Pythagorean_triplets_for_isoscel( i ):    # by Bogdan Trif
    ''':Usage:      >>> pyt = gen_Pythagorean_triplets(5,5)
                        # >>> next(pyt)
                        # >>> for i in gen_Pythagorean_triplets(8,8): print(i)
    :param i:   i
    :param j:   j
    :return:    a,b,c - pythagorean triplet
    '''
    for m in range(1, i+1):
        for n in range(m//5+1 , m//4+1):
        # for n in range(i//8 , i//4+1):

            a = m**2-n**2
            b = 2*m*n
            c = m**2 + n**2
            if a > 0:
                print(m,n,'    ',sorted((a,b,c)), end='  ')
                yield a,b,c


print('\n--------------------------TESTS------------------------------')

print('angle has : \t', math.acos(15/17)*180/math.pi, '  degrees ')
print('angle has : \t',math.acos(273/305)*180/math.pi,  '  degrees ')

print('\n---------------- Theory Test --------------')

cnt , SL = 0, 0

print(' Integer Test : ', pow ( ( (534252352/2)**2 + 534252353 **2  ), 1/2  ) , '\n' )

# for b in count(16, 16):
#     L1 = pow( ( pow(b+1, 2) + pow( b/2 , 2)), 1/2)
#     L2 = pow( ( pow(b-1, 2) + pow( b/2 , 2)), 1/2)
#
#     if abs(L1-round(L1)) < 1e-12   :
#         cnt+=1
#         SL += L1
#         print( str(cnt)+'.    b= ',b, get_factors(b) , ' ;     h=' ,b+1 , get_factors(b+1) , ' ;   L1=', '  ',L1, get_factors(L1)  ,'    case1')
#
#     if abs(L2-round(L2)) < 1e-12   :
#         SL += L2
#         cnt+=1
#         print( str(cnt)+'.    b= ',b, get_factors(b) , ' ;     h=' , b-1, get_factors(b-1) , ' ;   L2=',L2,'  ' ,get_factors(L2)  ,'    case2')
#     if cnt == 2 : break
#
# print('\nAnswer:',SL)



print('\n================  My FIRST ATTEMPT SOLUTION,   ===============\n')
t1  = time.time()

up_lim = 7*10**3
PT = Pythagorean_triplets_for_isoscel( up_lim )


# M=[1]
# for p in PT:
#     cnt+=1
#     print(str(cnt)+'.   ', p)
    # b, h, L = p[1], p[0], p[2]
    # if b*2 == h-1 or b*2 == h+1 :
    #     cnt+=1
    #     S += L
    #     M.append(L)
    #     print(str(cnt)+'.    ', p ,';      h=' ,h,'    ', get_factors(h) ,'    b=',2*b, '     ',get_factors(2*b),'     L=', L , '  ', get_factors(L), '   ', M[-1]/M[-2] )
    # if cnt ==6 : break
# print('\nAnswer :', S)



def special_Isosceles_Tiangles(how_many) :
    cnt, S = 0, 0
    m, n = 4, 1
    while True :
        for m in count(m, 1):
            h = m**2-n**2
            b = 2*m*n
            L = m**2 + n**2
            if b*2 == h+1 or b*2==h-1 :
                cnt+=1
                print('(m,n)=' ,m,n,'        (h, b, L)= ', (h, b ,L) )
                S+=L
                break
        n = m
        m = int(4.2*n)
        if cnt == how_many :
            return print('\nAnswer :', S)

special_Isosceles_Tiangles(12)





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
