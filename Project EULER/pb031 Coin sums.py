#!/usr/bin/python3
# Solved by Bogdan Trif @   Completed on Wed, 5 Oct 2016, 17:16
#The  Euler Project  https://projecteuler.net
'''
Coin sums   -   Problem 31
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
'''
import time
print('At this moment, 2016-10-04, I did not know how to solve this problem, I searched on the internet for the solution ... ')

print('\n-----------------FAST SOLUTION FOUND ON INTERNET, DYNAMIC PROGRAMMING-----------------------')

t1  = time.time()

# Dynamic Programming Python implementation of Coin Change problem
def count(S, m, n):
    # We need n+1 rows as the table is consturcted in bottom up
    # manner using the base case 0 value case (n = 0)
    table = [[0 for x in range(m)] for x in range(n+1)]

    # Fill the enteries for 0 value case (n = 0)
    for i in range(m):
        table[0][i] = 1

    # Fill rest of the table enteries in bottom up manner
    for i in range(1, n+1):
        for j in range(m):
            # Count of solutions including S[j]
            x = table[i - S[j]][j] if i-S[j] >= 0 else 0
            #print('x=', x, end=' ')


            # Count of solutions excluding S[j]
            y = table[i][j-1] if j >= 1 else 0
            #print('y=', y)
            # total count
            table[i][j] = x + y
        #print(table[i])

    return table[n][m-1]

# Driver program to test above function
S = [1, 2, 5, 10, 20, 50, 100, 200]
m = len(S)
n = 200
print(count(S, m, n))

t2  = time.time()
print('\n', ' Completed in  in :', round((t2-t1)*1000,4), 'ms\n')

print('\n=============== OTHER SOLUTIONS FROM THE EULER FORUM =================')
print('\n------------------ SOLUTION 1, caelum, USA ------------------------')
t1  = time.time()

coins=[1,2,5,10,20,50,100,200]
possible=[1]+[0]*200
for i in coins:
    for j in range(i,201):
        possible[j]+=possible[j-i]

print(possible[200])

t2  = time.time()
print('\n', ' Completed in  in :', round((t2-t1)*1000,4), 'ms\n')

print('\n------------------ SOLUTION 2, VERY NICE, RECURSIVE SOLUTION ------------------------')
# clear, recursive way in python, calculates number of ways for a given total and a given list of coins.
t1  = time.time()

