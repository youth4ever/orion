#!/usr/bin/python
# Solved by Bogdan Trif @       Completed on Tue, 11 Oct 2016, 11:05
#The  Euler Project  https://projecteuler.net
'''
Number spiral diagonals     -       Problem 28
Starting with the number 1 and moving to the right in a clockwise
direction a 5 by 5 spiral is formed as follows:

                              21 22 23 24  25
                              20  7  8   9   10
                              19  6  1   2   11
                              18  5  4   3   12
                              17 16 15 14  13

It can be verified that the sum of both diagonals is 101.
What is the sum of both diagonals in a 1001 by 1001 spiral formed in the same way?
'''
import time
t1  = time.time()

i = 0
L = S =1


while i <  500 :      #  2*i+1 :
    i += 1
    for j in range(1,5):
        L  += 2 * i
        S  += L
        #print(L, end=' ')
    #print('   --> ',str(i)+'.      ',  2*i+1,'   '  ,S)
print(S)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,4), 'ms\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1 ,  --------------------------')

print(sum([(3 * ((i - 2) ** 2)) + (6 * i) + (i ** 2) - 6 for i in range(3, 1002, 2)]))


print('\n--------------------------SOLUTION 2 ,  --------------------------')

D = 1
inner = 1

for s in range(3,1002,2):
    D += 4*inner + 10*(s-1)
    inner = s*s

print(D)

print('\n--------------------------SOLUTION 3 ,  --------------------------')

sum = adder = 1
size = 1001
for i in range(2, size, 2):
    for _ in range(4):
        adder += i
        sum += adder
print(sum)