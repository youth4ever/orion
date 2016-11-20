#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Mon, 10 Oct 2016, 11:46
#The  Euler Project  https://projecteuler.net
'''
Counting fractions      -       Problem 72
Consider the fraction, n/d, where n and d are positive integers. If n<d and High Common Factor HCF(n,d)=1,
it is called a reduced proper fraction.
If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:
1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
It can be seen that there are 21 elements in this set.
How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?
'''

import time
from math import gcd
from itertools import combinations
from numpy import prod
from pyprimes import factorise      # This is 4 times faster than my algorithm for factor split

print('------------------   FUNCTIONS  ---------------------------')

t1  = time.time()
def gen_primes(limit): # derived from
                      # Code by David Eppstein, UC Irvine, 28 Feb 2002
    D = {}            # http://code.activestate.com/recipes/117119/
    i = 2
    while i <= limit:
        if i not in D:
            yield i
            D[i * i] = [i]
        else:
            for p in D[i]:
                D.setdefault(p + i, []).append(p)
            del D[i]
        i += 1

p = gen_primes(210)
primes = [i for i in p]
print(len(primes),primes)

def is_prime(n):
    # Function which checks if a number is prime
    for i in range(2, int(pow(n,1.0/2))+1):
        if n%i==0:
            return 0
    return 1

def factorSplit(a): ##outputs a list of the unique prime factors of its input
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

def factor_split(n):
    return [i[0] for i in factorise(n)]

def Bogdan_totient(nr):
    A = list(set(factorSplit(nr)))
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
    print(nr+cnt-1)          # return nr+cnt-1

Bogdan_totient(510510)


print('\n------------------   MY SOLUTION  ---------------------------')
print('\n------------------   VERIFICATION  ---------------------------')


iter=0
for i in range (2, 101):                #510510, 510511)
    cnt=0
    for j in range(1, i) :
        if gcd(j, i ) == 1:
            iter += 1
            cnt +=1
            #print(str(iter)+'.  ',j, i , j/i)
    print(str(i)+'.   ', cnt)
    #print('-----'*10)

print('\nAnd the ANSWER with each term GCD computation  is :     ',iter)              # 3043 for d ≤ 100
#time.sleep(1)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,4), 'ms\n')                       #Completed in : 3.00 ms


print('\n------------------  MY SOLUTION ALGORITHM, From SCRATCH Computation of Totient Numbers  ---------------------------\n')
t1  = time.time()
#print(factor_split(510510))

superC = 0

for i in range (2, 101):
    if is_prime(i) == 1 :
        superC += i-1
    else :
        A = list(set(factor_split(i)))
        cnt = 0
         # Combinations  :          #THIS WORKS !!!!
        for k in range(len(A)):
            #print(A[k], A[0:k+1])
            for q in  range(len(A)) :
                Comb = list(combinations(A[0:k],q))
                #print(Comb)
                for l in range(len(Comb)):
                    if q % 2 == 1 :
                        cnt+= (i-1) // (prod(Comb[l])*A[k])
                    else :              # q % 2 ==0 :
                        cnt -= (i-1) // (prod(Comb[l])*A[k])
                    #print(i-1 , '//',Comb[l],A[k],'  --> ', (i-1) // (prod(Comb[l])*A[k]))
                    #print(cnt)
                    #print('---'*10)
            #print('==='*10)
        #print(cnt)
        #print(i-1+cnt)
        superC  += i -1 + int(cnt)
        #print(superC)

print('And the ANSWER (my ALGORITHM) is :     ',superC)    #Completed in : 6668.5854 s   ;  303963552391 for  d ≤ 1.000.000

t2  = time.time()
print('\nCompleted in :', round((t2-t1),4), 's\n\n')

print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1 , Bart23, Belgium --------------------------')

t1  = time.time()



sumt=0
for n in range(2,1001):
    div=list(factorise(n))
    totient=1
    for item in div:
        totient *= (item[0]**item[1] - item[0]**(item[1]-1))
    sumt += totient
print(sumt)

t2  = time.time()
print('\nCompleted in :', round((t2-t1),4), 's\n\n')        #  Completed in : 84.0608 s

print('\n--------------------------SOLUTION 2 , with Totient Function, froycard, from Venezuela --------------------------')

# Another impossible problem to solve using Brute-Force (unless you want to spend a half of day waiting for a solution).
# So, by using Wikipedia instead, you can find that Euler's totient formula can help you alot to find the solution
# in about 2 seconds (not wonder now why this page is named after this very famous mathematician: Euler),
# anyway, with the help of problem 69 (if you already solved that one) you can use a formula to calculate this one.
# The total sum of fractions can be easily calculated by phi(2)+phi(3)+...phi(1000000):

t1  = time.time()


def totient(n):
    product = 1
    f = 2
    while f**2 <= n:
    	if n % f == 0:
    		product *= f-1
    		n /= f
    		while n%f == 0:
    			product *= f
    			n/=f
    	f += 1
    if n > 1:
    	product *= n-1
    return product


