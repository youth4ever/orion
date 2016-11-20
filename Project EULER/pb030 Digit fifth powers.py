#!/usr/bin/python3
# Solved by Bogdan Trif @ 2016 Sept 15  13:35 PM
#The  Euler Project  https://projecteuler.net
'''
Digit fifth powers      -       Problem 30
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
1634 = 1**4 + 6**4 + 3**4 + 4**4
8208 = 8**4 + 2**4 + 0**4 + 8**4
9474 = 9**4 + 4**4 + 7**4 + 4**4
As 1 = 1**4 is not a sum it is not included.
The sum of these numbers is 1634 + 8208 + 9474 = 19316.
Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''
import time
t1  = time.time()

five_digit_numbers=[i for i in range(10,1000000)]         # range(10,1000000)
#print(five_digit_numbers[-1])
counter=0

def digit_powers(x):
        numbers_list=[]
        res=0
        for S in five_digit_numbers:
                S = str(S)
                temp = 0
                for a in S:
                        temp += int(a)**x
                if temp == int(S):
                        #print(int(S),end='')
                        res +=temp
                        numbers_list.append(temp)
                #print(numbers_list)
        print('the numbers are: ',numbers_list)
        print('The TOTAL SUM is : ', res)

digit_powers(5)

t2  = time.time()
print('\nCompleted in :', (t2-t1)*1000, 'ms')               #My solution was Completed in : 11639.665 ms

##################################################

print('-----'*20,'REALLY NICE AND FAST SOLUTION FROM THE FORUM','-----'*20)
t1  = time.time()

def prob30(x):
        s = 0
        for i in range(2,1000000):                  # range(2,1000000):
                t = 0
                for a in str(i):
                        t += int(a)**x
                if t == i:
                        s += t
        print('Sum: ',s)
prob30(5)

t2  = time.time()
print('\nCompleted in :', (t2-t1)*1000, 'ms')               #Completed in : 9909.5666 ms

