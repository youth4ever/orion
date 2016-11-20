#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
Goldbach's other conjecture     -       Problem 46
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12
It turns out that the conjecture was false.
What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''

def detect_prime(n):
    i = n
    while(i <= n):
        j = 2
        while(j <= (i/j)):
            if not(i%j):
                return False
                break
            j = j + 1
        if (j > i/j) : return True
        i = i + 1

def factor_split(nr_to_check):
    primes=[]
    n = nr_to_check
    i = 2
    while(i < n):
        j = 2
        while(j <= (i/j)):
            if not(i%j): break          # IF  it's TRUE it stops, if FALSE it continues    # VERY IMPORTANT This line checks if the number is PRIME
            j = j + 1                       #Returns FALSE and continues if is i%j = 0 ; Returns TRUE and stops if i%j = 1,2,....
        if (j > i/j) : primes.append(i)    #     print( i, end= ' ')     # If j > i/j means that the number is not already in the list, therefore must be another prime
        i = i + 1

    factors=[]
    for x in primes:
        while n % x == 0 :
            n = n / x
            factors.append(x)
    if len(factors) != 0:
        return factors #print('\nThe factors of ',nr_to_check ,'are : ' ,factors, end = '')
    #else : return False #print('    ',nr_to_check,' is prime   ')

print(set(factor_split(34)))

nr_factors=[]
odd_non_primes=[]
for i in range(4,1000):
    if (detect_prime(i) == False and i%2 == 1):
#        if ( int(i-1)+1 == int(i) ):
            odd_non_primes.append(i)

print(odd_non_primes)

for i in odd_non_primes:
    print(i, '  ',factor_split(i))

    here need to write the number in terms of a prime + a squared * 2