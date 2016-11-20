#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Mon, 10 Oct 2016, 13:56
#The  Euler Project  https://projecteuler.net
'''
Number letter counts        -       Problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
NOTE: Do not count spaces or hyphens.
For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
'''

import eulerlib as el

print('--------------TESTS -------------------')
print(el.word_numerical_val('Abcd'))
print(el.write_number(1633))
print(el.write_number(1633).replace(' ',''))
n = el.write_number(1633).replace(' ','')
print('Length : ', len(n))

print('\n---------------The SOLUTION -----------------')
S=0
for i in range(1,1001):
    n = el.write_number(i).replace(' ','')
    n = n.replace('-','')
    S += len(n)
    #print(len(n), n)
print(S)            #   Answer : 21124
