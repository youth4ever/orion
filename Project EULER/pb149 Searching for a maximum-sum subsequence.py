#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
Arithmetic expressions      -       Problem 93

bla
bla


'''
import time


# For 1 ≤ k ≤ 55, sk = [100003 − 200003k + 300007*k**3] (modulo 1000000) − 500000.
# For 56 ≤ k ≤ 4000000, sk = [sk−24 + sk−55 + 1000000] (modulo 1000000) − 500000.
L =[]
for k in range(1,56):
    s = ((100003 - 200003*k + 300007*k**3) % 1000000) - 500000
    print('s'+str(k)+'.  ',s)
    L.append(s)

print(L,'\n')
for k in range(56, 401):    # Need until 4.000.001
    s =  (( L[-24]+L[-55] +1000000 ) % 1000000) - 500000
    L.append(s)
    print('s'+str(k)+'.  ',s)


@ 2016-12-23, 01:33, Must find a function to calculate diagonals of custom length.
Also when calculating rows we need to calculate them with custom length

print('\n--------------------------TESTS------------------------------')








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