def ways(total, coins):
	if total in [0, 1] or len(coins) == 1:
		return 1
	else:
		coins_left = coins[:-1]
		coin = coins[-1]
		return sum(ways(total - (coin * x), coins_left) for x in range(1 + total // coin))

def main():
	coins = [1, 2, 5, 10, 20, 50, 100, 200]
	print(ways(200, coins))

if __name__ == '__main__':
	main()

t2  = time.time()
print('\n', ' Completed in  in :', round((t2-t1)*1000,4), 'ms\n')

print('\n------------------ SOLUTION 3,  NICE but SLOW  ------------------------')
t1  = time.time()

def f(rest, coins):
	if rest == 0:
		return 1
	counter = 0
	for coin in coins:
		if (coin <= rest):
			counter += f(rest-coin, [i for i in coins if coin >= i])
	return counter

coins = [200,100,50,20,10,5,2,1]

print(f(200,coins))

t2  = time.time()
print('\n', ' Completed in  in :', round((t2-t1)*1000,4), 'ms\n')

print('\n------------------ SOLUTION 4,  RECURSION ------------------------')

t1  = time.time()


def coin(x, den, i=0):
    return 1 if x == 0 else 0 if i == len(den) else\
           sum(coin(x - n * den[i], den, i+1) for n in range(x // den[i] + 1))

print(coin(200, [200, 100, 50, 20, 10, 5, 2, 1]))

t2  = time.time()
print('\n', ' Completed in  in :', round((t2-t1)*1000,4), 'ms\n')

print('\n------------------ SOLUTION 5,  RECURSION , without Memoization  SLOW ------------------------')
t1  = time.time()


def count(N, m):
    coin = [1,2,5,10,20,50,100,200]
    if N < 0 or m<=0:
        return 0
    if N == 0:
        return 1
    return count(N, m-1)+count(N-coin[m-1], m)

print (count(200,8))

t2  = time.time()
print('\n', ' Completed in  in :', round((t2-t1)*1000,4), 'ms\n')

print('\n------------------ SOLUTION 6, RECURSION wint Memoization, VERY FAST  ------------------------')
t1  = time.time()

coin = [1,2,5,10,20,50,100,200]

def pb031(n,arr):
    last = arr[-1]
    if len(arr) == 1:
        return 1
    return sum(pb031(n-last*i,arr[:-1]) for i in range(n//last+1))

print(pb031(200,coin))

t2  = time.time()
print('\n', ' Completed in  in :', round((t2-t1)*1000,4), 'ms\n')

print('\n------------------ SOLUTION 7, DYNAMIC PROGRAMMING - ONE ROW MATRIX - THE FASTEST ------------------------')
t1  = time.time()

'''
A dynamic way of doing it (not my idea, but I coded it having got the principle of the method).
I basically stole this from MathBlog, (which is the same as that of post 16 in this thread, and discussed as program 3
in the pdf of this thread) having read and understood the idea.

An array of length the total value is set up, initialised to zero, but with array[0]=1.
We then go through this array for each coin value, jumping places by the value of that coin.
Each time, we add to the new element the value of the element that is the current coin value number of places below it.

This way, for each new coin, we find the number of ways of getting any total up to our required value using
just the coins up to that value, and we don't have to start from scratch once we add in the next coin.

This takes total value x number of coins = 200 x 8 = 1600 calculations, in this case.

The problem is like those where we are trying to find our way across a grid of numbers,
following some rules about where we can go in each new step, and have to maximise the sum of the elements on the route.
In that case, a solution can be found by working out from one corner and building a new matrix
where each element now contains  the maximum sum for a route to the corner.
This way we avoid re-calculating the sums  for sub-routes, on the way to the complete route.
  See Problems 18,67 and 81, for example.
'''

import time

def coinsum(value):

    coins = [1,2,5,10,20,50,100,200]

    ways = [0] * (value+1)
    ways[0] = 1

    while coins[-1] > value:
        del(coins[-1])

    for i in range(len(coins)):
        for j in range (coins[i],value + 1):
            ways[j] += ways[j - coins[i]]

    print (ways[-1])

coinsum(200)

t2  = time.time()
print('\n', ' Completed in  in :', round((t2-t1)*1000,4), 'ms\n')

print('\n------------------ SOLUTION 8, RECURSION   ------------------------')

t1  = time.time()

def do_work(oldsum, available_coins):
    global okcount

    index = 0
    for coin in available_coins:
        newsum = oldsum + coin

        # Nailed it! Add one to the ok count
        if newsum == 200:
            okcount += 1

        # We can still check. However, slice the list to avoid repeating bigger coins!
        elif newsum < 200:
            do_work(newsum, available_coins[index:])

        # Increment the index, later used to skip the used coins
        index += 1


okcount = 0
do_work(0, [200, 100, 50, 20, 10, 5, 2, 1])
print(okcount)

t2  = time.time()
print('\n', ' Completed in  in :', round((t2-t1)*1000,4), 'ms\n')

print('\n------------------ SOLUTION 9, BRUTE FORCE FROM CANADA   ------------------------')

t1  = time.time()

ways = 0
for a in range(2):
    for b in range(3):
        for c in range(6):
            for d in range(11):
                for e in range(21):
                    if a*20 + b*10 + c*5 + d*2 + e*1  == 20:
                        ways += 1
                        print('a,  b,  c,  d,  e,       ',a,b,c,d,e)
print(ways)

t2  = time.time()
print('\n', ' Completed in  in :', round((t2-t1)*1000,4), 'ms\n')

print('\n------------------ SOLUTION 10, ITERATIVE , VERY VERY ELEGANT & FAST , MATRIX ROW,  celsberry USA   ------------------------')

t1  = time.time()

total = 200
combinations = [1] + [0]*total
monies = [1,2,5,10,20,50,100,200]

for x in monies:
	for i in range(x, total+1):
		combinations[i] += combinations[i-x]

print (combinations[total])

t2  = time.time()
print('\n', ' Completed in  in :', round((t2-t1)*1000,4), 'ms\n')

print('\n------------------ SOLUTION 11, ITERATIVE  andylewis31, England  ----------------------')


t1  = time.time()

coinvalues = [1, 2, 5, 10, 20, 50, 100, 200]

def count(total, largest):
    if largest > total: return 0
    if largest == 1 or largest == total: return 1
    c = 0
    remaining = total - largest
    for coin in coinvalues:
        if coin > largest: return c
        c += count(remaining, coin)
    return c

print (sum(count(200, coin) for coin in coinvalues))

t2  = time.time()
print('\n', ' Completed in  in :', round((t2-t1)*1000,4), 'ms\n')


print('\n------------------ SOLUTION 12,   ----------------------')

