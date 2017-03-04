#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
                                                    Number Rotations        -       Problem 168

Consider the number 142857. We can right-rotate this number by moving the last digit (7) to the front of it, giving us 714285.

It can be verified that 714285=5×142857.

This demonstrates an unusual property of 142857: it is a divisor of its right-rotation.

Find the last 5 digits of the sum of all integers n, 10 < n < 10**100, that have this property.

'''
import time
import gmpy2

def circulate_number(A):
      tmp=[]
      for v in range(len(str(A))):
            a , i , s =  str(A), len(str(A)), ''
            for c in range(i):
                  #print(a[(v+c) % j] ,end='  ')
                  s += str(a[(v+c) % i])
            #return s
            tmp.append(int(s))
            #print(s)
            v+= 1
      return tmp #print(tmp)

def right_rotate_number(n):
    n = str(n)
    return int(n[-1]+n[:-1])

print(circulate_number(142857))
print('is_prime :\t',gmpy2.is_prime(142857))
print('right_rotate_number Test :', right_rotate_number(142857142857142857))
print(714285714285714285 / 142857142857142857)

#### IMPORTANT - THE IDEA OF THE PROBLEM  ::  #############
# If we take  102564 and we right-rotate it ==> 410256  = 102564 * 4
# Let's multiply it step by step :
# 4 * 4 = 16                       => 6 keep 1        <<-- Start
# 6 * 4 = 24 + keep 1 = 25 => 5 keep 2
# 5 * 4 = 24 + keep 2 = 26 => 6 keep 2
# 2 * 4 =  8 + keep 2 = 10 => 0 keep 1
# 0 * 4 =  0 + keep 1 = 1 =>  1 keep 0        <<-- End
# 1 * 4  = 4
# Therefore the number is : 410256
# The trick is that this sequence keeps reapeating itself because we have again the 4 which multiplied by 4
# give 16 ==> 6 keep 1 ...and so on and so on :
# Therefore all the numbers of the type 102564, 102564.102564, 102564.102564.102564 repeat themselves
# All we need to do for this problem is to see how many are in 10**100 => digit length = 6 => 100 //6  = 16





print('\n--------------------------TESTS------------------------------')
t1  = time.time()

SUM = 0
S = []
cnt = 0
for n in range(10, 10**6) :
    a = right_rotate_number(n)
    if  a%n == 0 : #and len( set([int(i) for i in str(n)] ) ) > 1 :         # We will include later numbers like 666666, 777777
        if  len( set([int(i) for i in str(n)] ) ) > 1 :
            S.append(n)
        cnt+=1
        print (str(cnt)+'.      n=', n,'     a=', a , '     a / n=', a//n  )
        SUM+= n

print('\nPartial Answer : \t', SUM,'\n')

O = [ int( (str(i)*6 ) ) for i in range(1,10) ]
print('One digits : \t' , O )
print('6-digits :\t', S )

lim=100
one_digits = (lim-6) * sum(O)
six_digits = (lim//6 -1 ) * sum(S)

print('\nOne digits : ',one_digits  )
print( '6-digits  : \t', six_digits )

print('\nAnswer :\t', (one_digits + six_digits +SUM )%10**5 )

# TRIED : 40706, 40701

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
