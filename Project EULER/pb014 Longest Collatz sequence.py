#!/usr/bin/python
# Solved by Bogdan Trif @ 15 Sep 16 (10:30)
#The  Euler Project  https://projecteuler.net
'''
Longest Collatz sequence
Problem 14
The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)
n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.
'''
import time

t1  = time.time()

primes=[]
i = 999900          #Set the starting Prime, First Prime in the list, 1000

while(i <= 1000000):         # Set the last Prime Number Up, 9999
    j = 2
    while(j <= (i/j)):
        if not(i % j): break        # IF  it's TRUE it stops, if NOT TRUE it continues
        j = j + 1                       #Returns False and continues if is i%j = 0 ; Returns TRUE and stops if i%j = 1,2,....
    if (j > i/j) :
        primes.append(i)
        #print(i)
    i = i + 1

#print(primes)
collatz_array=[]
length_array=[]

for nr in range(800000,1000000):
    collatz_array=[]
    while nr > 1:
        collatz_array.append(int(nr))
        if  (nr % 2 ==0):
            nr = nr / 2
        else :
            nr = 3* nr + 1
    collatz_array.append(1)
    if len(collatz_array) > 500 :
        print('Number  :',collatz_array[0],'  ;  Length: ',len(collatz_array),collatz_array[0:10])
        length_array.append(collatz_array[0]); length_array.append(len(collatz_array));

print(length_array)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms')               #My solution was Completed in : 52317.99 ms


print('=============SOLUTION FROM THE FORUM=============')

print('------'*25)

t1  = time.time()
'''
def chain(start):
    step=0
    if start==1:
        return step
    while start!=1:
       if start%2==0:
           start=start/2
           step+=1
       else:
           start=start*3+1
           step+=1
    return step

longest=1

for number in range(1,1000000):
    if chain(number)>chain(longest):
        longest=number

print(longest)
'''
t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms')               #Completed in : 47013.80 ms

