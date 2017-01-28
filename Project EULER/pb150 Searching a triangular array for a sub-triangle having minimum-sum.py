#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
Searching a triangular array for a sub-triangle having minimum-sum      -       Problem 150

In a triangular array of positive and negative integers, we wish to find a sub-triangle
such that the sum of the numbers it contains is the smallest possible.

In the example below, it can be easily verified that the marked triangle satisfies this condition having a sum of −42.


We wish to make such a triangular array with one thousand rows, so we generate 500500
pseudo-random numbers sk in the range ±219, using a type of random number generator
(known as a Linear Congruential Generator) as follows:

t := 0
for k = 1 up to k = 500500:
    t := (615949*t + 797807) modulo 2**20
    sk := t−2**19

Thus: s_1 = 273519, s_2 = −153582, s_3 = 450905 etc

Our triangular array is then formed using the pseudo-random numbers thus:

                                                        s1
                                                     s2  s3
                                                   s4  s5  s6
                                                s7  s8  s9  s10
...
Sub-triangles can start at any element of the array and extend down as far as we like
(taking-in the two elements directly below it from the next row,
the three elements directly below from the row after that, and so on).
The "sum of a sub-triangle" is defined as the sum of all the elements it contains.
Find the smallest possible sub-triangle sum.


'''
import time


def Linear_Congruential_Generator():           # EFFICIENT GENERATOR
    '''      t := 0
            for k = 1 up to k = 500500:
                t := (615949*t + 797807) modulo 2**20
                sk := t−2**19
        Thus: s_1 = 273519, s_2 = −153582, s_3 = 450905 etc                 '''

    t=0
    while True :
        t = (615949*t + 797807)% (2**20)
        s = t - 2**19
        yield s


print('\n--------------------------TESTS------------------------------')

LCG = Linear_Congruential_Generator()

for i in range( 10):
    print(str(i)+'.   ', next(LCG), end='    ')

print('\n-------------------------------------')

def build_triangle(up_lim):
    LCG = Linear_Congruential_Generator()
    T=[]
    rows = int( -(1/2)+ ( (1+4*2*up_lim)**(1/2) )/2 )
    for i in range(0, rows):
        tmp=[]
        for j in range(0, i+1):
            tmp.append(next(LCG))
        T.append(tmp)
        print(tmp)

build_triangle(5050)

# print( (-1/2)+ ( (1+4*2*21)**(1/2) )/2 )

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
