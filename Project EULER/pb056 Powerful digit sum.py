#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Sat, 24 Sep 2016, 12:08
#The  Euler Project  https://projecteuler.net
'''
Powerful digit sum      -       Problem 56
A googol (10**100) is a massive number: one followed by one-hundred zeros; 100**100 is almost unimaginably large:
one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.
Considering natural numbers of the form, a**b, where a, b < 100, what is the maximum digital sum?
'''

#this one is easy, just compute the numbers power and sum the digits.

counter=1
maxval=0
for a in range(50, 100):
    for b in range(80,100):
        counter+=1
        c = list(str(a**b))
        S=0
        for i in range(len(c)):
            S += int(c[i])
        if S > 950 :
            print(str(counter)+'.   ',S , ' ',a,'**',b, len(str(a**b)),'   ',a**b )
            if maxval < S:
                maxval = S
print('The maximum value is : ', maxval)

print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1, travelalone from China --------------------------')


max=0
for a in range(1,100):
    for b in range(1,100):
        temp = sum(map(int,list(str(a**b))))
        if temp > max:
            max =temp
print (max)

print('\n--------------------------SOLUTION 1, LIST COMPREHENSION, zinebl from Algeria --------------------------')
zinebl