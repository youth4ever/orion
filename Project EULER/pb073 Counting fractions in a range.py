#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Wed, 5 Oct 2016, 23:20
#The  Euler Project  https://projecteuler.net
'''
Counting fractions in a range       -       Problem 73
Consider the fraction, n/d, where n and d are positive integers.
If n<d and Highest Common Factor  HCF(n,d)=1, it is called a reduced proper fraction.
If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:
1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
It can be seen that there are 3 fractions between 1/3 and 1/2.
How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000?
'''

import time
print('------------------   MY SOLUTION , using  DYNAMIC RANGING---------------------------')
t1  = time.time()

fractions=[]
max_nr = 1/2
min_nr = 1/3
iter=1

for i in range (1 , 12001) :
    for j in range(int(i*1/3)-1, int(i*1/2)+1) :
        iter+=1
        if ( min_nr < j/i < max_nr ) :
            fractions.append(j/i)
            #print(str(iter)+'.   j , i = ',j ,', ' , i  , '  ;   ','  ;  ', j / i  )

ordered_frac=sorted(fractions)
#print('\n',len(ordered_frac))
print('\n The unique elements (fractions) are :', len( set(ordered_frac)))    #   There are : 7295372
#time.sleep(1)

t2  = time.time()
print('\nCompleted in :', round( (t2-t1)*1000,4), 'ms')                       # Completed in : 26219.4995 ms


print('\n============== OTHER SOLUTIONS FROM THE EULER FORUM =============')

print('\n---------------------------- SOLUTION 1,  THE  FASTEST ,  PongHeng, Singapore -----------------------------')
t1  = time.time()

#Although I brute forced it, but it was rather quick....

def countFract(m):
	count = 0
	pfact = (m-1) * [0]
	for i in range(2,m+1):
		n = ((i-1) // 2) - (i // 3 + 1) + 1
		n -= pfact[i-2]
		j = i + i
		while j <= m:
			pfact[j-2] += n
			j += i
		count += n
	return count

print(countFract(12000))

t2  = time.time()
print('\nCompleted in :', round( (t2-t1)*1000,4), 'ms')             # Completed in : 58.0034 ms

print('\n---------------------------- SOLUTION 2, ELEGANT, More efficient mbh038, England-----------------------------')

#My first effort constructed the Farey sequence for n=12000 and made heavy use of the fractions module in Python,
#  and even with memoization it took about 3 minutes in 2.7 and 80s in 3.5 (just switched).
# In 3.5, this takes about 4s, or about as long as j123's one-liner.
# I use the method shown in the overview to this problem for finding the second fraction in the series
# and after that, go along the Farey sequence once again.

t1  = time.time()

def myfarey(n):
    a,b=1,3
    c0,d0=1,2
    c=c0+a*(n-d0)/b
    d=d0+b*(n-d0)/b
    count=0
    while d>2*c:
        k=int((n+b)/d)
        a,b,c,d=c,d,k*c-a,k*d-b
        count+=1
    print (count)

myfarey(12000)

t2  = time.time()
print('\nCompleted in :', round( (t2-t1)*1000,4), 'ms')             # Completed in : 12685.7255 ms


print('\n--------------------------------SOLUTION 3, Using gcd method from math-----------------------------')

t1  = time.time()

from math import gcd

count = 0
for n in range(1,12000):
	for d in range(n+1, 12001):
		if n/d >= 1/2:
			continue
		if n/d <= 1/3:
			break
		if gcd(n, d) != 1:
			continue
		count += 1

print(count)

t2  = time.time()
print('\nCompleted in :', round( (t2-t1)*1000,4), 'ms')


print('\n---------------------------- SOLUTION 3, Very SLOW ,LIST COMPREHENSION, George,  England-----------------------------')

'''
t1  = time.time()

from fractions import gcd
print(len(sorted([n/d for d in range(1,12001) for n in range(1,d) if gcd(n,d) == 1 and n<d and 1/3 < n/d < 1/2])))

t2  = time.time()
print('\nCompleted in :', round( (t2-t1)*1000,4), 'ms')
'''
