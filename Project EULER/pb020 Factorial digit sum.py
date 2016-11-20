#!/usr/bin/python3
# Solved by Bogdan Trif @   15 Sep 2016 (17:59)
#The  Euler Project  https://projecteuler.net
'''
Factorial digit sum       -       Problem 20
n! means n × (n − 1) × ... × 3 × 2 × 1
For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''
n=1
X=100

for i in range(1,X+1):
    n *= i

S=0
for a in ([z for z in str(n)]):
    S += int(a)
    print(a, end='')

print('\nThe sum of the digits of 100!  is :  ', S)