print (sum([totient(i) for i in range(2,1001)]))

t2  = time.time()
print('\nCompleted in :', round((t2-t1),4), 's\n\n')

print('\n--------------------------SOLUTION 3 , the FASTEST , kenkamau, from Kenya --------------------------')
#  Using Sieve of Eratosthenes...runs in 2 sec
t1  = time.time()

def farey(limit):
    limit = limit + 1
    not_prime = [False] * limit
    ans = list(range (limit))
    for i in range(2, limit):
        if not_prime[i]:
            continue
        for f in range(i, limit, i):
            not_prime[f] = True
            ans[f] -= ans[f] / i
    return sum(ans) - 1

print(farey(1000000))

t2  = time.time()
print('\nCompleted in :', round((t2-t1),4), 's\n\n')


print('\n--------------------------SOLUTION 4 , BRUTE FORCE , Totient Sympy Module , abzupfer --------------------------')
#  After a lot of programming, I discovered that with Python's Sympy the brute force still works
#  in well under 1 minute. And it is just a few lines of code:

from sympy.ntheory import totient

sum = 0
for i in range(2, 10001):
    sum += totient(i)
print (sum)


#Wikipedia have a nice recursive formula on Farey sequence length
#  Farey sequence length
# I've only applied dynamic optimization using memoization to make computation linear complexity


print('\n\n-------------BENCHMARK FACTOR SPLIT TEST---------')
t1  = time.time()
print(list(factorise(3932273)))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,8), 'ms\n\n')

t1  = time.time()


print(factor_split(3932273))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,8), 'ms\n\n')


print(list(i[0] for i in list(factorise(3932273))))








'''
        # Substractions -
        for m in range(1,len(A)+1):
            cnt += (i-1) // A[m-1]
            print(i-1,'//' ,A[m-1] , A[0:m] , ' --> ',(i-1) // A[m-1] )
            #print('cnt:  ',cnt)

            for n in range(m-1):
                cnt -= (i-1) // (A[n]*A[m-1])
                print(i-1,'//' ,A[n],A[m-1], ' -->  ', (i-1) // (A[n]*A[m-1]) )
                #print('cnt,2nd : ',cnt)
            print('----------------')
        print('__________')
        # Combinations +
        for k in range(len(A)):
            print(A[k], A[0:k+1])
            Comb = list(combinations(A[0:k],2))
            print(Comb)
            for l in range(len(Comb)):
                cnt+= (i-1) // (prod(Comb[l])*A[k])
                print(i-1 , '//',prod(Comb[l])*A[k],'  --> ', (i-1) // (prod(Comb[l])*A[k]))
                #print(cnt)
            print('---'*10)
        #print(cnt)
        superC  += i -1 - cnt
        print(superC)


'''

'''
BACKUP
cnt = 0
A = list(set(factor_split(210)))
i=210

# Substractions -
for m in range(1,len(A)+1):
    cnt += (i-1) // A[m-1]
    print(i-1,'//' ,A[m-1] , A[0:m] , ' --> ',(i-1) // A[m-1] )
    print('cnt:  ',cnt)

    for n in range(m-1):
        cnt -= (i-1) // (A[n]*A[m-1])
        print(i-1,'//' ,A[n],A[m-1], ' -->  ', (i-1) // (A[n]*A[m-1]) )
        print('cnt,2nd : ',cnt)
    print('----------------')

print('__________')
# Combinations +
for k in range(len(A)):
    print(A[k], A[0:k+1])
    Comb = list(combinations(A[0:k],2))
    print(Comb)
    for l in range(len(Comb)):
        cnt+= (i-1) // (prod(Comb[l])*A[k])
        print(i-1 , '//',prod(Comb[l])*A[k],'  --> ', (i-1) // (prod(Comb[l])*A[k]))
        print(cnt)
    print('---'*10)

'''
'''

print('-----------THIS WORKS, THE PRECIOUS ----------------------')

print('\n','------'*20)

i = 510510
print(factor_split(i))
A = factor_split(i)
print('____'*20)

cnt=0
# Combinations +            # THIS WORKS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
for k in range(len(A)):
    print(A[k], A[0:k+1])
    for q in  range(len(A)) :
        Comb = list(combinations(A[0:k],q))
        print(Comb)
        for l in range(len(Comb)):
            if q % 2 == 1 :
                cnt+= (i-1) // (prod(Comb[l])*A[k])
            else : # q % 2 ==0 :
                cnt -= (i-1) // (prod(Comb[l])*A[k])
            print(i-1 , '//',Comb[l],A[k],'  --> ', (i-1) // (prod(Comb[l])*A[k]))
            print(cnt)
            print('---'*10)
    print('==='*10)

print(cnt)
print(i-1+cnt)
superC  += i -1 + cnt
print(superC)

'''