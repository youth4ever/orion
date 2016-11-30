#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
Efficient exponentiation    -       Problem 122

The most naive way of computing n**15 requires fourteen multiplications:

n × n × ... × n = n**15

But using a "binary" method you can compute it in six multiplications:

n × n = n**2
n**2 × n**2 = n**4
n**4 × n**4 = n**8
n**8 × n**4 = n**12
n**12 × n**2 = n**14
n**14 × n = n**15

However it is yet possible to compute it in only five multiplications:

n × n = n**2
n**2 × n = n**3
n**3 × n**3 = n**6
n**6 × n**6 = n**12
n**12 × n**3 = n**15

We shall define m(k) to be the minimum number of multiplications to compute nk; for example m(15) = 5.

For 1 ≤ k ≤ 200, find ∑ m(k).

'''
import time
from  math import log2

print('\n--------------------------TESTS------------------------------')

import gmpy2

def factorise(n):
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    from pyprimes import factorise
    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]


print('test gmpy2 module : ',gmpy2.is_prime(2))


print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

D = {1 : 0, 2 : 1 }

for i in range(3, 201):
    F = factorise(i)
    if gmpy2.is_prime(i) == True :
        D[i] = (D[i-1]+1)
        print(str(i)+'.      m(',i,') = ' , D[i-1]+1, '           '  )
    elif log2(i-1) % 1 == 0 :
        D[i] = (D[i-1]+1)
        print(str(i)+'.      m(',i,') = ' , D[i-1]+1, '           '  )
    elif  F.count(7) > 1 or F.count(11) > 1 :
        D[i] = sum([D[i] for i in F])-1
        print(str(i)+'.      m(',i,') = ' , sum([D[i] for i in F])-1, '           '  )

    else :
        print(str(i)+'.      m(',i,') = ' , sum([D[i] for i in F]), '           ', [D[i] for i in F], '      ', F )
        D[i] = sum([D[i] for i in F])
print(D)

print( '\nAnswer:  ',sum([ v for v in D.values() ] ) )

# Tried :  Answer:   1635, 1654, 1636, 1625

#  Problema cu skepsis  @ 2016-11-24  00:33, the algorithm becomes too complicated !




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
