#!/usr/bin/python
# Solved by Bogdan Trif @ 21 Sep 16 (17:15)
#The  Euler Project  https://projecteuler.net
'''
                    Square root convergents     -       Problem 57
It is possible to show that the square root of two can be expressed as an infinite continued fraction.
√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...
By expanding this for the first four iterations, we get:
1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...
The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985,
is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.
In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?
'''
a=3/2
counter=3
for i in range(1,10):
    a = 1+(1/(1+a))
    print(str(counter)+'.  ', a)
    counter +=1
print('\n', 'sqrt 2 =',a, ' \n')

x, y = 1, 1
counter=1
for i in range(1,1001):
    u, v = x, y
    x = u + 2 * v
    y = u + v
    if len(str(x)) > len(str(y)):
        print(str(counter)+'.    ',len(str(x)), len(str(y)))
        counter+=1
