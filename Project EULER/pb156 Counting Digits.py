#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
                               Counting Digits      -       Problem 156
Starting from zero the natural numbers are written down in base 10 like this:
0 1 2 3 4 5 6 7 8 9 10 11 12....

Consider the digit d=1. After we write down each number n, we will update the number of ones that have occurred
and call this number f(n,1). The first values for f(n,1), then, are as follows:

                                                            n	f(n,1)
                                                            0	0
                                                            1	1
                                                            2	1
                                                            3	1
                                                            4	1
                                                            5	1
                                                            6	1
                                                            7	1
                                                            8	1
                                                            9	1
                                                            10	2
                                                            11	4
                                                            12	5
Note that f(n,1) never equals 3.
So the first two solutions of the equation f(n,1)=n are n=0 and n=1. The next solution is n=199981.

In the same manner the function f(n,d) gives the total number of digits d that have been written down
after the number n has been written.
In fact, for every digit d ≠ 0, 0 is the first solution of the equation f(n,d)=n.

Let s(d) be the sum of all the solutions for which f(n,d)=n.
You are given that s(1)=22786974071.

Find ∑ s(d) for 1 ≤ d ≤ 9.

Note: if, for some n, f(n,d)=n for more than one value of d this value of n is counted again
for every value of d for which f(n,d)=n.
'''

import time, zzz

D = {(k+1): int((k+1)*10**k) for k in range(-1, 15 )}

def f(n, d, D ) :

    # Dictionary will be EXTERNAL
    L = [ int(i) for i in str(n) ]
    # D = {(k+1): int((k+1)*10**k) for k in range(-1, len(L))}
        # STEP 1 : FIRST decompose the number into powers of base 10 :

    digits = 0

        # STEP 2 : loop through list and assign from dictionary
    bol, N =[], []
    for j in range(len(L)) :
        w = len(str(n))-j-1
        diff = L[j] - d

        if diff > 0 :
            digits += 10**(w)
            bol.append(0)
            N.append(L[j]*10**(len(L)-j-1) )
        if diff == 0 :
            digits+=1
            bol.append(1)
            N.append( L[j]*10**(len(L)-j-1) )
        if diff < 0 :
            bol.append(0)
            N.append(L[j]*10**(len(L)-j-1) )

        # print(' diff : ', L[j]  ,diff, 'digits : ' ,10**(w), ' dict=',D[w] , '  w=',w)
        digits += L[j] * D[w]
    @ 2017-03-10 --> Must correct the function. Missing some lower terms
        #     N.append(L[-1])
    M = [ bol[i]*N[i+1] for i in range(len(L)-1) ]
    # if L[0] ==d : digits +=L[-1]
    # print(L, D, digits, bol, N,    M)
    return digits + sum(M)

print( 'f function test: \t' , f(9006, 6, D) )


print('--------------------------TESTS------------------------------')
t1  = time.time()

# def f(n, d ) :
#     L = [ int(i) for i in str(n) ]
#     if

def string_brute_force_check(n, d):
    s = ''
    for i in range(1, n+1):
        s+=str(i)
    # print(len(s))
    # print( s.count(str(d))  )
    return s.count(str(d))

print('string_brute_force_check : \t ',string_brute_force_check(15, 1) )
print('string_brute_force_check : \t ',string_brute_force_check(199981, 1) )
print('string_brute_force_check : \t ',string_brute_force_check(200001, 1) )

# Algorithm construction and logic approach !! I must go from above, see if the count digit is bellow S
# if we are bellow go up, if the count(digit) > number go down

def algorithm_logic():
    S, s = 0, ''
    i = 1
    d = 1
    while S < 10**7 :
        S += str(i).count(str(d))
        if i == S :
            print(str(i)+'.     ', S)
        i+=1

# algorithm_logic()

def test_main_function( up_lim , d  ):
    S, s = 0, ''
    i = 1
    while S < up_lim :
        S += str(i).count(str(d))
        if S != f(i, d, D  ) :
            print(str(i)+'.     ', S , '             f = ', f(i, d, D))
        i+=1


test_main_function( 10**4  , 1 )



# zzz.Star_Wars()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()



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
