#!/usr/bin/python
# Solved by Bogdan Trif @       Completed on Thu, 2 Feb 2017, 11:30
#The  Euler Project  https://projecteuler.net
'''
            Tribonacci non-divisors     -   Problem 225

The sequence 1, 1, 1, 3, 5, 9, 17, 31, 57, 105, 193, 355, 653, 1201 ...
is defined by T1 = T2 = T3 = 1 and Tn = Tn-1 + Tn-2 + Tn-3.

It can be shown that 27 does not divide any terms of this sequence.
In fact, 27 is the first odd number with this property.

Find the 124th odd number that does not divide any terms of the above sequence.


'''
import time
from math import gcd
import gmpy2
from math import sqrt

def Fibon(n):
	#	Fibonacci with iteration, while loop
	counter = 0
	a, b = 0, 1
	while counter  < n :
		#print (b, end=" ")
		a  , b = b, a + b
		counter += 1
	return b

def Tribonacci_gen():
    """Tribonacci numbers generator"""
    a, b, c = 1, 1, 1
    while True:
        a, b, c = b, c, a+b+c
        yield c

T = Tribonacci_gen()

for i in range(200):
    t = next(T)
    print(str(i)+ '.        ', t,'      ' ,t % 27)

print('\n--------------------------INITIAL TESTS, 2 min ------------------------------')
t1  = time.time()

def brute_force():
    up_lim = int(2.5*10**4)
    odds = set([i for i in range(3, 2100, 2) ])
    print(odds)

    F = Tribonacci_gen()
    for i in range(up_lim):
        O=set()
        f = next(F)
        if f < up_lim :
            if gmpy2.is_prime(f ) :
                if f in odds : odds.remove(f)

        else :
            for d in odds :
                if  f%d == 0 :
                    O.add(d)

        odds = odds - O
        print(str(i)+'.      ',  )

    odds= sorted(list(odds))
    print('\n', len(odds),  odds[:250])

    return print('\nAnswer: \t', odds[124-1])              #       Answer: 	 2009

# brute_force()

t2  = time.time()
print('\nCompleted in :', round((t2-t1), 6), 's\n\n')

###### GENERAL IDEAS ##################
# ==== Mon, 29 Dec 2008, 14:40, 3lectrologos, Greece
# The modular sequence has to be periodic.
# Also, no two different triplets produce the same next triplet, so (1,1,1) has to show up again eventually.

# === Wed, 31 Dec 2008, 00:24, Susanne , Germany
# I found in the Internet that the modulo-values of numbers with Fibonacci-numbers are periodical.
# It is the same case with Tribonacci-numbers.
# The period starts over if there are three consecutive modulo-values of 1.
# A number cannot devide a Tribonacci-number, if during the period no modulo-value of 0 was found.

#=====Sat, 3 Jan 2009, 22:59, Taylor, USA
# Idea: Compute the tribonaccis modulo n. They have to repeat and if they do and we haven't found a 0,
# there is no 0.But often before 1,1,1 repeats, you get m,m,m for some m.
# When we get that, everything before the m,m,m will repeat but multiplied by m.
# So if gcd(m,n)=1, and we haven't found a 0 yet, there are no 0s.
# Also, since any odd multiple of something that works will also work,
# I check for that before doing anything else.

#===== Sun, 25 Jan 2009, 04:03, Axel Brzostowski, Argentina
# I've just brute forced it taking only the remainders modulo M where M is the number to check.
#  If some remainder is zero, then M divides a term.
# If the last three terms of the sequence are 1, 1, 1, then M doesn't divide any term.

#=== Sat, 8 Oct 2011, 13:53, learnmath, India
# For a long time, I did not know how to start. Then the bulb went on. Five minutes after the flash and I am here.
# If the sequence yields a 0 mod any number, it is divisible by the number. If it starts repeating, it is not.

#===Tue, 8 Nov 2011, 22:10, leonid, Japan
# Keep computing T_n mod k until either a term becomes zero or three consecutive terms become 1,1,1.

#=== Thu, 10 Nov 2011, 08:37, Narasimhan-S., India
# I enumerated the Tribonacci sequence mod k for all odd
# numbers k. If the remainder becomes zero , k is a divisor.
# If the terms 1, 1, 1 start repeating, k is a non-divisor.

# =====Thu, 1 Aug 2013, 04:24, jaswenso, USA
# As far as I see, no one has explicitly answered the question of @koen, @mario62, @tom.wheldon:
# why does [1, 1, 1] always recur in the sequence mod n?
# [Of course there has to be a cycle in the sequence, by the Pigeonhole Principle.]
#
# For me, the big idea is to think of the Tribonacci sequence as doubly infinite.
# That is: it extends infinitely far to the left as well as to the right, because for any k,
# T[k-1] = T[k+2] - T[k+1] - T[k].  Thus the cycle repeats infinitely often in both directions: there can't be a "transient" part.

print('\n==========  My FIRST SOLUTION, Learnt from Euler forum  ===============\n')
t1  = time.time()

