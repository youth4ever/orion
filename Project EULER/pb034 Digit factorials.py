#!/usr/bin/python
# Solved by Bogdan Trif @       Completed on Tue, 27 Sep 2016, 18:14
#The  Euler Project  https://projecteuler.net
'''
Digit factorials        -       Problem 34
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''
from math import factorial
import time
t1  = time.time()


big_SUM=0
for i in range(3,1000000):
    S=0
    for j in str(i):
        S += factorial(int(j))
    if i == S :
        big_SUM += S
        print(str(i)+'.  ' , S  )

print('The SUM of all is :  ', big_SUM)
t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,4), 'ms')

############################################
'''
Since the question of the upper bound seems to be still open:

As many have already argued 7*9!=2540160 is an upper bound.

We can further improve this upper bound:
Since no number bigger than 2540160 is possible, if we have a 7 digit number the first digit can be at most 2.
Thus, only 6 positions can range up until 9 and we obtain a new upper bound as 2!+6*9!= 2177282.

As we can see, if we have a 7-digit number, either the second digit is 0 or 1 or the first digit is 1.
If the first digit is 2 and thus the second digit is 0 or 1, the numbers are limited by 2!+1!+5*9! = 1814403 a contradiction to the first digit being 2.

Thus, a 7-digit number can be at most 1999999.

With some further analysis, we can reduce the upper bound to 1814425:
All factorials of digits at least 5 have the factors 5 and 2 and thus end on 0.
Let 1abcdef denote our 7 digit number. If a,b,c,d,e and f are all at least 5, the sum of the factorials -
which is supposed to be equal to 1abcdef - will end on 1 (coming from the 1! in the beginning).
This is a contradiction to the assumption that f is at least 5. Thus, at least one of the digits a-f can be at most 4.
Our new upper bound is 1!+4!+5*9!=1814425.

So now we know that (assuming we have a 7-digit number) our second digit is at most 8.
By the same argument as above, we have two cases:
If a is at least 5 and thus one of the remaining digits b-f has to be at most 4.
Then we obtain as upper bound (since a is at most 8): 1!+8!+4!+4*9!= 1491865, a contradiction to a being at least 5.
Thus, a is at most 4 and we have as new upper bound 1499999.

Im pretty sure the analysis can be further refined to reduce the upper bound even beyond that,
but considering the runtime improvements even the bound 2540160 is sufficient.


'''


print('\n=========== OTHER SOLUTIONS FROM THE EULER FORUM =================')
# Python. I think pre-calculating an array of factorials is more efficient compared to a function which repeatedly calculates them.

print('\n---------------------------SOLUTION 1------------------------------')

t1  = time.time()

f = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
s = 0
for n in range(3,1000000):
    if n == sum(f[int(d)] for d in str(n)):
        s += n
print(s)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,4), 'ms')

print('\n---------------------------SOLUTION 2------------------------------')
t1  = time.time()

from math import factorial as f
sum(i for i in range(3,1000000) if sum(f(int(j)) for j in str(i)) == i)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,4), 'ms')