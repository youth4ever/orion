#!/usr/bin/python3
# Solved by Bogdan Trif @ 2016-09-05 18:30
#The  Euler Project  https://projecteuler.net
'''1000-digit Fibonacci number      -       Problem 25
The Fibonacci sequence is defined by the recurrence relation:
Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:
F1 = 1,     F2 = 1,     F3 = 2,     F4 = 3,     F5 = 5,     F6 = 8
F7 = 13,        F8 = 21,        F9 = 34,        F10 = 55,       F11 = 89,       F12 = 144
The 12th term, F12, is the first term to contain three digits.
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
'''
fib=[]

iteration = 0
a, b = 0, 1
while len(str(b)) < 1000:           # The number of digits that the last term must have is 999 digits but because ...
    iteration += 1
    print('F',iteration,'=',b,',  ')
    a, b = b, a + b                     # ... the last operation is just another Fibonacci sequence sum this ends up to be the first term with 1000 digits !
    fib.append(b)

print('\nThis prints only the last element of the array : F',iteration+1, ',    Length:', len(str(fib[-1])),',\nNumber: ', str(fib[-1]), type(str(fib[-1])))
print('\nThe last index term (1000th) of the Fibonacci sequence is : ',iteration+1)


