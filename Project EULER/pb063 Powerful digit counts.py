#!/usr/bin/python
# Solved by Bogdan Trif @ Completed on Wed, 21 Sep 2016, 13:10
#The  Euler Project  https://projecteuler.net
'''
Powerful digit counts       -       Problem 63
The 5-digit number, 16807=7**5, is also a fifth power.  Similarly, the 9-digit number, 134217728=8**9, is a ninth power.
How many n-digit positive integers exist which are also an nth power?
'''

digit= [ i for i in range(1,10)]
print(digit)
counter=1
for i in digit:
    for j in range(1,50):
        if len(str(i**j)) == j :
            print(str(counter)+'.   Base :', i , ',  Power :', j , ' ;  Res = ', i**j)
            counter +=1