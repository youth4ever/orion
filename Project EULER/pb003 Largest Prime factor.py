#!/usr/bin/python3
# Solved by Bogdan Trif @ 2016-09-14 16:32
#The  Euler Project  https://projecteuler.net
'''
Largest prime factor    -   Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

z=100000            # The number you need to modify  87625999

nrs = [j for j in range(1,z+1)]
prime_factors=[]
primes=[]
N = 600851475143

# Generate the prime numbers we need for our range
i=1
while(i < z):                 # Set the last Prime Number - the Upper Limit
    j = 2
    while(j <= (i/j)):              # This condition checks in the lower list
        if not(i%j): break          # IF  it's TRUE it stops, if FALSE it continues    # VERY IMPORTANT This line checks if the number is PRIME
        j = j + 1                       #Returns FALSE and continues if is i%j = 0 ; Returns TRUE and stops if i%j = 1,2,....
    if (j > i/j) : primes.append(i)                # If j > i/j means that the number is not already in the list, therefore must be another prime
    i = i + 1

#print('Primes in this range are :', primes)

# iterations=0
for R in primes:
    if N%R == 0:
        prime_factors.append(R)
        print('===',R,'===')
   # if iterations%10000 == 0:  print('Iter:',iterations, end='   ')
    #iterations += 1
print('\nAnd the prime factors are :    ',prime_factors,'\nThe Largest Prime is:  ',prime_factors[-1])

print('\nDivision by primes found: ')
for i in prime_factors:
    a = N//i
    print(a)









def common_factor(a,b):         # this functions finds the common factors of two numbers,
    temp_a=[]
    factors=[]
    for i in [1,2,3,5,7,11]:                # here if you already have a prime array (list) you can replace it, here is : primes
        if a % i == 0:                      # it will not suffice this small list of primes when working with large numbers, >
            temp_a.append(i)
            #print(temp_a)
    for j in temp_a:
        if b%j == 0:
            factors.append(j); #print(j)

    return factors