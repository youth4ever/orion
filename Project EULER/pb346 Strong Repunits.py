#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
                    Strong Repunits     -   Problem 346

The number 7 is special, because 7 is 111 written in base 2, and 11 written in base 6
(i.e. 7_10 = 11_6 = 111_2). In other words, 7 is a repunit in at least two bases b > 1.

We shall call a positive integer with this property a strong repunit.
It can be verified that there are 8 strong repunits below 50: {1,7,13,15,21,31,40,43}.

Furthermore, the sum of all strong repunits below 1000 equals 15864.

Find the sum of all strong repunits below 10**12.

'''
import time


def toStr(n,base):
   convertString = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmn"
   # print(len(convertString))
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]



print('\n--------------------------INITIAL VERIFICATION TEST------------------------------')

up_range = 1000
S = 1
for n in range(2, up_range+1) :
    tmp = []
    for b in range(2, 11) :
        s = toStr(n, b)
        l =  list(s)
        if  len(set(l)) == 1 and l.count('1') >= 1    :
            tmp.append(s)
            print( n, b , s   )
    if len(tmp) >=2 :
        S += n

    print('--------')
print('\n\nAnswer :\t', S)

print()
convertString = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdef"
print(len(convertString))

print(' ---------------- the inverse procedure ------------- ')
# for i in range(2, 43) :
#     s = toStr(11, i)
#     l =  list(s)
#     if  len(set(l)) == 1 and l.count('1') >=1    :
#         print( i, s  , l  )
print(toStr(42**3+42**2+42**1+42**0, 42))

# below 10**12
print(10**12)


# @ 2016-12-17, 13:30 - My initial calibration failed. I can't find the maximum allowable base. I found 43 for <50
# but when I verify for the first 1000 numbers to be the sum S = 15864 I fail. I obtain only the numbers bellow 50
TODO : I need to find what is the maximum allowable base and re-do the calibration !

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
