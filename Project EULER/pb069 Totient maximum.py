#!/usr/bin/python
# Solved by Bogdan Trif @       Completed on Fri, 14 Oct 2016, 21:07
#The  Euler Project  https://projecteuler.net
'''
Totient maximum     -       Problem 69
Euler's Totient function, f(n) [sometimes called the phi function], is used to determine the number of numbers less than n
which are relatively prime to n.
For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, f(9)=6.

+------------------------------------------+
| n  | Relatively Prime  | φ(n) | n/φ(n)    |
|----+------------------+------+-----------|
| 2  | 1                          | 1    | 2         |
|----+------------------+------+-----------|
| 3  | 1,2                        | 2    | 1.5       |
|----+------------------+------+-----------|
| 4  | 1,3                         | 2    | 2         |
|----+------------------+------+-----------|
| 5  | 1,2,3,4                  | 4    | 1.25      |
|----+------------------+------+-----------|
| 6  | 1,5                       | 2    | 3         |
|----+------------------+------+-----------|
| 7  | 1,2,3,4,5,6              | 6    | 1.1666... |
|----+------------------+------+-----------|
| 8  | 1,3,5,7                  | 4    | 2         |
|----+------------------+------+-----------|
| 9  | 1,2,4,5,7,8              | 6    | 1.5       |
|----+------------------+------+-----------|
| 10 | 1,3,7,9                  | 4    | 2.5       |
+------------------------------------------+

It can be seen that n=6 produces a maximum n/φ(n) for n 10.
Find the value of n 1,000,000 for which n/φ(n) is a maximum.
'''
import time
from itertools import combinations
from numpy import prod


def factor_split(a): ##outputs a list of the unique prime factors of its input
    b = 2
    d = []
    f = a
    while f > 1:
        while f % b != 0:
            b = b + 1
        d = d + [b]
        f = f / d[-1]
    if len(d) >1:
        return d
    #else: print(a,' is prime')

#print(factorSplit(210))


class Bogdan_Totient_algorithm :
    # def __init__(self, nr):
    #     self.nr = nr

    def is_prime(self, nr):
    # Function which checks if a number is prime
        for i in range(2, int(pow(nr,1.0/2))+1):
            if nr%i==0:
                return 0
        return 1

    def factor_split(self, nr): ##outputs a list of the unique prime factors of its input
        b = 2
        d = []
        f = nr
        while f > 1:
            while f % b != 0:
                b = b + 1
            d = d + [b]
            f = f / d[-1]
        if len(d) >1:
            return d
        #else: print(a,' is prime')

    def count_elements(self, nr):
            #my_method = self.factor_split(nr=4)

            if self.is_prime(nr) == True :
                return nr-1
            else:
                A = list(set(self.factor_split(nr)))
                cnt = 0
                for k in range(len(A)):
                    #print(A[k], A[0:k+1])
                    for q in  range(len(A)) :
                        Comb = list(combinations(A[0:k],q))
                        #print(Comb)
                        for l in range(len(Comb)):
                            if q % 2 == 1 :
                                cnt+= (nr-1) // (prod(Comb[l])*A[k])
                            else :              # q % 2 ==0 :
                                cnt -= (nr-1) // (prod(Comb[l])*A[k])
                return int(nr+cnt-1)          # print (nr+cnt-1)

red = Bogdan_Totient_algorithm()
z = 1765937
Z = red.count_elements(z)
print(Z)
print(red.factor_split(510510))

print('-----------------END CLASS TEST ---------------------\n')

################################################

def is_prime(n):
    # Function which checks if a number is prime
    for i in range(2, int(pow(n,1.0/2))+1):
        if n%i==0:
            return 0
    return 1


#
# t1  = time.time()
# def phi(n):
#     y = n
#     for i in range(2,n+1):
#         if is_prime(i) and n % i == 0:
#             y *= 1 - 1.0/i
#     return int(y)
#
# print(phi(510510))
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

t1  = time.time()

def totient(nr):
    # Bogdan, My Algorithm for computing Totient number, the Euler Phi(n) function
    if is_prime(nr) == True : return nr-1
    else:
        A = list(set(factor_split(nr)))
        cnt = 0
        for k in range(len(A)):
            #print(A[k], A[0:k+1])
            for q in  range(len(A)) :
                Comb = list(combinations(A[0:k],q))
                #print(Comb)
                for l in range(len(Comb)):
                    if q % 2 == 1 :
                        cnt+= (nr-1) // (prod(Comb[l])*A[k])
                    else :              # q % 2 ==0 :
                        cnt -= (nr-1) // (prod(Comb[l])*A[k])
        return int(nr+cnt-1)          # print (nr+cnt-1)

print(totient(87109))                      # 5.53938 --> 510510
#print(factor_split(903210))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n------------------   MY SOLUTION  ---------------------------')

algo = Bogdan_Totient_algorithm()
print(algo.factor_split(9))

maxv = 0
#for i in range(520000, 500000, -10):
for i in range(500000, 520000, 1):
    a = algo.count_elements(i)
    if i/a > maxv :                                 # n/φ(n) is a maximum
        maxv = i/a
        print(str(i)+'.   ', a,'     ', i/a)                            # Answer : 510510

print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1 ,  nopria , Italy --------------------------')
## http://codegolf.stackexchange.com/a/26753/53996  modified as generator
# I found here a very interesting and fast algorithm to calculate totien(n) for all n under a certain limit,
# and then used it to find the lowest ratio required. It runs in less than 20 seconds with plain Python 3:

# TOTIENT GENERATOR, found in Problem 70
def totient_gen(limit):
    phi = (limit+1)*[0]
    phi[1] = 1
    yield 1
    for n in range(2,limit):
        if phi[n] == 0:
            phi[n] = n - 1
            for j in range(2,int(limit/n)):
                if phi[j] != 0:
                    q = j
                    f = n - 1
                    while q % n == 0:
                        f *= n
                        q //= n
                    phi[n * j] = f * phi[q]
        yield phi[n]
# for i in totient_gen(100):     print(i, end=' ')

