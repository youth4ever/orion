#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
                        Pandigital Fibonacci ends   -       Problem 104

The Fibonacci sequence is defined by the recurrence relation:

F_n = F_n−1 + F_n−2, where F_1 = 1 and F_2 = 1.

It turns out that F_541, which contains 113 digits, is the first Fibonacci number for which the
last nine digits are 1-9 pandigital (contain all the digits 1 to 9, but not necessarily in order).

And F_2749, which contains 575 digits, is the first Fibonacci number for which the first nine digits are 1-9 pandigital.

Given that F_k is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital, find k.


'''
import time
import gmpy2

def Fibonacci(n):
    iter = 0 		# Number of terms
    #	ORIGINAL Fibonacci with iteration, while loop
    a, b = 0, 1
    while iter < n:
        iter +=1
        a  , b = b, a + b
    return a

pan = '123456789'

def Fibo_gen(n):
    #   Fibonacci GENERATOR , while loop
#     a, b = 0, 1
#     F = [0, 1]
    a1, a2 = 0, 1
    while True:
#    a  , b = b, a + b
#         a = F[-1]+F[-2]
#         F.append(a)
#         F.pop(0)
        a = a1 + a2
        a1, a2 = a2, a
        yield a
        a+=1

print('\n--------------------------TESTS------------------------------')

print(Fibonacci(5))
a = Fibonacci(541)
b = Fibonacci(2749)
print(len(str(a)), str(a)[-9::] ,a )
print(len(str(Fibonacci(2749))), str(Fibonacci(2749))[:9] )

print('------------------------\n')

y = Fibo_gen(1)
for i in range(2, 30):    print(str(i)+'.    ' ,y.__next__() )




print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

from itertools import count

# print(gmpy2.is_prime(2749))

z = Fibo_gen(1)
I=[541]
for i in count(2):
    x = z.__next__()
    # print(str(i)+'.    ' , str(x)[:9], '   ' ,str(x)[-9::]  )
    f9 = ''.join(sorted(str(x)[:9]))
    l9 = ''.join(sorted(str(x)[-9::]))
    if i % 1e5 == 0 : print(str(i)+'.')
    # print(f9, l9)
    if  gmpy2.is_prime (i) and ( f9 == pan or l9  == pan ) :
        I.append(i)
        print(str(i)+'.   ', f9 , str(x)[:9],  '    ', l9, str(x)[-9::],'        ' , I[-1] - I[-2])
    if   f9 == pan and l9  == pan :
        print('\nAnswer :   F', i )
        break

# 541.    516212329      839725641
# 919.    513046096      965324781
# 2749.    143726895      002250249
# 7727.    314782956      397498593
# 20411.    198262300      241573689
# 28837.    168692931      283594617
# 32717.    125643798      869963797
# 34883.    583942167      566962697



# F_541    113  839725641       51621232927393794428283281722302417684416215565352081372219649050894399902811978842493025898332777796978839725641
# F_2749   575      143726895








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
