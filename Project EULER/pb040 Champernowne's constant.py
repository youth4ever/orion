#!/usr/bin/python3
# Solved by Bogdan Trif @   Thu, 29 Sep 2016, 22:45
#The  Euler Project  https://projecteuler.net
'''
Champernowne's constant     -       Problem 40
An irrational decimal fraction is created by concatenating the positive integers:
0.123456789101112131415161718192021...
It can be seen that the 12-th digit of the fractional part is 1.
If d_n represents the n-th digit of the fractional part, find the value of the following expression.
d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000
'''
s=''

for i in range(1,1000001):
    s += str(i)

print(s[0],s[9],s[99],s[999],s[9999],s[99999],s[999999],'  = ', int(s[0]) * int(s[9]) * int(s[99]) * int(s[999]) * int(s[9999]) * int(s[99999]) * int(s[999999])   )

#  the result = 210