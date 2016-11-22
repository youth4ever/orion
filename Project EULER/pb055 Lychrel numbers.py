#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Mon, 21 Nov 2016, 11:26
#The  Euler Project  https://projecteuler.net
'''
                                        Lychrel numbers     -       Problem 55

If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.
Not all numbers produce palindromes so quickly. For example,

                                    349 + 943 = 1292,
                                    1292 + 2921 = 4213
                                    4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.
Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome.
A number that never forms a palindrome through the reverse and add process is called a Lychrel number.
Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume
that a number is Lychrel until proven otherwise.
In addition you are given that for every number below ten-thousand, it will either :
(i) become a palindrome in less than fifty iterations, or,
(ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome.
In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome:
4668731596684224866951378664 (53 iterations, 28-digits).

Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.

How many Lychrel numbers are there below ten-thousand?

NOTE: Wording was modified slightly on 24 April 2007 to emphasise the theoretical nature of Lychrel numbers.
'''
import time

print('\n--------------------------TESTS------------------------------')

def is_Lychrel_50_iter(n):
    ''':Description: Check for Lychrel number unde 50 iterations.
    :param n: int
    :return: boolean: True or False    '''
    for i in range(50) :
        m = int(str(n)[::-1])
        # print(str(i+1)+'.    ',n, m)
        n = n+m
        #print(n)
        if str(n) == str(n)[::-1] :
            return False    # not Lychrel
    return True              # Yes, IS Lychrel

print('\nTest is_Lychrel_50_iter function :  ', is_Lychrel_50_iter(981))



print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

cnt = 0
for i in range(1,10001) :
    if is_Lychrel_50_iter(i) == True :
        cnt+=1

print('\nAnswer : ',  cnt)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1, RECURSION, joe056, USA  --------------------------')
t1  = time.time()
# Proud of my first recursive Project Euler solution!

def check_lychrel(x, i):
    x = x + int(str(x)[::-1])

    # Stop condition 1: if number is palindromic, then it's not lychrel.
    if str(x) == str(x)[::-1]:
        return 0

    # Stop condition 2: if number exceeds iteration count 50, we say it is lychrel enough.
    elif i == 50:
        return 1

    # otherwise, try adding back flipped version
    else:
        return check_lychrel(x, i+1)

print(sum([check_lychrel(n,0) for n in range(10000)]))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2, bravenabin, India  --------------------------')
t1  = time.time()
# Thought of using recursion and actually did but it said below 50 iterations therefore finally used a loop instead of recursion :)

def r(x):
    r=0
    y=x
    while x>0:
        r=r*10+x%10
        x//=10
    return r

def pal(x):
    y=r(x)
    n=x+y
    i=1
    while i<50:
        if r(n)==n:return True
        n=n+r(n)
        i+=1
    return False

count=0
for i in range(1,10000):
    if not pal(i):
        count+=1

print(count)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3, shwetalm, USA  --------------------------')
t1  = time.time()
# simple solution with recursion.


def check_palindrome(_123, count=0):
    """
    checks to see if num+num[::-1] is a palindrome
    :param _123: number to test
    :param count: base case, false at 50
    :return: Bool
    """
    if count == 50:
        return True
    else:
        num_str = str(_123)
        num_rev = int(num_str[::-1])
        new_num = _123 + num_rev
        if str(new_num) == (str(new_num))[::-1]:
            return False
        else:
            count += 1
            return check_palindrome(new_num, count)


def main():
    """main"""
    lychrel = 0
    for num in range(1, 10000):
        if check_palindrome(num):
            lychrel += 1
    else:
        print(lychrel)

if __name__ == '__main__':
    main()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,  DidierDubois, Switzerland --------------------------')
t1  = time.time()

def lychrel(n, i=0):
    if i == 50: # limit reached / closing iteration
        return True
    v = str(n) # storing  the stirng version
    if i != 0 and v == v[::-1]:
        return False # We do not consider the first iteration
    # And recrusively call..
    return lychrel(n + int(v[::-1]), i+1)

limit = 10000
print( len( [ i for i in range(1,limit) if lychrel(i)] ))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5, nicolasrivollet, France  --------------------------')
t1  = time.time()

c = 0
for i in range(10 * 1000) :
	x = i
	for j in range(50) :
		x += int(str(x)[::-1])
		if str(x) == str(x)[::-1] :
			break
	else :
		c += 1

print(c)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6, mbh038, England  --------------------------')
t1  = time.time()
# About 125 ms on my 8 year old machine for my Python 2.7 code, which is very similar to that of achampion:

def isLychrel(n):
   i=0
   while i < 50:
       i+=1
       n+=int(str(n)[::-1])
       if str(n)==str(n)[::-1]:
           return False
   return True

print (sum([1 for x in range(2,10000) if isLychrel(x)]))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

