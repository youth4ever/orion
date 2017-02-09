#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Thu, 2 Feb 2017, 18:26
#The  Euler Project  https://projecteuler.net
'''
                The hyperexponentiation of a number     -       Problem 188

The hyperexponentiation or tetration of a number a by a positive integer b,
denoted by a↑↑b or ba, is recursively defined by:

                            a↑↑1 = a,
                a↑↑(k+1) = a**(a↑↑k).

Thus we have e.g. 3↑↑2 = 3**3 = 27, hence 3↑↑3 = 3**27 = 7625597484987

and 3↑↑4 is roughly 10**(3.6383346400240996*10^12.)

Find the last 8 digits of 1777↑↑1855.


'''
import time

print('abcdefghijklmno'[-8::])

print('\n--------------------------TESTS------------------------------')

# b = 1
# e = 1777
# for i in range(1, 1777+1) :
#     b = b*e
#     print( str(i)+'.   ' ,b , '         ',str(b)[-8::] )
#     # print(a**i,'     ' ,b)
#     b = int(str(b)[-8::])


# OBSERVATION : @ 2016-12-21, 22:00
#         === 1777 ====
# 2 digits repetition : 20
# Let's see the last 3 digits repetition period :  100
# 4 digits :  1777 ending repeats with a period of 500. Actually the last 4 digits have a period of 500
# 5 digits : have a period of 500*5 = 2500
# 6 digits repetition : I guess is 2500 * 5 = 12500 ==> CORRECT
# 7 digits repetition : I guess is 12500 * 10 = 125.000
# 8 digits repetition : 125.000 *10 = 1.125.000
# Studiu de caz :
# 28.170.    444  92414049
# 153.170.   267 2 2414049
# 1.278.170.    444  92414049
# ==> The repetition of last 8 digits occur @ 1.250.000 powers of the number 1777  % 1.25*10**6 =>
# I must find somehow the exponent of the hyperexponentiation


print('\n\n-------------Confirmation TEST-----------------')

b = 1
e = 2
for i in range(1, 16+1) :
    b = b*e
    print( str(i)+'.   ' ,b , '         ',str(b)[-8::] )
    # print(a**i,'     ' ,b)
    b = int(str(b)[-8::])


print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()


def hyper_exponentiation(nr, hyper_exponent, last_digits):
    exp = nr
    for i in range(1, last_digits ) :      # We only need 7 iterations for the 8 digits we need
        x = pow(nr, exp, 10**last_digits)
        # print( str(i+1)+'.            ', x )
        exp = x

    return print('\nAnswer : \t',str(nr)+' ↑↑ ' +str(hyper_exponent)+'   =   ', str(x) )

hyper_exponentiation(1777, 1855, 100 )                # Solution : 1777 ↑↑ 1855      =        95962097


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