### IDEA : !!!!!!!!!!         VERY IMPORTANT                !!!!!!!!
# 1. Fibonacci, Tribonacci and other recurence sequences are periodic modulo n ( where n is the number) to test.
# https://en.wikipedia.org/wiki/Pisano_period
"In number theory, the nth Pisano period, written π(n), is the period with which "
"the sequence of Fibonacci numbers taken modulo n repeats."
# 2. So we take an odd number and we compute the modulo n of each Tribonacci. If  Tri_nr % n == 0 ==> it is divisors
#3.  If we find a sequence of three(3)  Tri_nr1 % n == 1, Tri_nr2 % n == 1, Tri_nr3% n == 1 ==> IT IS A NON-DIVISOR
# Example : for n = 27 the 114, 115, 116-th Tribonacci's  modulo 27 from the sequence give 1,1,1 and the cycle modulo start
# repeateaing again:  1 1 1 3 5 9 17 4 3 24 .....because the sequence % n starts repeating again

def Tribonacci_non_divisors_cycle(limit) :
    n=25
    cnt = 0
    while cnt < limit :
        n += 2
        a, b, c = 1, 1, 1
        while 1 :       # Here we take the sequence ( modulo n)
            a, b, c = b, c, a       # SUPER CLEVER
            s = a+ b+ c
            c = s % n
            if c ==0 :
                break
            if (a, b, c) == (1, 1, 1):
                cnt+=1
                break

    return print(str(cnt)+'-th       ' , n)

Tribonacci_non_divisors_cycle(124)




t2  = time.time()
print('\nCompleted in :', round((t2-t1), 6), 's\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,   --------------------------')
t1  = time.time()

# ==== Tue, 29 Nov 2016, 10:18, mbh038, England
# About 1.1 s in Python. For each odd integer I cycle through trios (T_n−2 (mod n), T_(n−1) (mod n),T_n (mod n)  ).
# If I get T_n (mod n=0), n must be a divisor, and if I get (1,1,1) then we have a repeating cycle
# and n must be a non-divisor. There must be a cycle for non-divisors, since the set of remainders must be finite.

def p225(limit):
    count=0
    n=25
    while count<limit:
        n+=2
        a,b,c=1,1,1
        while 1:
            a,b,c=b,c,a
            s=a+b+c
            c=s%n
            if c==0:
                break
            if (a,b,c)==(1,1,1):
                count+=1
                break

    print (count, n )

# p225(124)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()

# ====Wed, 7 Jan 2009, 06:55, Valdemarick, USA
# 14 lines of Python, runs in 1.59 seconds on a Pentium D @ 3ghz.
# edit: Does the 1000th (14715) in 5.36 minutes.

def prob225(n):
    nth,cur = 0,27
    while True:
        t1=t2=t3=1
        while True:
            mod = (t1+t2+t3) % cur
            if not mod: break
            t1,t2,t3 = t2,t3,mod
            if t1==1 and t2==1 and t3==1:
                nth+=1
                if nth==n: return cur
                break
        cur+=2

print (prob225(124))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,   --------------------------')
t1  = time.time()

# === Fri, 26 Jun 2015, 02:20,Haroun, Algeria
# I have test each odd number for cycles of (1,1,1)(1,1,1). this took one second on python, it takes much less on C.

def g(n):
    #0 if T(n) is divisible by n for some n, else 1.
    (a,b,c)=(1,1,3);
    while True :
        if c==0:
            return 0;
        if a==1:
            if b==1:
                if c==1:
                    return 1;
        (a,b,c)=(b,c,(a+b+c)%n);
n=3;count=0;
while count<124:
    n+=2
    if g(n):
        count+=1;

print ("the answer is " , n )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,   --------------------------')
t1  = time.time()

# ====Mon, 1 Apr 2013, 22:30, tom.wheldon, England
# I got the solution the same way as most people, looking for a recurrence of 1,1,1,
# but though it was obvious that the sequence is cyclic mod n it was not at all clear to me that 1,1,1
# had to be in the cycle, so this is my 'honest' version which looks for any cycle.
# It runs in 5s compared to 2s for the first version.
# I was unwilling to try this first as I didn't know how long the cycles would be and I'm not sure how Windows 8
# would react to me trying to store a billion integer triples -
# as it happens the longest cycle turned out to be just under 600,000 terms long.

def tom_wheldon():
    n = 27
    nondivs = 1
    while nondivs < 124:
        n += 2
        t1 = t2 = t3 = 1
        triples = {(1,1,1)}
        while True:
            t1, t2, t3 = t2, t3, (t1+t2+t3)%n
            if not t3:
                break
            elif (t1,t2,t3) in triples:
                nondivs += 1
                break
            else:
                triples.add((t1,t2,t3))

    return print(n)

tom_wheldon()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

# print('\n--------------------------SOLUTION 5,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
print('\n--------------------------SOLUTION 6,   --------------------------')
t1  = time.time()

# ==== Sat, 27 Dec 2008, 13:34, loreto, England

def tribonacciDivisor(n):
	a, b, c = 1, 1, 1
	seen = set()

	while (a, b, c) not in seen:
		seen.add((a, b, c))

		a, b, c = b, c, (a+b+c)%n
		if c == 0: return True

	return False

i = 3
nonDivisisors = []

while len(nonDivisisors) < 124:
	if not tribonacciDivisor(i):
		nonDivisisors += [i]
# 		print(len(nonDivisisors), i)

	i += 2

print(nonDivisisors)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

