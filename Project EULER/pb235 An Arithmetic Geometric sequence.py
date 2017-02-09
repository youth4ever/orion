#!/usr/bin/python                   ( ͡° ͜ʖ ͡°)
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
An Arithmetic Geometric sequence        -       Problem 235

Given is the arithmetic-geometric sequence u(k) = (900-3k)r**k-1.

            Let s(n) = Σ {k=1...n} u(k).

Find the value of r for which s(5000) = -600,000,000,000.

Give your answer rounded to 12 places behind the decimal point.


'''
import time

from decimal import *
getcontext().prec = 20





def u1(k, r):
    return Decimal((900-3*k) * r**(k-1))

u = lambda k, r : (900-3*k) * r**(k-1)

print('test u : ',u(2 , 2/33),'\n')

def s( r ):
    S=0
    for i in range(1, 5001):
        # S += Decimal(u1(i , Decimal(r)))
        # S += u(i , Decimal(r))
        S += u(i , r )
    return S






# 1001.   1.001         s = 	  -1647175481.404537
# 1002.   1.002         s = 	  -137389011510.7948

# 1320.   1.0023203189999998         s = 	  -595079742096.9348
# 1321.   1.0023213199999998         s = 	  -597826775555.0255
# 1322.   1.0023223209999998         s = 	  -600586575026.495
# 424.   1.0023221086328761852968227685778401792049407958984375         s = 	  -600000000000.1172755139854

print('\n--------------------------TESTS------------------------------')
t1  = time.time()

target =  -6*10**11


Scale = 10**18
cnt = 0
R = Decimal(1.002322108631888) #5962
print(len(str(R)), str(R),'\n' )
for i in range( int(R* Scale), 2* Scale, 1) :
    cnt+=1
    # r =  Decimal (i   / Scale )
    r =   (i   / Scale )
    # S = Decimal (s(r) )
    S = s(r)
    print( str(cnt)+'.  ',  r ,'        s = \t ', S    )
    if S < target :
        print(str(r)[:14])
        break




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
