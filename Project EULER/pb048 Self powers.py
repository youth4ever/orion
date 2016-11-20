#!/usr/bin/python
# Solved by Bogdan Trif @   Mon, 26 Sep 2016, 21:40
#The  Euler Project  https://projecteuler.net

'''
Self powers     -       Problem 48
The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.
Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.
'''
last_ten=[]
for i in range(1,1000):
    #if len(str(i**i)) > 2990:
    #print(i,' ; ',len(str(i**i)),' ;    ' , str(i**i)[-10::])
    last_ten.append(int(str(i**i)[-10::]))

#str='abcdefghijklmnopqrstuv'
#print(str[-5::])               #   List the last 5 characters of a string
#print(last_ten)
print('\n','Last ten digits are :   ',str(sum(last_ten))[-10::])

s='3453458124'
l = list(s)
print(l, type(l), len(l))