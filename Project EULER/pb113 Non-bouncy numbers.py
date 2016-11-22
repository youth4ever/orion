#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
                                          Non-bouncy numbers        -       Problem 113
Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

As n increases, the proportion of bouncy numbers below n increases such that
there are only 12951 numbers below one-million that are not bouncy
and only 277032 non-bouncy numbers below 10**10.

How many numbers below a googol (10**100) are not bouncy?
'''
import time

print('--------------------------TESTS------------------------------')

n = 9972  #, 9910, 6664, 6662

def monotonic_number(n) :
    listN = list(str(n))
    flag1 = False
    flag2 = False
    for i in range(1, len(listN)):
        if listN[i] > listN[i-1]:
            flag1 = True
        if listN[i] < listN[i-1]:
            flag2 = True
    if flag1 == True and flag2 == True:
        return False
    else : return True


print('Test for bouncy_number Function :  ', monotonic_number(n),'\n' )        # Functions Tests look good



print('------------------------------ AUTOMATED TESTS --------------------------')

def automated_test():
    cnt=0
    for i in range(1,1000001):
        b = monotonic_number(i)
        if b == True :
            print(str(i) + '.     : ' , b )
            # if i > 100 :
            cnt+=1

    return print('cnt:  ', cnt )

automated_test()

# 100-1000 : 375,   1000-10000 : 1200 ,   1e4-1e5 : 3279,     1e5-1e6 : 7998

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
