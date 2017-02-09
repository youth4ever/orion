#!/usr/bin/python                   ( ͡° ͜ʖ ͡°)
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
Factorial trailing digits       -       Problem 160

For any N, let f(N) be the last five digits before the trailing zeroes in N!.
For example,

9! = 362880 so f(9)=36288
10! = 3628800 so f(10)=36288
20! = 2432902008176640000 so f(20)=17664

Find f(1,000,000,000,000)


'''
import time
from math import factorial










print('\n--------------------------Preliminary TESTS------------------------------')
t1  = time.time()


# 2017-02-03, 12:06 --> Miss the idea  completely !

p = q  = 1
for i in range(2, 10**3 + 1) :
    p*=i
    q*=i
    if i%10 == 0 :
        while   p% 10 ==0 :
            p=p//10

    p = p%10**6
    # if str(p)[-5:]=='27392' :
    print(str(i)+'.    ', p,'       ', str(q).split('0000')[0][-8:] )

# 4109700 27753472000000
# 996.     633088
# 997.     188736
# 998.     358528
# 999.     169472
factorial non zero digit

http://mathforum.org/library/drmath/view/71768.html     !!!!!!!!!!!!!!!!!!
https://www.reddit.com/r/math/comments/4fjmt1/finding_the_last_nonzero_digits_of_ginormous/
http://math.stackexchange.com/questions/130352/last-non-zero-digit-of-a-factorial
http://mathcentral.uregina.ca/qq/database/qq.09.07/s/mukesh1.html
http://www.mathpages.com/home/kmath489.htm
https://comeoncodeon.wordpress.com/2009/06/20/lastnon-zero-digit-of-factorial/


print('\n\n' , len(str(factorial(999))) , str(factorial(999)) )                   # 27753472

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
