#!/usr/bin/python
# Solved by Bogdan Trif @ 2016-09-03 11:35
#The  Euler Project  https://projecteuler.net
''''
Multiples of 3 and 5
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''
my_array=[]

i = 1
while(i < 1000):
    if  (i % 3 == 0):
        print( i, " is multiple of 3 ")
        my_array.append(i)
        i = i + 1
    elif (i % 5 == 0):
        print( i, " is multiple of 5 ")
        my_array.append(i)
        i = i + 1
    else:
        i += 1

#print (my_array)
print('the sum of all the multiples of 3 or 5 below 1000 is :', sum(my_array))
print ("Good bye!")
