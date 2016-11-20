#!/usr/bin/python3
# Solved by Bogdan Trif @   Completed on Mon, 10 Oct 2016, 11:20
#The  Euler Project  https://projecteuler.net
'''
Square root digital expansion       -       Problem 80
It is well known that if the square root of a natural number is not an integer, then it is irrational.
The decimal expansion of such square roots is infinite without any repeating pattern at all.
The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.
For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.
'''
from decimal import *
getcontext().prec = 105

print('------------------  Testing : --------------------')
x = Decimal(2).sqrt()
print(x, len(str(x)))
D= str(x).split('.')[-1]
D=D[0:99]+str(x).split('.')[0]
print('Length:  ',len(str(x).split('.')[-1]),'   ',str(x).split('.')[-1])
print(sum(map(int, list(D))))
#print(len(list(str(x).replace('.',''))) ,  list(str(x).replace('.','')))
#print(sum(map(int,list(str(x).replace('.','')))))
# sum(map(int,list(str(a**b))))

def compute_quare_root(n, decimals=4) :
    ''' Algorithm to compute custom number of digits of square roots using powers.
    The dot is omitted. If you want the exact result just divide return by / 10**(decimals*2).

    :param:    :n: root to be calculated
                    :decimals: the number of decimal desired    '''

    n = n*10**(decimals*2)
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

root_2 = compute_quare_root(2, 99)
print(root_2, 'Sum of the digits : ',sum([int(i) for i in str(root_2)]) )

print('===='*20,'\n')
print('\n----------------------- MY SOLUTION --------------------------------------')
# Trebuiau adunate si numarul dinaintea virgulei, si am neglijat aspectul asta

big_S = []

for i in range(1,100):
    if len(str(Decimal(i).sqrt())) > 10:
            x = Decimal(i).sqrt()
            a = str(x).split('.')[-1]
            b = str(x).split('.')[0]
            print(str(i)+'.   ', b,'.',a)
            c=a[0:99]+b
            # print( type(c), len(c), c ,'\n      ')
            S = sum(map(int, list(c)))
            print('    sum  = ', S)
            print('----'*10)
            big_S.append(S)

print('The TOTAL SUM is:  ',sum(big_S),'\n', len(big_S) ,big_S)         # Answer : 40886 CORRECT

print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1  --------------------------')

from decimal import getcontext, Decimal

getcontext().prec = 102
L, d, s = 100, 100, 0
p = pow(10, d-1)

for z in range(2, L):
    q = Decimal(z).sqrt()
    s += sum(int(c) for c in str(q * p)[:d]) if  q % 1 != 0 else 0

print ("Project Euler 80 Solution =", s)




print('\n--------------------------SOLUTION 2, REMARKABLE ,  Efemena, Germany --------------------------')
# Cheated by using Python. Bigints and integer squareroot.
# this guy calculates the SQUARE ROOT with  custom digits number by raising to the power*2 of
# the number of digits wanted. Example: want to calculate sqrt(2) with 3 digits : just take 2*10*6 and use the function
# The result before   will be the main number with the first two decimals = 3 digits

from itertools import islice

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def digits(num):
    while num != 0:
        yield num % 10
        num //= 10

def non_squares(num):
    squares = [x*x for x in range(1, isqrt(num)+1)]
    yield from filter(lambda n: n not in squares, range(1, num+1))

dig_sum = 0
for num in non_squares(100):
    root = isqrt(num * 10**200 )
    dig_sum +=  sum( islice( digits(root), 1, None) )

print(dig_sum)


print('\n--------------------------SOLUTION 3 , darent, England --------------------------')
# Using long division and realizing we only need to look at 2 through to 99:
def root_digtal_sum(n):
    approx_root = n ** (1./2)
    if approx_root.is_integer():
        return 0
    sum_ = approx_root = int(approx_root)
    remainder = n - approx_root * approx_root
    for k in range(99):
        remainder *= 100
        approx_root *= 20
        for i in range(1, 10):
            if (approx_root + i) * i > remainder:
                next_digit = i - 1
                break
        else:
            next_digit = 9
        remainder -= (approx_root + next_digit) * next_digit
        approx_root >>= 1
        approx_root += next_digit
        sum_ += next_digit
    return sum_

print (sum(root_digtal_sum(i) for i in range(2, 100)))

print('\n--------------------------SOLUTION 4  --------------------------')



print('\n--------------------------SOLUTION 5 --------------------------')



print('\n--------------------------SOLUTION 6  --------------------------')









